from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Парсим названия тестов, id, вопрос-ответ в JSON

browser = webdriver.Chrome()
browser.get('http://edu.tltsu.ru/edu/index.php')

time.sleep(20)  #ручной вход


    

link = 'http://edu.tltsu.ru/md/trial.php?test_type=md&btz_id='
data = {}
num = 0

for id_ in range(15, 30):   #выбираем диапазон для перебора до 7к
    try:
        browser.get(f'{link}{id_}')
        name = browser.find_element(By.XPATH, '/html/body/table/tbody/tr[1]/td/table/tbody/tr[3]/td/p[1]').text[6:]
        if len(name) > 2:
            data[id_] = {'name': name}

            for _ in range(10):
                try:
                    question = browser.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/form/table/tbody/tr[1]/td/p/table/tbody/tr[3]/td/p').text
                except:
                    print('Не найден вопрос')
            

                try:
                    answer = browser.find_element(By.XPATH, '/html/body/table/tbody/tr[3]/td/form/table/tbody/tr[1]/td/p/table/tbody/tr[1]/td/p').text[19:]
                except:
                    print('Не найден ответ')


                if question not in data[id_]:
                    data[id_][question] = answer

                print(data)
                browser.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td[3]/input').click()

        
    except Exception as ex:
        print(ex)


with open('ques_answ.txt', 'w', encoding='utf-8') as file:
    json.dump(data, file,ensure_ascii=False)


time.sleep(10)
browser.refresh()
browser.quit()