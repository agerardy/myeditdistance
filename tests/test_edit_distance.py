import myeditdistance as ed

# tests: two strings two integers, int and string?


def test_edit_distance():
    assert ed.edit_distance("kitten", "sitting") == 3
