def geometric_progression(start, step):
    current = start
    while True:
        yield current
        current *= step


gen1 = geometric_progression(-2, -5)
for _ in range(10):
    print(next(gen1))

print("\n")

gen2 = geometric_progression(10, 3)
for _ in range(10):
    print(next(gen2))
