import requests
import sys


def resolve_domain(domain: str) -> str:
    url = 'https://cloudflare-dns.com/dns-query'
    params = {
        'name': domain,
        'type': 'A',
    }
    headers = { 
        'accept': 'application/dns-json' 
    }

    response = requests.get(url, params, headers=headers)
    response.raise_for_status()

    data = response.json()
    if "Answer" in data and len(data["Answer"]) > 0:
        ip_address = data["Answer"][0]["data"]
        return ip_address
    else:
        raise ValueError(f"No A record found for domain: {domain}")


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        raise ValueError('Invalid number of arguments. Usage: python script.py <domain>')

    domain = sys.argv[1]

    ip = resolve_domain(domain)
    print(f'{domain} -> {ip}')
