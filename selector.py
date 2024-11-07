from importlib.util import source_hash

import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com')

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('title')
print('title: {}'.format(title))
print(title.text)

print(soup.title)

# ========

first_quote=soup.find('div', class_='quote')
print('\nfirst_quote: {}'.format(first_quote))

# quote_text = first_quote.find('span', attrs={'itemprop': 'text'})
quote_text = first_quote.find('span', attrs={'itemprop': 'text'}).text

print('\nquote_text: {}'.format(quote_text))

tags_title = soup.find('h2', string='Top Ten tags')
print('\ntags_title: {}'.format(tags_title.text))

tag_box = tags_title.parent
print('\ntags_box: {}'.format(tag_box))

first_tag_span = tags_title.find_next_sibling()
print('\nfirst_tag_span: {}'.format(first_tag_span))

h2_again = first_tag_span.find_previous_sibling()
print('\nh2_again: {}'.format(h2_again))

tag_children = tag_box.children
print('\ntag_children: {}'.format(tag_children))
list_of_children = list(tag_children)
# print(len(list_of_children))

final_children = [ x for x in list_of_children if x != '\n' ]

print(len(final_children))

print('\nfirst_tag_span: {}'.format(first_tag_span))
print(type(first_tag_span))

top_tag_a = first_tag_span.a

print('\ntop_tag_a: {}'.format(top_tag_a))

print(type(top_tag_a))
# top_tag_href = top_tag_a

top_tag_href = top_tag_a['href']
print(top_tag_href)

print('\nfirst_quote: {}'.format(first_quote))
print('\nfirst_quote[class]: {}'.format(first_quote['class']))

print('\nfirst_tag_span: {}'.format(first_tag_span))
print('\nstyle: {}'.format(first_tag_span.a['style']))
