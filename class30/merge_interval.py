import functools


class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e
    def __repr__(self):
        return f"[{self.start},{self.end}]"
    # def __str__(self):
    #     return f"[{self.start},{self.end}]"

class Solution:
    def insert(self, intervals, newInterval):
        n = len(intervals)
        ans =[]
        for i in range(n):
            if intervals[i].end < newInterval.start:
                ans.append(intervals[i])
            elif intervals[i].start > newInterval.end:
                ans.append(newInterval)
                for j in range(i,n):
                    ans.append(intervals[j])
                return ans
            else:
                newInterval.start = min(intervals[i].start, newInterval.start)
                newInterval.e = max(intervals[i].end, newInterval.end)
        ans.append(newInterval)
        return ans

    def compare(self,x, y):

        if x.start < y.start:
            return -1
        else:
            return 1

    def merge(self, intervals):
        intervals.sort(key=functools.cmp_to_key(self.compare))
        n = len(intervals)
        ans =[]
        for i in range(1,n):
            if intervals[i-1].end < intervals[i].start:
                    ans.append(intervals[i-1])
            else:
                intervals[i].start = min(intervals[i-1].start, intervals[i].start)
                intervals[i].end = max(intervals[i-1].end, intervals[i].end)
                if intervals[i-1].start != intervals[i].start and intervals[i-1].end != intervals[i].end:
                    ans.append(intervals[i])

        ans.append(intervals[n - 1])
        return ans

sol = Solution()
A = [ (47, 76), (51, 99), (28, 78), (54, 94), (12, 72), (31, 72), (12, 55), (24, 40), (59, 79), (41, 100), (46, 99), (5, 27), (13, 23), (9, 69), (39, 75), (51, 53), (81, 98), (14, 14), (27, 89), (73, 78), (28, 35), (19, 30), (39, 87), (60, 94), (71, 90), (9, 44), (56, 79), (58, 70), (25, 76), (18, 46), (14, 96), (43, 95), (70, 77), (13, 59), (52, 91), (47, 56), (63, 67), (28, 39), (51, 92), (30, 66), (4, 4), (29, 92), (58, 90), (6, 20), (31, 93), (52, 75), (41, 41), (64, 89), (64, 66), (24, 90), (25, 46), (39, 49), (15, 99), (50, 99), (9, 34), (58, 96), (85, 86), (13, 68), (45, 57), (55, 56), (60, 74), (89, 98), (23, 79), (16, 59), (56, 57), (54, 85), (16, 29), (72, 86), (10, 45), (6, 25), (19, 55), (21, 21), (17, 83), (49, 86), (67, 84), (8, 48), (63, 85), (5, 31), (43, 48), (57, 62), (22, 68), (48, 92), (36, 77), (27, 63), (39, 83), (38, 54), (31, 69), (36, 65), (52, 68) ]
# intervals =[Interval(4,18),Interval(2,6),Interval(8,10),Interval(15,18)]
# intervals =[Interval(1,6),Interval(8,10),Interval(15,18)]
intervals =[]
for i in range(len(A)):
    intervals.append(Interval(A[i][0],A[i][1]))
print(sol.merge(intervals))

