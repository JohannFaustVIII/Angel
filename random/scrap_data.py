from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def get_text(text : str) -> str:
    return text if text else 'No data'

def get_page_to_parse() -> BeautifulSoup:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.worldometers.info/coronavirus/')
    return BeautifulSoup(driver.page_source, 'html.parser')

def get_rows_with_countries(page : BeautifulSoup) -> list[Tag]:
    return [t for t in page.find_all("tr") if t.find_all("a")]

def map_column_to_text(row : Tag) -> tuple[str, bool]:
    columns = row.find_all("td")
    index = columns[0].text
    country = columns[1].text
    infected = get_text(columns[3].text)
    dead = get_text(columns[5].text)

    message = f"{index:>4}\t {country:>30}\t {infected:>12}\t {dead:>12}"
    isPoland = country == "Poland"

    return message, isPoland

def print_countries_stats(countries : list[tuple[str, bool]]):
    keep_text = lambda country : country[0]
    countries_stats = list(map(keep_text, countries))

    for stat in countries_stats:
        print(stat)

def print_poland_stats(countries : list[tuple[str, bool]]):
    find_poland = lambda country : country[1]
    keep_text = lambda country : country[0]

    poland_row = list(map(keep_text, list(filter(find_poland, countries))))

    print(f"\nPoland stats:\n{poland_row[0]}")


if __name__ == "__main__":
    page = get_page_to_parse()
    countries = get_rows_with_countries(page)
    
    countries_rows = list(map(map_column_to_text, countries))

    print_countries_stats(countries_rows)
    print_poland_stats(countries_rows)

    

