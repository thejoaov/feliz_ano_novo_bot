import time

from selenium import webdriver


ATTACHMENT_XPATH = '//*[@id="main"]/header/div[3]/div/div[2]/div'
INPUT_XPATH = '//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input'

message='venho lhe convidar pra um jantar simples, em comemoração ao meu casamento sexta feira agora :D. A lista de casamento no cantinho do convite, é na pintos.'

def send_message(driver, contact_name='Neném', image_number=1):
    print(f'Procurando contato "{contact_name}"')
    search_box = driver.find_element_by_class_name('_2zCfw')
    search_box.send_keys(contact_name)
    time.sleep(2)
    contact = driver.find_element_by_xpath(
        f'//span[@title = "{contact_name}" and @class="_19RFN _1ovWX _F7Vk"]')
    contact.click()
    print(f'Achei o contato "{contact_name}"!')
    time.sleep(2)
    attach_button = driver.find_element_by_xpath(ATTACHMENT_XPATH)
    attach_button.click()
    print(f'Enviando foto para {contact_name}')
    time.sleep(1)
    input_button = driver.find_element_by_xpath(INPUT_XPATH)
    input_button.send_keys(
        f'/Users/thejoaov/Documents/Temp/feliz_ano_novo_bot/img/{image_number}.jpeg')
    time.sleep(1)
    attach_message = driver.find_element_by_class_name('_3u328')
    print(f'Escrevendo mensagem para {contact_name}:')
    print(f'{contact_name}, {message}')
    attach_message.send_keys(f'{contact_name}, {message}')
    time.sleep(1)
    send_attach_button = driver.find_element_by_class_name('_1g8sv')
    send_attach_button.click()
    print(f'Enviando mensagem para {contact_name}')
    time.sleep(2)
    print('------------')
