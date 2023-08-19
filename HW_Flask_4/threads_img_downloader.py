"""
1) Написать программу, которая скачивает изображения с заданных URL-адресов и
сохраняет их на диск. Каждое изображение должно сохраняться в отдельном
файле, название которого соответствует названию изображения в URL-адресе.
2) Например URL-адрес: https://example/images/image1.jpg -> файл на диске:
image1.jpg
3) Программа должна использовать многопоточный, многопроцессорный и
асинхронный подходы.
4) Программа должна иметь возможность задавать список URL-адресов через
аргументы командной строки.
5) Программа должна выводить в консоль информацию о времени скачивания
каждого изображения и общем времени выполнения программы.
threads download
"""
import argparse
from threading import Thread
import time
import os
import requests

URLS = [
    'https://rare-gallery.com/resol/1366x768/507291-space-stars.jpg',
    'https://rare-gallery.com/resol/1366x768/567026-space-stars.jpg',
    'https://rare-gallery.com/resol/1366x768/540709-Purple-Nebula.jpg',
    'https://rare-gallery.com/resol/1366x768/578218-planet-earth.jpg',
    'https://rare-gallery.com/resol/1366x768/112526-kepler-452b-exoplanet-planet-space-stars.jpg',
]

start_func_time = time.time()
if not os.path.exists('images'):
    os.makedirs('images')


def img_saver(url):
    response = requests.get(url)
    filename = f'{url.split("/")[-1]}'
    with open(f'images/{filename}', 'wb') as f:
        f.write(response.content)
        print(f'{filename} downloaded in {(time.time() - start_time):.2f} seconds')


threads = []
start_time = time.time()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    return args.url_list


for url in URLS:
    thread = Thread(target=img_saver, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Elapsed time: {(time.time() - start_func_time):.2f} seconds')
