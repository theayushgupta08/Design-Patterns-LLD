'''Startegy Design Pattern helps to define family of algorithms and choose among one dynamically according to situation.'''


# Algorithm Type
class DriveStrategy:
    def drive(self):
        print("This is drive Strategy!")

# Family of Algorithm

# Algorithm 1
class SportsDriveStrategy(DriveStrategy):
    def drive(self):
        print("This is Sports Drive Strategy!")  # 3. Choosen SportsDriveStrategy Dynamically

# Algorithm 2
class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print("This is a Normal Drive Startegy!")   # 3. Choosen NormalDriveStrategy Dynamically

# Algorithm 3
class XYZDriveStartegy(DriveStrategy):
    def drive(self):
        print("This is XYZ Drive Strategy!")


# Client Code
class Vehicle:
    def __init__(self, myDriveStrategy):
        self.myDriveStrategy = myDriveStrategy  # 2. Object recieved Dynamically goes to the object of DriveStartegy in Vehicle

    def letsDrive(self):
        self.myDriveStrategy.drive()

class SportsBike(Vehicle):
    def __init__(self, myDriveStrategy):
        super().__init__(myDriveStrategy)

class GoodsServiceTruck(Vehicle):
    def __init__(self, myDriveStrategy):
        super().__init__(myDriveStrategy)


# Main
if __name__=="__main__":
    # For Sports Bike
    mySportsBike = SportsBike(SportsDriveStrategy())  # 1. This object goes to myDriveStrategy
    mySportsBike.letsDrive()

    # For Goods Service Truck
    myGoodsServiceTruck = GoodsServiceTruck(NormalDriveStrategy())  # 1. This object goes to myDriveStrategy
    myGoodsServiceTruck.letsDrive()