import time
import random

from selenium import webdriver

from utils import send_message


CONTACTS = [
    'Me, myself and i', #teste
    'Tiago',
    'Thycyano',
    'Tio Ribamar',
    'Tia Rita',
    'Tia Rosângela',
    'Digníssimo George'

]

print('Abrindo o webdriver')
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print('Esperando a leitura do QRCode')
time.sleep(15)

for contact_name in CONTACTS:
    send_message(driver, contact_name, 1)
