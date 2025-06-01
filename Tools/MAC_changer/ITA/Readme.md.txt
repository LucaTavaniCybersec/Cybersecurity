MAC Address Changer per Windows

E' un piccolo tool `.exe` per cambiare il MAC address del tuo adattatore di rete su Windows, pensato per migliorare la tua privacy nelle reti locali.

> Alcune schede di rete moderne (es. Realtek WiFi 6) non permettono la modifica del MAC address via software. In questi casi, il tool ti avviserà in automatico.

---

- Come si usa

1. Scarica il file `AnonimatoMAC.exe`
2. Tasto destro → Esegui come amministratore
3. Segui le istruzioni nel terminale:
   - Seleziona l'interfaccia (Wi-Fi, Ethernet...)
   - Il programma proverà a cambiare il MAC
   - Ti dirà se ha funzionato o meno

---

- Requisiti

- Windows 10 o 11
- Privilegi amministratore
- Nessun bisogno di installare Python

---

- Suggerimenti

- Se la modifica non funziona, prova a usare un **adattatore USB Ethernet/Wi-Fi economico** (es. TP-Link, Atheros...)
- Puoi convertire il MAC anche da Linux con `macchanger` (funziona quasi sempre)
- In alternativa, stiamo sviluppando anche una versione che **oscura** il MAC invece di cambiarlo → `OscuraMAC.exe` (coming soon)

---

- Compatibilità nota

| Scheda di rete                 | Supporto cambio MAC |
|-------------------------------|---------------------|
| Realtek RTL8852BE Wi-Fi 6     | ❌                  |
| Intel Wireless-AC 9560        | ❌                  |
| Qualcomm Atheros AR9271       | ✅                  |
| TP-Link TL-WN722N (v1)        | ✅                  |
| USB dongle Realtek RTL8187    | ✅                  |

---

- Etica

Questo tool è stato creato per scopi **educativi** e **difensivi**, non è destinato all'uso malevolo. L'anonimato è un diritto, ma va usato con coscienza.

---

# 👤 Autore

Luca Tavani