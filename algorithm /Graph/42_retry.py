


def find_root(root, x):
    if root[x] != x:
        root[x] = find_root(root, root[x])
    return root[x]

def uni(root,a,b):

    a = find_root(root,a)
    b = find_root(root,b)

    if a > b:
        root[a] = b
    else:
        root[b] = a


def main():
    # 탑승구, 비행기 입력
    g = int(input())
    p = int(input())

    # 루트 노드
    root = [0] * (g+p+1)

    # 탑승구는 자기자신
    for i in range(1,g+1):
        root[i] = i

    # 비행기 연결
    for i in range(g+1,len(root)):
        root[i] = g+1


    count = 0

    # 비행기 도킹 가능한 범위 리스트
    seq = []

    for i in range(p):
        n = int(input())
        seq.append(n)

    # 비행기 도착 순서대로 도킹!
    for i in range(len(seq)):
        temp = 0
        num = seq[i]

        # 큰 번호부터 도킹
        for j in range(num, 0, -1):
            # 연결
            if find_root(root,j) != find_root(root, i+g+1):
                uni(root,i+g+1,j)
                count += 1
                break

            else:
                temp += 1

        # 도킹 못하면 중단!
        if temp ==  num :
            break


    # 출력
    print(count)


if __name__ == "__main__":
    main()