import sqlite3
from config import config

db = sqlite3.connect(config.db.name(), check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()


