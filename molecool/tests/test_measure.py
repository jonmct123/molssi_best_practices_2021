"""

Tests for measure module.

"""
import numpy as np
import molecool
import pytest

def test_calculate_distance():
    """
    Testing that calculate_distance performs as expected.
    """

    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])
    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1,r2)

    assert expected_distance == calculated_distance


def test_calculate_angle():
    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])
    expected = 90
    calc = molecool.calculate_angle(r1,r2,r3, degrees=True)
    assert calc == expected


def test_calc_angle():
    r1 = np.array([0,0,-1])
    r2 = np.array([0,1,0])
    r3 = np.array([1,0,0])
    expected = 60
    calc = molecool.calculate_angle(r1,r2,r3, degrees=True)
    assert pytest.approx(expected) == calc

@pytest.mark.parametrize("r1,r2,r3,angle",[
    (np.array([0,0,-1]),np.array([0,0,0]),np.array([1,0,0]),90),
    (np.array([0,0,-1]),np.array([0,1,0]),np.array([1,0,0]), 60),
])
def test_calc_angle_many(r1,r2,r3, angle):
    calculated_angle = molecool.calculate_angle(r1,r2,r3, degrees=True)

    assert pytest.approx(calculated_angle) == angle