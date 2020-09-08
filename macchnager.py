import subprocess #to invoke system commands
import optparse #parsing command line arguments
import re



def inputparser():#Parsing Command Line arguments
    parse=optparse.OptionParser();
    parse.add_option("-i","--interface",dest="inter",help="To check Interface use ifconfig or ipconfig. eg eth0,wlan0 etc.")
    parse.add_option("-m","--mac",dest="nmac",help="Specify the new mac address that has to be spoofed");
    return parse.parse_args();

def check_change(inter,nmac):
    cmd=subprocess.check_output(["ifconfig",inter])
    cmd2=cmd.decode('utf-8')
    mac_valu=re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",cmd2)
   
    
    if (mac_valu[0]==nmac):
        print("[+]Change successfull")
    else :
        print("Error changing Mac , specify Mac in this format XX:XX:XX:XX:XX:XX")
    


    
def mac_changer(inter,nmac): # function to change the mac addr
    print("[+]Changing Mac Address of "+inter+" to "+nmac);
    #Prebuit Commands
    subprocess.run(["ifconfig",inter,"down"])
    subprocess.run(["ifconfig",inter,"hw","ether",nmac]);
    subprocess.run(["ifconfig",inter,"up"])
    check_change(inter,nmac);

#storing input
data=inputparser()
inter=data[0].inter
nmac=data[0].nmac;

if (not inter and not nmac):
    print("Please Specify Both Interface and Mac")
    print("Use -h form more details")
else :
    mac_changer(inter,nmac)









