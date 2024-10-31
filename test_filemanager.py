import pytest
from function import sim_multi


@pytest.mark.parametrize("sim, val, res", [('=', 5, '====='),
                                       (0, 5, 0),
                                       (2, 5, 10),
                                       ('Max', 3, 'MaxMaxMax'),
                                       ('',5,'')])
def test_sim_multi(sim, val, res):
    assert sim_multi(sim, val) == res

def test_sim_multi_TypeError():
    with pytest.raises(TypeError):
        sim_multi(None, 3)
        sim_multi('Max', 'Max')


