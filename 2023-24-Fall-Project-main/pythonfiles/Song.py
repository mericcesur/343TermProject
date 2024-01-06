class Song:
    def __init__(self, popularity, duration):
        self.popularity = popularity
        self.duration = duration
    def song_by_ratio(self):
        return self.popularity/self.duration        