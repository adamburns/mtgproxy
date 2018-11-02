from mtgproxy import api

mtg_io = api.Magic_IO()
scryfall = api.Scryfall()


card_list = mtg_io.get_card_list('"Wurmcoil Engine"')
#print(card_list)
newest_set = mtg_io.get_newest_set(card_list)
oldest_set = mtg_io.get_oldest_set(card_list)
#print(dir(card_list[0]))
#print(card_list[0].release_date)
#for i, card in enumerate(card_list):
#    print(f'{i}: {card.release_date}')

#for p in card_list:
#    print(p.set)

#print(card_list)
#print('Newest set: \t' + newest_set.image_url)
#print('Oldest set: \t' + oldest_set.image_url)

#BASE_URL = 'https://img.scryfall.com/cards/png/en/'
card_set = mtg_io.get_set(oldest_set)
card_num = mtg_io.get_number(oldest_set)
#print(BASE_URL + card_set.lower() + '/' + card_num + '.png')

print(scryfall.get_image(card_num, card_set))

#print(newest_set.name)
#https://img.scryfall.com/cards/png/en/mps/28.png?1517813031
#https://img.scryfall.com/cards/png/en/MPS/28.png
