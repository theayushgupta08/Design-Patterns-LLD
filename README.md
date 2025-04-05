# Design Patterns

Design patterns are reusable solutions to common problems in software design. They represent best practices and provide a template for solving specific design issues in a flexible and scalable way. Design patterns are categorized into three main types:

1. **Creational Patterns**: Deal with object creation mechanisms.
2. **Structural Patterns**: Focus on the composition of classes or objects.
3. **Behavioral Patterns**: Concerned with communication between objects.

---

## Strategy Design Pattern

The **Strategy Design Pattern** is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one, and make them interchangeable. This pattern enables the algorithm to vary independently from the clients that use it.

### Use Case:
1. **Payment Processing System**:
   - Different payment methods (e.g., Credit Card, PayPal, Google Pay) can be implemented as strategies. The user can dynamically select a payment method at runtime.

2. **Sorting Algorithms**:
   - A program that needs to sort data using different algorithms (e.g., QuickSort, MergeSort, BubbleSort) can use the Strategy Pattern to switch between sorting strategies dynamically.

3. **Travel Route Planner**:
   - A navigation app can use different route calculation strategies (e.g., shortest distance, fastest time, scenic route) based on user preferences.

4. **Compression Algorithms**:
   - A file compression tool can use different compression strategies (e.g., ZIP, RAR, GZIP) depending on the user's choice.

5. **Game Character Behavior**:
   - In a game, characters can have different attack strategies (e.g., melee, ranged, magic). The Strategy Pattern allows switching between these behaviors dynamically.


---

## Observer Design Pattern

The **Observer Design Pattern** is a behavioral design pattern where an object (called the subject or observable) maintains a list of dependents (called observers) and notifies them of any state changes. This pattern is commonly used in event-driven systems.

### Use Case:
1. **Stock Market Monitoring**:
   - A stock price tracker notifies registered users (observers) whenever the stock price changes.

2. **Weather Station**:
   - A weather station broadcasts updates to multiple devices (e.g., mobile apps, websites, IoT devices) whenever the weather data changes.

3. **Social Media Notifications**:
   - Users receive notifications when someone likes, comments, or shares their posts.

4. **Auction System**:
   - Bidders (observers) are notified in real-time whenever a new bid is placed on an item.

5. **News Subscription Service**:
   - Subscribers are notified whenever a new article or update is published in their subscribed category.