from flask import Flask, render_template, jsonify
from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
import subprocess
import platform
import socket
import threading
import queue
import ipaddress
import time
import socket as sk

app = Flask(__name__)
mac_lookup = MacLookup()

PING_TIMEOUT = 1
PORT_SCAN_TIMEOUT = 0.3

def ping(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", "-w", str(PING_TIMEOUT*1000), ip] if platform.system().lower() == "windows" else ["ping", param, "1", "-W", str(PING_TIMEOUT), ip]
    try:
        res = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return res.returncode == 0
    except Exception:
        return False

def scan_port(ip, port=80):
    sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    sock.settimeout(PORT_SCAN_TIMEOUT)
    try:
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

def guess_device_type(vendor, hostname):
    vendor = vendor.lower() if vendor else ""
    hostname = hostname.lower() if hostname else ""
    if any(x in vendor for x in ['apple', 'samsung', 'huawei', 'xiaomi', 'google']):
        return "Smartphone/Tablet"
    if any(x in vendor for x in ['cisco', 'tplink', 'netgear', 'asus', 'd-link']):
        return "Routeur/Box"
    if any(x in vendor for x in ['intel', 'dell', 'hp', 'lenovo', 'acer']):
        return "Ordinateur"
    if any(x in hostname for x in ['iphone', 'ipad', 'android', 'pixel', 'galaxy']):
        return "Smartphone/Tablet"
    if any(x in hostname for x in ['nas', 'synology', 'qnap']):
        return "NAS"
    return "Inconnu"

def scan_network(network="192.168.1.0/24"):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    try:
        result = srp(packet, timeout=3, verbose=0)[0]
    except Exception as e:
        print(f"Erreur scan ARP: {e}")
        result = []

    macs = {received.psrc: received.hwsrc for sent, received in result}

    net = ipaddress.ip_network(network, strict=False)
    all_ips = [str(ip) for ip in net.hosts()]

    devices = []
    q = queue.Queue()

    def worker():
        while True:
            ip = q.get()
            if ip is None:
                break

            mac = macs.get(ip, "Inconnu")
            try:
                host = socket.gethostbyaddr(ip)[0]
            except:
                host = "Inconnu"

            alive = ping(ip)
            port80 = scan_port(ip)

            try:
                vendor = mac_lookup.lookup(mac) if mac != "Inconnu" else "Inconnu"
            except:
                vendor = "Inconnu"

            dtype = guess_device_type(vendor, host)

            devices.append({
                "ip": ip,
                "mac": mac,
                "host": host,
                "vendor": vendor,
                "alive": alive,
                "latency": None,
                "port80": port80,
                "device_type": dtype
            })
            q.task_done()

    num_threads = 50
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
        threads.append(t)

    for ip in all_ips:
        q.put(ip)

    q.join()

    for _ in range(num_threads):
        q.put(None)
    for t in threads:
        t.join()

    return devices

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan")
def scan():
    network = "X.X.X.X/24"     #X.X.X.X = Votre IP ! ( Ne pas toucher /24 !!! )
    devices = scan_network(network)
    return jsonify(devices)

if __name__ == "__main__":
    app.run(debug=True)
