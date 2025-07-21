topic=['10101','11110','00010']
n=len(topic)
max_topic=0
count=0
for i in range(n):
    for j in range(i+1,n):
        combined_topic=int(topic[i],2) | int(topic[j],2)
        combined_topic=bin(combined_topic).count('1')
        if combined_topic>max_topic:
            max_topic=combined_topic
            count=1
        elif combined_topic==max_topic:
            count+=1
print(max_topic,count)

