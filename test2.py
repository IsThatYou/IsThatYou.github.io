# m = [1,2,3..] pos, differnet
# output [1,2,3], [1,3,2],..

def recur(cur_list,m):
    if len(m) ==1:
        temp = cur_list.append(m)
        return [temp]
    all_lists = []
    for i in m:
        temp = cur_list.append(i)
        next_m = m.remove(i)
        sublists = recur(temp,next_m)
        all_lists = all_lists + sublists

    return all_lists

