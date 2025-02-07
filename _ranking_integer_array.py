#this program takes an array or list of scores and return an array of ranks corresponding to each score.

def rank_array(arr):
    sorted_arr = sorted(set(arr), reverse = True)
   
    rank_dict = {val: rank + 1 for rank, val in enumerate(sorted_arr)}
    return [rank_dict[val] for val in arr]
   
print(rank_array([9, 3,6, 10]))
print(rank_array([3, 3, 3, 1]))
