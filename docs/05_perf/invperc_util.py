"""Invasion percolation implementation utilities."""

import json
import random
import sys

from grid_lazy import GridLazy
from grid_list import GridList
from grid_array import GridArray


# [get_params]
def get_params(filename, cls):
    """Get parameters."""
    with open(filename, "r") as reader:
        d = json.load(reader)
        return cls(**d)
# [/get_params]


def initialize_grid(params):
    """Prepare grid for simulation."""
    lookup = {
        "lazy": GridLazy,
        "list": GridList,
        "array": GridArray,
    }
    assert params.kind in lookup, f"Unknown grid type {params.kind}"
    cls = lookup[params.kind]
    return cls(params.width, params.height, params.depth)


def initialize_random(params):
    """Initialize random number generation."""
    if params.seed is None:
        params.random.randrange(sys.maxsize)
    random.seed(params.seed)
