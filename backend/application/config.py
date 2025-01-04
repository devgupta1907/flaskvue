class Config():
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    # configurations for db
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskvueDB.db'
    DEBUG = True

    # configurations for security
    SECRET_KEY = "5#y2LF4Q8zddfdgxec]"  #used to hash user credentials and store them in sessions.
    SECURITY_PASSWORD_HASH = "bcrypt" #mechanism to hash credentials and store them in database.
    SECURITY_PASSWORD_SALT = "6#y2L485pddfdgxec"
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"