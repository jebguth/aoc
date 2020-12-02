


def part1(data):
    pass


with open('input') as f:
    cnt = 0
    cnt2 = 0
    for l in f:
        ar = l.split(' ')
        lim = ar[0].split('-')
        let = ar[1].strip(':')
        pw = ar[2]
        n = pw.count(let)
        if n >= int(lim[0]) and n <= int(lim[1]):
            cnt += 1

        if (pw[int(lim[0]) - 1] == let and pw[int(lim[1]) - 1] != let) or (pw[int(lim[0]) - 1] != let and pw[int(lim[1]) - 1] == let):
            cnt2 += 1

    print(f'{cnt} and {cnt2}')


