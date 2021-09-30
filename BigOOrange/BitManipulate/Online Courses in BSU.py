import queue
from queue import PriorityQueue
needed_courses = []
def topologicalSort(graph, result, needed_courses):
    indegree = [0]*n
    # zero_indegree = queue.Queue()
    zero_indegree = PriorityQueue()
    for u in range(n):
        for v in graph[u]:
            indegree[v] += 1
    count = 0
    for i in range(n):
        if(count==len(special_dict)):
            return True
        if indegree[i] == 0:
            zero_indegree.put(i)
            needed_courses.append(i)
            if(i in special_dict.keys() and special_dict[i]==1):
                special_dict[i] -= 1
                count+=1
    while not zero_indegree.empty():
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]:
            if(count==len(special_dict)):
                return True
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.put(v)
                needed_courses.append(v)
                if(v in special_dict.keys() and special_dict[v]==1):
                    special_dict[v] -= 1
                    count+=1
    for i in range(n):
        if indegree[i] != 0:
            return False
    return True

n, k = map(int, input().split())
specials = list(map(int, input().split()))
graph = [[] for i in range(n)]
result = []
needed_courses = []
special_dict = {}
for special in specials:
    special_dict[special-1] = 1
for i in range(n):
    inputs = list(map(int, input().split()))
    print(inputs)
    for j, course in enumerate(inputs):
        if j==0:
            continue
        print("i, j, course", i, j, course)
        course = course - 1
        graph[course].append(i)
check = topologicalSort(graph, result, needed_courses)
# for i in result:
#     if(count==len(special_dict.keys())):
#         break
#     needed_courses.append(i)
#     if i in special_dict.keys():
#         if(special_dict[i]==1):
#             count+=1
#             special_dict[i]-=1
# print(len(needed_courses), check)
for c in result:
    print(c+1, end=' ')
# print("\n")
print(needed_courses)
