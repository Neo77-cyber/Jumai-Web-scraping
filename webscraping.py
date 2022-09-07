
import bs4
from bs4 import BeautifulSoup
import requests
page_directory = "https://www.jumia.com.ng/catalog/?q=iphone&page={}#catalog-listing"
re = requests.get(page_directory.format(2))
soup = bs4.BeautifulSoup(re.text, "lxml")
product = soup.select(".core")

example = product[0]

phone_name = example.select(".name")

five_star_rating = []

for n in range (1,51):
    pages = page_directory.format(n)
    re = requests.get(pages)
    soup = bs4.BeautifulSoup(re.text, "lxml")
    phones = soup.select(".core")

    for phone in phones:
        if "5 out of 5" in str(phone):
            phone_id = phone.select(".name")
            five_star_rating.append(phone_id)
print(len(five_star_rating))