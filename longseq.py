from itertools import combinations
from bisect import bisect
from memo import memo
from bench import benchmark

# very slow
def naive_longest_inc_seq(seq):
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):
            if list(sub) == sorted(sub):
                print(sub)
                return len(sub)

# iterative solution
def longest_inc_seq(seq):
    end = []
    for val in seq:
        idx = bisect(end, val)
        if idx == len(end):
            end.append(val)
        else:
            end[idx] = val
    return len(end)

# another iterative solution
def longest_inc_seq2(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])
    return max(L)

# memoized recursive solution
def memoized_longest_inc_seq(seq):
    @memo
    def L(cur):
        res = 1
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                res = max(res, 1 + L(pre))
        return res
    return max(L(i) for i in range(len(seq)))

@benchmark
def test_naive_longest_seq():
    print(naive_longest_inc_seq(s1))

@benchmark
def test_longest_inc_seq2():
    print(longest_inc_seq2(s1))

@benchmark
def test_memoized_longest_inc_seq():
    print(memoized_longest_inc_seq(s1))

if __name__ == '__main__':
    from random import randrange
    s1 = [randrange(100) for i in range(17)]
    print(s1)
    
    test_naive_longest_seq()
    test_longest_inc_seq2()
    test_memoized_longest_inc_seq()
