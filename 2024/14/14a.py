import numpy as np

px, py, vx, vy = [], [], [], []

with open("input.txt", "r", encoding="UTF-8") as file:
    for line in file:
        if line.startswith("p="):
            parts = line.strip().split(" ")
            p = parts[0][2:].split(",")
            v = parts[1][2:].split(",")
            px.append(int(p[0]))
            py.append(int(p[1]))
            vx.append(int(v[0]))
            vy.append(int(v[1]))

px = np.array(px)
py = np.array(py)
vx = np.array(vx)
vy = np.array(vy)

# number of tiles
nx = max(px) + 1
ny = max(py) + 1

# perform update steps
for i in range(100):
    px = (px + vx) % nx
    py = (py + vy) % ny

# create robot image
img = np.zeros((ny, nx), dtype=np.uint16)

for i in range(len(px)):
    img[py[i], px[i]] += 1

img_q1 = img[: ny // 2, : nx // 2]
c1 = np.sum(img_q1)

img_q2 = img[-(ny // 2) :, : nx // 2]
c2 = np.sum(img_q2)

img_q3 = img[: ny // 2, -(nx // 2) :]
c3 = np.sum(img_q3)

img_q4 = img[-(ny // 2) :, -(nx // 2) :]
c4 = np.sum(img_q4)

res = c1 * c2 * c3 * c4
print(res)
