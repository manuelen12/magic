from class_magic import Magic


def test_magic_example():
    _example = [
        "1", "2", "abracadabra", "4", "alakazam", "abracadabra", "7", "8", "abracadabra", "alakazam", "11",
        "abracadabra", "13", "14", "abracadabraalakazam", "16", "17", "abracadabra", "19", "alakazam"]

    magic = Magic(20)
    result = magic.get_value()
    assert _example == result
