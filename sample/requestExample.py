# %%
# using requests
import urllib.request
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'https://www.kingstone.com.tw/new/basic/2013120504769?zone=book&lid=search&actid=WISE'
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")

# %%
# using urllib
url = 'http://aaa.24ht.com.tw/'
req = urllib.request.Request(url, headers=headers)
htmlfile = urllib.request.urlopen(req)
print(htmlfile.read().decode('utf-8'))
print('版本：', htmlfile.version)
print('網址：', htmlfile.geturl())
print('狀態：', htmlfile.status)
print('表頭：')
for header in htmlfile.getheaders():
    print(header)

# %%
# using urlretrieve()
url_pict = 'https://baidu.com/img/bd_logo1.png'
fn = 'baidu.png'
pict = urllib.request.urlretrieve(url_pict, fn)
