# MAXSS
MAXSS – Automated XSS Scanner 🚀

✨ Features
✅ Automated XSS Detection – Scans URLs and parameters for XSS vulnerabilities.
✅ Headless Chrome Automation – Uses Selenium to detect JavaScript-based XSS.
✅ Discord Webhook Notifications – Get real-time alerts when an XSS is found.
✅ Custom Payload Injection – Load custom payloads from a file.

Scanner Banner

This tool identifies Cross-Site Scripting (XSS) vulnerabilities in a provided list of URLs. It is intended for testing large lists of URLs for mass hunting in bug bounty and penetration testing.

🔧 Requirements

Python 3.7 or higher

📥 Installation

Clone the repository:
git clone https://github.com/your_username/MAXSS.git
cd MAXSS
pip install -r requirements.txt

🚀 Usage

Run the help command:

python3 maxss.py -h

Example usage:
python3 maxss.py -l urls.txt -p payloads.txt -o output.txt -d 1 -v
python3 maxss.py -l urls.txt -p payloads.txt --webhook "https://discord.com/api/webhooks/your-webhook-id/your-webhook-token"

📢 Discord Webhook Integration

This tool supports Discord webhook notifications to alert you when an XSS vulnerability is found. Simply provide your webhook URL using the --webhook parameter.

⚙️ Parameters

Parameter

Description

-l, --list

File containing the list of URLs to scan (required)

-p, --payload

File with test payloads (required)

-o, --output

File to save vulnerable URLs (default: output.txt)

-d, --delay

Delay in seconds between requests (default: 1.0)

-v, --verbose

Enable detailed output

--webhook

Discord webhook URL for sending alerts

⚠️ Disclaimer

MAXSS is for ethical hacking and security testing purposes only. Ensure you have proper authorization before scanning any web applications. The developers are not responsible for any misuse of this tool.

Modules specified in requirements.txt

⭐ Contribute & Support

Found a bug? Open an issue or submit a pull request.

If you like this tool, give it a star on GitHub! ⭐


