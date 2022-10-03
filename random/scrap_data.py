from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_text(text : str) -> str:
    return text if text else 'No data'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.worldometers.info/coronavirus/')

soup = BeautifulSoup(driver.page_source, 'html.parser')

nested = [t for t in soup.find_all("tr") if t.find_all("a")]

for nes in nested[:100]:
    tds = nes.find_all("td")
    text = f"{tds[0].text:>4}\t {tds[1].text:>30}\t {get_text(tds[3].text):>12}\t {get_text(tds[5].text):>12}"
    print(text)
    # print(nested)
    if tds[1].text == "Poland":
        poland_stats = text

print(f"Poland stats:\n\n{poland_stats}")

driver.close()

