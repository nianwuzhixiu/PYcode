import requests, fake_useragent, bs4

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
# type(exampleSoup)
