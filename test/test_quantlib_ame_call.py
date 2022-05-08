import QuantLib as ql
import pandas as pd
from time import time

# date settings
from QuantLib import Date

todaysDate: Date = ql.Date(10, ql.October, 2020)
ql.Settings.instance().evaluationDate = todaysDate
day_count = ql.Actual365Fixed()
calendar = ql.Japan()

# market data
spot = 120.0
risk_free = 0.001
dividend = 0.0163
vol = 0.20

# trade data
maturity = calendar.advance(todaysDate, 6 * ql.Months, ql.ModifiedFollowing)
strike = 130.0
option_type = ql.Option.Call

# numerical method settings
steps = 201
fdm_time_steps = 201
fdm_state_grid_points = 200

# make market objects
spot_handle = ql.QuoteHandle(ql.SimpleQuote(spot))
flat_rf_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(todaysDate, risk_free, day_count)
)
flat_div_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(todaysDate, dividend, day_count)
)
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(todaysDate, calendar, vol, day_count)
)

# make trade objects
payoff = ql.PlainVanillaPayoff(option_type, strike)
exercise = ql.AmericanExercise(todaysDate, maturity)
option = ql.VanillaOption(payoff, exercise)

# make model objects
bsm_process = ql.BlackScholesMertonProcess(
    spot_handle, flat_div_ts, flat_rf_ts, flat_vol_ts)

# make pricing engines
engines = {
    # make analytical approximation pricing engines
    # "BaroneAdesiWhaley": ql.BaroneAdesiWhaleyEngine(bsm_process),
    # "BjerksundStensland": ql.BjerksundStenslandEngine(bsm_process),
    "JuQuadraticApprox": ql.JuQuadraticApproximationEngine(bsm_process),
    # make binomial tree pricing engines
    "BinomialCRR": ql.BinomialCRRVanillaEngine(bsm_process, steps),
    "BinomialEQP": ql.BinomialEQPVanillaEngine(bsm_process, steps),
    "BinomialJR": ql.BinomialJRVanillaEngine(bsm_process, steps),
    "BinomialLR": ql.BinomialLRVanillaEngine(bsm_process, steps),
    "BinomialTian": ql.BinomialTianVanillaEngine(bsm_process, steps),
    "BinomialTrigeorgis": ql.BinomialTrigeorgisVanillaEngine(bsm_process, steps),
    "BinomialJoshi4": ql.BinomialJ4VanillaEngine(bsm_process, steps),
    # make FDM pricing engines
    "FDM": ql.FdBlackScholesVanillaEngine(bsm_process, fdm_time_steps, fdm_state_grid_points)
}

# run calculation
results = []
for name, engine in engines.items():
    time_s = time()
    option.setPricingEngine(engine)
    calc_time = time() - time_s
    results.append((name, option.NPV(), calc_time))

# show results
df = pd.DataFrame(results, columns=["Method", "BS Option NPV", "calc time"])
print(df)
