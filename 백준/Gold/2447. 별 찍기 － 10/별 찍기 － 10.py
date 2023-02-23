n = int(input())


def make_star(num):
    if num == 3:
        return ["***", '* *', '***']

    stars = make_star(num // 3)
    star_li = []

    for star in stars:
        star_li.append(star*3)

    for star in stars:
        star_li.append(star+' '*(num//3)+star)

    for star in stars:
        star_li.append(star*3)

    return star_li


print('\n'.join(make_star(n)))
