# Wi-Fi Troubleshooting Playbook

## 1. User Symptoms
- Intermittent Wi-Fi drops  
- Slow speeds  
- Cannot connect to SSID  
- Devices repeatedly ask for password  

---

## 2. Initial Questions
Ask the user:
1. When did the issue start?  
2. Are other users affected?  
3. Are they using 2.4GHz, 5GHz, or guest Wi-Fi?  
4. Has the device recently moved locations?  
5. Do they experience issues on mobile, laptop, or both?

---

## 3. Basic Troubleshooting
### Step 1 — Verify wireless is enabled  
- Check device Wi-Fi toggle  
- Forget/rejoin the network  

### Step 2 — Confirm network credentials  
- Ensure correct SSID  
- Check if password was recently updated  

### Step 3 — Test another device  
- Confirms whether the issue is user-specific or network-wide  

---

## 4. Intermediate Troubleshooting
### Signal & Interference
- Check signal strength (RSSI)  
- Look for interference (microwaves, cordless phones, walls, metal)  
- Move user closer to AP temporarily  

### DHCP & IP issues
- `ipconfig /release` / `ipconfig /renew` (Windows)  
- `ip a` (Linux)  
- Check if user is getting APIPA (169.x.x.x)  

---

## 5. Advanced Troubleshooting
### Check access point load
- Too many clients can cause random drops  

### Check roaming
- Device bouncing between APs too quickly  
- Adjust roaming aggressiveness if needed  

### Channel & Bandwidth
- Review 2.4GHz channel congestion  
- Move device to 5GHz when possible  

---

## 6. Escalation Criteria
Escalate to network engineering if:
- Multiple users are affected  
- AP stays in “degraded” or “down” state  
- DHCP scope exhausted  
- Controller logs show high interference or radio failure  

---

## 7. Resolution Documentation
Record:
- Root cause  
- Steps taken  
- Final action (reset AP, adjusted channel, device driver update, etc.)  
- Verification that issue is resolved  
