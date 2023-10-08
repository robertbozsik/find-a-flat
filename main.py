import json
import os
import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
from requests import Session

from settings import Settings
st = Settings()


def send_telegram_message(message: str) -> requests.Response:

    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    headers_dict = {
        "Content-Type": "application/json",
        "Proxy-Authorization": "Basic base64",
    }

    data_dict = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
        # "disable_notification": True,
    }
    data_json = json.dumps(data_dict)

    requests_session = Session()

    response = requests_session.request(
        method="POST",
        url=url,
        data=data_json,
        headers=headers_dict,
        # verify=False,
    )

    assert response.status_code == 200

    return response


def scrape_ebay_kleinanzeigen(url: str):
    headers_dict = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://www.google.com/',
    }

    res = (
        requests.get(
            url=url,
            headers=headers_dict,
        )
    )

    if res.status_code == 200:
        # open the scraped_flat_ids.txt file
        with open("scraped_flat_ids.txt", "r") as file:
            scraped_flat_ids = set(file.read().splitlines())

        # create a set for new flat results
        current_flat_ids = set()

        # create the text of the addition to the Telegram message
        additional_message_text = ""

        # unwanted keywords
        exclude_keywords = st.exclude_keywords

        # start to scrape the url
        soup = BeautifulSoup(res.content, 'html.parser')
        articles = soup.find_all("article", class_="aditem")

        for article in articles:
            flat_id = article.get("data-adid")

            if flat_id not in scraped_flat_ids:
                h2_tags = article.find_all("h2", class_="text-module-begin")
                for h2_tag in h2_tags:
                    links = h2_tag.find_all("a")

                    for link in links:
                        link_text = link.get_text(strip=True)
                        link_text_lowered = link_text.lower()
                        link_href = link.get("href")

                        if not any(keyword in link_text_lowered for keyword in exclude_keywords):
                            current_flat_ids.add(flat_id)
                            print(link_text)
                            additional_message_text += f"Ad title: {link_text}\n"
                            print(f"https://www.kleinanzeigen.de/{link_href}")
                            additional_message_text += f"Direct link: https://www.kleinanzeigen.de/{link_href}\n\n"

        if len(current_flat_ids) > 0:
            message = f"New flat found at {url} \n\n{additional_message_text}"
            send_telegram_message(message=message)

            with open("scraped_flat_ids.txt", "w") as file:
                file.write("\n".join(scraped_flat_ids.union(current_flat_ids)))
        return None
    else:
        print('response error:', res.status_code)
        return None


def main():
    load_dotenv()

    for url in st.urls_to_scrape:
        scrape_ebay_kleinanzeigen(url=url)
        time.sleep(3)


if __name__ == '__main__':
    main()
