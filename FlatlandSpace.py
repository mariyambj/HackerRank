n=5
c=[0,2]
distance=[]
for i in range(0,n):
    min_distance = float('inf')
    for point in c:
        min_distance = min(min_distance, abs(i - point))
    distance.append(min_distance)
print(max(distance))

    