import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "27394279")
    API_HASH = os.environ.get("API_HASH", "90a9aa4c31afa3750da5fd686c410851")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7567477886:AAEMI6V1ImkbEkwUIkMfHNfVrQFFB4GKNtI") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","Digital_Rename_Bot")     
    DB_URL = os.environ.get("DB_URL","mongodb+srv://telegramguy21:tnkIwvbNkJ5U3fZ7@botsuse.bpgag.mongodb.net/?retryWrites=true&w=majority&appName=Botsuse")
 
    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/b746aadfe59959eb76f59.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7465574522').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002288135729"))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002288135729"))
    OWNER = int(os.environ.get("OWNER", "7465574522"))

    # free upload limit 
    FREE_UPLOAD_LIMIT = 6442450944 # calculation 6*1024*1024*1024=results

    # premium mode feature ✅
    UPLOAD_LIMIT_MODE = True 
    PREMIUM_MODE = True 

    UPDATES = os.environ.get("UPDATES", "The_TGguy")
    
    #force subs
    try:
        FORCE_SUB = int(os.environ.get("FORCE_SUB", "")) 
    except:
        FORCE_SUB = os.environ.get("FORCE_SUB", "The_TGguy")
        
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()


#Token Verification 
VERIFY_EXPIRE = os.environ.get('VERIFY_EXPIRE', 3600) # VERIFY EXPIRE TIME IN SECONDS. LIKE:- 0 (ZERO) TO OFF VERIFICATION 
SHORTLINK_SITE = os.environ.get('SHORTLINK_SITE', 'linkmonetizer.in') # YOUR SHORTLINK URL LIKE:- site.com
SHORTLINK_API = os.environ.get('SHORTLINK_API', 'bf35b33b841943cdce510413393f35a9ff0bb558') # YOUR SHORTLINK API LIKE:- ma82owowjd9hw6_js7
PREMIUM_USERS = list(map(int, os.environ.get('PREMIUM_USERS', '1705634892').split()))
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Verified') #For Token verification 
    
