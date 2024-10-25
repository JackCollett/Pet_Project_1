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
            print(results)
            row = Media(row[0], row[1], row[2], row[3])
            medias.append(row)
        return medias
    
    def find(self, media_id):
        cursor = self._connection.cursor()
        cursor.execute(
            'SELECT * FROM medias WHERE id = %s', [media_id]
            )
        results = cursor.fetchone()
        return Media(results[0], results[1], results[2], results[3])
    
    def create(self, media):
        cursor = self._connection.cursor()
        cursor.execute(
            'INSERT INTO medias (web_url, rotation, brightness) VALUES (%s, %s, %s)', [media.web_url, media.rotation, media.brightness]
            )
        return None
    
    def delete(self, media_id):
        cursor = self._connection.cursor()
        cursor.execute(
            'DELETE FROM medias WHERE id = %s', [media_id]
            )
        return None