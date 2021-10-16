
def solution(skill, skill_trees):
    # 탐색하면서 조건 맞으면 answer++
    answer = 0
    skill = list(skill)

    # 탐색
    for i in range(len(skill_trees)):
        temp = ""
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                temp += skill_trees[i][j]

        # temp 와 스킬트리 비교
        count = 0
        for e in range(len(temp)):
            if temp[e] != skill[e]:
                count += 1
                break

        # 스킬트리 만족하면, ++
        if count == 0:
            answer += 1

    return answer