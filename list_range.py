nums = list(range(5,0,-1))
print(nums)
nums[2]=100
#range本身裡面其實沒有定義中括號
print(nums)

a=[1,2,3]
total=0
for el in a:
    total+=el
#sum 可以做list的運算
total2=sum(a)
print(total,total2)

strA = "Stone"
strA = list(strA)
#轉成list
strA[0]="Y"
print(strA)
print(','.join(strA))
#將list裡的東西用特定符號連接成string

