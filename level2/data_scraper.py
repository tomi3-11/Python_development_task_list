from bs4 import BeautifulSoup
import requests


def main():
    pass


def scrape_data():
    url = "https://books.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')




if __name__ == "__main__":
    main()
