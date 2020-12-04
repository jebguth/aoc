



def check_slope(data, right, down):
    cnt = 0
    x = 0
    row = 0
    for l in data:
        if row % down:
            row += 1
            continue
        row += 1

        cnt = cnt + 1 if l[x] == '#' else cnt
        w = len(l) - 1
        x = x + right
        x = x if x < w else x - w
    return cnt

with open('input','r') as f:
    data = [l for l in f]

# First part
cnt = check_slope(data, 3, 1)

print(f'First part: {cnt}')
# Second part
cnt = cnt * check_slope(data, 1, 1)
cnt = cnt * check_slope(data, 5, 1)
cnt = cnt * check_slope(data, 7, 1)
cnt = cnt * check_slope(data, 1, 2)

print(f'Second part: {cnt}')