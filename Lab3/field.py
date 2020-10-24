def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    for i in items:
        for j in args:
            yield i[j]



