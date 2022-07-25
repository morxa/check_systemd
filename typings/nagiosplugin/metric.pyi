"""
This type stub file was generated by pyright.
"""

import collections

"""Structured representation for data points.

This module contains the :class:`Metric` class whose instances are
passed as value objects between most of nagiosplugin's core classes.
Typically, :class:`~.resource.Resource` objects emit a list of metrics
as result of their :meth:`~.resource.Resource.probe` methods.
"""

class Metric(
    collections.namedtuple(
        "Metric", "name value uom min max context contextobj resource"
    )
):
    """Single measured value.

    The value should be expressed in terms of base units, so
    Metric('swap', 10240, 'B') is better than Metric('swap', 10, 'kiB').
    """

    def __new__(
        cls,
        name,
        value,
        uom=...,
        min=...,
        max=...,
        context=...,
        contextobj=...,
        resource=...,
    ):  # -> Self@Metric:
        """Creates new Metric instance.

        :param name: short internal identifier for the value -- appears
            also in the performance data
        :param value: data point, usually has a boolen or numeric type,
            but other types are also possible
        :param uom: :term:`unit of measure`, preferrably as ISO
            abbreviation like "s"
        :param min: minimum value or None if there is no known minimum
        :param max: maximum value or None if there is no known maximum
        :param context: name of the associated context (defaults to the
            metric's name if left out)
        :param contextobj: reference to the associated context object
            (set automatically by :class:`~nagiosplugin.check.Check`)
        :param resource: reference to the originating
            :class:`~nagiosplugin.resource.Resource` (set automatically
            by :class:`~nagiosplugin.check.Check`)
        """
        ...
    def __str__(self) -> str:
        """Same as :attr:`valueunit`."""
        ...
    def replace(self, **attr):  # -> Self@Metric:
        """Creates new instance with updated attributes."""
        ...
    @property
    def description(self):  # -> str:
        """Human-readable, detailed string representation.

        Delegates to the :class:`~.context.Context` to format the value.

        :returns: :meth:`~.context.Context.describe` output or
            :attr:`valueunit` if no context has been associated yet
        """
        ...
    @property
    def valueunit(self):  # -> str:
        """Compact string representation.

        This is just the value and the unit. If the value is a real
        number, express the value with a limited number of digits to
        improve readability.
        """
        ...
    def evaluate(self):
        """Evaluates this instance according to the context.

        :return: :class:`~nagiosplugin.result.Result` object
        :raise RuntimeError: if no context has been associated yet
        """
        ...
    def performance(self):
        """Generates performance data according to the context.

        :return: :class:`~nagiosplugin.performance.Performance` object
        :raise RuntimeError: if no context has been associated yet
        """
        ...
