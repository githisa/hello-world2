from instrument.instrument_base import Instrument
from enums.enums import *


class SwapBase(Instrument):
    def __init__(self, instrument_name: str):
        super().__init__(instrument_name)
        self._leg_num = 2


class IRS(SwapBase):
    def __init__(self, ccy: CurrencyName, index_name: str, spread: float, fixed_rate: float):
        instrument_name = IR_INSTRUMENT_NAME_STRINGS[IRInstrumentName.IRS]
        super().__init__(instrument_name)

        self._ccy = ccy
        self._index_name = index_name
        self._spread = spread
        self._fixed_rate = fixed_rate
