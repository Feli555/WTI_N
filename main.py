import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup
from selenium import webdriver

# Pages 2 use: Investing and markets insider
url_mktIns = "https://markets.businessinsider.com/commodities/oil-price?type=wti"

driver = webdriver.Chrome(os.path.abspath('chromedriver.exe'))
driver.get("https://www.investing.com/commodities/crude-oil-news")

art_d = []

page_source = BeautifulSoup(driver.page_source, "lxml")
sec = page_source.find("section")
div = sec.find("div", {'class': 'mediumTitle1'})
for tag in div.contents:
    if str(type(tag)) == "<class 'bs4.element.Tag'>":
        art_d.append(tag)
art_d.pop(-1)
for art in art_d:
    # print(f"Len: {len(art.attrs)}")
    # print("Text:")
    t_s_n = art.text.split('\n')
    # print(t_s_n)
    t_s_n = [s1 for s1 in t_s_n if s1 != '']
    # print(t_s_n)
    # print(f"Len: {len(t_s_n)}")
    if len(t_s_n) == 3:
        t_s_n[1] = t_s_n[1].split('\xa0-\xa0')
        t_s_n[1] = t_s_n[1][0] + ", " + t_s_n[1][1]
        print(f"Title: {t_s_n[0]}")
        print(f"Provider: {t_s_n[1]}")
        print(f"Abstract: {t_s_n[2]}")
    else:
        t_s_n[2] = t_s_n[2].split('\xa0-\xa0')
        t_s_n[2] = t_s_n[2][0] + ", " + t_s_n[2][1]
        print(f"Title: {t_s_n[1]}")
        print(f"Provider: {t_s_n[2]}")
        if len(t_s_n) == 6:
            print(f"Abstract: {t_s_n[5]}")
        else:
            print(f"Abstract: {t_s_n[4]}")

    if len(art.attrs) == 5:
        print(f"Link: {art.attrs['data-link']}")
    else:
        inv = "https://investing.com"
        print(f"Link: {inv + art.contents[1].attrs['href']}")
    print("-------------")
driver.close()
driver.quit()
