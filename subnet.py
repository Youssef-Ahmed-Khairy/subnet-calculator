import argparse
import sys


def ip_to_int(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        raise ValueError(f"Invalid IPv4 address: {ip}")
    value = 0
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            raise ValueError(f"Invalid IPv4 address: {ip}")
        value = (value << 8) | int(part)
    return value


def int_to_ip(value):
    return ".".join(str((value >> shift) & 0xFF) for shift in (24, 16, 8, 0))


def calculate(cidr):
    try:
        ip_str, prefix_str = cidr.split("/")
        prefix = int(prefix_str)
    except ValueError:
        raise ValueError("Use CIDR notation, e.g. 192.168.1.10/24")
    if not 0 <= prefix <= 32:
        raise ValueError("Prefix must be between 0 and 32")

    ip = ip_to_int(ip_str)
    mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
    wildcard = ~mask & 0xFFFFFFFF
    network = ip & mask
    broadcast = network | wildcard
    total = 2 ** (32 - prefix)

    if prefix >= 31:  # /31 point-to-point and /32 single host reserve no addresses
        first, last, usable = network, broadcast, total
    else:
        first, last, usable = network + 1, broadcast - 1, total - 2

    return {
        "network": int_to_ip(network),
        "mask": int_to_ip(mask),
        "wildcard": int_to_ip(wildcard),
        "broadcast": int_to_ip(broadcast),
        "first": int_to_ip(first),
        "last": int_to_ip(last),
        "total": total,
        "usable": usable,
    }


def main():
    parser = argparse.ArgumentParser(description="IPv4 subnet calculator")
    parser.add_argument("cidr", help="e.g. 192.168.1.10/24")
    args = parser.parse_args()
    try:
        result = calculate(args.cidr)
    except ValueError as err:
        sys.exit(f"Error: {err}")

    labels = [
        ("Network", "network"),
        ("Mask", "mask"),
        ("Wildcard", "wildcard"),
        ("Broadcast", "broadcast"),
        ("First host", "first"),
        ("Last host", "last"),
        ("Total addresses", "total"),
        ("Usable hosts", "usable"),
    ]
    for label, key in labels:
        print(f"{label:<16}{result[key]}")


if __name__ == "__main__":
    main()
