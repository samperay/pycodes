# Linux Hardening Checklist

## System Installations 
- Check for the latest version of OS installed
- Verify /tmp partition:
  - [ ] /tmp to be a seperate partition.
  - [ ] 'noexec' to be set on the /tmp partition.
  - [ ] 'nosuid' to be set on the /tmp partition. 
- Check for seperate volumes on /var, /var/log, /home
- Check for sticky bit 

## OS Hardening 
- Verify these services are installed(telnet­server; rsh, rlogin, rcp; ypserv, ypbind; tftp, tftp­server; talk and talk­server)
- Remove above services if they are installed. 
- Ensure syslog,rsyslog services are running. 

## User and Group Access 
- Enforce the use of strong password.
- Limit root users to access sudo 
- Warning Banner for users login
- Root login to be disabled for all users. 

# Reference 

- https://github.com/trimstray/linux-hardening-checklist
- https://www.ucd.ie/t4cms/UCD%20Linux%20Security%20Checklist.pdf
- https://gato-docs.its.txstate.edu/vpit-security/training/server-security/sans-linux-checklist/SANS_Linux_checklist.pdf


