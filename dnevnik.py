from gettext import find
import requests
import secret
from bs4 import BeautifulSoup

class Dnevnik:
    
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password
        
    
    def get_name(self):
        r = requests.post('https://login.dnevnik.ru/login/', data={"login": self.login, "password": self.password})
        soup = BeautifulSoup(r.content, 'html.parser')
        name = soup.find('div', class_ = 'user-profile-box'). find('p', class_ = 'user-profile-box__info_row-content user-profile-box__initials').text
        return name
        
dnevnik = Dnevnik(secret.LOGIN, secret.PASSWORD)
print(dnevnik.get_name())

# r = requests.post('https://login.dnevnik.ru/login/', data={"login": secret.LOGIN, "password": secret.PASSWORD})

# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.find('div', class_ = 'user-profile-box'). find('p', class_ = 'user-profile-box__info_row-content user-profile-box__initials').text)