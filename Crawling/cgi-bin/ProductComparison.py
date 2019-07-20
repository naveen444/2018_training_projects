#!C:/Python36/python.exe

import bs4 as bs
import urllib.request
import cgi

form = cgi.FieldStorage()

item_name = form.getvalue('item')

# item_name = 'redmi'

def print_html(amazonData, flipData):

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
    <h1>Amazon + Flipkart Data</h1>
    <ul id="amazon">{}</ul>
    <div id="flip">{}</div>
    """.format(str(amazonData).strip('[]'), str(flipData).strip('[]')).encode('utf-8'))
    print("""
    </body>
    </html>""")


def main():
    amazonData = []
    # sauce = urllib.request.urlopen("https://www.flipkart.com/")
    sauce_1 = urllib.request.urlopen("http://www.amazon.in/s/ref=nb_sb_noss_1/257-5609592-0603442?url=search-alias%3Daps&field-keywords="+item_name)
    soup_1 = bs.BeautifulSoup(sauce_1, 'lxml')

    data = soup_1.find_all('li', class_="s-result-item")

    for i in data:
        amazonData.append(i)
        # print(d)



    flipData = []
    sauce = urllib.request.urlopen("https://www.flipkart.com/search?q="+item_name)
    soup = bs.BeautifulSoup(sauce, 'lxml')

    data = soup.find_all('a', class_="_1UoZlX")

    for i in data:
        flipData.append(i)
        # print(d)

    print_html(amazonData, flipData)

main()
