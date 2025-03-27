from lib.media_repository import MediaRepository
from lib.media import Media
import psycopg2, pytest

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
'''
When I call #all on the MediaRepository
I get all the medias back in a list
'''
def test_list_all_medias(conn):
    seed_database(conn, "seeds/media_library.sql")
    repository = MediaRepository(conn)
    result = repository.all()
    assert result == [
        Media(1, "www.unsplash.test1", 0, 100),
        Media(2, "www.unsplash.test2", 0, 100),
        Media(3, "www.unsplash.test3", 0, 100)
    ]

'''
When I call #find on the MediaRepository with an id
I get the media corresponding to that id back
'''
def test_find(conn):
    seed_database(conn, "seeds/media_library.sql")
    repository = MediaRepository(conn)
    result = repository.find(3)
    assert result == Media(3, "www.unsplash.test3", 0, 100)
    
'''
When I call #create on MediaRepository with some fields 
And then I list out all of the records
My new media is in the list
'''
def test_create(conn):
    seed_database(conn, "seeds/media_library.sql")
    repository = MediaRepository(conn)
    
    media = Media(None, "www.unsplash.test4")
    assert repository.create(media) == None
    
    result = repository.all()
    assert result == [
        Media(1, "www.unsplash.test1", 0, 100),
        Media(2, "www.unsplash.test2", 0, 100),
        Media(3, "www.unsplash.test3", 0, 100),
        Media(4, "www.unsplash.test4", 0, 100)
    ]

'''
When I first call #all on Media Repository I see all records
Then I call #delete on MediaRepository with an id
And I get all the records
Then the deleted record does not show up
'''
def test_delete(conn):
    seed_database(conn, "seeds/media_library.sql")
    repository = MediaRepository(conn)
    
    result = repository.all()
    assert result == [
        Media(1, "www.unsplash.test1", 0, 100),
        Media(2, "www.unsplash.test2", 0, 100),
        Media(3, "www.unsplash.test3", 0, 100)
    ]
    media_id = 2
    assert repository.delete(media_id) == None
    
    result = repository.all()
    assert result == [
        Media(1, "www.unsplash.test1", 0, 100),
        Media(3, "www.unsplash.test3", 0, 100)
    ]