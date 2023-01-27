class UndergroundSystem:

    def __init__(self):
        self.open_trips = dict()
        self.closed_trips = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.open_trips[id] = {'start': stationName, 't': t}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        open_trip = self.open_trips[id]
        del self.open_trips[id]
        
        route = open_trip['start'] + '-' + stationName
        if not route in self.closed_trips:
            self.closed_trips[route] = {'sum': 0, 'num': 0}
        self.closed_trips[route]['sum'] += t - open_trip['t']
        self.closed_trips[route]['num'] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.closed_trips[startStation+'-'+endStation]['sum']/self.closed_trips[startStation+'-'+endStation]['num']


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)