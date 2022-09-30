dict={
    "one":1,
    "two":2,
    "three":3,
}
print("All keys:")
for key in dict.keys():
    print(key)
print('\n')
print(f"All values:")
for value in dict.values():
    print(value)
print('\n')
print("Add four:")
dict['four']=4
for key,value in dict.items():
    print(f"The key is {key},the value is {value}")
print('\n')
del(dict["one"])
print(f"After deleting the one:")
for key,value in dict.items():
    print(f"The key is {key},the value is {value}")
