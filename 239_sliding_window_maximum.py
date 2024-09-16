class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Find the maximum value in each sliding window of size k.

        This function takes a list of integers and an integer k, and returns a
        list of the maximum values for each sliding window of size k as it moves
        through the input list. It utilizes a deque to efficiently track the
        indices of the maximum values within the current window.

        Args:
            nums (List[int]): A list of integers from which to find the maximum values.
            k (int): The size of the sliding window.

        Returns:
            List[int]: A list containing the maximum values for each sliding window of size k.
        """


        res = []
        if not nums:
            return res

        dq: Deque = deque()

        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            start_index = i - k + 1

            if dq and dq[0] < start_index:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)
            res.append(nums[dq[0]])

        return res
