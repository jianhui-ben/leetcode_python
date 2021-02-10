#1396. Design Underground System
#Implement the UndergroundSystem class:

#void checkIn(int id, string stationName, int t)
#A customer with a card id equal to id, gets in the station stationName at time t.
#A customer can only be checked into one place at a time.
#void checkOut(int id, string stationName, int t)
#A customer with a card id equal to id, gets out from the station stationName at time t.
#double getAverageTime(string startStation, string endStation)
#Returns the average time to travel between the startStation and the endStation.
#The average time is computed from all the previous traveling from startStation to endStation that happened directly.
#Call to getAverageTime is always valid.
#You can assume all calls to checkIn and checkOut methods are consistent. If a customer gets in at time t1 at some station, they get out at time t2 with t2 > t1. All events happen in chronological order.

 

#Example 1:

#Input
#["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
#[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

#Output
#[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

#Explanation
#UndergroundSystem undergroundSystem = new UndergroundSystem();
#undergroundSystem.checkIn(45, "Leyton", 3);
#undergroundSystem.checkIn(32, "Paradise", 8);
#undergroundSystem.checkIn(27, "Leyton", 10);
#undergroundSystem.checkOut(45, "Waterloo", 15);
#undergroundSystem.checkOut(27, "Waterloo", 20);
#undergroundSystem.checkOut(32, "Cambridge", 22);
#undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
#undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
#undergroundSystem.checkIn(10, "Leyton", 24);
#undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000
#undergroundSystem.checkOut(10, "Waterloo", 38);
#undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.00000


class UndergroundSystem:

    def __init__(self):
        self.travellers=dict()
        self.station_times=dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travellers[id]= (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.travellers:
            start_station, start_time= self.travellers.pop(id)
            path='_'.join([start_station, stationName])
            if path not in self.station_times:
                self.station_times[path]=(1, float(t-start_time))
            else:
                cnt, pre_tot= self.station_times[path]
                self.station_times[path]=(cnt+1, float(pre_tot+t-start_time))
        else:
            print("no such travellers")

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        path= '_'.join([startStation, endStation])
        if path in self.station_times:
            cnt, tot=self.station_times[path]
            return tot/cnt
        return None
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)