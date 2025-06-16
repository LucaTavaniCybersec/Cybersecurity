import sys

def generate_nmap_command(scan_type, detail_level, target_ip="TARGET_IP"):
    scan_flags = {
        "1": {"name": "Stealth", "basic": "-sS", "os": "-sS -O", "full": "-sS -Pn -n -T3 -A -v"},
        "2": {"name": "Medium", "basic": "-sS -T3", "os": "-sS -T3 -O", "full": "-sS -T3 -Pn -A -v"},
        "3": {"name": "Aggressive", "basic": "-sS -T4", "os": "-sS -T4 -O", "full": "-sS -T4 -Pn -A -v"},
        "4": {
            "name": "Anti-Firewall",
            "basic": "-sA -Pn -n -v",
            "os": "-sS -Pn --scan-delay 1s --max-retries 2 -f",
            "full": "-sT -Pn -D RND:10 -f --data-length 25"
        }
    }

    explanation = {
        "-sS": "TCP SYN scan (stealth)",
        "-sT": "TCP connect scan (less stealthy, useful behind NAT/firewalls)",
        "-T3": "Balanced timing (medium)",
        "-T4": "Aggressive timing (fast)",
        "-sA": "TCP ACK scan (used to map firewall rules)",
        "-Pn": "No ping (skip host discovery, useful if ICMP is blocked)",
        "-n": "Skip DNS resolution",
        "-O": "OS detection",
        "-A": "Aggressive scan: version detection, script scan, traceroute",
        "-v": "Verbose output",
        "-D": "Use decoy IPs to obfuscate origin",
        "-f": "Fragment packets",
        "--data-length": "Add custom padding to confuse fingerprinting",
        "--scan-delay": "Delay between packets (IDS evasion)",
        "--max-retries": "Limit max retransmissions"
    }

    detail_keys = {"1": "basic", "2": "os", "3": "full"}

    try:
        flags = scan_flags[scan_type][detail_keys[detail_level]]
        command = f"nmap {flags} {target_ip}"
        flag_explanation = "\n".join(
            [f"- {flag} : {desc}" for flag, desc in explanation.items() if flag in flags]
        )

        return f"""\n💡 Suggested command for {scan_flags[scan_type]['name']} - {detail_keys[detail_level]} level:\n\n{command}\n\n📘 Flag explanation:\n{flag_explanation}\n"""
    except KeyError:
        return "❌ Invalid selection. Please try again."

def main_menu():
    while True:
        print("\n== NMAP COMMAND GENERATOR ==")
        print("1. Stealth")
        print("2. Medium")
        print("3. Aggressive")
        print("4. Anti-Firewall")
        print("0. Exit")
        scan_type = input("Choose scan type (1-4): ")

        if scan_type == "0":
            print("Exiting...")
            sys.exit()

        print("\nScan detail level:")
        print("1. Basic (open ports only)")
        print("2. OS Detection")
        print("3. Full (everything included)")
        detail_level = input("Choose level (1-3): ")

        target_ip = input("\nEnter the target IP (e.g., 192.168.1.10): ")

        result = generate_nmap_command(scan_type, detail_level, target_ip)
        print(result)

        input("Press ENTER to return to main menu...")

main_menu()
