from time import time, sleep


class Cache:
    def __init__(self, size: int):
        self.cache = {}
        self.size = size


class SimpleCache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value


class FIFOCache(Cache):

    key_name = []

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        if len(self.key_name) == self.size:
            del self.cache[self.key_name.pop(0)]
        self.cache[key] = value
        self.key_name.append(key)


class LRUCache(Cache):

    def get(self, key):
        if key in self.cache:
            self.cache[key][1] = time()
        return self.cache.get(key)

    def set(self, key, value):

        if len(self.cache) == self.size:
            del_key = min(self.cache, key=lambda k: self.cache[k][1])
            del self.cache[del_key]
        self.cache[key] = [value, time()]
        print(self.cache)


class TTLCache(Cache):
    def __init__(self, size, ttl):
        super().__init__(size)
        self.ttl = ttl

    def get(self, key):
        if key in self.cache:
            self.cache[key][1] = time()
        return self.cache.get(key)

    def set(self, key, value):
        key_to_del = [key for key, value in self.cache.items() if time() - value[1] >= self.ttl]
        if len(self.cache) == self.size:
            for k in key_to_del:
                del self.cache[k]
        self.cache[key] = [value, time()]


def cached(cache):
    def decoration(func):
        def wrapper(*args, **kwargs):
            if cache.get(args) is not None:
                return cache.get(args)
            else:
                result = func(*args, **kwargs)
                cache.set(args, result)
            return result
        return wrapper
    return decoration


@cached(cache=TTLCache(size=3, ttl=1))
def cache(word):
    return word


cache("A")
cache("B")
sleep(3)
cache("C")
sleep(1)
cache("A")
sleep(1)
cache("A")
cache("F")
