PyPi
===========================
https://pypi.python.org/pypi/dictsearch/2.0

Usage
===========================
Takes a dict, and a path delimited with slashes like A/B/C/D, and returns a list of objects found at all leaf nodes at all trajectories `dict[A][B][C][D]`. It does this using BFS not DFS. 
    
The word "leaf" hereby refers to an item at the search path level. That is, upon calling the function 

    iterate_dictionary(d_to_search, "A/B/C/D")

If `d_to_search` has five levels A/B/C/D/E, then D is the "leaf node level". Since `[E]` exists, then at least one object in the return list will be a dictionary. 

Rules
===========================
Each node can be either 
1) an arbitrary non-list, non-dictionary object
2) a dictionary
3) a list of arbitrary objects

All nodes of type 3 at each level are searched for nodes of type 1 and 2. Nodes of type 2 are the ones iterated in this tree search. 

At the current time, nodes of type 1 are *not* inspected. They are returned in a list if they are at the search path and ignored otherwise. 

Returns
===========================
1) If the path is an empty string, returns the original dict

2) *If* at least one object exists at the search path, it returns a list of all items at the search path. Using the above example terminology, a list of all objects at all trajectories `"A/B/C/D"`. 

*Special Parameter*: If the optional Boolean parameter `squash_single` is True, and the return list contains only one object, the object is returned (*not* a list), else a list with that one object is returned. This optional flag is useful so that [0] does not have to be indexed on the return list in the case where only one item is expected. 

3) None in the case that there are no objects at the search path. 

Motivation
===========================

TLDR; jsons sometimes have many levels and are a pain to parse. 

This package was motivated after calling simplejson on objects
 returned from Twitter API calls. The API objects I had to parse had quadruple level nested dictionaries, but sometimes an entire inner dictionary or level would be missing. Trying to query level 4 when level 1 2 or 3 does not exist bombs with a key error instead of just returning None; nothing in the Python language natively supports querying nested dicts when they may or may not exist:
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
    None
    [{'B': [{'C': 123}, {'C': 123}, {'D': {'E': 'ASDF'}}]}]
    [{'C': 123}, {'C': 123}, {'D': {'E': 'ASDF'}}]
    None
    [123, 123]
    None
    ['ASDF']
    None
    

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
