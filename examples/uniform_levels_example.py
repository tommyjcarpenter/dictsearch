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


