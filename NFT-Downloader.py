# Author : Akshay Arjun
# Can Contact Here: https://bit.ly/AkshayArjun
# Downloading NFTS DOESN'T make you the OWNER.
# THE AUTHOR IS NOT RESPONSILE FOR ANY MISUSE OF THIS CODE.
# BY USING THIS CODE YOU AGREE THAT YOU HAVE READ THESE COMMENTS AND UNDERSTOOD THAT THE AUTHOR DOESN'T HAVE ANY RESPONSIBLE FOR YOUR ACTIONS.
# Any actions and or activities related to this script is solely your responsibility. The misuse of this toolkit can result in criminal charges brought against the persons in question. The contributors will not be held responsible in the event any criminal charges be brought against any individuals misusing this toolkit to break the law.
# This toolkit contains materials that can be potentially damaging. Refer to the laws in your province/country before accessing, using,or in any other way utilizing this in a wrong way.
# the comments are for user understanding. You can uncomment PRINT statements to check what's happening.
from os.path import *
import os
import requests
import random
import sys
os.system('cls' if os.name == 'nt' else 'clear')
cryptopunks = "http://cryptopunks.app/cryptopunks/cryptopunk" #0-9999
meebits = "http://images.meebits.app/meebitimages/" #00001-10000 
download = int(input("Choose option to download all NFT's \n 1. Cryptopunks <=10000 \n 2. Meebits <=10000 \n "))
print("Note : Press CTRL+C to stop the program")
if download == 1:
    name = "Cryptopunks"
    str1 = cryptopunks
    ext = ".png"
    start = 0
    # folder creation
    try:
        folder_name = name
        print("Creating folder name "+name)
        os.mkdir(folder_name)
    except:
        print("Folder already exists ")
elif download == 2:
    name = "Meebits"
    str2 = "/full"
    ext = ".jpg"
    start = 1
    # folder creation
    try:
        print("Creating a folder named " + name )
        folder_name = name
        os.mkdir(folder_name)
    except:
        print("Folder already exists")
else :
    print("Wrong choice. Try again")
    exit()
COUNT = int(input("Enter no.of images : "))
# generating proxies
# REQUEST API
print(" Generating proxies to avoid ban")
rhttps = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all")
# HTTPS
https = []
https = rhttps.text
https = https.split()
lines = len(https)
print("Poxies generated")
try:
    if download == 2:
        COUNT = COUNT+1
        for i in range(start,COUNT):
            URL = meebits+str(i).zfill(5)+str2+ext
            #print(URL)
            path = "./"+name+"/"+str(i)+ext
            if os.path.exists(path):
                print("Found existing NFT on"+path)
                print("Skipping download of"+path)
            else:
               #print(path)
                f = open(path,'wb')
                proxy = https[random.choice([x for x in range(len(https))])]
                r = requests.get(URL,proxies={'https':proxy})
                #r = requests.get(URL,headers=headers)
                f.write(r.content)
                f.close()
                print("Downloaded "+str(i)+ext)
    else:
        for i in range(start,COUNT):
            URL=cryptopunks+str(i)+ext
            #print(URL)
            path = "./"+name+"/"+str(i)+ext
            if os.path.exists(path):
                print("Found existing NFT on"+path)
                print("Skipping download of"+path)
            else:
               #print(path)
                f = open(path,'wb')
                proxy = https[random.choice([x for x in range(len(https))])]
                r = requests.get(URL,proxies={'https':proxy})
                #print(r)
                f.write(r.content)
                f.close()
                print("Downloaded "+str(i)+ext)
except KeyboardInterrupt:
    print("Program stopped by user")
    sys.exit(1)
