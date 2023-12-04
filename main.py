k = 0
mi = 90000000
m_count = 0
m = 0
for i in range(68763, 90840+1):
    g = i
    for h in range(1, i+1):
        s = 0
        r = 0

        if g % h == 0:
            while h > 0:
                d = h % 10
                h = h//10
                s += d
                r += 1
            if s == 13 and r <= 4:
                k += 1
        if k >= 1:
            m = min(mi, i)
            m_count += 1

print(m)
print(m_count)













