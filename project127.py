from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedrive")
brower.get(START_URL)
time.sleep(10)
def scaper():
    headers = [["star_name","light_years_from_earth","star_mass","radius"]]
    star_data = []
    for i in range(0,482):
        soup = BeautifulSoup(browser.page_source,"html_parser")
        for url_tags in soup.find_all("ul",attrs={"class","star"}):
            li_tags = url_tags.find_all("li")
            tempt_list = []
            for li_tag,index in enumurate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].content[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
        
scrape()
