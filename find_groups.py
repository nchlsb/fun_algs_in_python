# use a dictionary to avoid a soultion with nested for loops
# time complexity:  O(n)
# space complexity: O(n)

def find_groups(arr, group_size):

    seen = {}
    groups = 0

    for i in range(0, len(arr)):         
        if seen.__contains__(arr[i]) == False:
            """
            You wouldn't need a more complicated method to find groups of
                size 1, but this hadnles it just in case
            """           
            if group_size != 1:
                seen[arr[i]] = 1
            else:
                groups += 1
            
        elif seen[arr[i]] + 1 >= group_size:
            del seen[arr[i]]
            groups += 1                               
            
        else:
            seen[arr[i]] += 1
            
    return groups
