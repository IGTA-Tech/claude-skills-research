#!/usr/bin/env python3
"""
Claude Skills Builder - Automation Tool
Systematically build, validate, and package Claude Code skills
"""

import os
import json
import zipfile
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

class SkillBuilder:
    """Build and manage Claude Code skills"""

    def __init__(self, base_dir: str = None):
        self.base_dir = Path(base_dir) if base_dir else Path.home() / "claude-skills"
        self.base_dir.mkdir(exist_ok=True)

    def create_skill_structure(self, skill_name: str, description: str,
                              instructions: str, category: str = "sales") -> Path:
        """Create the directory structure for a new skill"""

        # Create skill directory
        skill_dir = self.base_dir / skill_name
        skill_dir.mkdir(exist_ok=True)

        # Create SKILL.md
        skill_md_content = self._generate_skill_md(
            skill_name, description, instructions, category
        )

        (skill_dir / "SKILL.md").write_text(skill_md_content)

        print(f"✅ Created skill structure: {skill_dir}")
        return skill_dir

    def _generate_skill_md(self, name: str, description: str,
                          instructions: str, category: str) -> str:
        """Generate SKILL.md content"""

        return f"""---
name: {name}
description: {description}
---

# {self._titlecase(name)}
{description}

## Instructions

{instructions}

### Output Format

```markdown
# {self._titlecase(name)} Output

**Generated**: {{timestamp}}

---

## Results

[Your formatted output here]

---

## Recommendations

[Actionable next steps]

```

### Best Practices

1. **Be Specific**: Focus on concrete, actionable outputs
2. **Use Templates**: Provide copy-paste ready formats
3. **Include Examples**: Show real-world usage
4. **Add Context**: Explain why recommendations matter
5. **Stay Current**: Use latest best practices for {category}

### Common Use Cases

**Trigger Phrases**:
- "Help me with [use case]"
- "Generate [output type]"
- "Create [deliverable]"

**Example Request**:
> "[Sample user request here]"

**Response Approach**:
1. Understand user's context and goals
2. Generate comprehensive output
3. Provide actionable recommendations
4. Include examples and templates
5. Suggest next steps

Remember: Focus on delivering value quickly and clearly!
"""

    def _titlecase(self, text: str) -> str:
        """Convert kebab-case to Title Case"""
        return text.replace('-', ' ').title()

    def zip_skill(self, skill_name: str) -> Path:
        """Create a ZIP file of the skill"""

        skill_dir = self.base_dir / skill_name
        if not skill_dir.exists():
            raise FileNotFoundError(f"Skill directory not found: {skill_dir}")

        zip_path = self.base_dir / f"{skill_name}.zip"

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add SKILL.md
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                zipf.write(skill_md, f"{skill_name}/SKILL.md")

            # Add any additional files (scripts, etc.)
            for file_path in skill_dir.glob("**/*"):
                if file_path.is_file() and file_path.name != ".DS_Store":
                    arcname = str(file_path.relative_to(skill_dir.parent))
                    zipf.write(file_path, arcname)

        print(f"📦 Created ZIP: {zip_path}")
        return zip_path

    def validate_skill(self, skill_name: str) -> bool:
        """Validate skill structure and content"""

        skill_dir = self.base_dir / skill_name

        if not skill_dir.exists():
            print(f"❌ Skill directory not found: {skill_dir}")
            return False

        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            print(f"❌ SKILL.md not found")
            return False

        content = skill_md.read_text()

        # Check for required sections
        required_sections = [
            "---\nname:",
            "description:",
            "# ",
            "## Instructions",
        ]

        for section in required_sections:
            if section not in content:
                print(f"❌ Missing required section: {section}")
                return False

        print(f"✅ Skill validation passed: {skill_name}")
        return True

    def build_from_config(self, config_file: Path) -> List[str]:
        """Build multiple skills from a configuration file"""

        with open(config_file) as f:
            config = json.load(f)

        built_skills = []

        for skill_config in config.get('skills', []):
            name = skill_config['name']
            description = skill_config['description']
            instructions = skill_config.get('instructions',
                f"You are an expert at {name.replace('-', ' ')}. Provide comprehensive, actionable guidance.")
            category = skill_config.get('category', 'general')

            try:
                skill_dir = self.create_skill_structure(
                    name, description, instructions, category
                )

                if self.validate_skill(name):
                    self.zip_skill(name)
                    built_skills.append(name)
                    print(f"✅ Built: {name}")
                else:
                    print(f"⚠️ Validation failed: {name}")

            except Exception as e:
                print(f"❌ Error building {name}: {e}")

        return built_skills

    def list_skills(self) -> List[str]:
        """List all skills in the directory"""

        skills = []
        for item in self.base_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                if (item / "SKILL.md").exists():
                    skills.append(item.name)

        return sorted(skills)

    def generate_batch_config(self, phase: str, skills: List[Dict]) -> Path:
        """Generate a batch configuration file"""

        config = {
            "phase": phase,
            "generated": datetime.now().isoformat(),
            "skills": skills
        }

        config_path = self.base_dir / f"batch-{phase}.json"
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)

        print(f"📄 Generated config: {config_path}")
        return config_path


