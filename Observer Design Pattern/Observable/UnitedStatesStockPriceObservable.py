from StockPriceObservable import StockPriceObservable

class UnitedStatesStockPriceObservable(StockPriceObservable):
    observerList = []
    price = 0

    def addObserver(self, observer):
        self.observerList.append(observer)

    def removeObserver(self, observer):
        self.observerList.remove(observer)

    def notifyObserver(self):
        print("Notifying All Observers!")

    def setPrice(self, newPrice):
        if self.price != newPrice:
            self.price = newPrice
            self.notifyObserver()

    def getPrice(self):
        return self.price