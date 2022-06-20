start_num=int(input())
end_num=int(input())

num_list=[]

for num in range(start_num,end_num+1):
    cnt=0
    if num>1:
        for j in range(2,num):
            if num%j==0:
                cnt+=1
                break
        if cnt==0:
            num_list.append(num)

if len(num_list)>0:
    print(sum(num_list))
    print(min(num_list))
else:
    print(-1)
