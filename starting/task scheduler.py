class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-x for x in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()
        
        while maxHeap or q:
            time += 1
            if maxHeap:
                x = 1 + heapq.heappop(maxHeap)
                if x:
                    q.append([x, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
        