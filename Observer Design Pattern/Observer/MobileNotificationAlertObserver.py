from NotificationAlertObserver import NotificationAlertObserver
from StockPriceObservable import StockPriceObservable

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