from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Country:

    position = ""
    country = ""
    infected = "No data"
    dead = "No data"
    is_poland = False

    def __init__(self, position : str, country : str, infected : str, dead : str) -> None:
        self.position = position
        self.country = country
        self.infected = Country.__to_text(infected)
        self.dead = Country.__to_text(dead)
        self.is_poland = country == "Poland"

    def __to_text(text : str) -> str:
        return text if text else 'No data'

    def get_message(self) -> str:
        return f"{self.position:>4}\t {self.country:>30}\t {self.infected:>12}\t {self.dead:>12}"


def get_page_to_parse() -> BeautifulSoup:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.worldometers.info/coronavirus/')
    return BeautifulSoup(driver.page_source, 'html.parser')

def get_rows_with_countries(page : BeautifulSoup) -> list[Tag]:
    all_tables = [t for t in page.find_all("tr") if t.find_all("a")]
    return all_tables[:int(len(all_tables)/3)]

def map_column_to_text(row : Tag) -> Country:
    columns = row.find_all("td")
    index = columns[0].text
    country = columns[1].text
    infected = columns[3].text
    dead = columns[5].text

    return Country(index, country, infected, dead)

def print_countries_stats(countries : list[Country]):
    for stat in countries:
        print(stat.get_message())

def print_poland_stats(countries : list[Country]):
    find_poland = lambda country : country.is_poland

    poland_row = list(filter(find_poland, countries))

    print(f"\nPoland stats:\n{poland_row[0].get_message()}")


if __name__ == "__main__":
    page = get_page_to_parse()
    countries = get_rows_with_countries(page)
    
    countries_rows = list(map(map_column_to_text, countries))

    print_countries_stats(countries_rows)
    print_poland_stats(countries_rows)

    

