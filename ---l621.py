""" Task Scheduler """

class Solution:
    def leastInterval(self, tasks, N):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections
        task_counts = list(collections.Counter(tasks).values())
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (N + 1) + Mct)
        
s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"],2))