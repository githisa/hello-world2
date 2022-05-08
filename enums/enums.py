from enum import IntEnum, auto


class AssetClass(IntEnum):
    IR = auto()
    FX = auto()
    EQ = auto()
    CR = auto()


class IRInstrumentName(IntEnum):
    IRS = auto()
    XCCY = auto()
    CapFloor = auto()
    Swaption = auto()


IR_INSTRUMENT_NAME_STRINGS = {IRInstrumentName.IRS: "IRS",
                              IRInstrumentName.XCCY: "XCCY",
                              IRInstrumentName.CapFloor: "CapFloor",
                              IRInstrumentName.Swaption: "Swaption", }


class FXInstrumentName(IntEnum):
    FXForward = auto()
    FXCallPut = auto()


FX_INSTRUMENT_NAME_STRINGS = {FXInstrumentName.FXForward: "FXForward",
                              FXInstrumentName.FXCallPut: "FXCallPut", }


class EQInstrumentName(IntEnum):
    EQForward = auto()
    EQSwap = auto()
    EQCallPut = auto()


EQ_INSTRUMENT_NAME_STRINGS = {EQInstrumentName.EQForward: "EQForward",
                              EQInstrumentName.EQSwap: "EQSwap",
                              EQInstrumentName.EQCallPut: "EQCallPut", }


class CRInstrumentName(IntEnum):
    PlainBond = auto()
    CDS = auto()
    ReverseDualBond = auto()


CR_INSTRUMENT_NAME_STRINGS = {CRInstrumentName.PlainBond: "PlainBond",
                              CRInstrumentName.CDS: "CDS",
                              CRInstrumentName.ReverseDualBond: "ReverseDualBond", }


class CurrencyName(IntEnum):
    JPY = auto()
    USD = auto()
    EUR = auto()
    GBP = auto()
    AUD = auto()


CCY_CODES = {CurrencyName.JPY: "JPY",
             CurrencyName.USD: "USD",
             CurrencyName.EUR: "EUR",
             CurrencyName.GBP: "GBP",
             CurrencyName.AUD: "AUD", }
