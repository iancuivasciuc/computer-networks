import requests
import sys


def get_double_get(value: int) -> None:
    url = 'http://rt1:8080/double'
    payload = { 'value': value }
    headers = { 'content-type': 'application/json' }

    response = requests.get(url, params=payload, headers=headers)
    response.raise_for_status()

    data = response.json()
    print(data)


def get_double_post(value: int) -> None:
    url = 'http://rt1:8080/double'
    payload = { 'value': value }
    headers = { 'content-type': 'application/json' }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    data = response.json()
    print(data)


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        raise ValueError('Invalid number of arguments. Usage: python script.py <value>')

    value = int(sys.argv[1])

    get_double_get(value)
    get_double_post(value)
