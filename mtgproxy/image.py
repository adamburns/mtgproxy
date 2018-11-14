from PIL import Image
import os

def check_image(image):
    dpi = image.dpi
    


def process_image(image, image_name):
    loc = os.path.dirname(os.path.abspath(__file__))
    #print(loc)
    SAFE_AREA_SIZE = (678, 978)
    CUT_AREA_SIZE = (750, 1050)
    BLEED_AREA_SIZE = (822, 1122)
    #DPI = 300
    
    left = (CUT_AREA_SIZE[0] - SAFE_AREA_SIZE[0])/2
    top = (CUT_AREA_SIZE[1] - SAFE_AREA_SIZE[1])/2
    right = (CUT_AREA_SIZE[0] + SAFE_AREA_SIZE[0])/2
    bottom = (CUT_AREA_SIZE[1] + SAFE_AREA_SIZE[1])/2

    crop_image = image.crop((left, top, right, bottom))
    
    bleed_image = Image.new('RGB', BLEED_AREA_SIZE)
    dim_x = (BLEED_AREA_SIZE[0] - SAFE_AREA_SIZE[0])/2
    dim_y = (BLEED_AREA_SIZE[1] - SAFE_AREA_SIZE[1])/2
    dims = (int(dim_x), int(dim_y))
    bleed_image.paste(crop_image, (dims))
    #print(image.filename)
    bleed_image.save(loc + '/images/' + image_name + ' 300_crop.png', dpi=(300, 300))
