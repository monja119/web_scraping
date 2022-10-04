import requests
from bs4 import BeautifulSoup

# lists of available sites
sites = [
    'amazon',
    'target',
    'ebay'
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


class AmazonSite:
    def __init__(self):
        # array to stock data
        data = []
        # url
        url = "https://www.amazon.fr/gp/bestsellers/?ref_=nav_cs_bestsellers"

        # sending requests
        response = requests.get(url, headers=HEADERS)

        # returning pages as a text
        page = BeautifulSoup(response.text, 'html.parser')

        # GETTING DATA CATEGORIES
        # mix
        data.append({
            'categories': 'mix',
            'content': page.findAll('div', attrs={
                "class": "p13n-sc-uncoverable-faceout"
            })
        })

        # returning data
        self.file_product = data


class EbaySite:
    def __init__(self):
        # array to stock data
        data = []
        # url
        url = "https://www.ebay.fr/b/Telephones-mobiles/9355/bn_16576651"

        # sending requests
        response = requests.get(url, headers=HEADERS)

        # returning pages as a text
        page = BeautifulSoup(response.text, 'html.parser')

        # GETTING DATA CATEGORIES
        # technologies
        data.append({
            'categories': 'technologies',
            'content': page.findAll('div', attrs={
                "class": "s-item__wrapper clearfix"
            })
        })

        # returning data
        self.file_product = data


class TargetSite:
    def __init__(self):
        # array to stock data
        data = []
        # url
        url = "https://www.target.com/"

        # sending requests
        response = requests.get(url, headers=HEADERS)

        # returning pages as a text
        page = BeautifulSoup(response.text, 'html.parser')

        # GETTING DATA CATEGORIES
        # technologies
        data.append({
            'categories': 'all',
            'content': page.findAll('a', attrs={
                "class": "Link__StyledLink-sc-frmop1-0 styles__StoryblockLinkWrapper-sc-1nk1lqw-5 tTjrB dwnHge h-display-flex h-flex-direction-col"
            })
        })

        # returning data
        self.file_product = data

