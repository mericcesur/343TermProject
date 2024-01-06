class TSP:
    @staticmethod
    def nearest_neighbor_tsp(cities):
        num_cities = len(cities)
        visited = [False] * num_cities
        tour = []

        current_city = cities[0]  # Start from the first city
        visited[0] = True
        total_distance = 0  # Initialize total distance

        for _ in range(num_cities - 1):
            min_distance = float('inf')
            nearest_city_index = -1

            for i, other_city in enumerate(cities):
                if not visited[i]:
                    distance = current_city.distance_to(other_city)
                    if distance < min_distance:
                        min_distance = distance
                        nearest_city_index = i

            tour.append(current_city)
            total_distance += min_distance 
            visited[nearest_city_index] = True
            current_city = cities[nearest_city_index]

        tour.append(current_city)  ,
        total_distance += current_city.distance_to(tour[0])  
       
        print(f"Total Distance: {total_distance}")
        return tour
