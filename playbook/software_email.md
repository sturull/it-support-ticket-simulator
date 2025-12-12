# Email Troubleshooting Playbook

## 1. Common User Symptoms
- Email not syncing on mobile device  
- Outlook stuck on “Trying to connect…”  
- Unable to send/receive messages  
- Authentication prompts looping  
- Missing emails or delayed delivery  

---

## 2. Initial Questions
Ask:
1. Is this issue on mobile, desktop, or both?  
2. Has the password been changed recently?  
3. Are other apps or services working normally?  
4. When was the device last rebooted?  
5. Has this happened before?  

---

## 3. Basic Troubleshooting
### Step 1 — Restart & reconnect  
- Restart the device  
- Reconnect to Wi-Fi or cellular data  

### Step 2 — Confirm credentials  
- Verify user is using the correct, current password  
- Check MFA (multi-factor) device status  

### Step 3 — Check storage  
- Full mailbox or mobile storage can block syncing  

---

## 4. Intermediate Troubleshooting
### Outlook Issues
- Clear credential manager entries  
- Run Outlook in safe mode  
- Rebuild profile or repair account  
- Check for add-ins causing issues  

### Mobile Email
- Remove & re-add the mail account  
- Ensure correct server settings  
- Confirm ActiveSync/IMAP is enabled  

### Sending/Receiving Failures
- Check mail server status  
- Verify user is not blocked for spam  
- Confirm mailbox quota  

---

## 5. Advanced Troubleshooting
### Server/Cloud Provider
- Review mail logs  
- Check for throttling or rate limits  
- Validate DNS records (MX, SPF, DKIM, DMARC)  

### Client-Side
- Check OST/PST corruption  
- Rebuild search index  
- Examine firewall or VPN interference  

---

## 6. Escalation Criteria
Escalate if:
- Authentication fails despite known-good credentials  
- Mailbox corruption suspected  
- MFA token malfunction  
- Provider outage confirmed  
- DNS misconfiguration suspected  

---

## 7. Documentation Requirements
Record:
- Impacted platform (mobile/desktop)  
- Root cause  
- Steps taken  
- Profile rebuild or server fix details  
- Confirmation of successful send/receive  
