from homeWork3 import *
import pytest

def test_initialize_dictionary():
    d = initialize_dictionary()
    assert d!=None


@pytest.fixture()
def data_test():
    data_set =initialize_dictionary()
    yield data_set

def test_male_female(data_test):
    male,female=split_male_female(data_test)
    bo_male=True
    bo_female=True
    for id in male:
        if male[id]["sex"] != "male":
            bo_male=False
    for id in female:
        if female[id]["sex"] != "female":
            bo_female = False
    assert bo_male,bo_female


def test_find_maed_average(data_test):
    Average, Median=find_maedian_average(data_test)
    assert type(Average)==float,type(Median)==float

def test_values_above(data_test):
    assert print_values_above(data_test)

def test_format_values(data_test):
    bo_format=True
    for id in data_test:
        text_test = ""
        for k, v in data_test[id].items():
            text_test += f"{k}: {v} "
        if text_test!=format_values(data_test[id]):
            bo_format=False
    assert bo_format
