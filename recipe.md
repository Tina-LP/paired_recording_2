# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MusicTracker:
    # User-facing properties:
    #   songs: list

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   None
        pass # No code here yet

    def add_song(self, song_name):
        # Parameters:
        #   song_name: string representing the song
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the song to the songs list
        pass # No code here yet

    def get_song_list(self):
        # Returns:
        #   A list of the songs
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a song name
Adds song to song list
"""
music_tracker = MusicTracker()
music_tracker.add_song("Breathless")
music_tracker.songs # contains the song "Breathless"

"""
Given no parameters
Returns list of songs
"""
music.tracker = MusicTracker()
music_tracker.add_song("Breathless")
music_tracker.get_song_list() # => returns song name "Breathless"

"""
Given an empty string as song name
Raises Exception "Please enter song name"
"""
music.tracker = MusicTracker()
music_tracker.add_song("") # => "Please enter song name"

"""
Given a non-string parameter
Raises Input Error "Please enter song name in string format"
"""
music.tracker = MusicTracker()
music_tracker.add_song(800) # => "Please enter song name in string format"

"""
Given no parameters
Returns all songs on list correctly"
"""
music.tracker = MusicTracker()
music_tracker.add_song("Breathless")
music_tracker.add_song("Happy Birthday")
music_tracker.add_song("Disco Inferno") # => ['Breathless', 'Happy Birthday', 'Disco Inferno']
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
