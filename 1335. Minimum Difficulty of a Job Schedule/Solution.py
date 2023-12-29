class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        job_count = len(jobDifficulty)
        if job_count < d: return -1  # not enough jobs to work on at least one a day

        @lru_cache(None)
        def min_score(last_score=0, cur_idx=0, div_left=d-1):
            if div_left == 0: return max([last_score] + jobDifficulty[cur_idx:])  # our last day, we have to keep working until we're out of jobs
            cur_score = max(last_score, jobDifficulty[cur_idx])  # our difficulty for today might increase since we take on this job

            if job_count - cur_idx == div_left + 1:
                return cur_score + sum(jobDifficulty[cur_idx+1:]) # we have to keep splitting to have 1 job per day
            join_score = min_score(cur_score, cur_idx+1, div_left)  # keep working 
            div_score = cur_score + min_score(0, cur_idx+1, div_left-1) # start fresh tomorrow
            return min(join_score, div_score)

        return min_score()
        """i=0
        days = 0
        temp1 = 0
        while i<len(jobDifficulty):
            print(i,"here")
            temp1 += jobDifficulty[i]
            for j in range(i,len(jobDifficulty)):
                print(i,"i")
                if i<len(jobDifficulty)-1 and jobDifficulty[i+1]<temp1:
                    i+=1
                else:
                    i+=1
                    days+=1
                    break
        if days<d:
            return temp1
        else:
            return -1"""
