class Knapsack:
    @staticmethod
    def knapsack(songs, max_duration):
        num_songs = len(songs)
        selected_songs = []

        sorted_songs = sorted(songs, key=lambda song: song.song_by_ratio(), reverse=True)

        total_duration = 0
        for song in sorted_songs:
            if total_duration + song.duration <= max_duration:
                selected_songs.append(song)
                total_duration += song.duration

        return selected_songs
