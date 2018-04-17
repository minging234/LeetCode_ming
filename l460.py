""" LFU Cache """

import heapq
class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lim = capacity
        self.n = 0
        self.order = []
        self.cdict = {}
        print('init')
        # "name": value, count

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cdict:
            self.cdict[key][1] += 1
            pos = self.order.index(key)
            adr = pos
            val = self.cdict[key][1]
            while self.cdict[self.order[pos]][1] <= val:
                self.order[adr], self.order[pos] = self.order[pos], self.order[adr]
                adr = pos
                pos -= 1
                if pos < 0:
                    break
            return self.cdict[key][0]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cdict:
            self.cdict[key][0] = value
            self.cdict[key][1] += 1
            pos = self.order.index(key)
            adr = pos
            val = self.cdict[key][1]
            while self.cdict[self.order[pos]][1] <= val:
                self.order[adr], self.order[pos] = self.order[pos], self.order[adr]
                adr = pos
                pos -= 1
                if pos < 0:
                    break
        elif self.n >= self.lim > 0:
            obk = self.order.pop()
            del self.cdict[obk]
            self.order.append(key)
            self.cdict[key] = [value, 0]
            pos = self.order.index(key)
            adr = pos
            val = self.cdict[key][1]
            while self.cdict[self.order[pos]][1] <= val:
                self.order[adr], self.order[pos] = self.order[pos], self.order[adr]
                adr = pos
                pos -= 1
                if pos < 0:
                    break
        elif self.n < self.lim:
            self.order.append(key)
            self.cdict[key] = [value, 0]
            pos = self.order.index(key)
            adr = pos
            val = self.cdict[key][1]
            while self.cdict[self.order[pos]][1] <= val:
                self.order[adr], self.order[pos] = self.order[pos], self.order[adr]
                adr = pos
                pos -= 1
                if pos < 0:
                    break
            self.n += 1
            print(self.order)


a = LFUCache(3)
print(
a.put(1,1),
a.put(2,2),
a.put(3,3),
a.put(4,4),
a.get(4),a.get(3),a.get(2),a.get(1)

)