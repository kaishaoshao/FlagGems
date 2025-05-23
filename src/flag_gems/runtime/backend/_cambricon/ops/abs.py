import logging

import triton
import triton.language as tl

from ..utils.pointwise_dynamic import pointwise_dynamic


@pointwise_dynamic(promotion_methods=[(0, "COMPLEX_TO_FLOAT")])
@triton.jit
def abs_func(x):
    return tl.abs(x)


def abs(A):
    logging.debug("GEMS_CAMBRICON ABS")
    return abs_func(A)
