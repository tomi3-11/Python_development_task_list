from bs4 import BeautifulSoup
import requests
import csv


def main():
    try:
        books = scrape_data()
        save_to_csv(books)
        print(f"Saved {len(books)} records to scraped_books.csv")
    except requests.RequestException as error:
        print(f"Request failed: {error}")


def scrape_data():
    url = "https://books.toscrape.com"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    for book in soup.select('article.product_pod'):
        title_tag = book.select_one('h3 a')
        price_tag = book.select_one('p.price_color')
        availability_tag = book.select_one('p.instock.availability')

        books.append({
            'title': title_tag['title'].strip() if title_tag else 'N/A',
            'price': price_tag.get_text(strip=True) if price_tag else 'N/A',
            'availability': availability_tag.get_text(strip=True) if availability_tag else 'N/A',
        })

    return books


def save_to_csv(data, filename='scraped_books.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price', 'availability'])
        writer.writeheader()
        writer.writerows(data)




if __name__ == "__main__":
    main()
