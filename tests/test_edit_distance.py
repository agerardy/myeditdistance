import pytest

import myeditdistance as ed

# tests: two strings two integers, int and string?
# empty stirng, length , edge cases


def test_edit_distance():
    assert ed.edit_distance("kitten", "sitting") == 3


def test_int_edit_distance():
    with pytest.raises(TypeError):
        ed.edit_distance(3, "sitting")
