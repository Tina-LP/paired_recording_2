class music_tracker():
    
    def __init__(self):
        self.songs = []
    
    def add_song(self, song_name):
        if song_name == "":
            raise Exception("Please enter song name")
        elif not isinstance(song_name, str):
            raise TypeError("Please enter song name in string format")
        else:
            self.songs.append(song_name)
            
    def get_songs(self):
        return self.songs