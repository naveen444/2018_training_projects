#!C:/Python36/python.exe

import cgi
import bs4 as bs
import urllib.request
from urllib.request import FancyURLopener

class MyOpener(FancyURLopener):
    version = 'My new User-Agent'   # Set this to a string you want for your user agent


form = cgi.FieldStorage()

item_name = form.getvalue('item')

#item_name = 'redmi note 4'

def print_html(amazonData, snapData):

    am_data = str(amazonData).strip("[]")
    am_data = am_data.replace("\n","")

    sp_data = str(snapData).strip("[]")
    sp_data = sp_data.replace("\n","")
    sp_data = sp_data.replace("\r","")
    sp_data = sp_data.replace("\t","")

    # print(flipData)

    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
        <link rel="stylesheet" href='../custom2.css'>
    </head>
    <body>
    """)
    print("""
    <h1>Amazon + Flipkart Data</h1>
    <ul id="amazon">{}</ul>
    <div id="flip">{}</div>
    """.format(am_data, str(sp_data).strip('[]')).encode('utf-8'))
    print("""
    </body>
    </html>""")


def print_html_2(data):

    # print(flipData)

    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
        <link rel="stylesheet" href='../custom2.css'>
    </head>
    <body>
    """)
    print("""
    <h1>Product comparison</h1>
    <div >{}</div>
    """.format(data))
    print("""
    </body>
    </html>""")

def search_products():
    # sauce_1 = urllib.request.urlopen("http://www.amazon.in/s/ref=nb_sb_noss_1/257-5609592-0603442?url=search-alias%3Daps&field-keywords="+user_input)
    # sauce_1 = urllib.request.urlopen("https://www.compareraja.in/search?c=all&q="+user_input)
    myopener = MyOpener()
    sauce_1 = myopener.open("https://www.compareraja.in/search?c=all&q=" + item_name)

    soup = bs.BeautifulSoup(sauce_1, 'lxml')
    print("Available Products are : ")
    for data in soup.find_all('div', class_="prodcut-listing"):
        print(data)
        print("----------------------------")
    print_html_2(data)


search_products()