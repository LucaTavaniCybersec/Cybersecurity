import sys

def generate_nmap_command(scan_type, detail_level, target_ip="TARGET_IP"):
    scan_flags = {
        "1": {"name": "Stealth", "basic": "-sS", "os": "-sS -O", "full": "-sS -Pn -n -T3 -A -v"},
        "2": {"name": "Medium", "basic": "-sS -T3", "os": "-sS -T3 -O", "full": "-sS -T3 -Pn -A -v"},
        "3": {"name": "Aggressiva", "basic": "-sS -T4", "os": "-sS -T4 -O", "full": "-sS -T4 -Pn -A -v"},
        "4": {"name": "Anti-Firewall", 
              "basic": "-sA -Pn -n -v", 
              "os": "-sS -Pn --scan-delay 1s --max-retries 2 -f", 
              "full": "-sT -Pn -D RND:10 -f --data-length 25"}
    }

    explanation = {
        "-sS": "TCP SYN (stealth)",
        "-sT": "TCP connect (meno stealth, utile dietro NAT/firewall)",
        "-T3": "Timing bilanciato (medium)",
        "-T4": "Timing aggressivo (fast)",
        "-sA": "TCP ACK scan (bypass firewall)",
        "-Pn": "No ping (per host ICMP-blocked)",
        "-n": "No DNS resolution",
        "-O": "OS detection",
        "-A": "Aggressiva: version detection, script, traceroute",
        "-v": "Verbose output",
        "-D": "Decoy IP per offuscare origine",
        "-f": "Frammentazione pacchetti",
        "--data-length": "Aggiunge padding per confondere i pattern",
        "--scan-delay": "Ritardo tra pacchetti (elusione IDS)",
        "--max-retries": "Numero massimo di ritrasmissioni"
    }

    detail_keys = {"1": "basic", "2": "os", "3": "full"}

    try:
        flags = scan_flags[scan_type][detail_keys[detail_level]]
        command = f"nmap {flags} {target_ip}"
        flag_explanation = "\n".join([f"- {flag} : {desc}" for flag, desc in explanation.items() if flag in flags])

        return f"""\n💡 Comando suggerito per {scan_flags[scan_type]['name']} - {detail_keys[detail_level]}:\n\n{command}\n\n📘 Spiegazione:\n{flag_explanation}\n"""
    except KeyError:
        return "Scelte non valide."

def main_menu():
    while True:
        print("\n== NMAP COMMAND GENERATOR ==")
        print("1. Stealth")
        print("2. Medium")
        print("3. Aggressiva")
        print("4. Anti-Firewall")
        print("0. Esci")
        scan_type = input("Seleziona il tipo di scansione (1-4): ")

        if scan_type == "0":
            print("Uscita...")
            sys.exit()

        print("\nLivello di dettaglio:")
        print("1. Basic (solo porte aperte)")
        print("2. OS Detection")
        print("3. Full (tutto incluso)")
        detail_level = input("Scegli il livello (1-3): ")

        target_ip = input("\nInserisci l'IP target (es. 192.168.1.10): ")

        result = generate_nmap_command(scan_type, detail_level, target_ip)
        print(result)

        input("Premi INVIO per tornare al menu principale...")

main_menu()
