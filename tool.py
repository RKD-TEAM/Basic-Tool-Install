# RKD Basic Tool Installer
# By Mr. Rakibul Islam

import os
import sys
import time
import shutil

# -------------------
# Utility Functions
# -------------------
def animate_text(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def install_section(title, commands):
    print(f"\n\033[1;36m[{title}]\033[0m")
    choice = input("👉 \033[1;92mPress Enter to install, \033[31m0 to Exit: \033[0m").strip()
    if choice == "0":
        print("\033[91m❌ Exiting tool...\033[0m")
        sys.exit()
    else:  # Enter or anything else triggers installation
        for cmd in commands:
            os.system(cmd)
        print(f"\033[1;32m✔ {title} installation completed!\033[0m\n")

# -------------------
# Clear Screen + Animation
# -------------------
os.system("clear")
print("\n\n\n\n\n")
animate_text("                 \033[36m System Loading...........", 0.1)
print("\n\n\n\n\n")
time.sleep(2)
os.system("clear")
animate_text("                   \033[1;32m Loading Completed", 0.1)

# -------------------
# Name Input
# -------------------
while True:
    Name = input("     \n\n\n            \033[1;36m Enter Your Name: ").strip()
    if Name:
        break
    else:
        print("\033[91m      Name can't be empty. Please enter your name.\033[0m")

animate_text(f"\033[1;32m             Hey {Name}, Be Ethical....\033[0m", 0.1)
print("\n\n\n")
time.sleep(2)
os.system("clear")

# -------------------
# Logo
# -------------------
columns = shutil.get_terminal_size().columns
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
print(" Tool Name : Basic Tool Installer (130+ Packages)")
print("\033[32m" + "=" * columns + "\033[0m")
print("\033[1;91m!!!   This tool is for educational purposes only   !!!!!!   So don't use it for any illegal activities   !!!")
print("\033[32m" + "=" * columns + "\033[0m")

# -------------------
# Sections
# -------------------
SECTIONS = {
    "System Update": ["pkg update -y && pkg upgrade -y"],
    "Base Packages": [
        "pkg install -y git", "pkg install -y ruby", "pkg install -y python",
        "pkg install -y python2", "pkg install -y python-pip", "pkg install -y curl",
        "pkg install -y wget", "pkg install -y nano", "pkg install -y vim",
        "pkg install -y neovim", "pkg install -y emacs", "pkg install -y figlet",
        "pkg install -y toilet", "pkg install -y neofetch", "pkg install -y htop",
        "pkg install -y tree", "pkg install -y zip unzip", "pkg install -y tar",
        "pkg install -y gzip", "pkg install -y bzip2", "pkg install -y unrar",
        "pkg install -y cmatrix", "pkg install -y w3m", "pkg install -y lynx",
        "pkg install -y bc", "pkg install -y bcftools", "pkg install -y dialog",
        "pkg install -y bash-completion", "pkg install -y toilet-fonts"
    ],
    "Networking Tools": [
        "pkg install -y openssh", "pkg install -y tsu", "pkg install -y proot",
        "pkg install -y dnsutils", "pkg install -y net-tools", "pkg install -y iproute2",
        "pkg install -y nmap", "pkg install -y netcat", "pkg install -y tcpdump",
        "pkg install -y socat", "pkg install -y openvpn", "pkg install -y tor",
        "pkg install -y torsocks", "pkg install -y whois", "pkg install -y traceroute",
        "pkg install -y wgetrc", "pkg install -y curlftpfs"
    ],
    "Development Tools": [
        "pkg install -y clang", "pkg install -y gcc", "pkg install -y g++",
        "pkg install -y make", "pkg install -y cmake", "pkg install -y automake",
        "pkg install -y autoconf", "pkg install -y pkg-config", "pkg install -y gdb",
        "pkg install -y strace", "pkg install -y ltrace", "pkg install -y perl",
        "pkg install -y lua", "pkg install -y nodejs", "pkg install -y yarn",
        "pkg install -y php", "pkg install -y golang", "pkg install -y rust",
        "pkg install -y kotlin", "pkg install -y clojure"
    ],
    "Extra Utilities": [
        "pkg install -y jq", "pkg install -y fzf", "pkg install -y ranger",
        "pkg install -y mc", "pkg install -y ncurses-utils", "pkg install -y termux-api",
        "pkg install -y imagemagick", "pkg install -y ffmpeg", "pkg install -y sox",
        "pkg install -y aria2", "pkg install -y rsync", "pkg install -y screen",
        "pkg install -y tmux", "pkg install -y parallel", "pkg install -y ripgrep",
        "pkg install -y fd", "pkg install -y bat", "pkg install -y exa",
        "pkg install -y pv", "pkg install -y ncdu", "pkg install -y dust",
        "pkg install -y hping3", "pkg install -y wgetpaste", "pkg install -y whoami"
    ],
    "Python & Ruby Packages": [
        "pip install --upgrade pip", "pip install requests", "pip install bs4",
        "pip install lxml", "pip install rich", "pip install colorama", "pip install tqdm",
        "pip install pycryptodome", "pip install httpx", "pip install flask",
        "pip install django", "pip install scapy", "pip install pillow", "pip install numpy",
        "pip install pandas", "pip install matplotlib", "pip install seaborn",
        "pip install ipython", "pip install jupyter", "pip install sympy",
        "pip install networkx", "pip install paramiko", "gem install lolcat"
    ]
}

# -------------------
# Run Installer
# -------------------
for section_title, commands in SECTIONS.items():
    install_section(section_title, commands)

print("\n\033[1;32m🎉 All selected installations finished successfully!\033[0m ✅")
