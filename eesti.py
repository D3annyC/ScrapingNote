# %%
import requests
from bs4 import BeautifulSoup
import re


def main(word, lang):
    query = []
    query.append({
        'Q': word,
        'F': 'A',
        'C06': lang,
        'C01': '1',
        'C02': '1',
        'C03': '1',
        'C04': '1',
        'C05': '1',
        'C08': '1',
        'C09': '1',
        'C12': '1',
        'C13': '1'
    })
    print('English-Estonian MT dictionary')
    dom = requests.get(
        'http://www.eki.ee/dict/ies/index.cgi?Q=tere&F=M&C06=en').text
    soup = BeautifulSoup(dom, 'html5lib')
    for ele in soup.find_all('div', re.compile('tervikart')):
        print(
            ele.find('span', 'm').text,
            ele.find('span', 'x').text
        )


if __name__ == '__main__':
    main('palju', 'en')
