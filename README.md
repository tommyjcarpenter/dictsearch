PyPi
===========================
https://pypi.python.org/pypi/dictsearch/

Purpose
==========================
Has query and search functions for "nested dictionaries", where 
these nested structures contain dictionaries, lists, and other objects (that are treated as values). 

Motivation
===========================
This package was motivated after calling simplejson on objects
 returned from Twitter API calls. The API objects I had to parse had quadruple level nested dictionaries, but sometimes an entire inner dictionary or level would be missing. Trying to query level 4 when level 1 2 or 3 does not exist bombs with a key error instead of just returning None; nothing in the Python language natively supports querying nested dicts when they may or may not exist:
 http://stackoverflow.com/questions/26979046/python-check-multi-level-dict-key-existence

Examples
===========================
See `test_search.py` for more.

    from dictsearch.search import iterate_dictionary
    
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
    
    print(d)
    print(iterate_dictionary(d,"X/Y/Z"))
    print(iterate_dictionary(d,"A"))
    print(iterate_dictionary(d,"A/B"))
    print(iterate_dictionary(d,"A/C"))
    print(iterate_dictionary(d,"A/B/C"))
    print(iterate_dictionary(d,"A/B/C/D")) #DOES NOT EXIST; D NOT AFTER PATH "C"
    print(iterate_dictionary(d,"A/B/D/E")) 
    print(iterate_dictionary(d,"A/B/E"))   #DOES NOT EXIST; E NOT A SUBPATH OF "B"
        
    >>
    
    {'A': {'B': [{'C': 123}, {'C': 123}, {'D': {'E': 'ASDF'}}]}}
    None
    [{'B': [{'C': 123}, {'C': 123}, {'D': {'E': 'ASDF'}}]}]
    [{'C': 123}, {'C': 123}, {'D': {'E': 'ASDF'}}]
    None
    [123, 123]
    None
    ['ASDF']
    None
