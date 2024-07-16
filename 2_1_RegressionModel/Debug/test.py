# file = open('./columns copy.txt', 'r', encoding='utf-8-sig')

# data = []

# for line in file:
#     temp = f"{(line.strip())}"
#     data.append(temp)

# print(data)

test1 = [1.7,   1.1,   2.8,   4.,  256.,    0.,    0.,   15.6,  60.,   38.,    0.,    0.,               ## 12
         1.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,               ## 12
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,               ## 12
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,               ## 12
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,               ## 12
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,                   
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
         0.,    0.,    0.,    0.,    0.,    1.,    0.,    0.,    0.,    1.,    0.,    0.,
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
         0.,    0.,    1.,    0.,    0.,    0.,    0.,    0.,    0.,    1.,    0.,    0.,
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
         0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,    0.,
         1.,    0.,    0.,    0.,    0.,    0.,    0., ]

input_data = [1.7, 1.1, 2.8, 4, 256, 0, 0.0, 15.6, 60.0, 38.0, False, False, True, False,                   ## 14
              False, False, False, False, False, False, False, False, False, False, False, False,           ## 12
              False, False, False, False, False, False, False, False, False, False, False, False,           ## 12    
              False, False, False, False, False, False, False, False, False, False, False, False,           ## 12
              False, False, False, False, False, False, False, False, False, False, False, False,           ## 12
              False, False, False, False, False, False, False, False, False, False, False, False,           ## 12
              False, False, False, False, False, False, False, False, False, False, False, False,           ## 12
              False, False, False, True, False, False, False, True, False, False, False, False,             ## 12
              False, False, False, False, False, False, False, False, False, False, False, False,           ## 12
              True, False, False, False, False, False, False, True, False, False, False, False,             ## 12
              False, True, False, False, False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False, False, False, False, False,
              False, False, False, False, False, False, False, False, False, False, True, False,
              False, False, False, False, False]

# res = []

# for i in range(len(input_data)):
#     res.append(input_data[i] - test1[i])

# for i in range(len(res)):
#     if res[i] != 0:
#         print(i, res[i])

# print(res)

res = []

for i in range(15):
    res.append([0, 0, 0, 0])

count = 0
for i in range(len(input_data)):
    if input_data[i] != 0:
        # print(i, input_data[i])
        res[count][0] = i
        res[count][1] = input_data[i]
        count += 1

test1[123] = 1
print(test1)
count = 0
for i in range(len(test1)):
    if test1[i] != 0:
        # print(i, test1[i])
        res[count][2] = i
        res[count][3] = test1[i]
        count += 1

for i in range(len(res)):
    print(res[i])




