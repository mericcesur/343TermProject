
from csv_parser import CSVParser
from knapsack import Knapsack
from tsp import TSP
from City import City  # Adjust the import based on the actual structure of your project
from Song import Song
import time
def main():
    start=time.time()
    songs = CSVParser.parse_songs("../data/the_scorpions_songs_data.csv")
    max_duration = 0 # Replace this value with your desired maximum duration
    selected_songs = Knapsack.knapsack(songs, max_duration)
    for song in selected_songs:
        print(f"Song: Popularity - {song.popularity}, Duration - {song.duration}")

    file_name = "../data/furkan_meric_cities.csv"
    cities = CSVParser.parse_cities(file_name)
    result = TSP.nearest_neighbor_tsp(cities)
    # Other parts of your code
    total_pop=0
    total_dur=0
    print("Tour:")
    print()
    for city in result:
        
        print(city.get_name())
        duration_of_concert=city.get_duration()
        list_of_song=Knapsack.knapsack(songs, duration_of_concert)
        for song in list_of_song:
            total_pop+=song.popularity
            total_dur+=song.duration
    end=time.time()
    executipn_time=end-start
    print(f"Total Popularity Reach In Concerts: {total_pop}")
    print(f"Total Duration In all of the Concerts: {total_dur}")
    print(f"Execution Time is:{executipn_time}")    
if __name__ == "__main__":
    main()

