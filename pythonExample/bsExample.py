import requests
import bs4
import lxml

URL = 'https://www.ptt.cc/bbs/Gossiping/index.html'
header = {'cookie': 'over18=1;'}

respon = requests.get(URL, headers=header)
soup = bs4.BeautifulSoup(respon.text, 'lxml')
posts = soup.find('div', class_='r-list-container')
#push = soup.select('div .nrec')
pushes = posts.select('div .title')

for push in pushes:
    print(push.getText())
