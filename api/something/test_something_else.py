import api.something.something as something


def test_something():
    thing = something.Something()
    assert thing.do_something(-4) == -4
