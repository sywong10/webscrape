import requests
import os

os.mkdir('book_images')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

with open('image_links.txt', 'r') as f:
    links_text = f.read()
    links_list = links_text.split('\n')
    print(links_list)

for i, image_url in enumerate(links_list):
    response = requests.get(image_url, headers=headers)
    with open(f'book_images/{i+1}.jpg', 'wb') as imagefile:
        imagefile.write(response.content)


