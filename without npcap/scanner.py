import subprocess
import socket    

def isReachable(ip):
    try:
        answer = subprocess.check_output(["ping", "-n", "1", ip], timeout=0.05)
    except subprocess.TimeoutExpired:
        return False

    if "host unreachable" in answer.decode():
        return False
    
    return True

def scanNetwork(out=False):
    IPAdrr = getIPv4()
    IPAdrr = IPAdrr.split(".")

    devices = []
    for x in range(256):
        IPAdrr[2] = str(x)
        for i in range(256):
            IPAdrr[3] = str(i)
            ip = ".".join(IPAdrr)

            if isReachable(ip):
                devices.append(ip)
                if out:
                    print(f"found {ip}!")

    return devices

def getIPv4():
    hostname = socket.gethostname()    
    return socket.gethostbyname(hostname)

if __name__ == "__main__":
    devices = scanNetwork(out=True)

    with open("out.txt", "w+") as f:
        devices = "\n".join(devices)
        f.write(devices)
