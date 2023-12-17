from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import time

_baseurl_ = 'https://www.mumzworld.com'
driver = webdriver.Chrome()

productLinks = []
for x in range(1,9):
    driver.get("https://www.mumzworld.com/en/search.html?q=pigeonhttps://www.mumzworld.com/en/search.html?q=pigeon={}".format(x))
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    productlist = soup.find_all("a",{"class":"item-name-3AC"})
    for j in productlist:
        get = j['href']
        link = _baseurl_ + get
        productLinks.append(link)
    print (len(productLinks))

    data = []

for link in productLinks:
    driver.get(link)
    psoup = BeautifulSoup(driver.page_source, 'lxml')
    
    try:
        name=psoup.find("h1",{"class":"productFullDetail-productName-3Po"}).text.replace('\n',"")
    except:
        name = None
    
    try:
        description = psoup.find("div",{"class":"descriptionPDP-description-1ba"}).text.replace('\n'," ")
    except:
        description = None
    
    try:
        price=psoup.find("span",{"class":"price-integer-2Ym"}).text.replace('\n',"")
    except:
        price = None
        
    try:
        overview = psoup.find("div",{"class":"descriptionPDP-overview-TJH"}).text.replace('\n'," ")
    except:
        overview = None
    
    try:
        image = psoup.find("img",{"class":"image-image-TgM image-loaded-1bg"})['src']
    except:
        image = None

    product = {"name":name,"price":price,"description":description, "overview":overview, "image":image}
    
    data.append(product) 

df = pd.DataFrame(data)
print(df)
df.to_excel('products.xlsx', sheet_name='new_sheet_name')

