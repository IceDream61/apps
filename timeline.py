from datetime import datetime


class TimeSegment:
    def __init__(self, t0, mark):
        self.t0 = t0
        self.mark = mark
    def split(self, t1):
        assert t0 < t1
        return TimeSegment(t0, mark), TimeSegment(t1, mark)


class TimeLine:
    def __init__(self, time_segments):
        self.time_segments = time_segments
    def set_time_segment(self, t0, t1, mark):
        i = 0
        while i+1 < len(self.time_segment) and self.time_segments[i+1].t0 < t0:
            i += 1
        j = len(self.time_segments)
        while self.time_segments[j].t0 > t1:
            j -= 1
        heads, mids, tails = self.time_segments[:i], self.time_segments[i:j+1], self.time_segments[j+1:]
        new_mids = []
        for k in range(
            if 
        


class Task:
    def __init__(self, name):
        self.name = name
        self.times = [(0,False)]
    def add(self, new_time):
        self.times = add_time(self.times, new_time)
    def del(self, st, ed):
        pass


if __name__ == '__main__':
    print('Timeline')

