from datetime import date
from typing import List
from math import exp, log
import numpy as np

from error import MyError


class YieldCurve(object):
    def __init__(self):
        self._dates = np.array([])
        self._terms = np.array([])
        self._discount_factors = np.array([])
        self._zero_rates = np.array([])

    def set_from_date_and_df(self, in_dates: List[date], in_dfs: List[float]):
        MyError.require(len(in_dates) == len(in_dfs),
                        "the lengths of dates and discount factors are mismatched.")
        self._dates = np.array(in_dates)
        self._discount_factors = np.array(in_dfs)

        today = self._dates[0]
        for i in range(len(self._dates)):
            term = (self._dates[i] - today).days / 365.0
            self._terms = np.append(self._terms, term)

            if i == 0:
                zero_rate = 0.0
            else:
                zero_rate = -log(self._discount_factors[i]) / term
            self._zero_rates = np.append(self._zero_rates, zero_rate)
