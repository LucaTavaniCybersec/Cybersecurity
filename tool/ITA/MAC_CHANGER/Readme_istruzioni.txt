==========================
 MAC ADDRESS CHANGER TOOL
==========================

Descrizione:
Questo è uno script Python per cambiare il MAC address della tua interfaccia di rete (Wi-Fi, Ethernet, ecc.), compatibile sia con Windows che con Linux (POP_OS, Kali, Ubuntu, ecc.).

ATTENZIONE:
- Alcuni adattatori di rete (es. Realtek WiFi 6) non permettono la modifica del MAC address via software. In questi casi, il tool te lo segnalerà.
- Il tool è pensato per scopi etici e difensivi, come la protezione della privacy nelle reti pubbliche.

COME UTILIZZARLO

1. Assicurati di avere Python installato sul sistema:
   - Su Windows: https://www.python.org/downloads
   - Su Linux è già installato nella maggior parte dei casi.

2. Scarica il file mac_changer.py nella cartella desiderata (es: Download, Desktop, Tool, ecc.)

3. Apri il terminal o prompt dei comandi:
   - Su Windows: cerca "Prompt dei comandi", clic destro e seleziona "Esegui come amministratore"
   - Su Linux: apri il Terminale (CTRL + ALT + T)

4. Spostati nella cartella dove hai scaricato il file:
   - Esempio su Linux: cd ~/Download
   - Esempio su Windows: cd C:\Users\TUO_NOME\Downloads

5. Lancia il file con Python:
   python mac_changer.py
   oppure, se hai più versioni installate:
   python3 mac_changer.py

6. Segui le istruzioni:
   - Seleziona il sistema operativo (0 = Linux, 1 = Windows)
   - Scegli l’interfaccia di rete (Wi-Fi, Ethernet, VPN, ecc.)
   - Il tool genererà un nuovo MAC address e proverà a sostituirlo
   - Alla fine ti dirà se la modifica ha avuto successo oppure no

7. Premi INVIO per uscire dallo script.

AUTORE

Luca Tavani – https://github.com/LucaTavaniCybersec/Cybersecurity

Questo script è open-source e modificabile, ma usalo con responsabilità. L’anonimato è un diritto, non un alibi.

