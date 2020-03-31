from collections import Counter
sum=0
NoOfShoes = int(input())
ShoeSizes = []
ShoeSize = input()
ShoeSizes = ShoeSize.split()
ShoeSizes = [int(i) for i in ShoeSizes]
NoOfCustomers = int(input())
Queries = []
adding = []
for i in range(0,NoOfCustomers):
    Query = input()
    adding = Query.split()
    adding = [int(j) for j in adding]
    Queries.append(adding)
    adding = []

SizeRequired = []
PriceGive = []

for i in range(0,NoOfCustomers):
    adding = Queries[i]
    SizeRequired.append(adding[0])
    PriceGive.append(adding[1])
    adding = []

price=0

for i in range(0,NoOfCustomers):
    Buy = SizeRequired[i]
    for j in range(0,NoOfShoes):
        if Buy == ShoeSizes[j]:
            price = price + PriceGive[i]
            ShoeSizes[j] = 0
            break

print(price)
