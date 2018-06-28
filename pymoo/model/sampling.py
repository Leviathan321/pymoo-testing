from abc import abstractmethod
import numpy as np

from pymop.problem import Problem


class Sampling:
    """

    This abstract class represents any sampling strategy that can be used to create an initial population or
    an initial search point.

    """

    @abstractmethod
    def sample(self, problem, n_samples, **kwargs):
        """
        Sample new points with problem information if necessary.

        Parameters
        ----------
        problem: class
            The problem to which points should be sampled. (lower and upper bounds, discrete, binary, ...)

        n_samples: int
            Number of samples

        kwargs: class
            Any additional data that might be necessary. e.g. constants of the algorithm, ...

        Returns
        -------
        X : np.ndarray
            Samples points in a two dimensional array

        """
        pass


def sample_by_bounds(clazz, n_samples, n_var, x_min, x_max, **kwargs):
    """

    Convenience method if only the bounds are needed to create the sample points.

    Parameters
    ----------
    clazz : class
        The sampling strategy to be used.
    x_min : np.array
        lower bounds
    x_max : np.array
        upper bounds
    n_var : int
        number of variables
    n_samples : int
        number of samples
    kwargs : dict
        additional arguments

    Returns
    -------
    X : np.ndarray
        Samples points in a two dimensional array

    """

    class P(Problem):
        def __init__(self) -> None:
            self.n_var = n_var
            self.xl = np.full(n_var, x_min)
            self.xu = np.full(n_var, x_max)

    return clazz.sample(P(), n_samples, **kwargs)

