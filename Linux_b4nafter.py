#!/usr/bin/python2
import subprocess
import os,sys
import socket

hst=socket.gethostname()

def snap_before_activity ():
    os.system("echo '######OS-VERSION-START######'>>/tmp/"+hst+"_before")
    os.system("cat /etc/*release >>/tmp/"+hst+"_before")
    os.system("echo '######OS-VERSION-END######'>>/tmp/"+hst+"_before")
    os.system("echo '######START-FILESYSTEM######'>>/tmp/"+hst+"_before")
    os.system("df -Ph >>/tmp/"+hst+"_before")
    os.system("echo '######END-FILESYSTEM######'>>/tmp/"+hst+"_before")
    os.system("echo '######START-NETSTAT######'>>/tmp/"+hst+"_before")
    os.system("netstat -nr >>/tmp/"+hst+"_before")
    os.system("echo '######END-NETSTAT######'>>/tmp/"+hst+"_before")
    os.system("echo '######START-IFCONFIG######'>>/tmp/"+hst+"_before")
    os.system("ifconfig -a>>/tmp/"+hst+"_before")
    os.system("echo '######END-IFCONFIG######'>>/tmp/"+hst+"_before")
    os.system("echo '######START-PVS######'>>/tmp/"+hst+"_before")
    os.system("pvs >>/tmp/"+hst+"_before")
    os.system("echo '######END-PVS######'>>/tmp/"+hst+"_before")
    os.system("echo '######START-VGS######'>>/tmp/"+hst+"_before")
    os.system("vgs >>/tmp/"+hst+"_before")
    os.system("echo '######END-VGS######'>>/tmp/"+hst+"_before")
    os.system("echo '######START-FDISK######'>>/tmp/"+hst+"_before")
    os.system("fdisk -l >>/tmp/"+hst+"_before")
    os.system("echo '######END-FDISK######'>>/tmp/"+hst+"_before")
    os.system("echo '######START-LVS######'>>/tmp/"+hst+"_before")
    os.system("lvs >>/tmp/"+hst+"_before")
    os.system("echo '######END-LVS######'>>/tmp/"+hst+"_before")
    os.system("echo '######START-FSTAB######'>>/tmp/"+hst+"_before")
    os.system("cat /etc/fstab >>/tmp/"+hst+"_before")
    os.system("echo '######END-FSTAB######'>>/tmp/"+hst+"_before")
    os.system("echo '######START-RESOLV######'>>/tmp/"+hst+"_before")
    os.system("cat /etc/resolv.conf >>/tmp/"+hst+"_before")
    os.system("echo '######END-RESOLV######'>>/tmp/"+hst+"_before")
    os.system("cp '/tmp/"+hst+"_before' /home/arulprakasam/")


##Color coding class START
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
##Color coding class END




def verify_after_activity():
    ##After activity verification code
    ##Filesystem
    currFS = subprocess.Popen(['df','-Ph'], stdout=subprocess.PIPE)
    currFS_out = currFS.communicate()[0].strip().split("\n")
    current_mnt =[line.split()[5] for line in currFS_out]
    with open("/tmp/"+hst+"_before", "r") as fo:
        oldFS = []
        copy = False
        for line in fo:
            if line.strip() == "######START-FILESYSTEM######":
                copy = True
            elif line.strip() == "######END-FILESYSTEM######":
                copy = False
            elif copy:
                oldFS.append(line)
    old_mnt =[line.strip().split()[5] for line in oldFS]
    if len(current_mnt) <= len(old_mnt):
	   for l in old_mnt:
		  if l not in current_mnt:
			 print bcolors.FAIL+ l + " is missing"+ bcolors.ENDC
	   print bcolors.OKGREEN + "Filesystem check OK"+ bcolors.ENDC
    elif len(current_mnt) > len(old_mnt):
	   for l in current_mnt:
		  if l not in old_mnt:
			 print bcolors.OKBLUE+ l + " newly added FS"+ bcolors.ENDC
    else:
	   print "Everything's fine"
    ##Filesystem


def Usage():
    print bcolors.WARNING+sys.argv[0] + " requires single argument to run. \nuse '-b' before activity & '-a' After activity  \n"+bcolors.ENDC   		


if (len(sys.argv[1:])==0 or sys.argv[1]=='-h'):
    Usage()
elif(len(sys.argv)==2):
    if(sys.argv[1]=='-b'):
        if (os.path.isfile("/tmp/"+hst+"_before")):
            print bcolors.WARNING+"WARNING already before file exists.\n"+bcolors.ENDC
        else:
            snap_before_activity()
    elif (sys.argv[1]=='-a'):
        verify_after_activity()
else:
    Usage()
    
