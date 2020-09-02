# Stephen Bell: #001433854

class Time(object):
    # Stores times internally as seconds only, making operations easier. The
    # __init__ function takes in a string representing a time and converts it
    # into seconds.
    def __init__(self, time_str):
        (h, m, s) = time_str.split(':')
        self.seconds = int(s) + int(m) * 60 + int(h) * 3600

    # Takes in an integer representing a number of minutes and adds it to the
    # total number of seconds in the time.
    def add_minutes(self, mins):
        secs = 60 * mins
        self.seconds += secs

    def add_seconds(self, secs):
        self.seconds += secs

    def __eq__(self, other):
        return self.seconds == other.seconds

    def __le__(self, other):
        return self.seconds <= other.seconds

    def __lt__(self, other):
        return self.seconds < other.seconds

    def __ge__(self, other):
        return self.seconds >= other.seconds

    def __gt__(self, other):
        return self.seconds > other.seconds

    def __repr__(self):
        secs = self.seconds % 60
        mins = (self.seconds // 60) % 60
        hrs = ((self.seconds // 3600) % 60) % 24

        return f"{hrs:02d}:{mins:02d}:{secs:02d}"
