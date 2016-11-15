import heapq


class Heap(object):
    def __init__(self, initial=None, key=lambda x: x):
        self.key = key
        if initial:
            self._data = [(key(item), item) for item in initial]
            heapq.heapify(self._data)
        else:
            self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def peek(self):
        return self._data[0][1]

    def __len__(self):
        return len(self._data)


class MedianMaintainer:
    def __init__(self, input_file=None, input_array=None):
        self._heap_low = Heap(key=lambda x: -x)
        self._heap_high = Heap()
        self._median_sum = 0
        self.input_file = input_file
        self.input_array = input_array

    def sum_medians(self):
        if self.input_file is not None:
            with open(self.input_file) as file:
                for number in file.read().splitlines():
                    self._add_number(int(number))
        elif self.input_array is not None:
            for number in self.input_array:
                self._add_number(int(number))
        return self._median_sum % (len(self._heap_high) + len(self._heap_low))

    def _add_number(self, num):
        if not self._heap_low:
            self._heap_low.push(num)
            self._median_sum += num
            return
        if num <= self._heap_low.peek():
            self._heap_low.push(num)
        else:
            self._heap_high.push(num)
        if len(self._heap_low) - len(self._heap_high) > 1:
            self._heap_high.push(self._heap_low.pop())
        elif len(self._heap_high) - len(self._heap_low) > 1:
            self._heap_low.push(self._heap_high.pop())
        self._median_sum += self._heap_low.peek() if len(self._heap_low) >= len(
            self._heap_high) else self._heap_high.peek()

if __name__ == "__main__":
    median_maintainer = MedianMaintainer(input_file='assignment_3.txt')
    median_sum = median_maintainer.sum_medians()
    print(median_sum)

#Output : 1213
