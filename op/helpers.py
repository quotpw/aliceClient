import psutil


def get_mac_address():
    interfaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if address.family == psutil.AF_LINK:
                return address.address.replace('-', ':')

