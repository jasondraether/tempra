import numpy as np
from tempra import config, units


"""
Temper object: Combines multiple axes
Axis object: Contains the data, time axis, time units. Optionally includes
t0 and/or sampling rate

"""

"""
Basic idea: People can construct "Axis" objects which show how they
want to represent time. When these are created, they can add data to
the axis objects, and we handle syncing up the axis with the data

A Temper object combines these multiple axes and makes it easy
to work with
"""

"""
Constructor:
Start with checking time axis. If provided, just make sure its a primitive
we can actually use. If t0 and tn also provided, we can truncate the axis
to only use t0/tn
If time axis not provided, use t0 and tn to generate one, inferring based on units.
raise runtime warning if they're trying to do this without specifying a sampling rate

"""

"""
Example invoke:

Let's say i have time data and another data, like stock values

axis = Axis(times, unit='minutes')
axis.attach(data)

"""


class Axis(object):
    def __init__(self, t = None, unit: str = None, t0 = None, tn = None, period = None):
        # TODO: Can I do this? Lol
        self._config = config
        # Check individual attributes
        self._check_t(t)
        self._check_unit(unit)
        self._check_period(period)
        self._check_t0(t0)
        self._check_tn(tn)
        # At this point, internal attr have been set
        self._check_attr()


    def _check_t(self, t):
        """
        Check array for time values for axis
        :param t:
        :return:
        """
        self.t = t
        raise NotImplementedError("TODO: Implement!")

    def _check_unit(self, unit):
        if unit is None:
            self.unit = units.Seconds()
            raise RuntimeWarning(f"\'unit\' argument was not passed into Axis constructor. Inferring \'{str(units.Seconds())}\' as unit.")
        if unit not in self._config.supported_units:
            raise ValueError(f"Unit {unit} not supported.\nSupported units are {self._config.supported_units}.")

    def _check_period(self, period):
        raise NotImplementedError("TODO: Implement!")

    def _check_t0(self, to):
        raise NotImplementedError("TODO: Implement!")

    def _check_tn(self, tn):
        raise NotImplementedError("TODO: Implement!")

    def _check_attr(self):
        raise NotImplementedError("TODO: Implement!")

    def attach(self, d):
        raise NotImplementedError("TODO: Implement!")

    def detach(self, key):
        raise NotImplementedError("TODO: Implement!")
