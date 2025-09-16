import psycopg2

conn = psycopg2.connect(database="media", 
                        user="postgres", 
                        password="password6", 
                        host="localhost", 
                        port="5432")

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