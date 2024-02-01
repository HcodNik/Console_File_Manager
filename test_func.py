from file_manager.menu_mod import sim_multi


def test_sim_multi():
    assert sim_multi('=', 10) == '=========='



if __name__ == '__main__':
    test_sim_multi()

