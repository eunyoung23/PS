#나머지 분배 법칙을 알아야 함.
import sys

A,B,C=map(int,sys.stdin.readline().split())
result=1

def multi(a,n):
    if n==1:
        return a%C
    else:
        tmp=multi(a,n//2)
        if n%2==0:
            return (tmp*tmp)%C
        else:
            return (tmp*tmp*a)%C

print(multi(A,B))
