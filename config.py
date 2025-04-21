import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # digital_botz client config
    API_ID = os.environ.get("API_ID", "26385571")
    API_HASH = os.environ.get("API_HASH", "aac7a3c3c2f36e72201a6a5a21eb802a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8056090761:AAF8euR7g2HTgv9bYIINzFuoFJ2FyY7Alxo") 

    # premium account string session required 😢 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    
    # database config
    DB_NAME = os.environ.get("DB_NAME","BidhaanRENAMER_BOT")     
    DB_URL = os.environ.get("DB_URL","mongodb+srv://BIGFIISH:iFyAm2DZqEzo76VW@cluster0.z6bhz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/b746aadfe59959eb76f59.jpg")
    
    #ID's
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6169808990').split()]
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002586992832"))
    DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1002586992832"))
    OWNER = int(os.environ.get("OWNER", ""))
    

    # free upload limit 
    FREE_UPLOAD_LIMIT = 6442450944 # calculation 6*1024*1024*1024=results

    # premium mode feature ✅
    UPLOAD_LIMIT_MODE = True #True or False (if false, no daily limit)
    PREMIUM_MODE = True #True or False 

    # Usernames 
    UPDATES = os.environ.get("UPDATES", "BIDHAANBOTS") #Eg: The_TGguy
    DEV= os.environ.get("DEV", "BIG_FiiSH") #Eg: Itsme123i
    
    #force subs ID
    FORCE_SUB = int(os.environ.get("FORCE_SUB", "-1002668404997")) #Fsub 🆔 
      
    # wes response configuration     
    PORT = int(os.environ.get("PORT", "8080"))
    BOT_UPTIME = time.time()


#Token Verification 
VERIFY_EXPIRE = os.environ.get('VERIFY_EXPIRE', 0) # VERIFY EXPIRE TIME IN SECONDS. LIKE:- 0 (ZERO) TO OFF VERIFICATION 
SHORTLINK_SITE = os.environ.get('SHORTLINK_SITE', '') # YOUR SHORTLINK URL LIKE:- site.com
SHORTLINK_API = os.environ.get('SHORTLINK_API', '') # YOUR SHORTLINK API LIKE:- ma82owowjd9hw6_js7
PREMIUM_USERS = list(map(int, os.environ.get('PREMIUM_USERS', '').split()))
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Verified') #For Token verification 
    
