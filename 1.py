import requests
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def vacancy():
    number_of_pages = 20
    professional_role = [10, 12, 25, 34, 36, 73, 96, 104, 107, 112, 113, 114, 116, 121, 124, 125,
                         126]  # все, что относится к IT
    data = []
    for professional_role1 in professional_role:
        for i in range(number_of_pages):
            url = 'https://api.hh.ru/vacancies'
            par = {'text': '', 'from': 'suggest_post', 'area': '1342', 'professional_role': professional_role1,
                   'per_page': '10', 'page': i}  # area=ID Тюменской области
            r = requests.get(url, params=par)
            e = r.json()
            print(e)
            data.append(e)
            vacancy_details = data[0]['items'][0].keys()
            df = pd.DataFrame(columns=list(vacancy_details))
            ind = 0
            for i in range(len(data)):
                for j in range(len(data[i]['items'])):
                    df.loc[ind] = data[i]['items'][j]
                    ind+=1
            csv_name = "ogo.csv"
            df.to_csv(csv_name)



def resume_hrefs():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    for i in range(67):
        links_resumes = []
        link = 'https://tyumen.hh.ru/search/resume?text=&logic=normal&pos=full_text&exp_period=all_time&exp_company_size=any&exp_industry=any&professional_role=156&professional_role=160&professional_role=10&professional_role=12&professional_role=150&professional_role=25&professional_role=165&professional_role=34&professional_role=36&professional_role=73&professional_role=155&professional_role=96&professional_role=164&professional_role=104&professional_role=157&professional_role=107&professional_role=112&professional_role=113&professional_role=148&professional_role=114&professional_role=116&professional_role=121&professional_role=124&professional_role=125&professional_role=126&area=1342&relocation=living_or_relocation&salary_from=&salary_to=&currency_code=RUR&age_from=&age_to=&gender=unknown&order_by=relevance&search_period=0&items_on_page=50&page=' + str(
            i) + '&hhtmFrom=resume_search_result'
        browser.get(link)
        time.sleep(3)
        browser.refresh()
        time.sleep(3)
        print(link)
        resume_blocks = browser.find_elements(By.CLASS_NAME, "serp-item")
        for resume_block in resume_blocks:
            links_resumes.append(resume_block.find_element(By.TAG_NAME, 'a').get_attribute('href'))
        with open('resumes.csv', 'a+', newline='') as f:
            w = csv.writer(f)
            w.writerows([links_resumes])
    browser.quit()



# resume_hrefs()
# vacancy()