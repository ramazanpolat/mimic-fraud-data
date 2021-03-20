def generate(template: dict, count: int):
    for x in range(count):
        d = {}
        for key, generator in template.items():
            g = generator()
            d[key] = next(g)
        yield d
