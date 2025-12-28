# Security Policy

**Last Updated**: October 28, 2025
**Version**: 2.0.0

---

## 🔒 Reporting Security Vulnerabilities

### How to Report

**DO NOT** open public issues for security vulnerabilities.

**Instead**:
1. **Email**: Create a GitHub Security Advisory (preferred)
   - Go to: Repository → Security → Advisories → New draft security advisory
   - Or email: [Your security contact email]

2. **Include**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

3. **Response Time**: We aim to respond within 48 hours

---

## 🛡️ Security Measures

### 1. Secrets Management

**Secrets Are Never Committed**:
- ✅ All credentials use GitHub Secrets vault
- ✅ No hardcoded API keys or tokens
- ✅ .env files are gitignored
- ✅ Regular security audits performed

**Secrets Used in Workflows**:
- `GITHUB_TOKEN` - Auto-provided by GitHub (minimal permissions)
- `CLAUDE_CODE_OAUTH_TOKEN` - Claude Code authentication (scoped)
- `PROJECTS_TOKEN` - Project board access (scoped: repo + project only)

**Audit Status**: ✅ Last audited October 28, 2025 - No exposed credentials ([See Audit](.github/SECURITY_AUDIT.md))

---

### 2. Healthcare Data Protection

**For health-sdk-builder and healthcare applications**:

**Compliance Frameworks**:
- ✅ **HIPAA** (US) - Privacy Rule, Security Rule, Breach Notification
- ✅ **GDPR** (EU) - Articles 5-11, Data Subject Rights
- ✅ **DSGVO** (Germany) - German-specific requirements
- ✅ **PTV 10** (Germany) - Psychotherapy standards

**Data Protection**:
- ✅ Encryption at rest (AES-256)
- ✅ Encryption in transit (TLS 1.2+)
- ✅ Audit logging (all PHI/PII access)
- ✅ Access controls (role-based)
- ✅ Data minimization
- ✅ Retention policies
- ✅ Right to erasure

**Clinical Safety**:
- ✅ Crisis detection (suicide, self-harm, harm to others)
- ✅ Emergency escalation workflows
- ✅ Mandatory reporting compliance
- ✅ Professional boundaries
- ✅ Evidence-based practices only

**Documentation**: See [HEALTHCARE_COMPLIANCE_GUIDE.md](generated-skills/claude-health-sdk-builder/compliance/HEALTHCARE_COMPLIANCE_GUIDE.md)

---

### 3. GitHub Workflows Security

**4-Layer Security Model**:

**Layer 1: GitHub Permissions**
```yaml
# Only team members can trigger workflows
if: contains(fromJSON('["OWNER", "MEMBER", "COLLABORATOR"]'),
             github.event.comment.author_association)
```

**Layer 2: Tool Restrictions**
```yaml
# Allowlist specific commands only
claude_args: '--allowed-tools "Bash(gh issue:*),Bash(gh pr:*)"'
# Blocks: git push, rm -rf, curl, wget, etc.
```

**Layer 3: Token Scoping**
- GITHUB_TOKEN: Minimal permissions (read by default)
- PROJECTS_TOKEN: repo + project only (no admin)
- CLAUDE_CODE_OAUTH_TOKEN: Claude operations only

**Layer 4: Branch Protection**
- Required pull request workflow
- Status checks required (claude-review)
- No force pushes allowed
- Admin enforcement
- Conversation resolution required

---

### 4. Emergency Controls

**Kill Switch** (`.github/WORKFLOW_KILLSWITCH`):
- Master OFF switch for all workflows
- Current status: DISABLED (from Oct 24 incident)
- Instant shutdown capability (no code changes needed)

**Emergency Cleanup** (`.github/EMERGENCY_CLEANUP.sh`):
- Bulk issue closure for spam cleanup
- Dry-run mode for safety
- Documented procedures

