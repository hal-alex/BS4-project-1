from bs4 import BeautifulSoup
import requests
import lxml

text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(text, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
