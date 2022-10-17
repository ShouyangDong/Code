"""TVM Script Interface for PrimFunc"""

import inspect
from typing import Callable

from tvm.tir.function import PrimFunc
from ..parser import from_source


def prim_func(input_func: Callable) -> PrimFunc:
    """Decorate a python function as tvm script.

    Parameters
    ----------
    func : input_func
        The function to be parsed.

    Returns
    -------
    output : PrimFunc
        The result functions.
    """
    if inspect.isfunction(input_func):
        result = from_source(input_func)
        result.__name__ = input_func.__name__
        result.__qualname__ = input_func.__qualname__
        return result

    raise TypeError("Only function definitions are supported.")
