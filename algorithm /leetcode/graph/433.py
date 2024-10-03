import copy
from collections import  deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: [str]) -> int:
        bank_dic = {gene: True for gene in bank }
        bank_dic[startGene] = True

        if endGene not in bank_dic:
            return -1

        q = deque()

        q.append([0, list(startGene)])

        check_set = set()

        while q:
            mute_count, gene_str_list = q.popleft()

            target = ''.join(gene_str_list)

            # 재방문
            if target in check_set:
                continue

            #  not valid mutation
            if target not in bank_dic:
                continue

            if target == endGene:
                return mute_count

            # 방문 처리
            check_set.add(target)


            mute_count += 1
            for i in range(8):
                if gene_str_list[i] == 'A':
                    temp = copy.deepcopy(gene_str_list)
                    temp[i] = 'C'
                    q.append([mute_count, temp])

                    temp2 = copy.deepcopy(gene_str_list)
                    temp2[i] = 'G'
                    q.append([mute_count, temp2])

                    temp3 = copy.deepcopy(gene_str_list)
                    temp3[i] = 'T'
                    q.append([mute_count, temp3])


                elif gene_str_list[i] == 'C':
                    temp = copy.deepcopy(gene_str_list)
                    temp[i] = 'A'
                    q.append([mute_count, temp])

                    temp2 = copy.deepcopy(gene_str_list)
                    temp2[i] = 'G'
                    q.append([mute_count, temp2])

                    temp3 = copy.deepcopy(gene_str_list)
                    temp3[i] = 'T'
                    q.append([mute_count, temp3])

                elif gene_str_list[i] == 'G':
                    temp = copy.deepcopy(gene_str_list)
                    temp[i] = 'A'
                    q.append([mute_count, temp])

                    temp2 = copy.deepcopy(gene_str_list)
                    temp2[i] = 'C'
                    q.append([mute_count, temp2])

                    temp3 = copy.deepcopy(gene_str_list)
                    temp3[i] = 'T'
                    q.append([mute_count, temp3])


                else:
                    temp = copy.deepcopy(gene_str_list)
                    temp[i] = 'A'
                    q.append([mute_count, temp])

                    temp2 = copy.deepcopy(gene_str_list)
                    temp2[i] = 'C'
                    q.append([mute_count, temp2])

                    temp3 = copy.deepcopy(gene_str_list)
                    temp3[i] = 'G'
                    q.append([mute_count, temp3])

        return -1


a = Solution()
startGene = "AACCTTGG"
endGene = "AATTCCGG"
bank = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]

print(a.minMutation(startGene, endGene, bank))
