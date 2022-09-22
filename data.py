import csv
from logging import exception
import pandas as pd
import requests
from dotenv import load_dotenv
import os
from urllib.request import urlretrieve
from datetime import date

current_date = date.today().strftime("%d-%m-%Y")
current_month = date.today().strftime("%B-%Y")
load_dotenv()

def get_museos_csv():
    try:
        req = requests.get(os.getenv('URL_MUSEO'),stream=True) 
        status_code = req.status_code
        if status_code == 200:
            museo_dir = os.getenv('MUSEO_PATH')
            museo_path = os.path.join(museo_dir,current_month)
            mode = 0o666
            if not os.path.exists(museo_path): 
                os.makedirs(museo_path,mode)
            museo_csv = open(f'{museo_dir}/{current_month}/museos-{current_date}.csv','wb')
            museo_csv.write(req.content)
    except Exception as e:
        print('Error: ',e)

def get_bibliotecas_csv():
    try:
        req = requests.get(os.getenv('URL_BIBLIOTECAS'),stream=True) 
        status_code = req.status_code
        if status_code == 200:
            dir = os.getenv('BIBLIOTECAS_PATH')
            path = os.path.join(dir,current_month)
            mode = 0o666
            if not os.path.exists(path): 
                os.makedirs(path,mode)
            museo_csv = open(f'{dir}/{current_month}/bibliotecas-{current_date}.csv','wb')
            museo_csv.write(req.content)
    except Exception as e:
        print('Error: ',e)

def get_cines_csv():
    try:
        req = requests.get(os.getenv('URL_CINES'),stream=True) 
        status_code = req.status_code
        if status_code == 200:
            dir = os.getenv('CINES_PATH')
            path = os.path.join(dir,current_month)
            mode = 0o666
            if not os.path.exists(path): 
                os.makedirs(path,mode)
            museo_csv = open(f'{dir}/{current_month}/cines-{current_date}.csv','wb')
            museo_csv.write(req.content)
    except Exception as e:
        print('Error: ',e)
get_bibliotecas_csv()
get_museos_csv()
get_cines_csv()