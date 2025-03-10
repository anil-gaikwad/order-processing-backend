import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///orders.db")
DEBUG_MODE = os.getenv("DEBUG", "false").lower() == "true"
