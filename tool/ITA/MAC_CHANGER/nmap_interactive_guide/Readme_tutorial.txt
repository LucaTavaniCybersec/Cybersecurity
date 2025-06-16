-------------------------------------------------------------
NMAP INTERACTIVE GUIDE - by Luca Tavani
-------------------------------------------------------------

Descrizione:
Questo script Python genera comandi Nmap personalizzati sulla base delle esigenze dell'utente.
Non esegue scansioni automatiche, ma aiuta a scrivere rapidamente il comando giusto in base
al tipo di scansione desiderata e al livello di dettaglio richiesto.

Utilità:
- Apprendimento dei flag Nmap
- Riduzione degli errori di battitura
- Supporto per studenti e junior pentester

-------------------------------------------------------------
REQUISITI
-------------------------------------------------------------
- Sistema operativo: Linux (consigliato Kali, POP_OS, Ubuntu)
- Python 3 installato (verifica con: python3 --version)
- Nmap installato (sudo apt install nmap)

-------------------------------------------------------------
COME UTILIZZARLO
-------------------------------------------------------------
1. Scarica o clona il file nmap_interactive_guide_LucaTavani.py nella cartella desiderata
2. Apri il terminale
3. Spostati nella cartella (esempio: cd ~/Downloads)
4. Avvia lo script con:
   python3 nmap_interactive_guide_LucaTavani.py
5. Segui le istruzioni a schermo

-------------------------------------------------------------
ESEMPIO OUTPUT
-------------------------------------------------------------
Comando suggerito per Stealth - full:
nmap -sS -Pn -n -T3 -A -v 192.168.1.10

Spiegazione flag:
- -sS : TCP SYN scan (stealth)
- -Pn : Disabilita il ping (utile se host non risponde a ICMP)
- -n  : Disabilita DNS resolution
- -T3 : Timing bilanciato
- -A  : OS detection, version detection, script scanning, traceroute
- -v  : Verbose output

-------------------------------------------------------------
DISCLAIMER ETICO E LEGALE
-------------------------------------------------------------
Questo strumento è stato realizzato per scopi didattici e difensivi.
Non utilizzare su sistemi o reti che non ti appartengono, a meno di
contratto legale esplicito.

L'utilizzo è sotto la tua piena responsabilità.

Si raccomanda l'uso in ambienti di laboratorio o VM autorizzate.

-------------------------------------------------------------
AUTORE
-------------------------------------------------------------
Luca Tavani - https://github.com/LucaTavaniCybersec/Cybersecurity

-------------------------------------------------------------

