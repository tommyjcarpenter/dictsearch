from dictsearch.search import iterate_dictionary

A = dict()
A["A"] = []
A["A"].append("1")
A["A"].append(dict())
A["A"][1]["B"] = 123
A["A"].append("1")
A["A"].append(dict())
A["A"][3]["B"] = 123
print(iterate_dictionary(A, "A/B"))

