from mtgsdk import Card
from datetime import datetime as dt
from mtgsdk import Set

class Magic_IO(object):

    
    def datify(self, date):
        return dt.strptime(date, '%Y-%m-%d')


    def get_newest_set(self, card_list):
        return max(card_list, key=lambda card: self.datify(self.get_date(card.set).release_date))


    def get_oldest_set(self, card_list):
        return  min(card_list, key=lambda card: self.datify(self.get_date(card.set).release_date))


    def get_card_list(self, card_name):
        return Card.where(name=card_name) \
                    .all()   


    def get_date(self, set_code):
        return Set.find(set_code)


    def get_number(self, card):
        return card.number


    def get_set(self, card):
        return card.set

class Scryfall(object):


    def get_image(self, card_number, card_set):
        BASE_URL = 'https://img.scryfall.com/cards/png/en/'
        return (BASE_URL \
               + card_set.lower() \
               + '/'
               + str(card_number)
               + '.png')

