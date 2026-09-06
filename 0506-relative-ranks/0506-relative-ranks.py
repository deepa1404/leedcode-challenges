class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = [""] * len(score)

        ans = sorted(score, reverse= True)
        for i in range(len(score )):
            rank = ans.index(score[i]) + 1
            if rank == 1:
                result[i] = "Gold Medal"
            elif rank == 2:
                result[i] = "Silver Medal"
            elif rank == 3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank)
        return result
       