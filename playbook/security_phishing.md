# Phishing Incident Response Playbook

## 1. User Symptoms
- User received suspicious email  
- Email contains unexpected attachments or links  
- User clicked a link and entered credentials  
- User reports unusual account behavior  
- MFA push notifications they didn’t request  

---

## 2. Immediate Actions
1. Instruct user **not to interact further** with the email  
2. Capture a screenshot of the message  
3. Ask user if they clicked anything  
4. Ask if they entered credentials  
5. Ask if anything downloaded automatically  

---

## 3. Containment
If the user **clicked a link**:
- Disconnect device from network if malware is suspected  
- Change password immediately  
- Invalidate all active sessions  
- Confirm MFA is working  

If an **attachment was opened**:
- Run full antivirus scan  
- Check for unusual processes  
- Review browser downloads  
- Inspect quarantine logs  

---

## 4. Investigation
### Email Header Analysis
- Verify sender domain  
- Check SPF/DKIM/DMARC results  
- Look for spoofed “display names”  

### URL Inspection
- Hover to reveal full URL  
- Use safe tools (VirusTotal, URLscan)  
- Check for typosquatting domains  

### Account Activity
- Check login locations  
- Look for failed login attempts  
- Review authentication logs  

---

## 5. Remediation
Depending on findings:
- Reset password + MFA  
- Revoke OAuth tokens  
- Remove suspicious extensions or apps  
- Block sender domain  
- Create mail filter rules  
- Delete phishing email from mailbox + trash  

---

## 6. Escalation Criteria
Escalate to security team if:
- User entered credentials into a fake login page  
- Multiple users received the same phishing email  
- Malware executed or downloaded  
- Indicators of compromise found  
- Account takeover suspected  

---

## 7. Documentation Requirements
Record:
- Phishing email type (link, attachment, credential harvest)  
- User impact  
- Steps taken  
- Whether password reset was required  
- Log findings  
- Final status (contained / escalated / resolved)  
