import collections
# pip refused to work, wrote my own class instead
class Multiset:
    def __init__(self, iterable = []) -> None:
        self.value = collections.defaultdict(int)
        for e in iterable:
            self.value[e] += 1
    def subset(self, other) -> bool:
        for key in other.value:
            if self.value[key] < other.value[key]:
                return False
        return True
    def __sub__(self, other):
        if not self.subset(other):
            raise "must be a subset"
        _t = []
        for key in self.value.keys():
            for _ in range(self.value[key] - other.value[key]):
                _t.append(key)
        return Multiset(_t)
    def __iter__(self):
        for key in sorted(self.value.keys()):
            for _ in range(self.value[key]):
                yield key
    def __str__(self) -> str:
        return '{'+', '.join([str(key) for key in self]) +'}'
    def __hash__(self) -> int:
        _t = tuple()
        for key in sorted(self.value.keys()):
            _t += (key, self.value[key])
        return hash(_t)