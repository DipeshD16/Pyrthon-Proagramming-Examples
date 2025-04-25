def is_upside_down_same(n):
    flip_map = {'0': '0', '1':'1', '6':'9', '8':'8', '9':'6'}
    s = str(n)
   
    try:
        flipped = ''.join(flip_map[c] for c in reversed(s))
        return flipped == s
   
    except KeyError:
        return False
       
results = [n for n in range(1, 100001) if is_upside_down_same(n)]

print("Numbers that look upside down same")
print(results)