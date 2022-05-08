# base instrument class
class Instrument(object):
    def __init__(self, instrument_name: str):
        self._instrument_name = instrument_name
        self._leg_num = 0
