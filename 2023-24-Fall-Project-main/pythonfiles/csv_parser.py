from City import City
from Song import Song
class CSVParser:
    @staticmethod
    def parse_cities(file_name):
        cities = []
        with open(file_name, 'r') as file:
            header_skipped = False
            for line in file:
                if not header_skipped:
                    header_skipped = True
                    continue
                data = line.strip().split(',')
                city_name = data[0].strip()
                latitude = float(data[2].strip())
                longitude = float(data[3].strip())
                duration=float(data[4].strip())
                city = City(city_name, latitude, longitude,duration)
                cities.append(city)
        return cities

    @staticmethod
    def parse_songs(csv_file):
        songs = []
        with open(csv_file, 'r') as file:
            next(file)  # Skip header
            for line in file:
                data = line.strip().split(',')
                popularity = float(data[1])
                duration = float(data[2])
                song = Song(popularity, duration)
                songs.append(song)
        return songs
