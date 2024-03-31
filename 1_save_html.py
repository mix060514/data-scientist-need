#%%
import os 
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#%%
driver = webdriver.Chrome()

driver.get("https://www.104.com.tw/jobs/main/")
driver.implicitly_wait(0.5)


#%% close pop up foreign page
# css_selector = "#app > div > div.popup > div.popupBox.popup-box > div.popupWrapper.popup-wrapper > div.popup-footer.popupFooter > div > div:nth-child(1) > button"
# css_selector = "#app > div > div.popup > div.popupBox.popup-box > div.popupWrapper.popup-wrapper > div.popup-footer.popupFooter > div > div:nth-child(1) > button"
xpath_ = """//*[@id="app"]/div/div[10]/div[2]/div[2]/div[3]/div/div[1]/button"""
submit_button = driver.find_element(by=By.XPATH, value=xpath_)
submit_button.click()


#%% go to login page
css_selector = """//*[@id="global_bk"]/ul/li[2]/ul/li[6]/a"""
submit_button = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
submit_button.click()


#%% login
account = os.getenv('account')
css_selector = "#username"
account_input = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
account_input.send_keys(account)


password = os.getenv('password')
css_selector = "#password"
account_input = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
account_input.send_keys(password)


css_selector = "#submitBtn"
submit_button = driver.find_element(by=By.CSS_SELECTOR, value=css_selector)
submit_button.click()


#%% go to recommend page
driver.get("https://pda.104.com.tw/work/mate/list/recommend/?jobsource=m_index_job_r&utm_medium=cweb_job_login&utm_source=104")


# %% scroll down
# idea came from https://stackoverflow.com/a/48851166
for _ in range(10):
    driver.implicitly_wait(1)

    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height, new_height)
    last_height = new_height
    driver.implicitly_wait(3)
    time.sleep(1)



#%%
html_source = driver.page_source
import pathlib
import datetime 
pathlib.Path('data').mkdir(parents=True, exist_ok=True)

filename = f'data/recommend_{datetime.datetime.now().strftime("%Y%m%d")}.html'
with open(filename, 'wt', encoding='utf-8') as f:
    f.write(html_source)

