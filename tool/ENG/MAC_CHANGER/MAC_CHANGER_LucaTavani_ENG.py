import subprocess
import re
import random
import platform
import sys

def generate_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(5))

def windows_mac_changer():
    print("\n[ WINDOWS MODE ]\n")
    try:
        output = subprocess.check_output("getmac", shell=True).decode()
        interfaces = re.findall(r'([0-9A-Fa-f:-]{17})\s+.*?([^\s]+)', output)

        print("Available interfaces:")
        for i, (mac, name) in enumerate(interfaces):
            print(f"{i}. {name} ({mac})")

        index = int(input("\nSelect the interface number: "))
        selected_interface = interfaces[index][1]
        current_mac = interfaces[index][0]
        new_mac = generate_mac()

        subprocess.call(f'netsh interface set interface "{selected_interface}" admin=disable', shell=True)
        subprocess.call(f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\0001" /v NetworkAddress /d {new_mac} /f', shell=True)
        subprocess.call(f'netsh interface set interface "{selected_interface}" admin=enable', shell=True)

        output_check = subprocess.check_output("getmac", shell=True).decode()
        if new_mac.lower() in output_check.lower():
            print(f"\n✅ MAC successfully changed to {new_mac}")
        else:
            print("\n⚠️ MAC address was not changed.")
            print("Your network adapter may not support this operation.")
            print("Suggestion: try a cheap USB or Ethernet adapter.")

    except Exception as e:
        print(f"[!] Error: {e}")

def linux_mac_changer():
    print("\n[ LINUX MODE ]\n")
    try:
        interfaces_output = subprocess.check_output("ip link", shell=True).decode()
        interfaces = re.findall(r'^\d+: (\w+):', interfaces_output, re.MULTILINE)

        print("Available interfaces:")
        for i, iface in enumerate(interfaces):
            print(f"{i}. {iface}")

        index = int(input("\nSelect the interface number: "))
        iface = interfaces[index]
        new_mac = generate_mac()

        print(f"Disabling {iface}...")
        subprocess.call(f"sudo ip link set dev {iface} down", shell=True)
        print(f"Setting new MAC: {new_mac}")
        subprocess.call(f"sudo ip link set dev {iface} address {new_mac}", shell=True)
        subprocess.call(f"sudo ip link set dev {iface} up", shell=True)

        final_mac = subprocess.check_output(f"cat /sys/class/net/{iface}/address", shell=True).decode().strip()
        if final_mac.lower() == new_mac.lower():
            print(f"\n✅ MAC successfully changed to {new_mac}")
        else:
            print("\n⚠️ MAC address was not changed.")
            print("You may need to install 'macchanger' or use sudo.")

    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    print("Supported operating systems:\n0. Linux\n1. Windows")
    choice = input("Select your OS (0 or 1): ")

    if choice == "0":
        linux_mac_changer()
    elif choice == "1":
        windows_mac_changer()
    else:
        print("❌ Invalid choice.")

    input("\n[Press ENTER to exit]")

if __name__ == "__main__":
    main()
