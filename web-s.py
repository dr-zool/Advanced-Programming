"""
!apt install chromium-chromedriver
pip install selenium
pip install beautifulsoup4
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
#driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install())

products=[] #List to store name of the product
prices=[] #List to store price of the product
features=[] #List to store rating of the product

driver.get("https://www.flipkart.com/search?q=32%20inch%20tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")

content = driver.page_source
soup = BeautifulSoup(content)


for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    name=a.find('div',attrs={'class':'_4rR01T'})
    price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    feature=a.find('div',attrs={'class':'_2_R_DZ'})
    products.append(name.text)
    prices.append(price.text)
    features.append(feature.text)

df = pd.DataFrame({'Product Name':products,'Price':prices , 'Feature':features})
print(df.head())
df.to_csv('products.csv', index=False, encoding='utf-8')
