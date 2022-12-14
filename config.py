import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5685376427:AAEuI7_zEbY_1IQz6dOXE3yCwXdAYC0-cqA")
      API_ID = int(os.environ.get("APP_ID", 9303355))
      API_HASH = os.environ.get("API_HASH", "addd075f93980e9fc6817081ed682fd8")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Ts_Bots")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 1801434814)) 
      DB_URL = os.environ.get("DATABASE_URL", "postgres://njckswrw:vTb-KzYF46eQsV8xA34M-obf07m6ge2I@ziggy.db.elephantsql.com/njckswrw")
