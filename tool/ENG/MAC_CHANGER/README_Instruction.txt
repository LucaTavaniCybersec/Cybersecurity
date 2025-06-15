==========================
 MAC ADDRESS CHANGER TOOL
==========================

Description:
This is a Python script that changes the MAC address of your network interface (Wi-Fi, Ethernet, etc.), compatible with both Windows and Linux (POP_OS, Kali, Ubuntu, etc.).

IMPORTANT:
- Some modern network adapters (e.g. Realtek WiFi 6) do not allow software-based MAC address changes. In these cases, the tool will notify you.
- This tool was designed for ethical and defensive purposes, such as protecting privacy on public networks.

HOW TO USE

1. Make sure Python is installed on your system:
   - On Windows: https://www.python.org/downloads
   - On most Linux distros, it is already preinstalled.

2. Download the file mac_changer.py to your preferred folder (e.g. Download, Desktop, Tool, etc.)

3. Open the terminal or command prompt:
   - On Windows: search for "Command Prompt", right-click, and choose "Run as administrator"
   - On Linux: open the Terminal (CTRL + ALT + T)

4. Navigate to the folder where you downloaded the file:
   - Example on Linux: cd ~/Download
   - Example on Windows: cd C:\Users\YOUR_NAME\Downloads

5. Run the script with Python:
   python mac_changer.py
   or, if you have multiple versions:
   python3 mac_changer.py

6. Follow the on-screen instructions:
   - Select your operating system (0 = Linux, 1 = Windows)
   - Choose your network interface (Wi-Fi, Ethernet, VPN, etc.)
   - The tool will generate a new MAC address and attempt to apply it
   - At the end, it will confirm if the change was successful

7. Press ENTER to close the script.

AUTHOR

Luca Tavani – https://github.com/LucaTavaniCybersec/Cybersecurity

This script is open-source and modifiable, but please use it responsibly. Anonymity is a right — not an excuse.

