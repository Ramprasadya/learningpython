dic = {
    2 : "Ramprasad",
    3 : "Rohan"
}

print(dic)
# print(dic[2])
# print(dic.get(3))

# print(dic.keys())

# for key in dic.keys():
#     print(dic[key])

for key,value in dic.items():
    print(f"The key is  {key} and the value is  {value} ")


# Dictionary methods

ep1 = {12:3 ,113 : 34 , 344 : 69}

ep2 = {190 : 345 , 560 : 1838}

# ep1.update(ep2)
ep1.clear()



print(ep1)