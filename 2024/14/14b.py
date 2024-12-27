import numpy as np
import matplotlib.pyplot as plt

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

num_updates = 10000

img = np.zeros((num_updates, ny, nx), dtype=np.uint16)

# perform update steps
for i in range(num_updates):
    px = (px + vx) % nx
    py = (py + vy) % ny

    img[i, py, px] = 1


# vi = ThreeAxisViewer(img, cmap="Greys", base_fig_width=8.0 * num_updates / 500)

g0 = np.zeros_like(img)
g1 = np.zeros_like(img)

g0[:, :-1, :] = img[:, 1:, :] - img[:, :-1, :]
g1[:, :, :-1] = img[:, :, 1:] - img[:, :, :-1]
g = np.sqrt(g0**2 + g1**2).sum(axis=-1).sum(axis=-1)

amin = np.argmin(g)

print(amin + 1)

fig, ax = plt.subplots(1, 1, figsize=(8, 8), tight_layout=True)
ax.imshow(img[amin], cmap="Greys")
ax.set_title(f"Time: {amin + 1}")
fig.show()
