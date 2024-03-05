import json
import re
import time

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

cars = {
'Jac J7': 'https://www.avito.ru/all/predlozheniya_uslug/transport_perevozki/arenda_avto-ASgBAgICAkSYC8SfAZoL_vcB?f=ASgBAgECAkSYC8SfAZoL_vcBAUWCoRIIIkphYyBKNyI'
   #  'Geely Atlas Pro': 'https://www.avito.ru/all/predlozheniya_uslug/transport_perevozki/arenda_avto-ASgBAgICAkSYC8SfAZoL_vcB?f=ASgBAgECAkSYC8SfAZoL_vcBAUWCoRIRIkdlZWx5IEF0bGFzIFBybyI',
   #  'Haval F7': 'https://www.avito.ru/all/predlozheniya_uslug/transport_perevozki/arenda_avto-ASgBAgICAkSYC8SfAZoL_vcB?f=ASgBAgECAkSYC8SfAZoL_vcBAUWCoRIKIkhhdmFsIEY3Ig',
   #  'Jac7': 'https://www.avito.ru/all/predlozheniya_uslug/transport_perevozki/arenda_avto-ASgBAgICAkSYC8SfAZoL_vcB?f=ASgBAgECAkSYC8SfAZoL_vcBAUWCoRIGIkphYzci',
   #  'FAW Bestune NAT': 'https://www.avito.ru/all/predlozheniya_uslug/transport_perevozki/arenda_avto-ASgBAgICAkSYC8SfAZoL_vcB?f=ASgBAgECAkSYC8SfAZoL_vcBAUWCoRIRIkZBVyBCZXN0dW5lIE5BVCI',
   #  'Evolute i-Pro': 'https://www.avito.ru/all/predlozheniya_uslug/transport_perevozki/arenda_avto-ASgBAgICAkSYC8SfAZoL_vcB?f=ASgBAgECAkSYC8SfAZoL_vcBAUWCoRIPIkV2b2x1dGUgaS1Qcm8i'
  #  'Haval Jolion': 'https://www.avito.ru/all/predlozheniya_uslug/transport_perevozki/arenda_avto-ASgBAgICAkSYC8SfAZoL_vcB?f=ASgBAgECAkSYC8SfAZoL_vcBAUWCoRIOIkhhdmFsIEpvbGlvbiI'}
}
for car_name, car in cars.items():
    response = {}
    start = time.time()
    url = car
    driver = webdriver.Chrome()
    index = 0
    while True:
        index += 1
        driver.get(url + f'&p={index}')
        time.sleep(1)
        elements = driver.find_elements(By.CLASS_NAME, 'price-root-RA1pj')
        geos = driver.find_elements(By.CLASS_NAME, 'geo-root-zPwRk')
        print(len(elements), len(geos))
        if len(elements) == 0:
            break
        idx = -1
        for element in elements:
            try:
                idx += 1
                res = re.search(r'\d+(?:\s*\d+)*', element.text)
                if res:
                    v = int(res[0].replace(' ', ''))
                    locataion = geos[idx].text.split(',')[0]
                    if locataion in response.keys():
                        response[locataion].append(v)
                    else:
                        response[locataion] = [v]
                else:
                    pass
            except:
                print('error')
    with open(f'{car_name}.json', 'w') as json_file:
        json.dump(response, json_file)
