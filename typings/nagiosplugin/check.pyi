"""
This type stub file was generated by pyright.
"""

"""Controller logic for check execution.

This module contains the :class:`Check` class which orchestrates the
the various stages of check execution. Interfacing with the
outside system is done via a separate :class:`Runtime` object.

When a check is called (using :meth:`Check.main` or
:meth:`Check.__call__`), it probes all resources and evaluates the
returned metrics to results and performance data. A typical usage
pattern would be to populate a check with domain objects and then
delegate control to it.
"""
_log = ...

class Check:
    def __init__(self, *objects) -> None:
        """Creates and configures a check.

        Specialized *objects* representing resources, contexts,
        summary, or results are passed to the the :meth:`add` method.
        Alternatively, objects can be added later manually.
        """
        ...
    def add(self, *objects):  # -> Self@Check:
        """Adds domain objects to a check.

        :param objects: one or more objects that are descendants from
            :class:`~nagiosplugin.resource.Resource`,
            :class:`~nagiosplugin.context.Context`,
            :class:`~nagiosplugin.summary.Summary`, or
            :class:`~nagiosplugin.result.Results`.
        """
        ...
    def __call__(self):  # -> None:
        """Actually run the check.

        After a check has been called, the :attr:`results` and
        :attr:`perfdata` attributes are populated with the outcomes. In
        most cases, you should not use __call__ directly but invoke
        :meth:`main`, which delegates check execution to the
        :class:`Runtime` environment.
        """
        ...
    def main(self, verbose=..., timeout=...):
        """All-in-one control delegation to the runtime environment.

        Get a :class:`~nagiosplugin.runtime.Runtime` instance and
        perform all phases: run the check (via :meth:`__call__`), print
        results and exit the program with an appropriate status code.

        :param verbose: output verbosity level between 0 and 3
        :param timeout: abort check execution with a :exc:`Timeout`
            exception after so many seconds (use 0 for no timeout)
        """
        ...
    @property
    def state(self):  # -> Type[Unknown]:
        """Overall check state.

        The most significant (=worst) state seen in :attr:`results` to
        far. :obj:`~nagiosplugin.state.Unknown` if no results have been
        collected yet. Corresponds with :attr:`exitcode`. Read-only
        property.
        """
        ...
    @property
    def summary_str(self):  # -> str:
        """Status line summary string.

        The first line of output that summarizes that situation as
        perceived by the check. The string is usually queried from a
        :class:`Summary` object. Read-only property.
        """
        ...
    @property
    def verbose_str(self):  # -> list[Unknown] | Literal['']:
        """Additional lines of output.

        Long text output if check runs in verbose mode. Also queried
        from :class:`~nagiosplugin.summary.Summary`. Read-only property.
        """
        ...
    @property
    def exitcode(self):  # -> int:
        """Overall check exit code according to the Nagios API.

        Corresponds with :attr:`state`. Read-only property.
        """
        ...
