from lib.media import Media

class MediaRepository():
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM medias')
        results = cursor.fetchall()
        medias = []
        for row in results: 
            row = Media(row[0], row[1])
            medias.append(row)
        return medias
    
    def find(self, media_id):
        cursor = self._connection.cursor()
        cursor.execute(
            'SELECT * FROM medias WHERE id = %s', [media_id]
            )
        results = cursor.fetchone()
        return Media(results[0], results[1])
    
    def create(self, media):
        cursor = self._connection.cursor()
        cursor.execute(
            'INSERT INTO medias (web_url) VALUES (%s)', [media.web_url]
            )
        return None