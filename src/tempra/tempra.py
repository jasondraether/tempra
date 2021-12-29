"""
Temper object: Combines multiple axes
Axis object: Contains the data, time axis, time units. Optionally includes
t0 and/or sampling rate

"""


class Tempra(object):
    def __init__(self, axis, unit=None):

        self.axes = []
        self.base_unit = unit

    def add(self, axis, unit):
        pass

    def window(self, size, stride, unit=None):
        if unit is None:
            unit = self.base_unit

    def offset(self, size, unit=None):
        if unit is None:
            unit = self.base_unit

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

