class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lim = capacity
        self.n = 0
        self.log = 0
        self.cdict = {}
         # "name": value, count, log

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.log += 1
        if key in self.cdict:
            self.cdict[key][1] += 1
            self.cdict[key][2] = self.log
            return self.cdict[key][0]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.log += 1
        if key in self.cdict:
            self.cdict[key][0] = value
            self.cdict[key][1] += 1
            self.cdict[key][2] = self.log
        elif self.n > self.lim:

