import os

class Config:

    BOT_TOKEN = os.environ.get("1458522919:AAEg7FiWMkrluudHXzUbEaaQIMaMI4-hTt8")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", 'utubeupload')

    API_ID = int(os.environ.get("2844499"))

    API_HASH = os.environ.get("ca40c4342d8f467405d4a0768d8335b1")

    CLIENT_ID = os.environ.get("97571652909-u5j70q20g2e3ni3usc9a2nlhghhu7ncj.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("9wx27cE9445OKqbsf1TiRivK")

    BOT_OWNER = int(os.environ.get("1360321723"))
    
    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", '1360321723')

    AUTH_USERS = [BOT_OWNER, 1360321723] + ([int(user.strip()) for user in AUTH_USERS_TEXT.split(",")] if AUTH_USERS_TEXT else [])
    
    VIDEO_DESCRIPTION = os.environ.get("VIDEO_DESCRIPTION", '').replace('<', '').replace('>', '')
    
    VIDEO_CATEGORY = int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    
    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", '')
    
    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", '')
    
    DEBUG = bool(os.environ.get("DEBUG"))
    
    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ['private', 'public', 'unlisted']:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"



