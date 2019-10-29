from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cache.has_key(key):
            v = self.cache.get(key)
            del self.cache[key]
            self.cache[key] = v
            return v
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cache.has_key(key):
            v = self.cache.get(key)
            del self.cache[key]
            self.cache[key] = value
        elif len(self.cache) == self.size:
            self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            self.cache[key] = value

if __name__ == '__main__':
    l = LRUCache(2)
    l.put(1,1)
    l.put(2,2)
    print l.get(1)
    for k,v in l.cache.iteritems():
        print k,v
    l.put(3,3)
    for k,v in l.cache.iteritems():
        print k,v
    print l.get(2)
    for k,v in l.cache.iteritems():
        print k,v
    l.put(4,4)
    for k,v in l.cache.iteritems():
        print k,v
    print l.get(1)
    print l.get(3)
    print l.get(4)

