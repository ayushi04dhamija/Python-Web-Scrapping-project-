from urllib.request import urlopen as uReq
 from bs4 import BeautifulSoup as soup
 

 # opening up connection,grabbing the page

  uClient = uReq(my_url)
  page_html = uClient.read()
  uClient.close()
  
  # html parsing
  page_soup = soup(page_html, "html.parser")

  #grabs each product
  containers =  page_soup.findAll("div",{"class":"item-container"})
  len(containers)
  page_soup.h1
  page_soup.p
  page_soup.body.span
  containers[0]
 contain = containers[0]
 container = containers[0]
 container.a
 container.div
 container.div.div.a
 container.div.div.a.img


 containers .findAll("div",{"class":"item-title"})
 for container in containers:
 	brand = container.div.div.a.img["title"]


title_container = container.findAll("div",{"class":"item-title"})
title_container
title_container[0].text
shipping_container = container.findAll("li",{"class":"price-ship"}....) 	
shipping_container[0].text
shipping_container
shipping = shipping_container[0].text.strip()
print("brand:" + brand)
print("product_name:" + product_name)
print("shipping:" + shipping)

