class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxf = max(count.values())

        num_maxf_task = 0
        for t in count.values():
            if t == maxf:
                num_maxf_task+=1

        
        time = max(len(tasks), (maxf-1)*(n+1) + num_maxf_task)

        return time




        