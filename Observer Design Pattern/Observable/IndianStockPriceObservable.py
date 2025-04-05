from StockPriceObservable import StockPriceObservable


class IndianStockPriceObservable(StockPriceObservable):
    def __init__(self):
        self.observerList = []
        self.price = 0

    def addObserver(self, observer):
        self.observerList.append(observer)

    def removeObserver(self, observer):
        self.observerList.remove(observer)

    def notifyObserver(self):
        print("Notifying All Observers!")
        for observer in self.observerList:
            observer.update()

    def setPrice(self, newPrice):
        if self.price != newPrice:
            self.price = newPrice
            self.notifyObserver()

    def getPrice(self):
        return self.price