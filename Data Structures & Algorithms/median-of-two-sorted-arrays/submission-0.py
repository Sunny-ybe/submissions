class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2

        if len(B) < len(A):
            A,B = B,A
        
        m,n = len(A), len(B)
        total_left = (m+n+1) // 2

        l,r = 0, m

        while l <= r:
            i = (l+r) // 2
            j = total_left - i

            Aleft = A[i-1] if i > 0 else float("-inf")
            Aright = A[i] if i < m else float("inf")

            Bleft = B[j-1] if j > 0 else float("-inf")
            Bright = B[j] if j < n else float("inf")  

            if Aleft <= Bright and Aright >= Bleft:
                if (m+n) % 2 == 1:
                    return max(Aleft, Bleft)
                else:
                    return (min(Bright, Aright) + max(Aleft, Bleft)) / 2
            
            elif Aleft > Bright:
                r = i-1
            else:
                l = i + 1





        
        
        