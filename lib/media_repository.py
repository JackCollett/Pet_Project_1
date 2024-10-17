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