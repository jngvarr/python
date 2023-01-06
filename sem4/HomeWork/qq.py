x={0: 117, 1: 107, 2: 133, 3: 127, 4: 90, 5: 24, 6: 16}
print(x)
# z={v: k for k, v in x.items()}
y=dict(reversed(x.items()))
z=dict(sorted(y.items()))
print(y)
print(z)