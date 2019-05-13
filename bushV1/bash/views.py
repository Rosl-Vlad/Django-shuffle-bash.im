from django.shortcuts import render
from bs4 import BeautifulSoup
import numpy as np
import requests as req
import random
import re
from bs4 import BeautifulSoup


def all_change(url_name, file_name):
    try:
        with open(file_name, "x") as fout:
            pass
    except FileExistsError:
        pass
    file_page = open(file_name, 'w')
    file_page.truncate()
    response = req.get(url_name)
    page = response.content.decode('utf-8')

    soup = BeautifulSoup(page, 'html.parser')
    link_change = soup.find_all('link', rel="preload")
    link_change[0].attrs['href'] = "{% static 'css/4926e00a__bor.css' %}"
    link_change[1].attrs['href'] = "{% static 'js/52a03a44__bor.js' %}"
    link_change = soup.find_all('link', rel="stylesheet")
    link_change[0].attrs['href'] = "{% static 'css/4926e00a__bor.css' %}"
    link_change = soup.find_all(
        'script', src="/3.0/bor.js?164693d002ae549f37b0491dfe8d51ab")
    link_change[0].attrs['src'] = "{% static 'js/52a03a44__bor.js' %}"
    y = soup.find_all('div', class_="quote__body")
    for i in range(0, len(y)):
        #перемешивание по словам

        parts = np.random.permutation(y[i].text.split())

        #перемешивание по предложениям

        #parts = re.findall('.*?<br>|.*?[.!?\n]', y[i].text)

        new_quote = ''
        random.shuffle(parts)
        for word in parts:
            #добавление элемента в случае перемешивание по предложениям

            #new_quote += word

            #добавление элемента в случае перемешивание по предложениям

            new_quote += (word + ' ')
        soup.find_all('div', class_="quote__body")[i].string = new_quote

    file_page.write("{% load staticfiles %}\n")
    file_page.write(str(soup))
    file_page.close()


def fix_struct(file_name):
    file_html_exaption = open(file_name, 'r+')
    html_exaption = file_html_exaption.read()
    file_fix = open("bash/templates/bush/all_page/text.html", 'w')
    file_fix.truncate()
    soup_old = BeautifulSoup(html_exaption, 'html.parser')
    elem = soup_old.find('main', class_='columns__main')
    item = soup_old.find('section', class_='quotes')
    elem.append(item)
    item = soup_old.find('div', class_='sections desktop bottom')
    elem.append(item)
    elem = soup_old.find('div', class_='columns')
    item = soup_old.find('aside', class_='columns__aside')
    elem.append(item)
    file_fix.write(str(soup_old))
    file_fix.close()
    file_html_exaption.close()


def bash_main(request):
    url_name = "https://bash.im"
    file_name = "bash/templates/bush/all_page/main.html"
    all_change(url_name, file_name)
    fix_struct(file_name)
    return render(request, 'bush/all_page/text.html')


def bash_best(request):
    url_name = "https://bash.im/best"
    file_name = "bash/templates/bush/all_page/best.html"
    all_change(url_name, file_name)
    return render(request, 'bush/all_page/best.html')


def bash_random(request):
    url_name = "https://bash.im/random"
    file_name = "bash/templates/bush/all_page/random.html"
    all_change(url_name, file_name)
    return render(request, 'bush/all_page/random.html')


def bash_byrating(request):
    url_name = "https://bash.im/byrating"
    file_name = "bash/templates/bush/all_page/byrating.html"
    all_change(url_name, file_name)
    fix_struct(file_name)
    return render(request, 'bush/all_page/text.html')


def bash_abyss(request):
    url_name = "https://bash.im/abyss"
    file_name = "bash/templates/bush/all_page/abyss.html"
    all_change(url_name, file_name)
    return render(request, 'bush/all_page/abyss.html')


def bash_abysstop(request):
    url_name = "https://bash.im/abysstop"
    file_name = "bash/templates/bush/all_page/abysstop.html"
    all_change(url_name, file_name)
    return render(request, 'bush/all_page/abysstop.html')


def bash_abyssbest(request):
    url_name = "https://bash.im/abyssbest"
    file_name = "bash/templates/bush/all_page/abyssbest.html"
    all_change(url_name, file_name)
    return render(request, 'bush/all_page/abyssbest.html')


def bash_faq(request):
    url_name = "https://bash.im/faq"
    file_name = "bash/templates/bush/all_page/faq.html"
    all_change(url_name, file_name)
    return render(request, 'bush/all_page/faq.html')
