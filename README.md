# MAXSS
MAXSS – Automated XSS Scanner 🚀

## Scanner Banner

![maxss_blur](https://github.com/user-attachments/assets/027185ea-e87e-4679-abd6-b7133a02df91)

This tool identifies Cross-Site Scripting (XSS) vulnerabilities in a provided list of URLs. It is intended for testing large lists of URLs for mass hunting in bug bounty and penetration testing.

## 🔧 Requirements

Python 3.7 or higher

## 📥 Installation

```bash
git clone https://github.com/patfire94/MAXSS.git
cd MAXSS
pip install -r requirements.txt
python -m venv .venv
source .venv/bin/activate

Chrome Installation
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
If you encounter any errors during installation, use the following command:
sudo apt -f install
sudo dpkg -i google-chrome-stable_current_amd64.deb
Chrome Driver Installation
wget https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.119/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
cd chromedriver-linux64 
sudo mv chromedriver /usr/bin

```
## 🚀 Usage

Run the help command:

```bash
python3 maxss.py -h
python3 maxss.py -l urls.txt -p payloads.txt -o output.txt -d 1 -v
python3 maxss.py -l urls.txt -p payloads.txt --webhook "https://discord.com/api/webhooks/your-webhook-id/your-webhook-token"
```
## 📢 Discord Webhook Integration

This tool supports Discord webhook notifications to alert you when an XSS vulnerability is found. Simply provide your webhook URL using the --webhook parameter.

## Parameters

| Parameter                | Description                                                                      |
|--------------------------|----------------------------------------------------------------------------------|
| `-l`, `--list`           | File containing the list of URLs to scan (required)                              |
| `-p`, `--payload`        | File with test payloads (required)                                               |
| `-o`, `--output`         | File to save vulnerable URLs (default: `output.txt`)                             |
| `-t`, `--timeout`        | Request timeout in seconds (default: `30`)                                       |
| `-d`, `--delay`          | Response time in seconds suggesting vulnerability (default: `5.0`)               |
| `-v`, `--verbose`        | Enable detailed output                                                           |
| `--webhook`              | Discord webhook URL for sending alerts                                           |


## ⚠️ Disclaimer

MAXSS is for ethical hacking and security testing purposes only. Ensure you have proper authorization before scanning any web applications. The developers are not responsible for any misuse of this tool.

Modules specified in requirements.txt
 
## ⭐ Contribute & Support

Found a bug? Open an issue or submit a pull request.

If you like this tool, give it a star on GitHub! ⭐


