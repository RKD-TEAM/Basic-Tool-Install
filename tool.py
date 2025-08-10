#Logo Desighn 

#Clear & Then Run Tools
# (module)
import os #for Clear
import sys#for Animation
import time#for Time
import shutil

os.system("clear")

#Type With Animation
print("\n\n\n\n\n")
ab="                 \033[36m System Loading..........."

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

# Name Input
while True:
    Name=input("     \n\n\n            \033[1;36m Enter Your Name: ").strip()
    if Name:
        break
    else:
        print("\033[91m      Name can't be empty. Please enter your name.\033[0m")
  
ab="\033[1;32m             Hey "+ Name +", Be Ethical....\033[0m"

for c in ab:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.1)
print("\n\n\n")
time.sleep(2)
os.system("clear")

# Terminal width
columns = shutil.get_terminal_size().columns

# RKD logo
logo_lines = [
    ":::::::::  :::    ::: ::::::::: ",
    ":+:    :+: :+:   :+:  :+:    :+:",
    "+:+    +:+ +:+  +:+   +:+    +:+",
    "+#++:++#:  +#++:++    +#+    +:+",
    "+#+    +#+ +#+  +#+   +#+    +#+",
    "#+#    #+# #+#   #+#  #+#    #+#",
    "###    ### ###    ### #########"
]

print("\033[1;91m")
for line in logo_lines:
    print(line.center(columns))
print("\033[0m")

print("\033[32m" + "=" * columns + "\033[1;96m")
print(" Owner     : Mr.Rakibul Islam")
print(" Github    : https://github.com/RKD-TEAM")
print(" Facebook  : Alex Rk Khan")
print(" Tool Name : _____________")
print("\033[32m" + "=" * columns + "\033[1;96m")
print("\033[31m!!!   This tool is for educational purposes only   !!!!!!   So don't use it for any illegal activities   !!!")
print("\033[32m" + "=" * columns + "\033[0m")


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

