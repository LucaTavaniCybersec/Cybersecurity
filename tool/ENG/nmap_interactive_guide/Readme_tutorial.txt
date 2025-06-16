-------------------------------------------------------------
NMAP INTERACTIVE GUIDE - by Luca Tavani
-------------------------------------------------------------

Description:
This Python script generates custom Nmap commands based on user choices.
It does NOT run automatic scans, but helps users quickly build the correct
Nmap command for their target and scan style.

Use cases:
- Learn Nmap flags easily
- Avoid typing mistakes
- Great support for students and junior pentesters

-------------------------------------------------------------
REQUIREMENTS
-------------------------------------------------------------
- OS: Linux (recommended: Kali, POP_OS, Ubuntu)
- Python 3 installed (check with: python3 --version)
- Nmap installed (sudo apt install nmap)

-------------------------------------------------------------
HOW TO USE IT
-------------------------------------------------------------
1. Download or clone the file nmap_interactive_guide_LucaTavani.py
2. Open a terminal
3. Move to the correct folder (example: cd ~/Downloads)
4. Launch the script:
   python3 nmap_interactive_guide_LucaTavani.py
5. Follow the on-screen instructions

-------------------------------------------------------------
SAMPLE OUTPUT
-------------------------------------------------------------
Suggested command for Stealth - full:
nmap -sS -Pn -n -T3 -A -v 192.168.1.10

Flag explanation:
- -sS : TCP SYN scan (stealth)
- -Pn : No ping (for ICMP-blocked hosts)
- -n  : Skip DNS resolution
- -T3 : Balanced timing
- -A  : OS detection, version detection, scripts, traceroute
- -v  : Verbose output

-------------------------------------------------------------
ETHICAL & LEGAL DISCLAIMER
-------------------------------------------------------------
This tool is for educational and defensive purposes only.
Do not use it on networks or systems you don’t own unless
you have explicit legal permission.

You are fully responsible for how you use it.

Always test in virtual environments or authorized labs.

-------------------------------------------------------------
AUTHOR
-------------------------------------------------------------
Luca Tavani - https://github.com/LucaTavaniCybersec/Cybersecurity

-------------------------------------------------------------

