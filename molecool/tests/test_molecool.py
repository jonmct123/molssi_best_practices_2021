"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import numpy as np
import pytest
import sys

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules


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

def test_build_bond_list():
    coord = np.array([[1,1,1],[2.4,1,1],[-0.4,1,1],[1,1,2.4],[1,1,-0.4]])
    bonds = molecool.build_bond_list(coord)
    assert len(bonds) == 4
    for bond_length in bonds.values():
        assert bond_length == 1.4
    
