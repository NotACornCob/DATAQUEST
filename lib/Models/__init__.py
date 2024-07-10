# lib/config.py
import sqlite3

CONN = sqlite3.connect('/home/notacorncob/phase3/DATAQUEST/lib/dataquest.db')
CURSOR = CONN.cursor()