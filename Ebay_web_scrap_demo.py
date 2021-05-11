from bs4 import BeautifulSoup
import requests
import pandas as pd



url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312&_nkw=ipads&_sacat=0"

content = requests.get(url).content

soup = BeautifulSoup(content, "html.parser")

content = soup.find(id="mainContent")

products_on_the_page = content.find_all('li', class_="s-item")
num_of_products_on_page = len(products_on_the_page) - 1
product_name_list = []
product_price_list = []


for item_number in range(1, num_of_products_on_page):
    item_name = products_on_the_page[item_number].find('a', class_="s-item__link").text
    item_Price = products_on_the_page[item_number].find('div', class_="s-item__detail s-item__detail--primary").text
    product_name_list.append(item_name)
    product_price_list.append(item_Price)

ebay_items_dictionary = {'name': product_name_list, 'price': product_price_list}


df = pd.DataFrame(ebay_items_dictionary, columns=['name','price'])

df.to_csv('output.csv')


