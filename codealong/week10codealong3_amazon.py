from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=2560,3840") # set a large vertically oriented browser window so more deals load
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s, options=chrome_options)
#driver = webdriver.Chrome(s.path, options=chrome_options) # if you have service problems on line 15

driver.get('https://www.amazon.com/deals')
time.sleep(5)

deal_divs = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="product-card"]')

deal_titles = []
deal_links = []
for deal_div in deal_divs:
    deal_titles.append(deal_div.find_element(By.CSS_SELECTOR, 'span[class*="a-truncate-full"]').get_attribute('innerHTML'))
    deal_links.append(deal_div.find_element(By.CSS_SELECTOR, 'a[data-testid="product-card-link"]').get_attribute('href'))

title_with_links = dict(zip(deal_titles, deal_links))
print(title_with_links)
print(f'total deals: {len(title_with_links)}')
