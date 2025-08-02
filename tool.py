#Logo Desighn 

#Clear & Then Run Tools
# (module)
import os #for Clear
import sys#for Animation
import time#for Time

os.system("clear")

#Type With Animation
print("\n\n\n\n\n")
ab="                 \033[33m System Loading..........."

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)#Animation with Time
print("\n\n\n\n\n")

time.sleep(2)
os.system("clear")

ab="                   \033[1;32m Loading Completed"

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)#Animation with Time
Name=input("     \n\n\n            \033[1;31m Enter Your Name: ")
  
  
ab="             \033[1;32 Hey "+ Name +", Be Ethical...."

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\n\n")
time.sleep(2)
os.system("clear")

print("""
      :::::::::  :::    ::: ::::::::: 
     :+:    :+: :+:   :+:  :+:    :+: 
    +:+    +:+ +:+  +:+   +:+    +:+  
   +#++:++#:  +#++:++    +#+    +:+   
  +#+    +#+ +#+  +#+   +#+    +#+    
 #+#    #+# #+#   #+#  #+#    #+#     
###    ### ###    ### #########        
\n\n \033[1;32m============================                                                             \n Owner : RKD TEAM
 Github : Something
 Facebook :RKD TEAM
==============================
\033[0m""") 



#Basic Package Installer Tool
import os

os.system("clear")
os.system("pkg update -y && pkg upgrade -y")

# Base packages
os.system("pkg install -y git")
os.system("pkg install -y ruby")
os.system("pkg install -y python")
os.system("pkg install -y curl")
os.system("pkg install -y wget")
os.system("pkg install -y nano")
os.system("pkg install -y figlet")
os.system("pkg install -y toilet")
os.system("pkg install -y neofetch")
os.system("pkg install -y htop")

# Python & Ruby packages
os.system("pip install requests")
os.system("gem install lolcat")

print("\033[1;32mInstallation Complete!\033[0m ✅")
#এভাবে যত ইচ্ছা Command & Module যোগ করে দেয়া যাবে।

