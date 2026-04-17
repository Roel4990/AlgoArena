from collections import deque

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = deque(nums1)
        nums2 = deque(nums2)
        nums = []

        while 1:
            if len(nums1) == 0:
                for i in nums2:
                    nums.append(i)
                break
            elif len(nums2) == 0:
                for i in nums1:
                    nums.append(i)
                break

            if nums1[0] < nums2[0]:
                nums.append(nums1[0])
                nums1.popleft()
            elif nums1[0] > nums2[0]:
                nums.append(nums2[0])
                nums2.popleft()
            else:
                nums.append(nums1[0])
                nums1.popleft()

            # print(nums)

        return median(nums)