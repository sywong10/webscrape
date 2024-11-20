import requests

from src.page_count import headers

headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36' }

with open('proxy_list.txt', 'r') as p:
    proxy_string = p.read()
    proxy_list = proxy_string.split('\n')

for proxy in proxy_list:
    proxy_url = f'http://{proxy}'

    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }

    url = 'https://books.toscrape.com'

    try:
        response = requests.get(url, proxies=proxies, headers=headers)

        if response.status_code == 200:
            print(f'Request is successful.  Proxy: {proxy}')
        else:
            print(f'Request failed.  Proxy: {proxy}, Status code: {response.status_code}')
    except Exception as e:
        print(f'Request failed.  Proxy: {proxy}, Exception: {e}')

