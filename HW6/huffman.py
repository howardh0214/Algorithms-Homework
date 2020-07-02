import heapq

def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))



if __name__ == '__main__':
    data = input()
    freq = {}
    for symbol in data:
        freq[symbol] = 0
    for symbol in data:
        freq[symbol] += 1
    huff = encode(freq)
    for p in huff:
        print ("{}:{}".format(p[0], p[1]))

        









"""
if __name__ == '__main__':
    n_tests = int(input())
    for _ in range(n_tests):
        word = input()
"""
        