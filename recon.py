import subprocess
import os

def main():
    target=input("Enter the target URL")
    sublister(target)
    amass(target)
    #crtndstry(target)  //closing this due to invalid numeric literal error
    knock(target)
    subbrute(target)

def sublister(target):
    subprocess.run(['sublist3r','-d',target,'-o','sublister.txt'])

def amass(target):
    subprocess.run(['amass','enum','-d',target,'|','tee','-a','amass.txt'])

def crtndstry(target):
    os.chdir('/crtndstry')
    subprocess.run(['./crtndstry.sh',target,'|','tee','-a','crtndstry.txt'])

def knock(target):
    virustotal_api=input("Did you enter the virustotal API Key in config.json(Y/N)")
    if(virustotal_api=="Y"):
        subprocess.run(['knockpy','-c',target])
    else:
        pass

def subbrute(target):
    domain_brute=input("Do you want to bruteforce subdomains using subrute(Y/N)")
    if(domain_brute=="Y"):
        os.chdir('subbrute/')
        subprocess.run(['python','subbrute.py',target,'-o','../subbrute.txt'])

    else:
        pass


main()