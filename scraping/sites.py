import requests
from bs4 import BeautifulSoup

# lists of available sites
sites = [
    'amazon',
    'flipkart',
    'newegg',
    'target',
    'overstock',
    'bestbuy',
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
        self.data = []
        # GETTING DATA CATEGORIES

        # mix
        self.add_data('mix',
                      "https://www.amazon.fr/gp/bestsellers/?ref_=nav_cs_bestsellers",
                      "div",
                      "class",
                      "p13n-sc-uncoverable-faceout")

        # latest
        self.add_data('latest',
                      "https://www.amazon.fr/gp/new-releases/?ref_=nav_em_cs_newreleases_0_1_1_3",
                      'div',
                      "class", "p13n-sc-uncoverable-faceout")

        # books
        self.add_data('books',
                      'https://www.amazon.fr/livre-achat-occasion-litterature-roman/b/?ie=UTF8&node=301061&ref_=nav_cs_books',
                      'div',
                      'class',
                      'a-section a-spacing-none octopus-pc-item-block octopus-pc-asin-block')

        # returning data
        self.file_product = self.data

    def add_data(self, categories, url, tag, attr, value):
        # url
        response = requests.get(url, headers=HEADERS)
        page = BeautifulSoup(response.text, 'html.parser')
        self.data.append({
            'categories': str(categories),
            'content': page.findAll(str(tag), attrs={
                attr: value
            })
        })


class FlipkartSite:
    def __init__(self):
        self.data = []

        # mix
        self.add_data('mix',
                      'https://www.flipkart.com/offers-store?otracker=nmenu_offer-zone',
                      'a',
                      'class',
                      '_6WQwDJ')
        self.file_product = self.data

    def add_data(self, categories, url, tag, attr, value):
        # url
        response = requests.get(url, headers=HEADERS)
        page = BeautifulSoup(response.text, 'html.parser')
        self.data.append({
            'categories': str(categories),
            'content': page.findAll(str(tag), attrs={
                attr: value
            })
        })


class NeweggSite:
    def __init__(self):
        self.data = []

        # mix
        self.add_data('technologies',
                      'https://www.newegg.ca/p/pl?d=french',
                      'div',
                      'class',
                      'item-container')
        self.file_product = self.data

    def add_data(self, categories, url, tag, attr, value):
        # url
        response = requests.get(url, headers=HEADERS)
        page = BeautifulSoup(response.text, 'html.parser')
        self.data.append({
            'categories': str(categories),
            'content': page.findAll(str(tag), attrs={
                attr: value
            })
        })


class OverstockSite:
    def __init__(self):
        self.data = []

        # mix
        self.add_data('mix',
                      'https://www.overstock.com/',
                      'div',
                      'class',
                      'FeaturedTileStyles_contentWrapper__U4zQo')
        self.file_product = self.data

    def add_data(self, categories, url, tag, attr, value):
        # url
        response = requests.get(url, headers=HEADERS)
        page = BeautifulSoup(response.text, 'html.parser')
        self.data.append({
            'categories': str(categories),
            'content': page.findAll(str(tag), attrs={
                attr: value
            })
        })


class TargetSite:
    def __init__(self):
        # array to stock data
        self.data = []

        # mix
        self.add_data('mix',
                      'https://www.target.com/',
                      'a',
                      'class',
                      'Link__StyledLink-sc-frmop1-0 styles__StoryblockLinkWrapper-sc-1nk1lqw-5 tTjrB dwnHge '
                      'h-display-flex h-flex-direction-col')
        # returning data
        self.file_product = self.data

    def add_data(self, categories, url, tag, attr, value):
        # url
        response = requests.get(url, headers=HEADERS)
        page = BeautifulSoup(response.text, 'html.parser')
        self.data.append({
            'categories': str(categories),
            'content': page.findAll(str(tag), attrs={
                attr: value
            })
        })


class BestbuySite:
    def __init__(self):
        # array to stock data
        self.data = []

        # technologies
        self.add_data('technologies',
                      'https://www.bestbuy.com/site/top-deals/computer-tablet-deals/pcmcat1563302961332.c?id=pcmcat1563302961332',
                      'div',
                      'class',
                      'wf-offer-top')

        # health and fitness
        self.add_data('health',
                      'https://www.bestbuy.com/site/top-deals/health-fitness-deals/pcmcat1616769208882.c?id=pcmcat1616769208882',
                      'div',
                      'class',
                      'carousel-item carousel-item-border')
        # returning data
        self.file_product = self.data

    def add_data(self, categories, url, tag, attr, value):
        # url
        response = requests.get(url, headers=HEADERS)
        page = BeautifulSoup(response.text, 'html.parser')
        self.data.append({
            'categories': str(categories),
            'content': page.findAll(str(tag), attrs={
                attr: value
            })
        })


class EbaySite:
    def __init__(self):
        # array to stock data
        self.data = []

        # technologies
        self.add_data('techologies',
                      'https://www.ebay.fr/b/Telephones-mobiles/9355/bn_16576651',
                      'div',
                      'class',
                      's-item__wrapper clearfix')

        # fashion
        self.add_data('fashion',
                      'https://www.ebay.fr/b/Vetements-et-accessoires/11450/bn_16576896',
                      'li',
                      'class',
                      's-item s-item--large')

        # returning data
        self.file_product = self.data

    def add_data(self, categories, url, tag, attr, value):
        # url
        response = requests.get(url, headers=HEADERS)
        page = BeautifulSoup(response.text, 'html.parser')
        self.data.append({
            'categories': str(categories),
            'content': page.findAll(str(tag), attrs={
                attr: value
            })
        })

