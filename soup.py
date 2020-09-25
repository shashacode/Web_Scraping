from bs4 import BeautifulSoup
import requests

# html_file = open("C:/Users/fresh/Documents/Overall python/coding/Beautifulsoup/index.html", "r")
# html_data = html_file.read()

# soup = BeautifulSoup(html_data, features="html.parser")
# print(soup)

# filter = soup.find('u')
# print(filter.text)  #.text gives d body alone without the code

#using beautiful soup with resources on internet
# jumia_url ="https://www.jumia.com.ng/smartphones/"
# jumia_request = requests.get(jumia_url)

# jumia_html = jumia_request.content

# # print(jumia_html) 

# jumia_soup = BeautifulSoup(jumia_html, features = "html.parser")
# h3_filter = jumia_soup.find_all("h3")


# for product in h3_filter:
#     print(product.text)
#     print() 

# wiki_url = "https://en.wikipedia.org/wiki/Nigeria"
# wiki_request = requests.get(wiki_url)

# wiki_html = wiki_request.content

# print(wiki_html)

# wiki_soup = BeautifulSoup(wiki_html, features = "html.parser")

# filter_1 = wiki_soup.find_all("th")

# filter_2 = wiki_soup.find_all("a")

# filter_3 = wiki_soup.find_all("td")

# filter_4 = wiki_soup.find_all("th", "a", "td")



# for Nigeria in filter_1:
#     print(Nigeria.text)
#     print()

# for Nigeria in filter_2:
#     print(Nigeria.text)
#     print()

# for Nigeria in filter_3:
#     print(Nigeria.text)
#     print()

# for Nigeria in filter_4:
#     print(Nigeria.text)
#     print() 