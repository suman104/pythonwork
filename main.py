#Find second highest number
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     set1 = set(arr)
#     length = len(set1)
#     set2= sorted(set1,reverse=True)
#     print(set2)
#     print(set2.pop(1))

#Find second lowest graded students. For multiple results, print then in alphabetical order
# if __name__ == '__main__':
#     outerlist= list()
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         innerlist= [name,score]
#         outerlist.append(innerlist)
#     print(outerlist)
#     secondleastvalue = sorted(list(set(mark for name,mark in outerlist)))[1]
#     print("\n".join([name for name,mark in sorted(outerlist) if mark == secondleastvalue]))

#Finding the percentage
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
def add(a,b):
	c = a+b
        return c
if __name__== '__main__':
    a=5
    b=10
    add(a,b)