import bs4
import urllib.request

url = urllib.request.urlopen('https://www.indeed.com/resumes?q=python&l=')

soup = bs4.BeautifulSoup(url,'lxml')

data = soup.find_all('a', class_='app_link')

for i in range(len(data)):
    # print("Developer",i,data[i].text)
    href = data[i]['href']
    new_url = urllib.request.urlopen('https://www.indeed.com'+href)

    new_soup = bs4.BeautifulSoup(new_url, 'lxml')
    heading = new_soup.find('h1',id='resume-contact')
    print("Developer",i,heading.text)

    work_title = new_soup.find_all('p',class_='work_title')
    for w_t in work_title:
        print("Title",w_t.text)

    work_company = new_soup.find_all('p', class_='work_company')
    for w_c in work_company:
        print("Company", w_c.text)

    work_dates = new_soup.find_all('p', class_='work_dates')
    for w_d in work_dates:
        print("Dates", w_d.text)

    print("-------------------")