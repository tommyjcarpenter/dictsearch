def iterate_dictionary(d, path, squash_single = False):
    """
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
    """
    path_parts = path.split("/")
    return_list = []
    
    if len(path_parts) == 0: #no search string
        return d
    else:
        try:
            sub_dicts = [d] #BFS, start with root node
            for i in range(0, len(path_parts)): #BFS
                new_sub_dicts = []    
                for s in sub_dicts:
                    if path_parts[i] in s: #this tree node is part of the search path
                        the_list = s[path_parts[i]] if isinstance(s[path_parts[i]], list) else [s[path_parts[i]]]
                        for j in the_list: 
                            if i < len(path_parts) -1: #not a leaf node; check level
                                if isinstance(j, dict): #skip this non-leaf node if not a dict
                                    new_sub_dicts.append(j) #BFS expansion
                            else: #leaf node at the desired path; add to final return list
                                return_list.append(j)
                sub_dicts = new_sub_dicts
            
            #return 
            return return_list[0] if squash_single and len(return_list) == 1 else return_list if len(return_list) >= 1 else None
        except:
            return None

def get_all_values(d):
    """
    This function returns a list of all values in a nested dictionary. 
    By nested, this means each item X in d can either be a dict, a list, or a "value".
    Other iterables other than dicts and lists are treated as values and are not iterated currently.

    Returns a list, or None if there are no values found (for example a nested structure of all 
    empty dicts)
    """
    if not isinstance(d,dict):
        raise ValueError("input is not a dictionary")
    return _get_all_values(d)
def _get_all_values(d):
    vals = []
    if isinstance(d, dict):
        for k, v in d.iteritems():
            vals += _get_all_values(v)
    elif isinstance(d, list):
        for l in d:
            vals += _get_all_values(l) 
    else:
        vals.append(d)
    return vals

