# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.temperature.kang2002` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest
from itertools import permutations

from colour.temperature import CCT_to_xy_Kang2002
from colour.utilities import ignore_numpy_errors

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2019 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['TestCCT_to_xy_Kang2002']


class TestCCT_to_xy_Kang2002(unittest.TestCase):
    """
    Defines :func:`colour.temperature.kang2002.CCT_to_xy_Kang2002` definition
    units tests methods.
    """

    def test_CCT_to_xy_Kang2002(self):
        """
        Tests :func:`colour.temperature.kang2002.CCT_to_xy_Kang2002`
        definition.
        """

        np.testing.assert_almost_equal(
            CCT_to_xy_Kang2002(4000),
            np.array([0.380528282812500, 0.376733530961114]),
            decimal=7)

        np.testing.assert_almost_equal(
            CCT_to_xy_Kang2002(7000),
            np.array([0.306374019533528, 0.316552869726577]),
            decimal=7)

        np.testing.assert_almost_equal(
            CCT_to_xy_Kang2002(25000),
            np.array([0.25247299, 0.252254791243654]),
            decimal=7)

    def test_n_dimensional_CCT_to_xy_Kang2002(self):
        """
        Tests :func:`colour.temperature.kang2002.CCT_to_xy_Kang2002` definition
        n-dimensional arrays support.
        """

        CCT = 4000
        xy = CCT_to_xy_Kang2002(CCT)

        CCT = np.tile(CCT, 6)
        xy = np.tile(xy, (6, 1))
        np.testing.assert_almost_equal(CCT_to_xy_Kang2002(CCT), xy, decimal=7)

        CCT = np.reshape(CCT, (2, 3))
        xy = np.reshape(xy, (2, 3, 2))
        np.testing.assert_almost_equal(CCT_to_xy_Kang2002(CCT), xy, decimal=7)

    @ignore_numpy_errors
    def test_nan_CCT_to_xy_Kang2002(self):
        """
        Tests :func:`colour.temperature.kang2002.CCT_to_xy_Kang2002` definition
        nan support.
        """

        cases = [-1.0, 0.0, 1.0, -np.inf, np.inf, np.nan]
        cases = set(permutations(cases * 3, r=2))
        for case in cases:
            CCT_to_xy_Kang2002(case)


if __name__ == '__main__':
    unittest.main()