import psycopg2, os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.getenv("DB_URL")) 

cur = conn.cursor() 

with open("seeds/media_library.sql", 'r') as seed_file:
    sql = seed_file.read()
    statements = sql.split(";")
    for statement in statements:
        statement = statement.strip()
        if statement:
            cur.execute(statement)
conn.commit()
  
# close the cursor and connection 
cur.close() 
conn.close() 
