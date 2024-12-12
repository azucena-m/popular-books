import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver






driver = webdriver.Chrome()
driver.get('https://sandbox.oxylabs.io/products')
url = 'https://www.oxylabs.io/blog'
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for element in soup.find_all(attrs={'class': 'product-card'}):
    name = element.find('h4')
    if name not in results:
        results.append(name.text)
df = pd.DataFrame({'Names': results})
df.to_excel('names.xlsx', index=False)