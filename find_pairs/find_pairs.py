# use a dictionary to avoid a soultion with nested for loops
# time complexity:  O(n)
# space complexity: O(n)

def find_pairs(ar):

    seen = {}
    pairs = 0

    for i in range(0, len(ar)):
        if seen.__contains__(ar[i]) == False:
            seen[ar[i]] = None # this is just a dummy value, hence None
        else:
            del seen[ar[i]]
            pairs += 1
    
    return pairs
