# Chromeを使ったスクレイピング
import requests
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# オプションでPROXYを設定
PROXY = "socks5://localhost:9050"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--lang=ja-JP')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(chrome_options=options)

# Torを経由できているかの確認
driver.get("http://check.torproject.org")
temp = BeautifulSoup(driver.page_source)
print(temp)
