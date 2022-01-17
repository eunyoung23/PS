import re

def solution(new_id):
    # case1
    new_id = new_id.lower()
    
    # case2
    p = re.compile('[a-z0-9-._]+')
    result = p.findall(new_id)
    new_id = "".join(result)
    
    # case3
    while ".." in new_id:
        new_id = new_id.replace('..','.')
    
    # case4
    new_id = new_id.strip('.')
    
    # case5
    if new_id == "":
        new_id = "a"
    
    # case6
    if len(new_id)>=16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
        
    # case7
    if len(new_id)<=2:
        while len(new_id) < 3:
            new_id += new_id[len(new_id)-1:]
    
    answer = new_id
    
    return answer
