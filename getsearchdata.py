from google_play_scraper import search
import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
import requests

#from google_play_scraper.scraper import PlayStoreScraper

run = True
rounds = 0
while True: 
    #scraper = PlayStoreScraper()
    #results = scraper.get_app_ids_for_query("period tracker")
    #print(results)

    #code o remove duplicate rows because i tried to see if it would give new data with each run
    #df_state=pd.read_csv("export.csv")
    #Dup_Rows = df_state[df_state.duplicated()]
    #DF_RM_DUP = df_state.drop_duplicates(keep='first')
    #DF_RM_DUP.to_csv('nodups.csv',index=False)

    #break
    #round = round + 1

    result = search("period tracker",
                    lang="en",  # defaults to 'en'
                    country="us",  # defaults to 'us'
                    n_hits=100  # defaults to 30 (= Google's maximum)
    )
    #print(result)

    import json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
        #f.close()
    

    pdObj = pd.read_json('data.json', orient='records')
    #if run:
     #   pdObj.to_csv('export.csv', index=False)
      #  run=False
    #else:
     #   pdObj.to_csv('export.csv', mode='a', index=False, header=False)

    pdObj.to_csv('export.csv', index=False)
    

