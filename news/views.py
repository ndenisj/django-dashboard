from django.shortcuts import render
import requests
requests.packages.urllib3.disable_warnings() #remove all the request packsges warnings
from bs4 import BeautifulSoup

# Create your views here.
# def scrape():
#     session = requests.Session()
#     session.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"}
#     url = "https://www.bbc.com/"
#
#     content = session.get(url, verify=False).content
#
#     soup = BeautifulSoup(content, "html.parser");
#
#     post = soup.find_all('ul', {'class': 'media-list'})
#
#     # print(post)
#
#     for i in post:
#         link = i.find('a', {'class': 'media__link'})[1]['href']
#         # image_source = i.find('img', {'class': 'image-replace'})['alt']
#         print(link)
#         # print(image_source)
#
# scrape()