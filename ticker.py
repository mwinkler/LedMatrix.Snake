import supervisor

_TICKS_PERIOD = 1<<29
_TICKS_MAX = _TICKS_PERIOD-1
_TICKS_HALFPERIOD = _TICKS_PERIOD//2

def ticks_diff(ticks1, ticks2):
    "Compute the signed difference between two ticks values, assuming that they are within 2**28 ticks"
    diff = (ticks1 - ticks2) & _TICKS_MAX
    diff = ((diff + _TICKS_HALFPERIOD) & _TICKS_MAX) - _TICKS_HALFPERIOD
    return diff

class Ticker():

    def __init__(self):
        self.reset()

    def reset(self):
        self.timestamp = supervisor.ticks_ms()

    def elapsed(self):
        return ticks_diff(supervisor.ticks_ms(), self.timestamp)