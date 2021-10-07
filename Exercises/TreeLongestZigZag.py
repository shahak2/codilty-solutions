class Tree(object):
  x = 0
  l = None
  r = None

def solution(T):
    max_count = 0
    stack = []
    if T.l != None:
        stack.append((T.l,0,'l'))
    if T.r != None:
        stack.append((T.r,0,'r'))
    while stack != []:
        node, curr_count, direction = stack.pop()
        if node.l != None:
            if direction == "r":
                max_count = max(max_count,curr_count + 1)
                stack.append((node.l,curr_count+1,'l'))
            else:
                stack.append((node.l,curr_count,'l'))
                max_count = max(max_count,curr_count)

        if node.r != None:
            if direction == "l":
                max_count = max(max_count,curr_count + 1)
                stack.append((node.r,curr_count + 1,'r'))
            else:
                stack.append((node.r,curr_count,'r'))
                max_count = max(max_count,curr_count)
    return(max_count)

def test():
    t = Tree()
    t1 = Tree()
    t2 = Tree()
    t3 = Tree()
    t.l = t1
    t.r = t2
    t2.l = t3
    print(solution(t))

test()
        
        
        
        
