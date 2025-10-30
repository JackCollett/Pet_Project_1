from lib.media import Media
"""
Constructs with id and photo_url
"""
def test_constucts_with_fields():
    media = Media(1,"www.unsplash.com/testurl", "Brian")
    assert media.id == 1
    assert media.web_url == "www.unsplash.com/testurl"
    assert media.creator == "Brian"
    
"""
When I construct two Medias with the same fields
They are equal
"""
def test_equality():
    media_1 = Media(1, "www.unsplash.com/testurl", "Brian")
    media_2 = Media(1, "www.unsplash.com/testurl", "Brian")
    assert media_1 == media_2
    
"""
When I construct a Media 
And I format it to a string 
Then it comes out in a friendly format
"""
def test_formatting():
    media_1 = Media(1, "www.unsplash.com/testurl", "Brian")
    assert str(media_1) == "Media(1, www.unsplash.com/testurl, Brian, 0, 100, 1, 0, 0, 1, 0, 0, False, #e66465, #000000)"
