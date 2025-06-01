MAC Address Changer for Windows

A lightweight `.exe` tool to change the MAC address of your network adapter on Windows, designed to enhance your privacy on local networks.

> Some modern network adapters (e.g. Realtek WiFi 6) do not allow MAC address modification via software. In these cases, the tool will automatically detect and notify you.

---

- How to Use

1. Download the file `AnonimatoMAC.exe`
2. Right-click → Run as Administrator
3. Follow the instructions in the terminal:
   - Select the network interface (Wi-Fi, Ethernet...)
   - The tool will attempt to change the MAC address
   - It will tell you whether it succeeded or not

---

- Requirements

- Windows 10 or 11
- Administrator privileges
- No need to install Python

---

- Tips

- If the MAC change fails, try using an **external USB Wi-Fi or Ethernet adapter** (e.g. TP-Link, Atheros...)
- You can also spoof your MAC address on Linux using `macchanger` (it works in most cases)
- Alternatively, we are developing a version that **hides** your MAC instead of changing it → `OscuraMAC.exe` (coming soon)

---

- Known Compatibility

| Network Adapter                  | MAC Spoofing Support |
|----------------------------------|-----------------------|
| Realtek RTL8852BE Wi-Fi 6        | ❌                    |
| Intel Wireless-AC 9560           | ❌                    |
| Qualcomm Atheros AR9271          | ✅                    |
| TP-Link TL-WN722N (v1)           | ✅                    |
| USB dongle Realtek RTL8187       | ✅                    |

---

- Ethics

This tool is intended for **educational** and **defensive** purposes only. It is not designed for malicious use.  
Privacy is a right, but it must be exercised responsibly.

---

# 👤 Author

Luca Tavani