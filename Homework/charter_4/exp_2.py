from random import choice
nums=list(range(65,90))
nums2=list()
for num in nums:
    nums2.append(chr(num))

nums=list(range(97,122))
for num in nums:
    nums2.append(chr(num))

for co in list(range(10)):
    nums2.append(str(co))
for j in list(range(1,11)):
    mima=""
    for i in list(range(8)):
        mima+=choice(nums2)
    print(f"第{j}个密码为：{mima}")