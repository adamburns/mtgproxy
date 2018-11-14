#https://stackabuse.com/parallel-processing-in-python/

def load_deck(deck_loc):
    deck_list = open('vintage_cube.txt', 'r')
    deck = Queue()
    for card in deck_list:
        deck.put(card)
    deck_list.close()
    return deck




