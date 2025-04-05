'''
Walmart Interview - Design Amazon Product Page Notify Me Button which sends mails to users for the product avalaibility if they have click on the button.

In this an object (observable) maintais a list of dependents (observers) and notfies then of any change in the state.

Similar to publisher - subscriber, where publisher maintains a list of subscribers and notifies them about any change. Subscribers can be added to list and removed dynamically.


'''

class StockPriceObservable:
    def addObserver(self, observer):
        pass 

    def removeObserver(self, observer):
        pass 

    def notifyObserver(self):
        pass 

    def setPrice(self, newPrice):
        pass 

    def getPrice(self):
        pass

class NotificationAlertObserver:
    def update(self):
        pass 

class EmailNotificationAlertObserver(NotificationAlertObserver):
    email = ''
    observable = StockPriceObservable()

    def __init__(self, email, observable):
        self.email = email
        self.observable = observable

    def sendMail(self, email, message):
        print(f"Hi {email}, {message} to {self.observable.getPrice()}!")

    def update(self):
        self.sendMail(self.email, "Stock price is just Updated")


class MobileNotificationAlertObserver(NotificationAlertObserver):
    phone = ''
    name = ''
    observable = StockPriceObservable()

    def __init__(self, name, phone, observable):
        self.phone = phone
        self.name = name 
        self.observable = observable

    def sendMail(self, name, message):
        print(f"Hi {name}, {message} to {self.observable.getPrice()}!")

    def update(self):
        self.sendMail(self.name, "Stock price is just Updated")


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

    
if __name__=="__main__":
    India = IndianStockPriceObservable()

    observer1 = EmailNotificationAlertObserver("ayush@gmail.com", India)
    observer2 = EmailNotificationAlertObserver("xyz@gmail.com", India)
    observer3 = MobileNotificationAlertObserver("Ayush Gupta","546565465", India)

    India.addObserver(observer1)
    India.addObserver(observer2)
    India.addObserver(observer3)

    India.setPrice(100)