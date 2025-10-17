from lib.music_tracker import *
import pytest

def test_add_song_successfully():
    test = music_tracker()
    test.add_song("Breathless")
    assert test.songs == ["Breathless"]
    
def test_get_songlist_successfully():
    test = music_tracker()
    test.add_song("Happy Birthday")
    assert test.get_songs() == ["Happy Birthday"]
    
def test_add_song_empty_string():
    test = music_tracker()
    with pytest.raises(Exception) as e:
        test.add_song("")
    error_message = str(e.value)
    assert error_message == "Please enter song name"
    
def test_add_song_not_string():
    test = music_tracker()
    with pytest.raises(TypeError) as e:
        test.add_song(3)
    error_message = str(e.value)
    assert error_message == "Please enter song name in string format"
    
def test_get_songlist_multiple_songs():
    test = music_tracker()
    test.add_song("Breathless")
    test.add_song("Happy Birthday")
    test.add_song("Disco Inferno")
    assert test.get_songs() == ['Breathless', 'Happy Birthday', 'Disco Inferno']