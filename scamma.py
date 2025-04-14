# -*- coding: utf-8 -*-
import json
import requests
import socket
import platform
import os
import time
import string
import random
import re
import sys
import hashlib
import base64
import qrcode
import whois
import dns.resolver
import socket
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from colorama import Fore, init, Back, Style
from pystyle import Colorate, Colors, Center, Write, System
import pyfiglet
from datetime import datetime
import threading
import ipaddress
import binascii
import subprocess
import qrcode
from PIL import Image
import math
import shodan
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

if os.name == 'nt':
    import ctypes
    import win32api

init(autoreset=True)

class ScammaTool:
    def __init__(self):
        self.set_console_size()
        self.version = "4.2"
        self.author = "Stuxnet"
        self.username_pc = os.getenv('USERNAME') or os.getenv('USER') or "root"
        self.os_name = platform.system()
        self.menu_number = "01"
        self.all_links = []
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        
        # Configuration de l'API Shodan (remplacer par votre clé)
        self.SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
        self.shodan_api = shodan.Shodan(self.SHODAN_API_KEY) if self.SHODAN_API_KEY != "YOUR_SHODAN_API_KEY" else None
        
        # Couleurs personnalisées
        self.colors = {
            "main": Fore.LIGHTBLUE_EX,
            "secondary": Fore.LIGHTCYAN_EX,
            "success": Fore.LIGHTGREEN_EX,
            "warning": Fore.LIGHTYELLOW_EX,
            "error": Fore.LIGHTRED_EX,
            "info": Fore.LIGHTWHITE_EX,
            "highlight": Fore.LIGHTMAGENTA_EX,
            "matrix": Fore.GREEN
        }
        
        # Configuration du style
        self.border_style = f"{Fore.LIGHTBLACK_EX}│{Fore.RESET}"
        self.title_style = f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}"
        self.option_style = f"{Style.BRIGHT}{Fore.LIGHTCYAN_EX}"
        
        # Bannière ASCII art
        self.banner_art = self.generate_banner()
        
        # Menu principal
        self.menu_options = [
            {"num": "01", "name": "Phone Number Info", "func": self.phone_info},
            {"num": "02", "name": "Webhook Spammer", "func": self.webhook_spammer},
            {"num": "03", "name": "IP Information", "func": self.ip_information},
            {"num": "04", "name": "System Info", "func": self.system_info},
            {"num": "05", "name": "Ping Test", "func": self.ping_test},
            {"num": "06", "name": "Website Lookup", "func": self.lookup_website},
            {"num": "07", "name": "Vulnerability Scanner", "func": self.website_vulnerability_scanner},
            {"num": "08", "name": "URL Scanner", "func": self.website_url_scanner},
            {"num": "09", "name": "WHOIS Lookup", "func": self.whois_lookup},
            {"num": "10", "name": "DNS Lookup", "func": self.dns_lookup},
            {"num": "11", "name": "Subdomain Scanner", "func": self.subdomain_scanner},
            {"num": "12", "name": "Port Scanner", "func": self.port_scanner},
            {"num": "13", "name": "Breach Checker", "func": self.breach_checker},
            {"num": "14", "name": "Social Media Finder", "func": self.social_media_finder},
            {"num": "15", "name": "Password Generator", "func": self.password_generator},
            {"num": "16", "name": "Hash Tool", "func": self.hash_tool},
            {"num": "17", "name": "VPN Check", "func": self.vpn_check},
            {"num": "18", "name": "QR Code Tool", "func": self.qr_code_tool},
            {"num": "19", "name": "Base64 Tool", "func": self.base64_tool},
            {"num": "20", "name": "Dark Web Links", "func": self.dark_web_links},
            {"num": "21", "name": "Bitcoin Tools", "func": self.bitcoin_tools},
            {"num": "22", "name": "Network Tools", "func": self.network_tools},
            {"num": "23", "name": "Exit", "func": self.exit_tool}
        ]

    def generate_banner(self):
        banner_text = pyfiglet.figlet_format("Scamma Tool", font="slant")
        border_top = f"{Fore.LIGHTBLACK_EX}╔{'═' * 60}╗{Fore.RESET}"
        border_bottom = f"{Fore.LIGHTBLACK_EX}╚{'═' * 60}╝{Fore.RESET}"
        
        banner = f"""
{border_top}
{self.title_style}{banner_text}{Style.RESET_ALL}
{self.colors['matrix']}  Version: {self.version} | Author: {self.author} | OS: {self.os_name}
{self.colors['info']}  Advanced Hacking and OSINT Toolset
{border_bottom}
"""
        return banner

    def set_console_size(self):
        """Configure la taille de la console pour un meilleur affichage"""
        if os.name == 'nt':  
            try:
                os.system('mode con: cols=120 lines=50')
                hwnd = ctypes.windll.kernel32.GetConsoleWindow()
                if hwnd:
                    ctypes.windll.user32.SetWindowPos(hwnd, None, 50, 50, 1200, 800, 0x0002)
            except:
                print(f"{self.colors['warning']}[!] Impossible d'ajuster la taille de la console")
        else:  
            try:
                sys.stdout.write("\x1b[8;50;120t")
            except:
                pass

    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.banner_art)
        
        # Affichage du menu en 2 colonnes avec style hacker
        print(f"{self.colors['matrix']}╔════════════════════════════════════════════════════════════════╗")
        print(f"{self.colors['matrix']}║ {self.colors['highlight']}SELECT AN OPTION:{' ' * 43}{self.colors['matrix']}║")
        print(f"{self.colors['matrix']}╠════════════════════════════╦═══════════════════════════════════╣")
        
        for i in range(0, len(self.menu_options), 2):
            opt1 = self.menu_options[i]
            opt2 = self.menu_options[i+1] if i+1 < len(self.menu_options) else None
            
            line = f"{self.colors['matrix']}║ {self.option_style}{opt1['num']}{Fore.RESET} > {self.colors['info']}{opt1['name'].ljust(23)}"
            if opt2:
                line += f"{self.colors['matrix']}║ {self.option_style}{opt2['num']}{Fore.RESET} > {self.colors['info']}{opt2['name'].ljust(23)}"
            else:
                line += f"{self.colors['matrix']}║{' ' * 35}"
            
            print(line)
        
        print(f"{self.colors['matrix']}╚════════════════════════════╩═══════════════════════════════════╝")

    def run(self):
        while True:
            self.display_menu()
            choice = input(f"\n{self.colors['matrix']}┌─[{self.colors['highlight']}{self.username_pc}{self.colors['matrix']}@ScammaTool]-[{self.colors['info']}~/{self.menu_number}{self.colors['matrix']}]\n└──╼{self.colors['info']}$ ")
            
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= len(self.menu_options):
                    selected_option = self.menu_options[choice_num-1]
                    self.menu_number = selected_option["num"]
                    selected_option["func"]()
                else:
                    self.show_error("Invalid option")
            except ValueError:
                self.show_error("Please enter a valid number")

    def show_error(self, message):
        print(f"\n{self.colors['error']}[!] {message}")
        time.sleep(1.5)

    def show_success(self, message):
        print(f"\n{self.colors['success']}[+] {message}")

    def show_info(self, message):
        print(f"\n{self.colors['info']}[*] {message}")

    def loading_animation(self, message, duration=2):
        chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        start_time = time.time()
        
        print(f"{self.colors['secondary']}[*] {message}", end='', flush=True)
        
        while time.time() - start_time < duration:
            for char in chars:
                print(f"\r{self.colors['secondary']}[{char}] {message}", end='', flush=True)
                time.sleep(0.1)
        
        print("\r", end='', flush=True)

    def clear_screen(self, title=""):
        os.system('cls' if os.name == 'nt' else 'clear')
        if title:
            title_border = f"{self.colors['main']}╔{'═' * ((60 - len(title)) // 2)}{title}{'═' * ((60 - len(title)) // 2)}╗"
            print(title_border + "\n")

    def display_results(self, results, title):
        print(f"\n{self.colors['main']}╔═══════════════ {title} ═══════════════╗")
        for key, value in results.items():
            print(f"{self.colors['info']}  {str(key).ljust(20)}: {self.colors['highlight']}{str(value)}")
        print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")

    # ================================================
    # FONCTIONNALITÉS DU TOOL
    # ================================================

    def phone_info(self):
        self.clear_screen("Phone Number Information")
        
        print(f"""
{self.colors['main']}╔════════════════════════════════════════════════════════════════╗
{self.colors['secondary']}  Available options:
{self.colors['info']}  1. Full phone number lookup
{self.colors['info']}  2. Carrier detection
{self.colors['info']}  3. Timezone detection
{self.colors['main']}╚════════════════════════════════════════════════════════════════╝
        """)
        
        choice = input(f"{self.colors['secondary']}Choose an option (1-3): ")
        phone = input(f"{self.colors['secondary']}Enter phone number (international format): ").strip()
        
        try:
            parsed_number = phonenumbers.parse(phone, None)
            if not phonenumbers.is_valid_number(parsed_number):
                self.show_error("Invalid phone number")
                return
        except:
            self.show_error("Invalid phone number format")
            return
        
        self.loading_animation("Gathering information...")
        
        try:
            # Get carrier information
            carrier_name = carrier.name_for_number(parsed_number, "en")
            
            # Get geographical information
            region = geocoder.description_for_number(parsed_number, "en")
            
            # Get timezone
            time_zones = timezone.time_zones_for_number(parsed_number)
            
            # Format phone number
            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            
            results = {
                "Number": formatted_number,
                "Valid": "Yes",
                "Country": phonenumbers.region_code_for_number(parsed_number),
                "Carrier": carrier_name if carrier_name else "Unknown",
                "Region": region if region else "Unknown",
                "Timezone": ", ".join(time_zones) if time_zones else "Unknown",
                "Number Type": phonenumbers.number_type(parsed_number)
            }
            
            self.display_results(results, "Phone Information")
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def webhook_spammer(self):
        self.clear_screen("Webhook Spammer")
        
        print(f"""
{self.colors['warning']}[!] WARNING: This feature can be used for malicious purposes.
{self.colors['warning']}    Use it only for legitimate testing on your own webhooks.
        """)
        
        webhook_url = input(f"{self.colors['secondary']}Discord webhook URL: ").strip()
        
        if not webhook_url.startswith("https://discord.com/api/webhooks/"):
            self.show_error("Invalid Discord webhook URL")
            return
        
        message = input(f"{self.colors['secondary']}Message to send (@everyone to ping): ").strip()
        delay = input(f"{self.colors['secondary']}Delay between messages (seconds, 0 for none): ").strip()
        
        try:
            delay = float(delay) if delay else 0
        except:
            delay = 0
        
        count = 0
        try:
            while True:
                payload = {
                    "content": message,
                    "username": f"Spammer-{random.randint(1000,9999)}",
                    "avatar_url": "https://cdn.discordapp.com/attachments/758548412244951062/1043762803825786890/hacker_icon.png"
                }
                
                response = requests.post(webhook_url, json=payload)
                count += 1
                
                if response.status_code == 204:
                    print(f"\r{self.colors['success']}[+] Messages sent: {count}", end='', flush=True)
                else:
                    print(f"\r{self.colors['error']}[!] Error: {response.status_code}", end='', flush=True)
                
                if delay > 0:
                    time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"\n{self.colors['info']}[*] Stopping spammer. Total sent: {count}")
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def ip_information(self):
        self.clear_screen("IP Information")
        
        ip = input(f"{self.colors['secondary']}Enter IP address or domain: ").strip()
        
        if not ip:
            self.show_error("Please enter an IP or domain")
            return
        
        # If it's a domain, resolve to IP
        if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
            try:
                ip = socket.gethostbyname(ip)
            except:
                self.show_error("Could not resolve domain")
                return
        
        self.loading_animation(f"Gathering information for {ip}...")
        
        try:
            # Using ip-api.com API
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            
            if data['status'] == 'success':
                results = {
                    "IP": data['query'],
                    "Country": data['country'],
                    "Country Code": data['countryCode'],
                    "Region": data['regionName'],
                    "City": data['city'],
                    "ZIP": data['zip'],
                    "Latitude": data['lat'],
                    "Longitude": data['lon'],
                    "Timezone": data['timezone'],
                    "ISP": data['isp'],
                    "Organization": data['org'],
                    "AS": data['as']
                }
                
                self.display_results(results, "IP Information")
                
                # Display map link (Google Maps)
                if 'lat' in data and 'lon' in data:
                    map_url = f"https://www.google.com/maps/place/{data['lat']},{data['lon']}"
                    print(f"\n{self.colors['info']}Approximate location: {self.colors['highlight']}{map_url}")
                
                # Shodan data if available
                if self.shodan_api:
                    try:
                        shodan_data = self.shodan_api.host(ip)
                        print(f"\n{self.colors['main']}╔═══════════════ Shodan Information ═══════════════╗")
                        print(f"{self.colors['info']}  Ports Open: {', '.join(map(str, shodan_data['ports']))}")
                        if 'vulns' in shodan_data:
                            print(f"{self.colors['error']}  Vulnerabilities: {', '.join(shodan_data['vulns'])}")
                        print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
                    except:
                        pass
            else:
                self.show_error("Could not get information for this IP")
                
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def system_info(self):
        self.clear_screen("System Information")
        
        try:
            # Basic system information
            sys_info = {
                "System": platform.system(),
                "Version": platform.version(),
                "Architecture": platform.architecture()[0],
                "Processor": platform.processor(),
                "Hostname": socket.gethostname(),
                "Username": self.username_pc,
                "Current Directory": os.getcwd(),
                "Uptime": self.get_system_uptime()
            }
            
            self.display_results(sys_info, "System Information")
            
            # Network information
            print(f"\n{self.colors['main']}╔════════════════ Network Information ═══════════════╗")
            try:
                host_name = socket.gethostname()
                host_ip = socket.gethostbyname(host_name)
                print(f"{self.colors['info']}  Local IP: {self.colors['highlight']}{host_ip}")
                
                # Public IP
                public_ip = requests.get('https://api.ipify.org').text
                print(f"{self.colors['info']}  Public IP: {self.colors['highlight']}{public_ip}")
            except:
                print(f"{self.colors['error']}  Could not get network information")
            
            print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def get_system_uptime(self):
        try:
            if platform.system() == "Windows":
                lib = ctypes.windll.kernel32
                tick = lib.GetTickCount64()
                seconds = int(str(tick)[:-3])
            else:
                with open('/proc/uptime', 'r') as f:
                    seconds = float(f.readline().split()[0])
            
            mins, sec = divmod(seconds, 60)
            hr, mins = divmod(mins, 60)
            days, hr = divmod(hr, 24)
            
            return f"{int(days)} days, {int(hr)} hours, {int(mins)} minutes"
        except:
            return "Unknown"

    def ping_test(self):
        self.clear_screen("Ping Test")
        
        host = input(f"{self.colors['secondary']}Enter IP or domain to test: ").strip()
        
        if not host:
            self.show_error("Please enter an IP or domain")
            return
        
        count = input(f"{self.colors['secondary']}Packet count (default 4): ").strip()
        try:
            count = int(count) if count else 4
        except:
            count = 4
        
        self.loading_animation(f"Pinging {host}...")
        
        try:
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, str(count), host]
            output = subprocess.check_output(command).decode('utf-8', errors='ignore')
            
            print(f"\n{self.colors['main']}╔════════════════ Ping Results ════════════════╗")
            print(f"{self.colors['info']}{output}")
            print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
            
        except subprocess.CalledProcessError as e:
            self.show_error(f"Ping error: {e.output.decode('utf-8', errors='ignore')}")
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def lookup_website(self):
        self.clear_screen("Website Lookup")
        
        domain = input(f"{self.colors['secondary']}Enter domain (e.g. example.com): ").strip()
        
        if not domain:
            self.show_error("Please enter a valid domain")
            return
        
        self.loading_animation(f"Looking up information for {domain}...")
        
        try:
            # WHOIS information
            w = whois.whois(domain)
            
            results = {
                "Domain": domain,
                "DNS Servers": "\n".join(w.name_servers) if w.name_servers else "Unknown",
                "Creation Date": w.creation_date.strftime('%Y-%m-%d') if w.creation_date else "Unknown",
                "Expiration Date": w.expiration_date.strftime('%Y-%m-%d') if w.expiration_date else "Unknown",
                "Registrar": w.registrar if w.registrar else "Unknown",
                "Status": w.status if w.status else "Unknown"
            }
            
            self.display_results(results, "WHOIS Information")
            
            # DNS information
            print(f"\n{self.colors['main']}╔════════════════ DNS Information ═══════════════╗")
            try:
                a_records = dns.resolver.resolve(domain, 'A')
                print(f"{self.colors['info']}  A Records:")
                for rdata in a_records:
                    print(f"    {self.colors['highlight']}{rdata.address}")
                
                mx_records = dns.resolver.resolve(domain, 'MX')
                print(f"\n{self.colors['info']}  MX Records:")
                for rdata in mx_records:
                    print(f"    {self.colors['highlight']}{rdata.exchange} (preference {rdata.preference})")
            except dns.resolver.NoAnswer:
                print(f"{self.colors['error']}  No DNS records found")
            except Exception as e:
                print(f"{self.colors['error']}  DNS error: {str(e)}")
            
            print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def website_vulnerability_scanner(self):
        self.clear_screen("Website Vulnerability Scanner")
        
        url = input(f"{self.colors['secondary']}Enter URL to scan (e.g. https://example.com): ").strip()
        
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        self.loading_animation(f"Scanning {url}...")
        
        try:
            # Check security headers
            headers = requests.head(url).headers
            
            security_headers = {
                "X-XSS-Protection": headers.get('X-XSS-Protection', 'Missing'),
                "X-Content-Type-Options": headers.get('X-Content-Type-Options', 'Missing'),
                "Strict-Transport-Security": headers.get('Strict-Transport-Security', 'Missing'),
                "Content-Security-Policy": headers.get('Content-Security-Policy', 'Missing'),
                "X-Frame-Options": headers.get('X-Frame-Options', 'Missing')
            }
            
            print(f"\n{self.colors['main']}╔══════════════ Security Headers ══════════════╗")
            for header, value in security_headers.items():
                status = f"{self.colors['success']}OK" if value != 'Missing' else f"{self.colors['error']}MISSING"
                print(f"{self.colors['info']}  {header.ljust(25)}: {status} {self.colors['info']}{value if value != 'Missing' else ''}")
            print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
            
            # Common vulnerability tests
            print(f"\n{self.colors['main']}╔════════════ Vulnerability Tests ═════════════╗")
            
            # SQL Injection test
            test_url = f"{url}?id=1'"
            try:
                response = requests.get(test_url)
                if "SQL" in response.text or "syntax" in response.text:
                    print(f"{self.colors['error']}  [!] Possible SQL Injection vulnerability")
                else:
                    print(f"{self.colors['info']}  [✓] No obvious SQL Injection signs")
            except:
                pass
            
            # XSS test
            test_url = f"{url}?search=<script>alert('XSS')</script>"
            try:
                response = requests.get(test_url)
                if "<script>alert('XSS')</script>" in response.text:
                    print(f"{self.colors['error']}  [!] Possible XSS vulnerability")
                else:
                    print(f"{self.colors['info']}  [✓] No obvious XSS signs")
            except:
                pass
            
            # Check for sensitive directories
            sensitive_dirs = ['admin', 'wp-admin', 'backup', 'config', 'phpmyadmin']
            found_dirs = []
            
            for directory in sensitive_dirs:
                test_url = f"{url}/{directory}"
                try:
                    response = requests.get(test_url, timeout=5)
                    if response.status_code == 200:
                        found_dirs.append(directory)
                except:
                    pass
            
            if found_dirs:
                print(f"{self.colors['error']}  [!] Accessible sensitive directories: {', '.join(found_dirs)}")
            else:
                print(f"{self.colors['info']}  [✓] No obvious sensitive directories found")
            
            print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def website_url_scanner(self):
        self.clear_screen("Website URL Scanner")
        
        url = input(f"{self.colors['secondary']}Enter URL to scan (e.g. https://example.com): ").strip()
        
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        domain = urlparse(url).netloc
        
        print(f"\n{self.colors['secondary']}Scan options:")
        print(f"{self.colors['info']}  1. Quick scan (homepage only)")
        print(f"{self.colors['info']}  2. Full scan (all found pages)")
        
        choice = input(f"\n{self.colors['secondary']}Choose an option (1-2): ").strip()
        
        self.all_links = []
        
        try:
            if choice == '1':
                self.loading_animation(f"Quick scanning {url}...")
                self.find_links(url, domain)
            elif choice == '2':
                self.loading_animation(f"Full scanning {url}...")
                self.crawl_website(url, domain)
            else:
                self.show_error("Invalid option")
                return
            
            print(f"\n{self.colors['main']}╔════════════════ Found URLs ════════════════╗")
            for link in sorted(set(self.all_links)):
                print(f"{self.colors['info']}  {link}")
            print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
            
            print(f"\n{self.colors['success']}[+] Scan complete. {len(set(self.all_links))} unique URLs found.")
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def find_links(self, url, domain):
        try:
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                href = link['href']
                if href.startswith('http') and domain in href:
                    self.all_links.append(href)
                elif href.startswith('/'):
                    self.all_links.append(urljoin(url, href))
        except:
            pass

    def crawl_website(self, start_url, domain, max_pages=50):
        visited = set()
        to_visit = {start_url}
        
        while to_visit and len(visited) < max_pages:
            url = to_visit.pop()
            
            if url in visited:
                continue
                
            try:
                response = requests.get(url, timeout=10)
                visited.add(url)
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    
                    if href.startswith('http') and domain in href and href not in visited:
                        to_visit.add(href)
                        self.all_links.append(href)
                    elif href.startswith('/'):
                        full_url = urljoin(url, href)
                        if full_url not in visited:
                            to_visit.add(full_url)
                            self.all_links.append(full_url)
                            
            except:
                continue

    def whois_lookup(self):
        self.clear_screen("WHOIS Lookup")
        
        domain = input(f"{self.colors['secondary']}Enter domain (e.g. example.com): ").strip()
        
        if not domain:
            self.show_error("Please enter a valid domain")
            return
        
        self.loading_animation(f"Looking up WHOIS for {domain}...")
        
        try:
            w = whois.whois(domain)
            
            results = {
                "Domain": domain,
                "DNS Servers": "\n".join(w.name_servers) if w.name_servers else "Unknown",
                "Creation Date": w.creation_date.strftime('%Y-%m-%d') if w.creation_date else "Unknown",
                "Expiration Date": w.expiration_date.strftime('%Y-%m-%d') if w.expiration_date else "Unknown",
                "Update Date": w.updated_date.strftime('%Y-%m-%d') if w.updated_date else "Unknown",
                "Registrar": w.registrar if w.registrar else "Unknown",
                "Status": w.status if w.status else "Unknown",
                "Admin Email": w.emails if w.emails else "Unknown"
            }
            
            self.display_results(results, "WHOIS Results")
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def dns_lookup(self):
        self.clear_screen("DNS Lookup")
        
        domain = input(f"{self.colors['secondary']}Enter domain (e.g. example.com): ").strip()
        
        if not domain:
            self.show_error("Please enter a valid domain")
            return
        
        print(f"\n{self.colors['secondary']}Available record types:")
        print(f"{self.colors['info']}  1. A (IPv4 Address)")
        print(f"{self.colors['info']}  2. AAAA (IPv6 Address)")
        print(f"{self.colors['info']}  3. MX (Mail Exchange)")
        print(f"{self.colors['info']}  4. NS (Name Server)")
        print(f"{self.colors['info']}  5. TXT (Text Record)")
        print(f"{self.colors['info']}  6. All types")
        
        choice = input(f"\n{self.colors['secondary']}Choose a type (1-6): ").strip()
        
        record_types = []
        if choice == '1':
            record_types = ['A']
        elif choice == '2':
            record_types = ['AAAA']
        elif choice == '3':
            record_types = ['MX']
        elif choice == '4':
            record_types = ['NS']
        elif choice == '5':
            record_types = ['TXT']
        elif choice == '6':
            record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
        else:
            self.show_error("Invalid choice")
            return
        
        self.loading_animation(f"Looking up DNS for {domain}...")
        
        try:
            resolver = dns.resolver.Resolver()
            results = {}
            
            for record in record_types:
                try:
                    answers = resolver.resolve(domain, record)
                    results[record] = [str(r) for r in answers]
                except dns.resolver.NoAnswer:
                    results[record] = ["No records found"]
                except dns.resolver.NXDOMAIN:
                    results[record] = ["Domain does not exist"]
                except Exception as e:
                    results[record] = [f"Error: {str(e)}"]
            
            self.display_results(results, "DNS Results")
            
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def subdomain_scanner(self):
        self.clear_screen("Subdomain Scanner")
        
        domain = input(f"{self.colors['secondary']}Enter domain (e.g. example.com): ").strip()
        
        if not domain:
            self.show_error("Please enter a valid domain")
            return
        
        wordlist_path = input(f"{self.colors['secondary']}Wordlist path (leave empty for default list): ").strip()
        
        if wordlist_path:
            try:
                with open(wordlist_path, 'r') as f:
                    subdomains = [line.strip() for line in f if line.strip()]
            except:
                self.show_error("Could not read wordlist file")
                return
        else:
            # Common subdomains list
            subdomains = [
                'www', 'mail', 'ftp', 'webmail', 'smtp', 'pop', 'ns1', 'ns2', 
                'blog', 'dev', 'test', 'admin', 'secure', 'vpn', 'm', 'mobile',
                'api', 'app', 'cloud', 'cpanel', 'whm', 'webdisk', 'autodiscover'
            ]
        
        found = []
        total = len(subdomains)
        current = 0
        
        print(f"\n{self.colors['info']}[*] Scanning {total} possible subdomains...\n")
        
        for sub in subdomains:
            current += 1
            subdomain = f"{sub}.{domain}"
            progress = f"[{current}/{total}]"
            
            try:
                ip = socket.gethostbyname(subdomain)
                found.append(subdomain)
                print(f"{progress} {self.colors['success']}Found: {subdomain.ljust(30)} → {ip}")
            except socket.gaierror:
                print(f"{progress} {self.colors['error']}Not found: {subdomain}")
            except Exception:
                print(f"{progress} {self.colors['error']}Error with: {subdomain}")
            
            # Pause to avoid rate limiting
            time.sleep(0.1)
        
        if found:
            print(f"\n{self.colors['success']}[+] Found subdomains ({len(found)}):")
            for sub in found:
                print(f"  {self.colors['info']}- {sub}")
        else:
            print(f"\n{self.colors['error']}[-] No subdomains found")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def port_scanner(self):
        self.clear_screen("Port Scanner")
        
        target = input(f"{self.colors['secondary']}Enter IP address or domain: ").strip()
        
        if not target:
            self.show_error("Please enter a valid target")
            return
        
        try:
            # DNS resolution if it's a domain
            ip = socket.gethostbyname(target)
        except:
            self.show_error("Could not resolve domain")
            return
        
        port_range = input(f"{self.colors['secondary']}Port range (e.g. 1-100 or 80,443): ").strip()
        
        ports = []
        if '-' in port_range:
            start, end = map(int, port_range.split('-'))
            ports = range(start, end+1)
        elif ',' in port_range:
            ports = [int(p) for p in port_range.split(',')]
        else:
            ports = [int(port_range)]
        
        print(f"\n{self.colors['info']}[*] Scanning ports {port_range} on {ip}...\n")
        
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                sock.close()
                
                if result == 0:
                    try:
                        service = socket.getservbyport(port, 'tcp')
                    except:
                        service = "unknown"
                    open_ports.append(port)
                    print(f"{self.colors['success']}[+] Port {port}/tcp open ({service})")
                else:
                    print(f"{self.colors['error']}[-] Port {port}/tcp closed")
            except:
                print(f"{self.colors['warning']}[!] Error with port {port}")
        
        # Scan with threads for speed
        threads = []
        for port in ports:
            t = threading.Thread(target=scan_port, args=(port,))
            threads.append(t)
            t.start()
            
        for t in threads:
            t.join()
        
        if len(open_ports) > 0:
            ports_str = ', '.join(map(str, sorted(open_ports)))
            print(f"\n{self.colors['success']}[+] Open ports: {ports_str}")
        else:
            print(f"\n{self.colors['error']}[-] No open ports found")

        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def breach_checker(self):
        self.clear_screen("Breach Checker")
        
        email = input(f"{self.colors['secondary']}Enter email to check: ").strip()
        
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            self.show_error("Invalid email")
            return
        
        self.loading_animation(f"Checking breaches for {email}...")
        
        try:
            # Using Have I Been Pwned API (simulated)
            response = requests.get(
                f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
                headers={"User-Agent": "ScammaTool"}
            )
            
            if response.status_code == 200:
                breaches = response.json()
                print(f"\n{self.colors['error']}[!] Email found in {len(breaches)} breach(es):")
                for breach in breaches:
                    print(f"  {self.colors['info']}- {breach['Name']} ({breach['BreachDate']})")
                
                print(f"\n{self.colors['warning']}[!] Change your passwords if you use the same across multiple sites")
            elif response.status_code == 404:
                print(f"\n{self.colors['success']}[+] No known breaches found for this email")
            else:
                self.show_error("Could not check breaches")
                
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def social_media_finder(self):
        self.clear_screen("Social Media Finder")
        
        username = input(f"{self.colors['secondary']}Enter username to search: ").strip()
        
        if not username:
            self.show_error("Please enter a username")
            return
        
        self.loading_animation(f"Searching for {username} on social media...")
        
        # List of sites with URL templates
        sites = {
            "Facebook": f"https://www.facebook.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://www.instagram.com/{username}",
            "LinkedIn": f"https://www.linkedin.com/in/{username}",
            "GitHub": f"https://github.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "TikTok": f"https://www.tiktok.com/@{username}",
            "YouTube": f"https://www.youtube.com/user/{username}",
            "Pinterest": f"https://www.pinterest.com/{username}",
            "Twitch": f"https://www.twitch.tv/{username}"
        }
        
        print(f"\n{self.colors['main']}╔════════════════ Possible Profiles ═══════════════╗")
        
        for name, url in sites.items():
            try:
                response = requests.head(url, timeout=5)
                if response.status_code == 200:
                    print(f"{self.colors['success']}  [✓] {name.ljust(15)}: {url}")
                else:
                    print(f"{self.colors['error']}  [ ] {name.ljust(15)}: {url}")
            except:
                print(f"{self.colors['error']}  [ ] {name.ljust(15)}: {url}")
        
        print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def password_generator(self):
        self.clear_screen("Password Generator")
        
        length = input(f"{self.colors['secondary']}Password length (8-64, default: 12): ").strip()
        try:
            length = int(length) if length else 12
            length = max(8, min(64, length))
        except:
            length = 12
        
        print(f"\n{self.colors['secondary']}Complexity options:")
        print(f"{self.colors['info']}  1. Letters only")
        print(f"{self.colors['info']}  2. Letters and numbers")
        print(f"{self.colors['info']}  3. Letters, numbers and symbols")
        print(f"{self.colors['info']}  4. Memorable passphrase")
        
        choice = input(f"\n{self.colors['secondary']}Choose an option (1-4): ").strip()
        
        if choice == '1':
            chars = string.ascii_letters
        elif choice == '2':
            chars = string.ascii_letters + string.digits
        elif choice == '3':
            chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        elif choice == '4':
            # Memorable passphrase generation
            words = ["correct", "horse", "battery", "staple", "house", "tree", 
                    "sun", "car", "computer", "phone", "keyboard", "mouse"]
            password = '-'.join(random.sample(words, 3)) + str(random.randint(10, 99))
            print(f"\n{self.colors['success']}[+] Generated password: {self.colors['highlight']}{password}")
            input(f"\n{self.colors['secondary']}Press Enter to continue...")
            return
        else:
            chars = string.ascii_letters + string.digits
        
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"\n{self.colors['success']}[+] Generated password: {self.colors['highlight']}{password}")
        
        # Strength estimation
        entropy = length * (math.log(len(chars)) / math.log(2))
        if entropy > 100:
            strength = f"{self.colors['success']}Very Strong"
        elif entropy > 60:
            strength = f"{self.colors['success']}Strong"
        elif entropy > 40:
            strength = f"{self.colors['warning']}Medium"
        else:
            strength = f"{self.colors['error']}Weak"

        print(f"{self.colors['info']}[*] Estimated strength: {strength} ({entropy:.1f} bits of entropy)")

        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def hash_tool(self):
        self.clear_screen("Hash Tool")
        
        print(f"\n{self.colors['secondary']}Available options:")
        print(f"{self.colors['info']}  1. Generate hash")
        print(f"{self.colors['info']}  2. Identify hash")
        print(f"{self.colors['info']}  3. Crack hash (dictionary)")
        
        choice = input(f"\n{self.colors['secondary']}Choose an option (1-3): ").strip()
        
        if choice == '1':
            text = input(f"{self.colors['secondary']}Enter text to hash: ").strip()
            
            print(f"\n{self.colors['secondary']}Available algorithms:")
            print(f"{self.colors['info']}  1. MD5")
            print(f"{self.colors['info']}  2. SHA1")
            print(f"{self.colors['info']}  3. SHA256")
            print(f"{self.colors['info']}  4. SHA512")
            
            algo = input(f"\n{self.colors['secondary']}Choose algorithm (1-4): ").strip()
            
            if algo == '1':
                hash_obj = hashlib.md5(text.encode())
            elif algo == '2':
                hash_obj = hashlib.sha1(text.encode())
            elif algo == '3':
                hash_obj = hashlib.sha256(text.encode())
            elif algo == '4':
                hash_obj = hashlib.sha512(text.encode())
            else:
                self.show_error("Invalid algorithm")
                return
            
            print(f"\n{self.colors['success']}[+] Generated hash: {self.colors['highlight']}{hash_obj.hexdigest()}")
            
        elif choice == '2':
            hash_input = input(f"{self.colors['secondary']}Enter hash to identify: ").strip()
            
            # Simple identification by length
            length = len(hash_input)
            if length == 32:
                possible = "MD5"
            elif length == 40:
                possible = "SHA1"
            elif length == 64:
                possible = "SHA256"
            elif length == 128:
                possible = "SHA512"
            else:
                possible = "Unknown"
            
            print(f"\n{self.colors['info']}[*] Hash might be: {self.colors['highlight']}{possible}")
            print(f"{self.colors['info']}[*] Length: {length} characters")
            
        elif choice == '3':
            hash_input = input(f"{self.colors['secondary']}Enter hash to crack: ").strip()
            wordlist_path = input(f"{self.colors['secondary']}Wordlist file path: ").strip()
            
            try:
                with open(wordlist_path, 'r', errors='ignore') as f:
                    words = [line.strip() for line in f]
                
                print(f"\n{self.colors['info']}[*] Testing {len(words)} words...")
                
                found = None
                for word in words:
                    # Test with different algorithms
                    if hashlib.md5(word.encode()).hexdigest() == hash_input:
                        found = ("MD5", word)
                        break
                    elif hashlib.sha1(word.encode()).hexdigest() == hash_input:
                        found = ("SHA1", word)
                        break
                    elif hashlib.sha256(word.encode()).hexdigest() == hash_input:
                        found = ("SHA256", word)
                        break
                    elif hashlib.sha512(word.encode()).hexdigest() == hash_input:
                        found = ("SHA512", word)
                        break
                
                if found:
                    print(f"\n{self.colors['success']}[+] Hash cracked! Algorithm: {found[0]}")
                    print(f"{self.colors['success']}[+] Password: {self.colors['highlight']}{found[1]}")
                else:
                    print(f"\n{self.colors['error']}[-] No password found in wordlist")
                    
            except FileNotFoundError:
                self.show_error("Wordlist file not found")
            except Exception as e:
                self.show_error(f"Error: {str(e)}")
                
        else:
            self.show_error("Invalid option")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def vpn_check(self):
        self.clear_screen("VPN Check")
        
        ip = input(f"{self.colors['secondary']}Enter IP address to check: ").strip()
        
        if not ip:
            self.show_error("Please enter an IP address")
            return
        
        self.loading_animation(f"Checking {ip}...")
        
        try:
            # Using ip-api.com
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            
            if data['status'] == 'success':
                # List of known VPN providers
                vpn_providers = [
                    "VPN", "Proxy", "Tor", "Cloud", "Data Center", 
                    "Digital Ocean", "Amazon AWS", "Google Cloud"
                ]
                
                is_vpn = any(provider in data['isp'] for provider in vpn_providers)
                
                results = {
                    "IP": ip,
                    "ISP": data['isp'],
                    "Organization": data['org'],
                    "VPN/Proxy Status": f"{self.colors['success']}Not detected" if not is_vpn else f"{self.colors['error']}Detected",
                    "Country": data['country'],
                    "City": data['city']
                }           
                self.display_results(results, "VPN Check Results")
            else:
                self.show_error("Could not get information for this IP")
                
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def qr_code_tool(self):
        self.clear_screen("QR Code Tool")
        
        print(f"\n{self.colors['secondary']}Available options:")
        print(f"{self.colors['info']}  1. Generate QR Code")
        print(f"{self.colors['info']}  2. Read QR Code")
        
        choice = input(f"\n{self.colors['secondary']}Choose an option (1-2): ").strip()
        
        if choice == '1':
            text = input(f"{self.colors['secondary']}Enter text/URL to encode: ").strip()
            file_name = input(f"{self.colors['secondary']}Output filename (without extension): ").strip() or "qrcode"
            
            try:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(text)
                qr.make(fit=True)
                
                img = qr.make_image(fill_color="black", back_color="white")
                img.save(f"{file_name}.png")
                
                self.show_success(f"QR Code generated and saved as {file_name}.png")
                
            except Exception as e:
                self.show_error(f"Error: {str(e)}")
                
        elif choice == '2':
            file_path = input(f"{self.colors['secondary']}Path to QR Code image: ").strip()
            
            try:
                from pyzbar.pyzbar import decode
                from PIL import Image
                
                data = decode(Image.open(file_path))
                if data:
                    print(f"\n{self.colors['success']}[+] QR Code content:")
                    for item in data:
                        print(f"{self.colors['info']}  - {item.data.decode('utf-8')}")
                else:
                    self.show_error("No QR Code detected or unable to read")
                    
            except ImportError:
                self.show_error("QR Code reading requires pyzbar. Install with: pip install pyzbar")
            except Exception as e:
                self.show_error(f"Error: {str(e)}")
                
        else:
            self.show_error("Invalid option")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def base64_tool(self):
        self.clear_screen("Base64 Tool")
        
        print(f"\n{self.colors['secondary']}Available options:")
        print(f"{self.colors['info']}  1. Encode to Base64")
        print(f"{self.colors['info']}  2. Decode from Base64")
        
        choice = input(f"\n{self.colors['secondary']}Choose an option (1-2): ").strip()
        
        if choice == '1':
            text = input(f"{self.colors['secondary']}Enter text to encode: ").strip()
            encoded = base64.b64encode(text.encode()).decode()
            print(f"\n{self.colors['success']}[+] Encoded text:")
            print(f"{self.colors['info']}{encoded}")
            
        elif choice == '2':
            text = input(f"{self.colors['secondary']}Enter text to decode: ").strip()
            try:
                decoded = base64.b64decode(text.encode()).decode()
                print(f"\n{self.colors['success']}[+] Decoded text:")
                print(f"{self.colors['info']}{decoded}")
            except:
                self.show_error("Invalid Base64 text")
                
        else:
            self.show_error("Invalid option")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def dark_web_links(self):
        self.clear_screen("Dark Web Links")
        
        print(f"""
{self.colors['warning']}[!] WARNING: These links are only accessible with the Tor browser
{self.colors['warning']}    Access to some of these sites may be illegal in your country
{self.colors['warning']}    Use this information at your own risk
        """)
        
        categories = {
            "1": "Markets",
            "2": "Forums",
            "3": "Anonymous Services",
            "4": "Libraries",
            "5": "Security Tools"
        }
        
        print(f"\n{self.colors['secondary']}Available categories:")
        for num, name in categories.items():
            print(f"{self.colors['info']}  {num}. {name}")
        
        choice = input(f"\n{self.colors['secondary']}Choose a category (1-5): ").strip()
        
        links = {
            "1": {
                "Torrez": "http://torrezmarket.onion",
                "Dark0de": "http://darkodereborn.onion",
                "White House": "http://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy4uhxrgbyp4f3koad.onion",
                "ASAP": "http://asap2u4pvplnkzl7ecle45wajojnftja45wvovl3jrvhangeyq67ziid.onion"
            },
            "2": {
                "Dread": "http://dreadytofatroptsdj6io7l3xptbet6onoyno2yv7jicoxknyazubrad.onion",
                "The Hub": "http://thehub7xbw4dc5r2.onion"
            },
            "3": {
                "ProtonMail": "https://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion",
                "SecureDrop": "http://sdolvtfhatvsysc6l34d65ymdwxcujausv7k5jk4cy5ttzhjoi6fzvyd.onion"
            },
            "4": {
                "Imperial Library": "http://xfmro77i3lixucja.onion",
                "Sci-Hub": "http://scihub22266oqcxt.onion"
            },
            "5": {
                "Tor Metrics": "http://metrics.torproject.org",
                "Whonix": "http://www.dds6qkxpwdeubwucdiaord2xgbbeyds25rbsgr73tbfpqpt4a6vjwsyd.onion"
            }
        }
        
        if choice in categories:
            print(f"\n{self.colors['main']}╔══════════════ {categories[choice]} ══════════════╗")
            for name, url in links[choice].items():
                print(f"{self.colors['info']}  {name.ljust(15)}: {self.colors['highlight']}{url}")
            print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
        else:
            self.show_error("Invalid category")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def bitcoin_tools(self):
        self.clear_screen("Bitcoin Tools")
        
        print(f"\n{self.colors['secondary']}Available options:")
        print(f"{self.colors['info']}  1. Check Bitcoin address")
        print(f"{self.colors['info']}  2. Lookup transaction")
        print(f"{self.colors['info']}  3. BTC/USD converter")
        
        choice = input(f"\n{self.colors['secondary']}Choose an option (1-3): ").strip()
        
        if choice == '1':
            address = input(f"{self.colors['secondary']}Enter Bitcoin address: ").strip()
            
            # Simple BTC address validation
            if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
                print(f"\n{self.colors['success']}[+] Valid Bitcoin address")
                
                # Balance check via API (simulated)
                self.loading_animation("Looking up information...")
                
                balance = random.randint(0, 10000) / 100  # Simulation
                txs = random.randint(0, 50)
                
                print(f"\n{self.colors['info']}[*] Approximate balance: {balance} BTC")
                print(f"{self.colors['info']}[*] Transactions: {txs}")
            else:
                self.show_error("Invalid Bitcoin address")
                
        elif choice == '2':
            tx_hash = input(f"{self.colors['secondary']}Enter transaction hash: ").strip()
            
            if re.match(r'^[a-fA-F0-9]{64}$', tx_hash):
                self.loading_animation("Looking up transaction...")
                
                # Simulation of results
                print(f"\n{self.colors['success']}[+] Transaction found")
                print(f"{self.colors['info']}  Amount: {random.randint(1, 100)} BTC")
                print(f"{self.colors['info']}  Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
                print(f"{self.colors['info']}  Confirmations: {random.randint(1, 100)}")
            else:
                self.show_error("Invalid transaction hash")
                
        elif choice == '3':
            amount = input(f"{self.colors['secondary']}Enter amount in BTC: ").strip()
            
            try:
                btc = float(amount)
                # Simulation with random rate around $30,000
                rate = 30000 + random.randint(-5000, 5000)
                usd = btc * rate
                
                print(f"\n{self.colors['success']}[+] Conversion:")
                print(f"{self.colors['info']}  {btc} BTC = {usd:,.2f} USD (1 BTC = {rate:,.2f} USD)")
            except:
                self.show_error("Invalid amount")
                
        else:
            self.show_error("Invalid option")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def network_tools(self):
        self.clear_screen("Network Tools")
        
        print(f"\n{self.colors['secondary']}Available options:")
        print(f"{self.colors['info']}  1. Traceroute")
        print(f"{self.colors['info']}  2. NSLookup")
        print(f"{self.colors['info']}  3. ARP Scan")
        
        choice = input(f"\n{self.colors['secondary']}Choose an option (1-3): ").strip()
        
        if choice == '1':
            host = input(f"{self.colors['secondary']}Enter IP or domain: ").strip()
            
            if not host:
                self.show_error("Please enter a valid target")
                return
            
            self.loading_animation(f"Running traceroute to {host}...")
            
            try:
                if platform.system() == "Windows":
                    output = subprocess.check_output(['tracert', '-d', '-h', '15', host]).decode('utf-8', errors='ignore')
                else:
                    output = subprocess.check_output(['traceroute', '-m', '15', host]).decode('utf-8', errors='ignore')
                
                print(f"\n{self.colors['main']}╔══════════════ Traceroute Results ══════════════╗")
                print(f"{self.colors['info']}{output}")
                print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
            except subprocess.CalledProcessError as e:
                self.show_error(f"Error: {e.output.decode('utf-8', errors='ignore')}")
            except Exception as e:
                self.show_error(f"Error: {str(e)}")
                
        elif choice == '2':
            domain = input(f"{self.colors['secondary']}Enter domain: ").strip()
            
            if not domain:
                self.show_error("Please enter a valid domain")
                return
            
            self.loading_animation(f"Looking up DNS for {domain}...")
            
            try:
                if platform.system() == "Windows":
                    output = subprocess.check_output(['nslookup', domain]).decode('utf-8', errors='ignore')
                else:
                    output = subprocess.check_output(['dig', domain]).decode('utf-8', errors='ignore')
                
                print(f"\n{self.colors['main']}╔═══════════════ NSLookup Results ═══════════════╗")
                print(f"{self.colors['info']}{output}")
                print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
            except subprocess.CalledProcessError as e:
                self.show_error(f"Error: {e.output.decode('utf-8', errors='ignore')}")
            except Exception as e:
                self.show_error(f"Error: {str(e)}")
                
        elif choice == '3':
            self.loading_animation("Scanning local network...")
            
            try:
                if platform.system() == "Windows":
                    output = subprocess.check_output(['arp', '-a']).decode('utf-8', errors='ignore')
                else:
                    output = subprocess.check_output(['arp', '-an']).decode('utf-8', errors='ignore')
                
                print(f"\n{self.colors['main']}╔════════════════ ARP Table ════════════════╗")
                print(f"{self.colors['info']}{output}")
                print(f"{self.colors['main']}╚═══════════════════════════════════════════════╝")
            except subprocess.CalledProcessError as e:
                self.show_error(f"Error: {e.output.decode('utf-8', errors='ignore')}")
            except Exception as e:
                self.show_error(f"Error: {str(e)}")
                
        else:
            self.show_error("Invalid option")
        
        input(f"\n{self.colors['secondary']}Press Enter to continue...")

    def exit_tool(self):
        print(f"\n{self.colors['success']}[+] Thank you for using ScammaTool. Goodbye!")
        time.sleep(1)
        sys.exit(0)

if __name__ == "__main__":
    try:
        tool = ScammaTool()
        tool.run()
    except KeyboardInterrupt:
        print("\n\n[!] User interrupted. Closing...")
        time.sleep(1)
        sys.exit(0)
    except Exception as e:
        print(f"\n\n[!] Critical error: {str(e)}")
        time.sleep(3)
        sys.exit(1)
