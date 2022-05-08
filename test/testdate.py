from datetime import date
from dateutil.relativedelta import relativedelta
from time import time

import numpy as np

today = date(2021, 3, 31)
spot = today + relativedelta(days=2)
dates_ = [today,
          today + relativedelta(days=1),
          today + relativedelta(days=2),
          spot + relativedelta(weeks=1),
          spot + relativedelta(weeks=2),
          spot + relativedelta(weeks=3),
          spot + relativedelta(months=1),
          spot + relativedelta(months=2),
          spot + relativedelta(months=3),
          ]

N_year = 30
for i in range(N_year * 2):
    dates_.append(spot + relativedelta(months=6 * (i + 1)))

dates = np.array(dates_)
t1 = time()
for i in range(len(dates_)):
    dates_[i] = dates_[i] + relativedelta(days=0)
print("List calc time = " + (str(time() - t1)))

t1 = time()
for i in range(len(dates)):
    dates[i] = dates[i] + relativedelta(days=0)
print("Numpy calc time = " + (str(time() - t1)))
