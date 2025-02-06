import tempfile
import shutil
import os
import time
import argparse
import asyncio
import aiohttp
import signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Style, init
from tqdm import tqdm
import psutil
from threading import Lock
import json
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# Inizializza colorama
init(autoreset=True)

BACKUP_FILE = "backup_xss.txt"

def print_banner():
    banner = '''

    ███╗   ███╗ █████╗ ██╗  ██╗███████╗███████╗
    ████╗ ████║██╔══██╗╚██╗██╔╝██╔════╝██╔════╝
    ██╔████╔██║███████║ ╚███╔╝ ███████╗███████╗
    ██║╚██╔╝██║██╔══██║ ██╔██╗ ╚════██║╚════██║
    ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗███████║███████║
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝

                   MAXSS by GR33NSLIM3
    '''
    print(Fore.CYAN + banner)

class ChromeDriverManagerSingleton:
    _instance = None
    _lock = Lock()

    @classmethod
    def get_driver(cls):
        with cls._lock:
            if cls._instance is None:
                options = Options()
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")
                options.add_argument("--no-sandbox")
                cls._instance = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            return cls._instance

    @classmethod
    def close_driver(cls):
        with cls._lock:
            if cls._instance is not None:
                cls._instance.quit()
                cls._instance = None

async def send_discord_notification(webhook_url, message):
    if webhook_url:
        async with aiohttp.ClientSession() as session:
            payload = {"content": message}
            await session.post(webhook_url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

async def test_xss(session, url, payload, webhook_url, verbose):
    driver = ChromeDriverManagerSingleton.get_driver()
    try:
        driver.get(url)
        await asyncio.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        message = f"[+] XSS Found: {url}"
        print(f"{Fore.GREEN}{message}")
        await send_discord_notification(webhook_url, message)
        return url
    except:
        return None

def generate_payload_urls(base_url, payload, verbose):
    parsed_url = urlparse(base_url)
    query_params = parse_qs(parsed_url.query)
    urls_with_payload = []
    
    for param in query_params.keys():
        modified_params = query_params.copy()
        modified_params[param] = [payload]
        new_query = urlencode(modified_params, doseq=True)
        new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query, parsed_url.fragment))
        urls_with_payload.append(new_url)
        if verbose:
            print(f"{Fore.YELLOW}[VERBOSE] Testing URL: {new_url.replace(payload, Fore.RED + payload + Fore.YELLOW)}")
    
    return urls_with_payload

async def run_tests(url_list, payload_list, output_file, webhook_url, delay, verbose):
    async with aiohttp.ClientSession() as session:
        with open(output_file, 'w') as file, tqdm(total=len(url_list), desc="Testing XSS", unit="url") as progress_bar:
            for url in url_list:
                found_xss = False
                for payload in payload_list:
                    if found_xss:
                        break
                    payload_urls = generate_payload_urls(url, payload, verbose)
                    for test_url in payload_urls:
                        result = await test_xss(session, test_url, payload, webhook_url, verbose)
                        if result:
                            file.write(f"{result}\n")
                            found_xss = True
                            break
                        await asyncio.sleep(delay)
                progress_bar.update(1)
    ChromeDriverManagerSingleton.close_driver()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test for XSS vulnerabilities.")
    parser.add_argument("-u", "--url", help="Base URL to test.")
    parser.add_argument("-p", "--payload", help="File with XSS payloads to inject.")
    parser.add_argument("-o", "--output", help="File to store successful XSS results.", required=True)
    parser.add_argument("-l", "--list", help="File with list of URLs to test.")
    parser.add_argument("-w", "--webhook", help="Discord webhook URL to send notifications.")
    parser.add_argument("-d", "--delay", type=float, default=1.0, help="Delay in seconds between requests (default: 1s).")
    parser.add_argument("-r", "--resume", action="store_true", help="Resume from the last backup file.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output to see payload injection details.")

    args = parser.parse_args()
    print_banner()

    url_list = [args.url] if args.url else open(args.list).read().splitlines()
    payload_list = open(args.payload).read().splitlines()
    asyncio.run(run_tests(url_list, payload_list, args.output, args.webhook, args.delay, args.verbose))
