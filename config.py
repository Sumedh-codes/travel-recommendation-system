import os
from dotenv import load_dotenv

load_dotenv()# loading the data
TRANSACTION_PATH = os.getenv("TRANSACTION_FILE_PATH")
ITEM_PATH = os.getenv("ITEM_FILE_PATH")