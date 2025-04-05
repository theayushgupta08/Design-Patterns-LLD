from Observable.IndianStockPriceObservable import IndianStockPriceObservable
from Observer.EmailNotificationAlertObserver import EmailNotificationAlertObserver
from Observer.MobileNotificationAlertObserver import MobileNotificationAlertObserver

if __name__=="__main__":
    India = IndianStockPriceObservable()

    observer1 = EmailNotificationAlertObserver("ayush@gmail.com", India)
    observer2 = EmailNotificationAlertObserver("xyz@gmail.com", India)
    observer3 = MobileNotificationAlertObserver("Ayush Gupta","546565465", India)

    India.addObserver(observer1)
    India.addObserver(observer2)
    India.addObserver(observer3)

    India.setPrice(10)