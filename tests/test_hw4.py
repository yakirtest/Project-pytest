from homeWork4 import *
import pytest


def test_Date__init__():
    d=Date(20,1,1999)
    assert type(d) == Date


def test_Date__isValid__(day1):
    assert day1.__isValid__()

@pytest.fixture()
def day1():
    day1 =Date(20,1,1999)
    yield day1

@pytest.fixture()
def day2():
    day2 =Date(20,11,1998)
    yield day2

def test_Date__str__(day1):
    day_str=f"{day1._day}/{day1._month}/{day1._year}"
    day_test=day1.__str__()
    assert day_str==day_test


def test_Date_leap_year():
    assert Date.leap_year(1992)


def test_Date_getnextday(day1):
    assert day1 < day1.getnextday()


def test_Date_getNextDays(day1):
    assert day1 < day1.getnextday()
def test_Date__days__(day1):
    assert day1.__days__()>0

def test_Date__eq__(day1):
    assert day1.__eq__(day1)

def test_Date__gt__(day1,day2):
    assert day2.__gt__(day1)

def test_Date__lt__(day1,day2):
    assert day1.__lt__(day2)

def test_Date__ge__(day1,day2):
    assert day2.__ge__(day1)

def test_Date__le__(day1,day2):
    assert day1.__le__(day2)

def test_Date__days__(day1):
    assert day1.__days__()>0

def test_Date__sub__(day1,day2):
    assert day1.__sub__(day2)>=0

