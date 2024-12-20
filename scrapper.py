import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import TimeoutException, NoSuchElementException,StaleElementReferenceException
import pandas as pd
from bs4 import BeautifulSoup


# driver.get()

def scrape_website(website):
    print("Launching chrome browser...")

    options = Options()
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service,options=options)
    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

# text = scrape_website('https://www.onlinekhabar.com/')
# print(text)

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,"html.parser")

    for script_or_style in soup(["script","style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def split_dom_content(dom_content,max_length=6000):
    return [
        dom_content[i:i + max_length] for i in range(0,len(dom_content),max_length)
    ]
