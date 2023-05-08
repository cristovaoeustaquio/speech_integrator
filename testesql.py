import numpy as np
import pandas as pd
import sqlite3
import json
import io
dbFileName = 'database/database.db'

email = 'yurih@gmail.com'

with sqlite3.connect(dbFileName) as conn:
        cursor = conn.cursor()
        query = 'SELECT question, answer FROM perguntas_e_respostas'
        cursor.execute(query)
        rows = cursor.fetchall()
        rows=np.array(rows)
        print(rows)
