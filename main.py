#first I will start by making sure i can scrape data from one website
# gather information from different websites
#use data to create a list of current most liked books
#allow users to select a genre 
#generate the top 10 based on genre
#save list to excel sheet
# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# book_genre = ('romance', 'fantasy', 'young adult', 'sicence fiction', 'self-help', 'romantasy', 'historical fantasy', 'mystery', 'thriller')
# print('These are the current genre options: \n' )
# for genre in book_genre:
#     print(genre + '\n')

# coice = input('What genre are you interested in? ').lower()

driver = webdriver.Chrome()
driver.get('https://www.barnesandnoble.com/b/books/_/N-1fZ29Z8q8')

results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for element in soup.find_all(attrs={'class': 'product-shelf-title'}):
    name = element.find('a')
    if name not in results:
        results.append(name.text)
for x in results:
    print(x)
# df = pd.DataFrame({'Names': results})
# df.to_excel('names.xlsx', index=False)

