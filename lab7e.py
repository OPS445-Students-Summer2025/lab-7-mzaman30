#!/usr/bin/env python3
# Student ID: mzaman30

class Time:
    def __init__(self,hour=12,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        nt = sec_to_time(self.time_to_sec() + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def time_to_sec(self):
        return (self.hour * 60 + self.minute) * 60 + self.second

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
