


# 2번 문제 
def solution(needs, r):

  dic = {}
  
  for need in needs:
    length = len(need)
    for num in range(len(need)):
      if need[num] == 1:
        if num not in dic:
          dic[num] = 1
        else:
          dic[num] += 1
  
  blank = []

  for i in range(length):
    blank.append([i,dic[i]])
  

  blank.sort(key = lambda x : x[1])

  check = []

  
  for i in range(length - r):
    check.append(blank[i][0])

  print(check)


  answer = len(needs)
  

  for need in needs:
    for num in check:
      if need[num] == 1:
        answer -= 1
        break
  

  print(answer)

  



needs = [[1,0,0], [1,1,0], [1,1,0],[1,0,1],[1,1,0],[0,1,1]]
r = 2

solution(needs, r)
