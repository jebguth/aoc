import re

with open('input','r') as f:
    data = [l for l in f]

byr = re.compile(r"(19[2-9]\d|200[0-2])$")
iyr = re.compile(r"20(1\d|20)$")
eyr = re.compile(r"20(2\d|30)$")
hgt = re.compile(r"((1[5-8]\d|19[0-3])cm)|((59|6\d|7[0-6])in)$")
hcl = re.compile(r"#([0-9a-f]{6})$")
pid = re.compile(r"[0-9]{9}$")
ecl = re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)$")



cnt = 0
cnt2 = 0
got_cid = False
n_items = 0
n_items2 = 0
for d in data:
    if d == '\n':
        if (n_items == 7 and not got_cid) or n_items == 8:
            cnt += 1
        if (n_items2 == 7 and not got_cid) or n_items2 == 8:
            cnt2 += 1
        got_cid = False
        n_items = 0
        n_items2 = 0
        continue

    d = d.strip('\n')
    for a in d.split(' '):
        a = a.split(':')
        if a[0] == 'byr' and byr.match(a[1]):
            n_items2 += 1
        elif a[0] == 'hgt' and hgt.match(a[1]):
            n_items2 += 1
        elif a[0] == 'eyr' and eyr.match(a[1]):
            n_items2 += 1
        elif a[0] == 'iyr' and iyr.match(a[1]):
            n_items2 += 1
        elif a[0] == 'hcl' and hcl.match(a[1]):
            n_items2 += 1
        elif a[0] == 'ecl' and ecl.match(a[1]):
            n_items2 += 1
        elif a[0] == 'pid' and pid.match(a[1]):
            n_items2 += 1
        elif a[0] == 'cid':
            got_cid = True
            n_items2 += 1
        else:
            print(f'{a[0]}:{a[1]}')

        n_items += len(a) / 2

print(f"{cnt}")
print(f"{cnt2}")