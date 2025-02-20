import requests
import webbrowser
from bs4 import BeautifulSoup

print("🚀 This is Our Powerful OSINT Tool for Cyber Recon")

# Define functions before they are used
def netcraft(domain):
    """Fetches Netcraft Report and Opens in Chrome"""
    site = f"https://sitereport.netcraft.com/?url={domain}"
    print(site)  # Print the link
    webbrowser.open(site)  # Open in Chrome
    return {"Netcraft URL": site}

def dnslookup(domain):
    """Fetches DNS  Report and Opens in Chrome"""
    site = f"https://www.nslookup.io/domains/{domain}/dns-records/"
    print(site)  # Print the link
    webbrowser.open(site)  # Open in Chrome
    return {"DNSLOOKUP URL": site}

def pwend(domain):
    """Fetches Data is Breached or not and Opens in Chrome"""
    site = f"https://haveibeenpwned.com/"
    print(site)  # Print the link
    webbrowser.open(site)  # Open in Chrome
    return {"Data breach information": site}

# 🌐 Get User Input
print("1>>>For Email_id's information")
print("2>>>For Any Particular Website information")
m = int(input("Enter your choice: "))

match m:
    case 1:
        domain = input("Enter your E-mail_id here ::::::: ").strip()
        print("Select options Related to Email")
        print("1>>Check Data Breached or not")
        h = int(input("Enter your choice: "))

        match h:
            case 1:
                pwend_data = pwend(domain)

    case 2:
        domain = input("Enter your Website here ::::::: ").strip()
        print("Select your options related to Your Target")
        print("1. Show website-related information like Server Info, Country, etc. (Netcraft)")
        print("2. Show DNS-related information of Your Target")

        n = int(input("Enter your choice: "))

        match n:
            case 1:
                netcraft_data = netcraft(domain)
            case 2:
                dnslookup_data = dnslookup(domain)
