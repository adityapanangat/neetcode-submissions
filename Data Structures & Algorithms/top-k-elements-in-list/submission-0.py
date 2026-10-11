import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        freqs = {}

        for i in nums:
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1
        
        for num, freq in freqs.items():
            heapq.heappush_max(heap, (freq, num))

        output = []

        for i in range(k):
            output.append(heapq.heappop_max(heap)[1])
        
        return output
    