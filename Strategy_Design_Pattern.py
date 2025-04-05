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
        print("This is a Normal Drive Startegy!")

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


mySportsBike = Vehicle(SportsDriveStrategy())  # 1. This object goes to myDriveStrategy
mySportsBike.letsDrive()