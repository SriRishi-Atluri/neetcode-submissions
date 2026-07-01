"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
   def canAttendMeetings(self, intervals):
        def get_start(interval):
            return interval.start

        intervals.sort(key=get_start)

        for i in range(len(intervals) - 1):
            current_end = intervals[i].end
            next_start = intervals[i + 1].start

            if next_start < current_end:
                return False

        return True
