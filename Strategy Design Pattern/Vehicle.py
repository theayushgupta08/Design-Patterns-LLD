class Vehicle:
    def __init__(self, myDriveStrategy):
        self.myDriveStrategy = myDriveStrategy  # 2. Object recieved Dynamically goes to the object of DriveStartegy in Vehicle

    def letsDrive(self):
        self.myDriveStrategy.drive()