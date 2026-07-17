import os
from dotenv import load_dotenv
import requests
from tavily import TavilyClient
from bs4 import BeautifulSoup
from langchain.tools import tool
from rich import print

load_dotenv()



