from lib.media_repository import MediaRepository
from lib.media import Media
import psycopg2, pytest
'''
When I call #all on the MediaRepository
I get all the medias back in a list
'''
@pytest.fixture(scope='module')
def conn():
    connection = psycopg2.connect(
        database="media", 
        user="postgres", 
        password="password6", 
        host="localhost", 
        port="5432")
    yield connection
    
    connection.close()

def seed_database(conn, seed_file_path):
    with conn.cursor() as cursor:
        with open(seed_file_path, 'r') as seed_file:
            sql = seed_file.read()
            cursor.execute(sql)
        conn.commit()

def test_list_all_medias(conn):
    seed_database(conn, "seeds/media_library.sql")
    repository = MediaRepository(conn)
    result = repository.all()
    assert result == [
        Media(1, "www.unsplash.test1"),
        Media(2, "www.unsplash.test2"),
        Media(3, "www.unsplash.test3")
    ]