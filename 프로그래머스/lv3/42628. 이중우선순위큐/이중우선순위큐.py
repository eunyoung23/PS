import heapq

def solution(operations):
    heap=[]

    for op in operations:
        o,n=op.split()
        if o=="I":
            heapq.heappush(heap,int(n))
        else:
            if heap:
                if n=="1":
                    tmp=[]
                    while len(heap)>1:
                        tmp.append(heapq.heappop(heap))
                    heapq.heappop(heap)
                    heap=tmp
                else:
                    heapq.heappop(heap)
    if heap:
        min_value=heapq.heappop(heap)
        max_value=min_value
        while heap:
            max_value=heapq.heappop(heap)
        return [max_value,min_value]
    return [0,0]
    