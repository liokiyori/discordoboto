import feedparser 
import os
from dotenv import load_dotenv


load_dotenv()

RSS_url = os.getenv("bfm_business_tech")

def fetch_rss():
    return feedparser.parse(RSS_url)