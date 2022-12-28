#REQ ANS :::  [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

i_p = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
srt = sorted(i_p, key=lambda x:x[-1])
print(srt)