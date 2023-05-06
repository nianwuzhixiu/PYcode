import requests,fake_useragent,bs4

url = 'https://www.1qxs.com/xs/61487/1.html'
ua = fake_useragent.UserAgent()
headers = {
    'Authorization': 'Basic YOUR_AUTH_INFO',  # 提供Token认证
    'User-Agent': ua.random  # 随机生成一个User-Agent
}
res = requests.get(url, headers=headers)
try:
    res.raise_for_status()
    playFile = open('downwb.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
except Exception as exc:
    print('There was a problem: %s' %  (exc))
