from gettext import find
from operator import le
import requests
import json
from bs4 import BeautifulSoup

import secret

class Dnevnik:
    
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password
        
    
    def get_name(self):
        r = requests.post('https://login.dnevnik.ru/login/', data={"login": self.login, "password": self.password})
        soup = BeautifulSoup(r.content, 'lxml')
        
        # name = soup.find('div', class_ = 'user-profile-box').find('p', class_ = 'user-profile-box__info_row-content user-profile-box__initials').text
        find_in_script = soup.find_all('script')
        to_json = json.loads(find_in_script[27].string[250:-3700])
        print(to_json['userMarks']['children'][0]['schoolId'])
        return None
        
dnevnik = Dnevnik(secret.LOGIN, secret.PASSWORD)
print(dnevnik.get_name())

# r = requests.post('https://login.dnevnik.ru/login/', data={"login": secret.LOGIN, "password": secret.PASSWORD})

# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.find('div', class_ = 'user-profile-box'). find('p', class_ = 'user-profile-box__info_row-content user-profile-box__initials').text)