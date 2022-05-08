# https://quantcollege.net/tag/quantlib-python Quant College記事
# QuantLib-Python 公式PDF https://quantlib-python-docs.readthedocs.io/_/downloads/en/latest/pdf/

import QuantLib as ql
import matplotlib.pyplot as plt

# date settings
todayDate = ql.Date(1, 10, 2020)
ql.Settings.instance().evaluationDate = todayDate
day_count = ql.Actual365Fixed()
calendar = ql.TARGET()

# market data
spot = 130
risk_free_rate = 0.02
dividend = 0.0
vol = 0.20

# trade data
maturity = ql.Date(1, 4, 2021)
strike = 130
option_type = ql.Option.Call

# make market objects
spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot))
flat_rf_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(todayDate, risk_free_rate, day_count))
flat_div_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(todayDate, dividend, day_count))
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(todayDate, calendar, vol, day_count))

N = 100  # number of output strike grid
strikes = []
result_pvs = []
for i in range(N):
    strike = spot + (2 * i - N) / N * spot
    # make trade objects
    payoff = ql.PlainVanillaPayoff(option_type, strike)
    exercise = ql.EuropeanExercise(maturity)
    option = ql.VanillaOption(payoff, exercise)

    # make model object
    bsm_process = ql.BlackScholesMertonProcess(
        spot_handle, flat_div_ts, flat_rf_ts, flat_vol_ts)

    # make pricing engine
    engine = ql.AnalyticEuropeanEngine(bsm_process)

    # set pricing engine
    option.setPricingEngine(engine)

    # run and restore results
    strikes.append(strike)
    result_pvs.append(option.NPV())

plt.scatter(strikes, result_pvs)
plt.show()
