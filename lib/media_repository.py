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
            print(row)
            row = Media(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            medias.append(row)
        return medias
    
    def find(self, creator):
        cursor = self._connection.cursor()
        cursor.execute(
            'SELECT * FROM medias WHERE creator = %s', [creator]
            )
        results = cursor.fetchall()
        return results
    
    def create(self, media):
        cursor = self._connection.cursor()
        cursor.execute(
            'INSERT INTO medias (web_url, creator, rotation, brightness, skew, gradient, gradient_colors) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id', 
            (media.web_url, media.creator, media.rotation, media.brightness, media.skew, media.gradient, media.gradient_colors))
        new_id = cursor.fetchone()[0]
        media.id = new_id
        return media
    
    def update(self, media_id, rotation, brightness, skew, gradient, gradient_colors):
        cursor = self._connection.cursor()
        cursor.execute(
            'UPDATE medias SET rotation = (%s), brightness = (%s), skew = (%s), gradient = (%s), gradient_colors = (%s) WHERE id = (%s)', 
            (rotation, brightness, skew, gradient, gradient_colors, media_id))
        return None
    
    def delete(self, media_id):
        cursor = self._connection.cursor()
        cursor.execute(
            'DELETE FROM medias WHERE id = %s', [media_id]
            )
        return None