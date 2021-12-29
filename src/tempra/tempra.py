"""
Temper object: Combines multiple axes
Axis object: Contains the data, time axis, time units. Optionally includes
t0 and/or sampling rate

"""

class Temper(object):
    def __init__(self, axis, unit):

        self._axes = []

        self.core_unit = unit

    def add(self, axis, unit):
        pass

    def window(self, rate, unit, stride):
        pass

    def offset(self, rate, unit):
        pass

    def _unify(self):
        """
        Attempt to combine data to be 1:1
        :return:
        """
        pass

    def upsample(self):
        pass

    def downsample(self):
        pass

    def _check_compat_unit(self, unit):
        pass

