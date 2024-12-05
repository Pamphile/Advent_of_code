import re
import numpy as np
with open('order2.txt') as f:
    orders = list()
    for line in f:
        line = line.replace('\n', '')
        numbers = line.split('|')
        numbers  = [int(x) for x in numbers ]
        orders.append(numbers)

with open('request2.txt') as f:
    requests = list()
    for line in f:
        line = line.replace('\n', '')
        line = re.findall('\d+', line)
        line  = [int(x) for x in line ]
        requests.append(line)


def iscorrect(request, orders):
    valid = True
    for itemId, requestItem in enumerate(request):
        for order in orders:
            # print(request)
            # print(order)
            if requestItem == order[0]:

                # print(f"{requestItem} == {order[0]}")
                for idCheck in range(0, itemId):
                    # print(request[idCheck])
                    if order[1] == request[idCheck]:
                        return False
                    # print("Invalid")

            # print(" ")
    return valid

results = list()
sums = 0
for request in requests:
    if iscorrect(request, orders):
        sums +=request[int((len(request) - 1)/2)]

print(sums)

def reordered(request, orders):
    valid = True
    for itemId, requestItem in enumerate(request):
        for order in orders:
            # print(request)
            # print(order)
            if requestItem == order[0]:

                # print(f"{requestItem} == {order[0]}")
                for idCheck in range(0, itemId):
                    # print(request[idCheck])
                    if order[1] == request[idCheck]:
                        request[idCheck] = requestItem
                        request[itemId] = order[1]
                        return request
                    # print("Invalid")

results = list()
sums = 0
for request in requests:
    if iscorrect(request, orders) == False:
        temp = reordered(request, orders)
        while iscorrect(temp, orders) == False:
            temp = reordered(request, orders)
        print(temp)
        sums +=temp[int((len(temp) - 1)/2)]

print(sums)