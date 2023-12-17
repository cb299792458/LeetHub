class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings = dict()
        self.cuisines = defaultdict(list)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.ratings[food] = (rating, cuisine)
            heapq.heappush(self.cuisines[cuisine], (-rating, food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.ratings[food][1]
        self.ratings[food] = (newRating, cuisine)
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        # print(self.cuisines[cuisine][0][0] , -self.ratings[self.cuisines[cuisine][0][1]][0])
        while self.cuisines[cuisine][0][0] != -self.ratings[self.cuisines[cuisine][0][1]][0]:
            heapq.heappop(self.cuisines[cuisine])
        return self.cuisines[cuisine][0][1]