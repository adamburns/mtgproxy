from mtgproxy import api
from mtgproxy import deck
from mtgproxy import image
from time import sleep
import multiprocessing


def worker(process_name, tasks, results):
    print('[%s] evaluation routine starts' % process_name)

    while True:
        new_value = deck_list.get()
        if new_value < 0:
            print('[%s] evaluation routine quits' % process_name)
            results.put(-1)
            break
        else:
            image(new_value)
            sleep(0.10)
            print('[%s] Processing: %s' %(process_name, new_value))
    return

def read_cube(loc):
    f = open(loc, 'r')
    e = open('error.txt', 'w')
    lines = f.readlines()
    for line in lines:
        print(line.rstrip())
        try:
            url = run_image(line.rstrip(), api.get_newest_set)
        except:
            e.write('run_image: ' + line.rstrip() + '\n')
            continue
        try:
            img = api.download_image(url)
        except:
            e.write('download_image: ' + line.rstrip() + '\n')
            continue
        try:
            image.process_image(img, line)
        except:
            e.write('process_image: ' + line.rstrip() + '\n')
            continue
        sleep(0.1)
    f.close()
    e.close()

def run_image(card, version):
    card_list = api.get_card_list('"' + card + '"')
    card_info = version(card_list)
    card_set = api.get_set(card_info)
    card_num = api.get_number(card_info)
    this_image = api.get_image_url(card_num, card_set)
    return this_image

read_cube('vintage_cube.txt')

