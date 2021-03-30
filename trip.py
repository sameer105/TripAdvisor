import csv
from selenium import webdriver
import time
def crawling(pages):
    driver = webdriver.Chrome()
    url = 'https://www.tripadvisor.in/Attraction_Review-g34515-d953101-Reviews-Disney_s_Hollywood_Studios-Orlando_Florida.html'
    driver.get(url)
    time.sleep(3)

    for n in range(pages):
        elements = driver.find_elements_by_css_selector(".ui_header_link")
        username = [el.text for el in elements]
        print(username)

        elements = driver.find_elements_by_css_selector("._2fxQ4TOx")
        review_date = [el.text.split("review ")[-1] for el in elements]
        print(review_date)

        elements = driver.find_elements_by_css_selector(".nf9vGX55")
        tags = [el.find_element_by_tag_name("span") for el in elements]
        star = [(int(el.get_attribute("class").split()[-1].split("_")[-1])/10) for el in tags]
        print(star)

        elements = driver.find_elements_by_css_selector(".ocfR3SKN")
        title = [el.text for el in elements]
        print(title)

        elements = driver.find_elements_by_css_selector(".IRsGHoPm")
        review = [el.text for el in elements]
        print(review)

        elements = driver.find_elements_by_css_selector("._34Xs-BQm")
        date_of_experience = [el.text for el in elements]
        print(date_of_experience)


        fields = ['Username', 'Review_date', 'Star', 'Title', 'Review', 'Date of Experience']
        rows = [username, review_date ,star ,title , review , date_of_experience]
        filename = "travel_data.csv"
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)

            csvwriter.writerow(fields)

            csvwriter.writerows(rows)

        elements = driver.find_element_by_css_selector(".next")
        elements.click()
        time.sleep(3)



crawling(5)