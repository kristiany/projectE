seq = (1, 2)
fsum = 0
while seq[1] < 4000000:
    if seq[1] % 2 == 0:
        fsum += seq[1]
    seq = (seq[1], seq[0] + seq[1])

print(fsum)
