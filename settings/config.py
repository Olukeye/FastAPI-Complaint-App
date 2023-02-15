from dotenv import load_dotenv
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(BASEDIR, '.env')

load_dotenv(path)

def load_env_config():
    return {
        'server': os.getenv("DATABASE_SERVER"),
        'database': os.getenv("DATABASE"),
        'access_token_expire_minute': os.getenv("ACCESS_TOKEN_EXPIRE_MINUTE"),
        'algorithm': os.getenv("ALGORITHM"),
        'cleardb_database_url': os.getenv("CLEARDB_DATABASE_URL"),
        'database_string': os.getenv("DATABASE_STRING"),
        'secret_key': os.getenv("SECRET_KEY"),
        # 'password_salt': os.getenv("ACCESS_SALT"),
    }

