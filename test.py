# a, b ll head 
# outpu first intersection 

#a -> value, ->next (a==b)
def find_intersection(a,b):
    n = 0
    m = 0
    a_node = a
    while a_node:
        n += 1
        a_node = a_node.next
    b_node = b
    while b_node:
        m+=1
        b_node = b_node.next

    diff = n-m
    cur_a = a
    cur_b = b
    while diff >0:
        cur_a = cur_a.next
        diff -= 1
    
    while cur_a:
        if cur_a == cur_b:
            return cur_a
        cur_a = cur_a.next
        cur_b = cur_b.next
        
    return None