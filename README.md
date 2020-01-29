# My Python Learning

Here are some of the detailed information about the programs I have written. I don't consider myself a programmer, But I have started using these little programs as a experiment in using/learning or solving problem myself using Python. I would be glad to accept pointers from others to improve code and make it more efficient. If you would like to suggest me please feel free to email me at **sunlnx@gmail.com**

In each program at the beginning, comments are marked to know what this code would be used for.

These examples are being written/tested in python3.5. 

## sysadmin:

These below scripts can be used for **Linux System Administration** and have provided brief comment on what each code would do.
If the code seems to be having referenced with more files, shall be created with a directory and will be placed over there.

**getsysinfo.py** Provides the basic information on the system

**search_replace.py** Search for a particular pattern in a file, on success take a backup and append in same file

**find_duplicates.py** lists duplicate files from folder specified

**filechecksum.py** compare files using checksum

**list_files_dirs.py** choice to provide either listing of files and directories

**backup_compress.py** make backup copy of folder and compress .gzip format

**deletefilesNdays.py** remove files older than X days

**remotessh.py** execute command in remote through SSH 

**rsync.py** sync two directories and email when synced

**searchlogs.py** search for a pattern in log folders

**yumlocalrepo.py** create local repository on Redhat/Centos Linux

**smbversionchk.py** check the minor version of samba and add necessary patch if required

**addparamconfig.py** adds the parameter to apache config without duplicating any parameter

**appendConfig_rsyslog.py** appends the entry to rsyslog.conf without any duplications

**revertConfig_rsyslog.py** revert from main config file if it exists

**portscanner.py** scans the open port on the hosts.

**authlockfix.py** modifies pam module for autolock featuring for failed logins

**changeGRUBdefaultKernel.py** Lets you know the current default GRUB entry and you can set your default GRUB leven on which listed/installed kernels

**replaceDNSentry.py** you can search and replace your existing DNS entry in /etc/resolv.conf to your new DNS resolver

# Python-Interview-Questions

This, subfolder consists some of the *python Interview Questions* which are being asked during your interview. One can refer this folder as a python refresher..

You can practice this code using *juypter* notebook. 

you can start this repo using this below code.

```
git clone https://github.com/samperay/practice-python.git
cd interviews
source bin/activate
jupyter notebook
```

Now, by default there would be a tab being opened in your browser. You can practice or work on the code. 



