from NotificationAlertObserver import NotificationAlertObserver
from StockPriceObservable import StockPriceObservable

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