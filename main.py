# import random
# class Human:
#     def __init__(self):
#         self.name=name
#         self.alive = True
#         self.progress = 0
#         self.gladness = 50
#         self.money = 1000
#         self.truant = 0
#         self.gladness1 = 7
#
#     def to_work(self):
#         print('go to work')
#         self.money+=350
#         self.gladness1 -=100
#
#     def to_study(self):
#         print ('time to study')
#         self.progress += 0.12
#         self.gladness -=3
#
#     def to_sleep(self):
#         print('I am going to sleep')
#         self.gladness +=3

# import requests
# from bs4 import beautifulsoup
# import lxml
# import fake_useragent
# import time
#
# url = 'https://kups.club'
# user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWedkit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537/36'
#
# headers = {'user-agent': user}
# session = requests.Session()
#
# response = requests.get(url, headers=headers)
# time.sleep(2)
# soup=BeautifulSoup(response.text, 'lmxl')
# time.sleep(2)
# all_product = soup.find('div', clas = "row mt-4")
# # print(all_product)
# product_list = all_product.find_all('div, clas = 'card h-100')
# print(product_list)
# for i in range(len(product_list)):
#     product = product_list[i].find('h3', class = 'card-title').text
#     price = product_list[i].find('p', class = 'card-title').text
#     try:
#         shop = product_list[i].find ('a', class = 'text-black link-deafult').text
#         with open('my product.txt', 'w', encoding='UTF-8')as file:
#             file.write(f"{product}  Price{price}  Shop{shop}'\n'")
#     exept AttributeError:
#         print('No shop')


# collection = (1, 2, 5, 6, 8)
# aggregate = ListCollection(collection)
# itr = aggregate.iterator()
#
# # обход коллекции
# while True:
#     try:
#         itr.next()
#     except StopIteration:
#         break
#     print(itr.current())
#     itr.first()
#
#     while True:
#         try:
#             itr.next()
#         except StopIteration:
#             break
#         print(itr.current())

# class Table:
#     def __init__(self, l, w, h):
#         self.length = l
#         self.width = w
#         self.height = h
#
#
# class DeskTable(Table):
#     def square(self):
#         return self.width * self.length
#
#
# class ComputerTable(DeskTable):
#     def square(self, monitor=0.0):
#         return self.width * self.length - monitor
#
#
# t3 = ComputerTable(0.8, 0.6, 0.7)
# print(t3.square(0.3))

pip install cryptography
from cryptography.fernet import Fernet
def write_key():
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('crypto.key', 'rb').read()
def encrypt(filename, key):
    f = Fernet(key)

with open(filename, 'rb') as file:

        file_data = file.read()



    encrypted_data = f.encrypt(file_data)



    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, key):

    f = Fernet(key)
    with open(filename, 'rb') as file:

        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, 'wb') as file:
        file.write(decrypted_data)


write_key()
key = load_key()
file = 'report.csv'
encrypt(file, key)
decrypt(file, key)