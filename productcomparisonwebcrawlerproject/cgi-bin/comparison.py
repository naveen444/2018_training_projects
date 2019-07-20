#!C:/Python36/python.exe

import bs4 as bs
import urllib.request
import cgi
from urllib.request import FancyURLopener

class MyOpener(FancyURLopener):
    version = 'My new User-Agent'

form = cgi.FieldStorage()

item_name = form.getvalue('item')

# item_name = 'redmi note 4'

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
        <link rel="stylesheet" href='../styles.css'>
    </head>
    <body>
    """)
    print("""
    <h1>Amazon + Flipkart Data</h1>
    <div id="wrapper" style="display:flex;">
    <ul id="amazon">{}</ul>
    <div id="flip">{}</div>
    </div>
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
        <link rel="stylesheet" href='../custom.css'>
    </head>
    <body>
    """)
    print("""
    <h1>Product comparison</h1>
    <ul id="amazon">{}</ul>
    <div id="flip">{}</div>
    """.format(data))
    print("""
    </body>
    </html>""")

def main():
    amazonData = []
    # sauce = urllib.request.urlopen("https://www.flipkart.com/")
    # sauce_1 = urllib.request.urlopen("http://www.amazon.in/s/ref=nb_sb_noss_1/257-5609592-0603442?url=search-alias%3Daps&field-keywords="+item_name)
    # soup_1 = bs.BeautifulSoup(sauce_1, 'lxml')
    myopener = MyOpener()
    sauce_1 = myopener.open("http://www.amazon.in/s/ref=nb_sb_noss_1/257-5609592-0603442?url=search-alias%3Daps&field-keywords="+item_name)
    soup_1 = bs.BeautifulSoup(sauce_1, 'lxml')
    data = soup_1.find_all('li', class_="s-result-item", limit=5)

    for i in data:
        amazonData.append(i)

    flipData = []
    sauce = myopener.open("https://www.snapdeal.com/search?keyword="+item_name)
    soup = bs.BeautifulSoup(sauce, 'lxml')

    data = soup.find_all('div', class_="favDp", limit=5)
    print("Requested for " + "https://www.snapdeal.com/search?keyword="+item_name)

    for i in data:
        flipData.append(i)
        # print(d)

    print_html(amazonData, flipData)

main()
