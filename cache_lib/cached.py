from time import time, sleep
from typing import Callable, TypeVar, ParamSpec, Any, Optional, TypeAlias


RT = TypeVar('RT')
P = ParamSpec('P')


class Cache:
    def __init__(self, size: int) -> None:
        self.cache: dict[str, list[str]] = {}
        self.size = size


class SimpleCache:
    def __init__(self) -> None:
        self.cache: dict[str, list[str]] = {}

    def get(self, key: str) -> Optional[list[str]]:
        return self.cache.get(key)

    def set(self, key: str, value: Any) -> None:
        self.cache[key] = value


class FIFOCache(Cache):

    key_name: list[str] = []

    def get(self, key: str) -> list[str] | None:
        return self.cache.get(key)

    def set(self, key: str, value: Any) -> None:
        if len(self.key_name) == self.size:
            del self.cache[self.key_name.pop(0)]
        self.cache[key] = value
        self.key_name.append(key)


class LRUCache(Cache):

    def get(self, key: Any) -> list[str] | None:
        if key in self.cache:
            self.cache[key][1] = str(time())
        print(self.cache.get(key))
        return self.cache.get(key)

    def set(self, key: str, value: Any) -> None:

        if len(self.cache) == self.size:
            del_key = min(self.cache, key=lambda k: self.cache[k][1])
            del self.cache[del_key]
        self.cache[key] = [value, str(time())]


class TTLCache(Cache):
    def __init__(self, size: int, ttl: int) -> None:
        super().__init__(size)
        self.ttl: int = ttl

    def get(self, key: str) -> list[str]:
        if key in self.cache:
            self.cache[key][1] = str(time())
        return self.cache.get(key, [])

    def set(self, key: str, value: Any) -> None:
        key_to_del = [key for key, value in self.cache.items() if time() - float(value[1]) >= self.ttl]
        if len(self.cache) == self.size:
            for k in key_to_del:
                del self.cache[k]
        self.cache[key] = [value, str(time())]


CL: TypeAlias = SimpleCache | FIFOCache | LRUCache | TTLCache


def cached(cache: CL) -> Callable[[Callable[P, RT]], Callable[P, RT]]:
    def inner(func: Callable[P, RT]) -> Callable[P, RT]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT | Any:
            if cache.get(str(args)) is not None:
                return cache.get(str(args))
            else:
                result = func(*args, **kwargs)
                cache.set(str(args), result)
            return result
        return wrapper
    return inner


@cached(cache=TTLCache(size=3, ttl=1))
def cache(word: str) -> str:
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
