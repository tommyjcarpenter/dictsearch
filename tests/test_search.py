import pytest
from dictsearch.search import iterate_dictionary, get_all_values


def test_empty():
    d = {}
    d[1] = "foo"
    assert iterate_dictionary(d, "") == d


def test_nodict():
    with pytest.raises(ValueError):
        get_all_values([])


def test_get():
    d = dict()
    d["1"] = []
    d["1"].append({})
    d["1"][0]["foo"] = "bar"
    assert get_all_values(d) == ["bar"]


def test_iterate_1():
    A = dict()
    A["A"] = []
    A["A"].append("1")
    A["A"].append(dict())
    A["A"][1]["B"] = 123
    A["A"].append("1")
    A["A"].append(dict())
    A["A"][3]["B"] = 456
    assert iterate_dictionary(A, "A/B") == [123, 456]


def test_iterate_2():
    d = dict()
    d["A"] = dict()
    d["A"]["B"] = []
    d["A"]["B"].append(dict())
    d["A"]["B"][0]["C"] = 123
    d["A"]["B"].append(dict())
    d["A"]["B"][1]["C"] = 123
    d["A"]["B"].append(dict())
    d["A"]["B"][2]["D"] = dict()
    d["A"]["B"][2]["D"]["E"] = "ASDF"

    assert d == {"A": {"B": [{"C": 123}, {"C": 123}, {"D": {"E": "ASDF"}}]}}
    assert iterate_dictionary(d, "X/Y/Z") is None
    assert iterate_dictionary(d, "A") == [{"B": [{"C": 123}, {"C": 123}, {"D": {"E": "ASDF"}}]}]
    assert iterate_dictionary(d, "A/B") == [{"C": 123}, {"C": 123}, {"D": {"E": "ASDF"}}]
    assert iterate_dictionary(d, "A/C") is None
    assert iterate_dictionary(d, "A/B/C") == [123, 123]
    assert iterate_dictionary(d, "A/B/C/D") is None  # DOES NOT EXIST; D NOT AFTER PATH "C"
    assert iterate_dictionary(d, "A/B/D/E") == ["ASDF"]
    assert iterate_dictionary(d, "A/B/E") is None  # DOES NOT EXIST; E NOT A SUBPATH OF "B"
