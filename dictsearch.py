def iterate_dictionary(d, path, squash_single = False):
    """see readme.txt
       
       if squash_single is true, if there is only one item in the final list
       that would be returned, only the item, instead of a list with one item, is returned

       If anything fails, for example an inner dictionary is not found, 
       or there are no objects at the path, returns None
    """
    path_parts = path.split("/")
    return_list = []
    
    if len(path_parts) == 0:
        return d
    else:
        try:
            sub_dicts = [d]
            for i in range(0, len(path_parts)):
                new_sub_dicts = []    
                for s in sub_dicts:
                    if path_parts[i] in s:
                        the_list = [] #path_parts[i] could be a list that contains dicts or just a dict
                        if isinstance(s[path_parts[i]], list):
                            the_list = s[path_parts[i]]
                        else:
                            the_list.append(s[path_parts[i]]) #the_list is just a list of one element now
                        for j in the_list:
                            if i < len(path_parts) -1: #not a leaf node
                                if isinstance(j, dict): #skip this non-leaf node if not a dict
                                    new_sub_dicts.append(j)
                            else: #leaf node
                                return_list.append(j)
                sub_dicts = new_sub_dicts
            
            #return 
            if squash_single and len(return_list) == 1:
                return return_list[0]
            else:
                return return_list if len(return_list) >= 1 else None
        except:
            return None
