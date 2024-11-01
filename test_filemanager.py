import pytest
from function import *
from victory import data_string_in_data_word



@pytest.mark.parametrize("sim, val, res", [('=', 5, '====='),
                                           (0, 5, 0),
                                           (2, 5, 10),
                                           ('Max', 3, 'MaxMaxMax'),
                                           ('', 5, '')])
def test_sim_multi(sim, val, res):
    assert sim_multi(sim, val) == res


def test_sim_multi_TypeError():
    with pytest.raises(TypeError):
        sim_multi(None, 3)
        sim_multi('Max', 'Max')


@pytest.mark.parametrize("data_string, res", [('10.10.1966', 'десятое октября 1966'),
                                              ('11.11.1955', 'одиннадцатое ноября 1955'),
                                              ('01.12.2000', 'первое декабря 2000'),
                                              ('111', 0),
                                              ('dasfasgsadg242525', 0),
                                              (555, 0),
                                              (None, 0)])
def test_data_string_in_data_word(data_string, res):
    assert data_string_in_data_word(data_string) == res


@pytest.mark.parametrize("total, correct, res", [(1000, 100, 10),
                                                 (100, 50, 50),
                                                 (2, 1, 50)])
def test_calc_the_percentage(total, correct, res):
    assert calc_the_percentage(total, correct) == res


def test_calc_the_percentage_TypeError():
    with pytest.raises(TypeError):
        calc_the_percentage(None, None)
        calc_the_percentage(100, None)
        calc_the_percentage('str', 100)
        calc_the_percentage(0, 100)
        calc_the_percentage(-1, 100)