def main():
    """Main CLI interface"""

    parser = argparse.ArgumentParser(
        description="Build and manage Claude Code skills"
    )

    parser.add_argument(
        '--name',
        help='Name of skill to create'
    )

    parser.add_argument(
        '--description',
        help='Description of skill'
    )

    parser.add_argument(
        '--batch',
        help='Build from batch config file'
    )

    parser.add_argument(
        '--validate',
        help='Validate an existing skill'
    )

    parser.add_argument(
        '--zip',
        help='ZIP an existing skill'
    )

    parser.add_argument(
        '--list',
        action='store_true',
        help='List all skills'
    )

    parser.add_argument(
        '--generate-phase1-config',
        action='store_true',
        help='Generate Phase 1 batch config'
    )

    args = parser.parse_args()

    builder = SkillBuilder()

    if args.list:
        skills = builder.list_skills()
        print(f"\n📚 Found {len(skills)} skills:\n")
        for skill in skills:
            print(f"  - {skill}")
        print()

    elif args.validate:
        builder.validate_skill(args.validate)

    elif args.zip:
        builder.zip_skill(args.zip)

    elif args.batch:
        config_path = Path(args.batch)
        built_skills = builder.build_from_config(config_path)
        print(f"\n✅ Built {len(built_skills)} skills")

    elif args.generate_phase1_config:
        # Generate Phase 1 configuration
        phase1_skills = [
            {
                "name": "slack-message-formatter",
                "description": "Convert long text into Slack-optimized format with emojis, bullets, code blocks, and threading suggestions",
                "category": "communication",
                "instructions": "You are an expert at Slack communication. Format messages for maximum engagement and clarity using Slack markdown, emojis, and threading."
            },
            {
                "name": "sms-text-optimizer",
                "description": "Condense messages to 160 characters without losing meaning. Remove unnecessary words while keeping tone.",
                "category": "communication",
                "instructions": "You are an expert at concise communication. Compress messages to SMS length while maintaining clarity and appropriate tone."
            },
            {
                "name": "internal-email-composer",
                "description": "Casual but professional tone for team communication. Uses company-specific terminology with scannable format.",
                "category": "communication",
                "instructions": "You are an expert at internal communications. Write clear, scannable emails for team collaboration."
            },
            {
                "name": "company-announcement-writer",
                "description": "Executive communication style for all-hands emails. Balances transparency with appropriate messaging.",
                "category": "communication",
                "instructions": "You are an expert at executive communications. Draft company-wide announcements that are clear, transparent, and appropriately messaged."
            },
            {
                "name": "linkedin-post-optimizer",
                "description": "Professional narrative style with line breaks, hashtag strategy, and hooks in first 2 lines to avoid truncation",
                "category": "communication",
                "instructions": "You are an expert at LinkedIn engagement. Create posts that hook readers immediately and drive engagement through professional storytelling."
            }
        ]

        config_path = builder.generate_batch_config("phase1", phase1_skills)
        print(f"\n✅ Run: python build_skills.py --batch {config_path}")

    elif args.name and args.description:
        # Interactive single skill creation
        instructions = input("Enter instructions (or press Enter for default): ")
        if not instructions:
            instructions = f"You are an expert at {args.name.replace('-', ' ')}. Provide comprehensive, actionable guidance."

        skill_dir = builder.create_skill_structure(
            args.name, args.description, instructions
        )

        if builder.validate_skill(args.name):
            builder.zip_skill(args.name)
            print(f"\n✅ Skill ready: {skill_dir}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
