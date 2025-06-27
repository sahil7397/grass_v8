import os
import sys
import time
import asyncio

try:
    from PyGrassClient import PyGrassClient
except ImportError:
    print("[❌] PyGrassClient not found. Installing it now...")
    os.system("pip install PyGrassClient")

def show_banner():
    banner = """
    ┌────────────────────────────────────────────┐
    │        🌲 FOREST ARMY SCRIPT TOOL 🌲       │
    ├────────────────────────────────────────────┤
    │ Author   : ITSMESATYAVIR                   │
    │ Version  : 8.1 (with Grass 1.25x Boost)    │
    │ Contact  : t.me/forestarmy                 │
    │           t.me/rspyder2_bot                │
    └────────────────────────────────────────────┘
    """
    print(banner)

show_banner()

urls = [
    "https://www.profitableratecpm.com/rfzgg4b8?key=d854215a4b3c449e653cd67d89b382d0",
    "https://www.profitableratecpm.com/zssjbg72?key=e386c4eb68236f3c2f097be5345b01fc"
]

for url in urls:
    print(f"[+] Opening: {url}")
    os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
    time.sleep(5)

print("\nTHANK YOU!!")

# ─── Terminal Color Setup ──────────────────────
BOLD = "\033[1m"
RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
BLUE = "\033[94m"

# ─── Menu Display ──────────────────────────────
BANNER = f"""
{GREEN}{BOLD}
╔═════════════════════════════════════════════════╗
║               🛠️ SCRIPT MENU TOOL                ║
╠═════════════════════════════════════════════════╣
║ {CYAN}1 - Run Grass Client (1.25×){GREEN}                   ║
║ {CYAN}2 - Delete Logs (free space){GREEN}                    ║
║ {CYAN}3 - Enter Proxy (manual input){GREEN}                  ║
║ {CYAN}4 - Download Free Proxy List{GREEN}                    ║
║ {CYAN}5 - Exit{GREEN}                                        ║
╚═════════════════════════════════════════════════╝

{YELLOW}🔄 Never Pay Full Price Again!{RESET}
Use {BOLD}FOREST15{RESET} on {BLUE}https://youproxy.io/{RESET} 💸

{GREEN}{BOLD}
╔═════════════════════════════════════════════════╗
║ 🔰 FORESTARMY Community                         ║
║ 🔗 https://t.me/forestarmy                      ║
╚═════════════════════════════════════════════════╝
{RESET}
"""

# ─── GRASS CLIENT RUNNER ────────────────────────
async def run_grass_client():
    try:
        with open("user_id.txt", "r") as f:
            user_ids = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{RED}[❌] user_id.txt not found. Please create it and add your Grass user ID(s).{RESET}")
        return

    try:
        with open("proxy.txt", "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        proxies = [None] * len(user_ids)

    if not user_ids:
        print(f"{RED}[❌] No user IDs found in user_id.txt.{RESET}")
        return

    print(f"{YELLOW}[🌿] Starting {len(user_ids)} Grass client(s)...{RESET}\n")

    tasks = []
    for i, user_id in enumerate(user_ids):
        proxy = proxies[i] if i < len(proxies) else None
        print(f"{CYAN}[🟢] Connecting user {user_id} {'with proxy' if proxy else 'without proxy'}...{RESET}")
        client = PyGrassClient(user_id=user_id, proxy_url=proxy)
        tasks.append(client.connect_ws())

    await asyncio.gather(*tasks)

def run_script():
    asyncio.run(run_grass_client())

# ─── MENU OPTION: Delete Logs ───────────────────
def delete_logs():
    print(f"\n{YELLOW}[🧹] Deleting logs...{RESET}\n")
    os.system("rm -f *.log logs/*.log")

# ─── MENU OPTION: Proxy Entry ───────────────────
def enter_proxy():
    print(f"\n{CYAN}[✍️] Enter proxy manually (one per line). Type 'done' to finish.{RESET}\n")
    proxies = []
    while True:
        proxy = input("Proxy: ").strip()
        if proxy.lower() == 'done':
            break
        if proxy:
            proxies.append(proxy)
    with open("proxy.txt", "w") as f:
        f.write("\n".join(proxies))
    print(f"\n{GREEN}[✅] Saved {len(proxies)} proxies to proxy.txt{RESET}")

# ─── MENU OPTION: Download Proxies ───────────────
def download_free_proxy():
    print(f"\n{CYAN}[🌐] Downloading free proxy list...{RESET}\n")
    os.system("curl -s https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt -o proxy.txt")
    print(f"{GREEN}[✅] Proxy list downloaded to proxy.txt{RESET}")

# ─── Main Menu Loop ──────────────────────────────
def main():
    while True:
        print(BANNER)
        choice = input(f"{BOLD}Select an option (1-5): {RESET}").strip()
        if choice == '1':
            run_script()
        elif choice == '2':
            delete_logs()
        elif choice == '3':
            enter_proxy()
        elif choice == '4':
            download_free_proxy()
        elif choice == '5':
            print(f"\n{YELLOW}[👋] Exiting. Have a great day!{RESET}\n")
            sys.exit()
        else:
            print(f"{RED}[❌] Invalid choice. Please select 1-5.{RESET}\n")

if __name__ == "__main__":
    main()