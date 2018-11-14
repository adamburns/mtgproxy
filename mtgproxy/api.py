from mtgsdk import Card
from datetime import datetime as dt
from mtgsdk import Set
from io import BytesIO
import requests
from PIL import Image



def datify(date):
    return dt.strptime(date, '%Y-%m-%d')


def get_newest_set(card_list):
    return max(card_list, key=lambda  
               card: datify(get_date(card.set).release_date))


def get_oldest_set(card_list):
    return min(card_list, key=lambda 
               card: datify(get_date(card.set).release_date))


def get_card_list(card_name):
    return Card.where(name=card_name) \
                .all()   


def get_date(set_code):
    return Set.find(set_code)


def get_number(card):
    return card.number


def get_set(card):
    return card.set


def get_image_url(card_number, card_set):
    BASE_URL = 'https://img.scryfall.com/cards/png/en/'
    return (BASE_URL \
           + card_set.lower() \
           + '/'
           + str(card_number)
           + '.png')


def download_image(URL):
    response = requests.get(URL)
    image = Image.open(BytesIO(response.content))
    return image