**Emergency Procedures**: See [.github/GITHUB_WORKFLOWS_GUIDE.md](.github/GITHUB_WORKFLOWS_GUIDE.md#emergency-procedures)

---

## 🔐 Security Best Practices

### For Contributors

**Never Commit**:
- ❌ API keys (sk-ant-*, any provider)
- ❌ GitHub tokens (ghp_*, github_pat_*)
- ❌ OAuth tokens
- ❌ Passwords or credentials
- ❌ .env files with secrets
- ❌ Private keys (.key, .pem files)
- ❌ Patient data (PHI/PII)

**Always Use**:
- ✅ .env.example templates (no real values)
- ✅ GitHub Secrets for CI/CD
- ✅ .gitignore for sensitive files
- ✅ Placeholder values in examples

---

### For Healthcare Applications

**Patient Data Protection**:
- ✅ Never commit patient data
- ✅ Use anonymized examples only
- ✅ Implement encryption (AES-256 minimum)
- ✅ Audit all data access
- ✅ Comply with HIPAA/GDPR/DSGVO

**Generated Applications**:
- ✅ Include compliance by default
- ✅ Document security requirements
- ✅ Provide encryption examples
- ✅ Include audit logging
- ✅ Add crisis detection (mental health apps)

---

### For Skill Development

**Safe Skill Creation**:
- ✅ No secrets in SKILL.md files
- ✅ No hardcoded credentials in Python files
- ✅ Use environment variables for configuration
- ✅ Document security requirements
- ✅ Include security best practices in generated code

**Testing**:
- ✅ Use test API keys (rotated after testing)
- ✅ Never commit test credentials
- ✅ Use separate testing repository
- ✅ Clean up after testing

---

## 🎯 Supported Versions

**Current Versions Receiving Security Updates**:

| Version | Supported | Status |
|---------|-----------|--------|
| 2.0.x   | ✅ Yes    | Current, active development |
| 1.2.x   | ✅ Yes    | Maintained, security fixes only |
| 1.1.x   | ⚠️ Limited | Critical security fixes only |
| < 1.0   | ❌ No     | Not supported |

**Upgrade Recommendation**: Always use latest version (2.0.x)

---

## 🚨 Known Security Considerations

### 1. Code Execution Tool

**What**: Skills can execute Python code (Code Execution Tool required)
**Risk**: Malicious skills could execute harmful code
**Mitigation**:
- ✅ Only use trusted skills (from this repository or verified sources)
- ✅ Review skill code before importing
- ✅ Code Execution runs in sandboxed environment (Anthropic-managed)
- ✅ No filesystem access outside sandbox

**Recommendation**: Review SKILL.md and Python files before importing unknown skills

---

### 2. Workflow Automation

**What**: GitHub workflows can modify issues, PRs, project boards
**Risk**: Malicious workflow changes could spam or delete content
**Mitigation**:
- ✅ Kill switch for emergency shutdown
- ✅ Branch protection (workflow changes require PR + review)
- ✅ Tool allowlists (restrict dangerous commands)
- ✅ Permission scoping (minimal required)
- ✅ Team-only access (@claude mentions)

**Recommendation**: Never merge workflow changes without review

---

### 3. Healthcare Applications

**What**: Generated apps handle sensitive patient data (PHI/PII)
**Risk**: Data breach, compliance violations, patient harm
**Mitigation**:
- ✅ HIPAA/GDPR/DSGVO compliance built-in
- ✅ Encryption templates provided
- ✅ Audit logging examples included
- ✅ Crisis detection for mental health apps
- ✅ Clear disclaimers (not replacement for professional care)

**Recommendation**:
- Clinical validation required before patient use
- Legal review for compliance
- Professional oversight mandatory

---

## 📋 Security Checklist

### Before Using This Repository

- [ ] Review all workflow files for understanding
- [ ] Configure GitHub Secrets (never hardcode)
- [ ] Enable branch protection on main
- [ ] Review SECURITY_AUDIT.md
- [ ] Understand kill switch mechanism

### Before Importing Skills

- [ ] Review SKILL.md content
- [ ] Check Python files (if any)
- [ ] Verify source is trusted
- [ ] Check for hardcoded credentials
- [ ] Test in isolated environment first

### Before Deploying Healthcare Apps

- [ ] Complete HIPAA/GDPR/DSGVO compliance review
- [ ] Clinical validation by healthcare professionals
- [ ] Legal review for regulatory compliance
- [ ] Security audit (encryption, access controls, audit logs)
- [ ] Penetration testing (if handling real patient data)
- [ ] Privacy policy and terms of service
- [ ] Incident response plan
- [ ] Data breach notification procedures

---

## 🔗 Security Resources

### Documentation
- **Security Audit**: [.github/SECURITY_AUDIT.md](.github/SECURITY_AUDIT.md)
- **Workflows Guide**: [.github/GITHUB_WORKFLOWS_GUIDE.md](.github/GITHUB_WORKFLOWS_GUIDE.md)
- **Healthcare Compliance**: [HEALTHCARE_COMPLIANCE_GUIDE.md](generated-skills/claude-health-sdk-builder/compliance/HEALTHCARE_COMPLIANCE_GUIDE.md)

### External Resources
- **GitHub Security**: https://docs.github.com/en/code-security
- **HIPAA**: https://www.hhs.gov/hipaa/
- **GDPR**: https://gdpr-info.eu/
- **Claude Security**: https://www.anthropic.com/security

---

## 📞 Contact

**Security Issues**: Use GitHub Security Advisory (preferred)
**General Questions**: Open issue with `question` label
**Healthcare Compliance**: Document in issue with `documentation` label

---

## 🏆 Security Certifications

**Repository Security**:
- ✅ No exposed credentials (audited October 28, 2025)
- ✅ Proper secrets management
- ✅ Minimal permissions enforced
- ✅ Emergency controls in place

**Healthcare Applications**:
- ✅ HIPAA compliance templates
- ✅ GDPR/DSGVO compliance frameworks
- ✅ Clinical safety protocols
- ✅ Evidence-based practices

**Code Quality**:
- ✅ Type hints (Python)
- ✅ Input validation
- ✅ Error handling
- ✅ Security best practices

---

## 📅 Security Maintenance Schedule

**Weekly**:
- Monitor failed workflow runs
- Review GitHub Actions logs
- Check for unusual activity

**Monthly**:
- Review secrets expiration
- Audit new workflow changes
- Update dependencies

**Quarterly**:
- Rotate PROJECTS_TOKEN
- Comprehensive security audit
- Review permissions and access
- Update security documentation

**Annually**:
- Full security assessment
- Penetration testing (if applicable)
- Compliance review (HIPAA/GDPR)
- Update security policy

---

## ⚡ Incident Response

**If Security Issue Discovered**:

1. **Immediate**: Activate kill switch (disable workflows)
2. **Assess**: Determine scope and impact
3. **Contain**: Revoke compromised credentials
4. **Remediate**: Fix vulnerability
5. **Communicate**: Notify affected users (if applicable)
6. **Document**: Post-incident report
7. **Prevent**: Update procedures to prevent recurrence

**Emergency Contacts**: See [.github/GITHUB_WORKFLOWS_GUIDE.md](.github/GITHUB_WORKFLOWS_GUIDE.md#emergency-procedures)

---

## 📜 Compliance & Regulations

**For Healthcare Applications**:
- **HIPAA** (US): 45 CFR Parts 160, 162, 164
- **GDPR** (EU): Regulation (EU) 2016/679
- **DSGVO** (Germany): Bundesdatenschutzgesetz (BDSG)
- **PTV 10** (Germany): Psychotherapeutenvereinbarung

**Responsibility**: Users are responsible for ensuring compliance in their deployments. This repository provides templates and guidance, not legal advice.

---

## ✅ Safe to Use

**This repository is secure and safe to**:
- ✅ Use in production
- ✅ Share publicly
- ✅ Accept community contributions
- ✅ Deploy in enterprise environments

**With proper**:
- ✅ Secrets configuration (GitHub Secrets)
- ✅ Access controls (team permissions)
- ✅ Regular audits (quarterly minimum)
- ✅ Healthcare validation (for medical apps)

---

**Last Audited**: October 28, 2025
**Next Audit**: January 28, 2026
**Status**: ✅ Secure

For questions or concerns, please use GitHub Security Advisory or open an issue.
