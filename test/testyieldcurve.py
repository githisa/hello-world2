from yield_curve import YieldCurve
from datetime import date
from dateutil.relativedelta import relativedelta

yc = YieldCurve()

dates = []
dfs = []

today = date.today()
for i in range(50):
    dates.append(today + relativedelta(days=i))
    dfs.append(1.0 - 0.001 * i)

yc.set_from_date_and_df(dates, dfs)
