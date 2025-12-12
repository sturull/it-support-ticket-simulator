# Laptop Hardware Troubleshooting Playbook

## 1. Common User Symptoms
- Screen flickering or blinking  
- Laptop won’t power on  
- Battery not charging  
- Overheating or fan constantly running  
- USB ports not reading devices  
- Random shutdowns or freezes  

---

## 2. Initial Questions
Ask the user:
1. When did the issue begin?  
2. Has the laptop been dropped or damaged?  
3. Are they using the original charger?  
4. Does the issue happen on battery, AC power, or both?  
5. Has anything new been installed recently?  

---

## 3. Basic Troubleshooting
### Power Issues
- Check power cable connection  
- Try a known-good charger  
- Remove the battery (if removable) and power reset:  
  - Hold power button 10–15 seconds  
- Verify power light indicators

### Display Issues
- Check brightness keys  
- Connect external monitor  
- Toggle display output (`Windows + P`)  
- Boot into BIOS to rule out OS-level problem  

---

## 4. Intermediate Troubleshooting
### Battery Diagnostics
- Windows: `powercfg /batteryreport`  
- Check battery health in BIOS  
- Confirm wattage matches factory spec  

### Overheating
- Inspect air vents for dust  
- Ensure laptop is on a hard surface  
- Check CPU usage in Task Manager  

### USB / Peripheral Problems
- Test ports with multiple devices  
- Update chipset & USB drivers  
- Disable USB selective suspend  

---

## 5. Advanced Troubleshooting
### SSD / Storage Issues
- Run SMART check  
- Check event viewer for disk warnings  
- Boot into recovery environment if OS isn’t loading  

### RAM / Memory
- Reseat RAM (if accessible)  
- Run Windows Memory Diagnostic  

### Motherboard / Hardware Failure Signs
- No POST  
- Burning smell  
- Liquid damage  

---

## 6. Escalation Criteria
Escalate if:
- Hardware component failure is confirmed  
- Screen or motherboard must be replaced  
- Laptop fails POST or BIOS access  
- Battery is swollen  
- Data backup or recovery is required  

---

## 7. Resolution Documentation
Include:
- Root cause  
- Troubleshooting steps taken  
- Hardware replaced (if any)  
- Tests confirming the fix  
