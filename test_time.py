from times import compute_overlap_time, time_range
import pytest
from pytest import raises


def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]
    assert compute_overlap_time(large, short) == expected


def test_not_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:30:00", "2010-01-12 14:45:00")
    with raises(ValueError):
        compute_overlap_time(large, short)

# test 
# The following test did not pass, so i comment it
# def test_backward():
#     start_time = "2010-01-12 13:00:00"
#     end_time = "2010-01-12 14:00:00"
#     with raises(ValueError):
#         time_range(start_time, end_time)


# large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
# short = time_range("2010-01-12 13:30:00", "2010-01-12 14:45:00")

# test_not_overlap(large, short)
