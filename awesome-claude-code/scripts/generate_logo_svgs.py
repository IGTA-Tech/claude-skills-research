#!/usr/bin/env python3
"""
Generate responsive SVG logos for the Awesome Claude Code repository.

This script creates:
- Light and dark theme versions of the ASCII art logo
- The same logo is used for all screen sizes (scales responsively)
"""

from pathlib import Path

# ASCII art for the desktop version
ASCII_ART = [
    " █████┐ ██┐    ██┐███████┐███████┐ ██████┐ ███┐   ███┐███████┐",
    "██┌──██┐██│    ██│██┌────┘██┌────┘██┌───██┐████┐ ████│██┌────┘",
    "███████│██│ █┐ ██│█████┐  ███████┐██│   ██│██┌████┌██│█████┐",
    "██┌──██│██│███┐██│██┌──┘  └────██│██│   ██│██│└██┌┘██│██┌──┘",
    "██│  ██│└███┌███┌┘███████┐███████│└██████┌┘██│ └─┘ ██│███████┐",
    "└─┘  └─┘ └──┘└──┘ └──────┘└──────┘ └─────┘ └─┘     └─┘└──────┘",
    "",
    "────────────────────────────────────────────────────────────────────────────────────",
    "",
    " ██████┐██┐      █████┐ ██┐   ██┐██████┐ ███████┐     ██████┐ ██████┐ ██████┐ ███████┐",
    "██┌────┘██│     ██┌──██┐██│   ██│██┌──██┐██┌────┘    ██┌────┘██┌───██┐██┌──██┐██┌────┘",
    "██│     ██│     ███████│██│   ██│██│  ██│█████┐      ██│     ██│   ██│██│  ██│█████┐",
    "██│     ██│     ██┌──██│██│   ██│██│  ██│██┌──┘      ██│     ██│   ██│██│  ██│██┌──┘",
    "└██████┐███████┐██│  ██│└██████┌┘██████┌┘███████┐    └██████┐└██████┌┘██████┌┘███████┐",
    " └─────┘└──────┘└─┘  └─┘ └─────┘ └─────┘ └──────┘     └─────┘ └─────┘ └─────┘ └──────┘",
]


def generate_logo_svg(theme: str = "light") -> str:
    """Generate SVG with full ASCII art for all screen sizes."""
    fill_color = "#24292e" if theme == "light" else "#e1e4e8"

    svg_lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 320" '
        'preserveAspectRatio="xMidYMid meet">',
        "  <style>",
        "    text {",
        "      font-family: 'Courier New', Courier, monospace;",
        "      font-size: 14px;",
        f"      fill: {fill_color};",
        "      white-space: pre;",
        "    }",
        "  </style>",
    ]

    # Add each line of ASCII art as a text element
    y_position = 25
    for line in ASCII_ART:
        svg_lines.append(f'  <text x="10" y="{y_position}">{line}</text>')
        y_position += 20

    svg_lines.append("</svg>")
    return "\n".join(svg_lines)


def main():
    """Generate all logo SVG files."""
    # Get the project root directory
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    assets_dir = project_root / "assets"

    # Create assets directory if it doesn't exist
    assets_dir.mkdir(exist_ok=True)

    # Generate logo SVGs (same for all screen sizes)
    logo_light = generate_logo_svg("light")
    logo_dark = generate_logo_svg("dark")

    # Write files
    files_to_write = {
        "logo-light.svg": logo_light,
        "logo-dark.svg": logo_dark,
    }

    for filename, content in files_to_write.items():
        filepath = assets_dir / filename
        filepath.write_text(content, encoding="utf-8")
        print(f"✅ Generated: {filepath}")

    print("\n🎨 All logo SVG files have been generated successfully!")
    print("📝 Run 'make generate' to update the README with the new logos.")


if __name__ == "__main__":
    main()
