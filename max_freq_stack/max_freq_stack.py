'''module maximum frequency stack'''
from collections import deque

class FreqStack:
    '''class frequency stack'''
    def __init__(self):
        self.max_freq = 0
        self.freq_dict = {}
        self.groups_by_freq = {}

    def push(self, val: int) -> None:
        '''adds element to stack'''
        self.freq_dict[val] = self.freq_dict.get(val, 0) + 1

        f = self.freq_dict[val]
        if f not in self.groups_by_freq:
            self.groups_by_freq[f] = deque()
        self.groups_by_freq[f].append(val)

        self.max_freq = max(f, self.max_freq)

    def pop(self) -> int:
        '''deletes element with the most frequency and last mentioned'''
        el = self.groups_by_freq[self.max_freq].pop()
        self.freq_dict[el] -= 1

        if not self.groups_by_freq[self.max_freq]:
            self.max_freq -= 1
        return el


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
