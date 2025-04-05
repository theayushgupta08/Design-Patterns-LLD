from DriveStrategies.SportsDriveStrategy import SportsDriveStrategy
from DriveStrategies.NormalDriveStrategy import NormalDriveStrategy

from Vehicles.SportsBike import SportsBike
from Vehicles.GoodsServiceTruck import GoodsServiceTruck

# Main
if __name__=="__main__":
    # For Sports Bike
    mySportsBike = SportsBike(SportsDriveStrategy())  # 1. This object goes to myDriveStrategy
    mySportsBike.letsDrive()

    # For Goods Service Truck
    myGoodsServiceTruck = GoodsServiceTruck(NormalDriveStrategy())  # 1. This object goes to myDriveStrategy
    myGoodsServiceTruck.letsDrive()


