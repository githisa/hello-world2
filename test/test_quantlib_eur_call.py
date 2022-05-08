import QuantLib as ql

# date settings
todayDate = ql.Date(1, 10, 2020)
ql.Settings.instance().evaluationDate = todayDate
day_count = ql.Actual365Fixed()
calendar = ql.UnitedStates()

# market data
spot = 130
risk_free_rate = 0.001
dividend = 0.02
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

# run calculation
print(option.NPV())
