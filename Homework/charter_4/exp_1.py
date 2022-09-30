nums=list()
print("Enter 6 numbers")
for x in range(6):
    num=int(input("Please enter the num: "))
    nums.append(num)
ji=ou=0
for num in nums:
    if num%2==0:
        ou+=num
    else:
        ji+=num
print(f"奇数的和：{ji}")
print(f"偶数的和：{ou}")