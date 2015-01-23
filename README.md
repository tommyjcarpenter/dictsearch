PyPi
===========================
https://pypi.python.org/pypi/dictsearch/1.2

Usage
===========================

Takes a dict, and a path delimited with slashes like A/B/C/D, and returns a list of all leaves at all trajectories dict[A][B][C][D]
    
If the path is an empty string, returns the original dict

Each non-leaf node can be either a dictionary or list of objects including dictionaries. 

Each leaf node can be an arbitrary object. 

Non-leaf inner nodes that are not dictionaries are ignored. 


Motivation
===========================

TLDR; jsons sometimes have many levels and are a pain to parse. 

This package was motivated whencalling simplejson on objects
 returned from Twitter API calls. The API objects I had to parse had quadruple level nested dictionaries,
 and when I was playing around with the data, I wanted to be able to query different levels to see if the data was interesting.
 The problem was that sometimes an entire inner dictionary or level would be missing, instead of
 None.Then I found out nothing in the Python language natively supports querying nested dicts when they may or may not exist:
 http://stackoverflow.com/questions/26979046/python-check-multi-level-dict-key-existence


Examples
===========================


EXAMPLE 1 (all levels are dicts or list of dicts)

    import dictsearch
    
    
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
    print( dictsearch.iterate_dictionary(d,"X/Y/Z"))
    print( dictsearch.iterate_dictionary(d,"A"))
    print( dictsearch.iterate_dictionary(d,"A/B"))
    print( dictsearch.iterate_dictionary(d,"A/C"))
    print( dictsearch.iterate_dictionary(d,"A/B/C"))
    print( dictsearch.iterate_dictionary(d,"A/B/C/D")) #DOES NOT EXIST; D NOT AFTER PATH "C"
    print( dictsearch.iterate_dictionary(d,"A/B/D/E")) 
    print( dictsearch.iterate_dictionary(d,"A/B/E"))   #DOES NOT EXIST; E NOT A SUBPATH OF "B"
    
    >>
    
    {'A': {'B': [{'C': 123}, {'C': 123}, {'D': {'E': 'ASDF'}}]}}
    []
    [{'B': [{'C': 123}, {'C': 123}, {'D': {'E': 'ASDF'}}]}]
    [{'C': 123}, {'C': 123}, {'D': {'E': 'ASDF'}}]
    []
    [123, 123]
    []
    ['ASDF']
    []
    

EXAMPLE 2 (mixed levels)

    A = dict()
    A["A"] = []
    A["A"].append("1")
    A["A"].append(dict())
    A["A"][1]["B"] = 123
    A["A"].append("1")
    A["A"].append(dict())
    A["A"][3]["B"] = 123
    print(iterate_dictionary(A, "A/B"))
    
    >>
    
    [123, 123]
