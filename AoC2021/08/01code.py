a = [12,13,14,9]
ans = 0
for i in range(1, len(a), 1):
    if a[i] > a[i-1]:
        ans += 1
print(ans)


ans = 0
for i in range(1, len(a)-2, 1):
    abc = a[i-1] + a[i] + a[i+1]
    bcd = a[i] + a[i+1] + a[i+2]
    if bcd > abc:
        ans += 1
print(ans)
