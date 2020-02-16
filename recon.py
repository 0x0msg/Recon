import subprocess
import os


def main():
    target=input("Enter the target URL")
    sublister(target)
    amass(target)
    #crtndstry(target)  //closing this due to invalid numeric literal error
    knock(target)
    subbrute(target)
    crtsh(target)
    certspotter(target)
    assetfinder(target)

def sublister(target):
    subprocess.run(['sublist3r','-d',target,'-o','sublister.txt'])

def amass(target):
    subprocess.run(['amass','enum','-d',target,'-o','amass.txt'])

def crtndstry(target):
    os.chdir('/crtndstry')
    subprocess.run(['./crtndstry.sh',target,'|','tee','-a','crtndstry.txt'])

def crtsh(target):
    command_crtsh=r"curl -s https://crt.sh/\?q\=\%."+target+"\&output\=json | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | tee -a crtsh.txt"
    os.system(command_crtsh)

def certspotter(target):
    command_cerspotter="curl -s https://certspotter.com/api/v0/certs\?domain\="+target+" | jq '.[].dns_names[]' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u | grep "+target+" | tee -a certspotter.txt"
    os.system(command_cerspotter)

def knock(target):
    virustotal_api=input("Did you enter the virustotal API Key in config.json(Y/N)")
    if(virustotal_api=="Y"):
        subprocess.run(['knockpy','-c',target])
    else:
        pass

def assetfinder(target):
    command_assetfinder=r"assetfinder --subs-only "+target+" | tee -a assetfinder.txt"
    os.system(command_assetfinder)

def subbrute(target):
    domain_brute=input("Do you want to bruteforce subdomains using subrute(Y/N)")
    if(domain_brute=="Y"):
        os.chdir('subbrute/')
        subprocess.run(['python','subbrute.py',target,'-o','../subbrute.txt'])

    else:
        pass


main()