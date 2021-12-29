import tempra as tp

x1 = [1, 3, 7, 13, 20]  # Timestamps
y1 = [1, 2, 3, 4, 5]

x2 = [2, 10, 13, 18, 19]  # Timestamps
y2 = [5, 4, 3, 2, 1]

s1 = zip(x1, y1)
s2 = zip(x2, y2)

a1 = tp.Axis(s1)
a2 = tp.Axis(s2)

t1 = tp.Tempra([a1, a2])

for win in t1.window(size=5, stride=5):
    print(win.mean())




