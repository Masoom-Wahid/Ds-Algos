"""
this is the way to solve this probelm not the last implementation
"""

def solve(arr : list[list[int,int]]) -> int:
    times = []
    for i in arr:
        times.append((i[0],+1))
        times.append((i[1],-1))

    times.sort(key = lambda x : x[0])
    curr = 0
    max = 0

    for i in times:
        curr += i[1]
        if curr > max : max = curr
    return max


if __name__ == "__main__":
    intervals = [
        [5,10],
        [15,20],
        [0,30]
    ]
    res = solve(intervals)
    print(res)