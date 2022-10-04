import requests
from bs4 import BeautifulSoup
# lists of available sites
sites = [
    'amazon'
]

# header to allow accessing
HEADERS = (
    {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 '
            'Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'
    }
)


class Amazon:
    def __init__(self):
        # array to stock data
        self.file_product = ''

        # url
        url = "https://www.amazon.fr/gp/bestsellers/?ref_=nav_cs_bestsellers"

        # sending requests
        response = requests.get(url, headers=HEADERS)

        # returning pages as a text
        page = BeautifulSoup(response.text, 'html.parser')

        # getting data
        product_file = page.findAll('div', attrs={
            "class": "p13n-sc-uncoverable-faceout"
        })

        # returning data
        self.file_product = product_file


