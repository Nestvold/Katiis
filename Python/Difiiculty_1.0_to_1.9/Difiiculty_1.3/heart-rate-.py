
number_of = int(input())

for _ in range(number_of):
    b, p = input().split()
    b = int(b)
    p = float(p)

    if b >= 1 <= 1000 and 1000 > p > 0:
        BPM = (60 * b) / p
        MIN_ABPM = BPM - 60/p
        MAX_ABPM = BPM + 60/p

        print(round(MIN_ABPM, 4), round(BPM, 4), round(MAX_ABPM, 4))
