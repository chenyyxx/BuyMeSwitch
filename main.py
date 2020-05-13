from datetime import datetime
from bs4 import BeautifulSoup
import time
import requests
import SendMail
import call


# return a status of availability of a product
def status (url, headers):
    respond = requests.get(url, headers=headers)
    print('HTTP', respond.status_code)
    html = respond.content
    soup = BeautifulSoup(html, 'lxml')
    match = soup.find('div', class_='fulfillment-add-to-cart-button')
    status = match.text
    return status

def status_target(url, headers):
    respond = requests.get(url, headers=headers)
    print('HTTP', respond.status_code)
    html = respond.content
    soup = BeautifulSoup(html, 'lxml')
    out_of_stock = soup.select("#viewport > div:nth-child(4) > div > div.Row-uds8za-0.kPQaTV > div.Col-favj32-0.eKPqHP.h-padding-h-default.h-padding-t-tight > div:nth-child(1) > div > div > div > div.styles__StyledShipping-sc-1gn4z07-1.fGhQiy > div.styles__ShippingHeading-sc-1n8m629-1.gpHhH")[0].text
    return out_of_stock

# Start in 2 hours
#time.sleep(7200)
url0 = 'https://www.bestbuy.com/site/nintendo-switch-32gb-console-neon-red-neon-blue-joy-con/6364255.p?skuId=6364255' # Red switch
url1 = 'https://www.bestbuy.com/site/nintendo-switch-32gb-console-gray-joy-con/6364253.p?skuId=6364253'
target_url_red = 'https://www.target.com/p/nintendo-switch-with-neon-blue-and-neon-red-joy-con/-/A-77464001'
target_url_grey = 'https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-77464002'
# target_url_red = 'https://www.target.com/p/super-mario-bros-u-deluxe-nintendo-switch/-/A-54136573'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
counter = 0
status_list = []  # Red, Black, Green color of switch

while True:
    counter += 1
    status_list = [status(url0, headers), status(url1, headers), status_target(target_url_red, headers), status_target(target_url_grey, headers)]  #[Sold out, Sold out, Add to Cart] could be one of the examples
    time.sleep(1)
    print(datetime.now())
    body = "Best Buy Red is {0}, Best Buy Grey is {1}, Target Red is {2}, Target Grey is {3}".format(status_list[0], status_list[1], status_list[2], status_list[3]) # Sold Out, Add to Cart, Check Stores
    print(body)

    print('Number of visit: {0}\n'.format(counter))

    if status_list[0] == 'Add to Cart':
        SendMail.sentmail(url0)
    if status_list[1] == 'Add to Cart':
        SendMail.sentmail(url1)
    if status_list[2] == 'Shipping':
        SendMail.sentmail(target_url_red)
    if status_list[3] == 'Shipping':
        SendMail.sentmail(target_url_grey)
        # print("Calling you now....\n")
        # call.call()

    time.sleep(180)
