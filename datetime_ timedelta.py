'''

У модулі datetime є клас timedelta, який використовується для представлення різниці між двома моментами в часі. 
'''

from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta) # 64 days, 8:05:56.000010


#=====================================
from datetime import datetime, timedelta

now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date)
