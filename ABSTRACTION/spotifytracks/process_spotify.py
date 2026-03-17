"""
1. Create a Track Class
Create a class Track with attributes:
track_name
artist
popularity
Create a method display_info() to print track details.

"""

from csv import DictReader

class Track:

    def  __init__(self):
        
        fr = open("ABSTRACTION\\spotifytracks\\spotify-tracks-dataset.csv")

        self.tracks = list(DictReader(fr))

        print(len(self.tracks))


# for t in tracks[:5]:

#         track_instance = Track(t["track_name"], t["artists"],t["popularity"])

#         track_instance.display_info()

track = Track()


