import requests
import ipaddress


def main():
    response = requests.get("https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2024/04/large-scale-brute-force"
                            "-activity-targeting-vpns-ssh-services-with-commonly-used-login-credentials.txt")

    iocs = [ioc.replace('[', '').replace(']', '') for ioc in response.text.split("\n")]

    iocs_ip = []
    try:
        for ip in iocs[1::]:
            if ipaddress.ip_address(ip):
                iocs_ip.append(ip)
    except Exception:
        pass

    with open("iocs_ip.txt", 'w') as file:
        file.write(iocs_ip[0])
        for ip in iocs_ip[1::]:
            file.write(f"\n{ip}")


if __name__ == "__main__":
    main()
