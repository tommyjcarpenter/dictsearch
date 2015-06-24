def iterate_dictionary(d, path, squash_single = False):
    """see readme.txt
       
       if squash_single is true, if there is only one item in the final list
       that would be returned, only the item, instead of a list with one item, is returned

       If anything fails, for example an inner dictionary is not found, 
       or there are no objects at the path, returns None
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
