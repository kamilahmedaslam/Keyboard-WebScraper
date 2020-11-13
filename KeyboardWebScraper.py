from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from urllib.request import Request as req

url = 'https://mechanicalkeyboards.com/shop/index.php?l=product_list&c=1&display=tile&show=100&sortby='

#opening the connection to grab the page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

filename = "keyboards.csv"
f = open(filename, "w")
headers = "keyboard_name, key_types, keyboard_price, keyboard_ratings\n"

f.write(headers)

#html parser
page_soup = soup(page_html, "html.parser")

boxes = page_soup.findAll("div", {"class":"product-box"})

for box in boxes:
	keyboard_name = box.div.div.a.img["alt"]
	
	info_box = box.findAll('div', {"class":"info"})
	key_types = info_box[0].text.strip()
	
	sale_box = box.findAll("span", {"class":"sale"})
	keyboard_price = sale_box[0].text

	compare_box = box.findAll("div", {"class":"rating"})
	keyboard_ratings = compare_box[0].img["alt"]

	print("keyboard_name: " + keyboard_name)
	print("key_types: " + key_types)
	print("keyboard_price: " + keyboard_price)
	print("keyboard_ratings: " + keyboard_ratings)

	f.write(keyboard_name.replace(",", "|") + ',' + key_types + ',' + keyboard_price + ',' + keyboard_ratings + '\n')

f.close()