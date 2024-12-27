import numpy as np

with open("input.txt", "r", encoding="UTF-8") as f:
    data = np.array(list(f.readline().strip()), dtype=int)

filesizes = data[0::2]
filespaces = data[1::2]

# %%
# setup disk
disksize = data.sum()
disk = np.full((disksize,), -1, dtype=int)

curpos = 0

for i_file, filesize in enumerate(filesizes):
    disk[curpos : curpos + filesize] = i_file
    curpos += filesize

    if i_file < (len(filespaces) - 1):
        gaps = filespaces[i_file]
        disk[curpos : curpos + gaps] = -1
        curpos += gaps

original_disk = disk.copy()
# %%
gap_inds = np.where(disk == -1)[0].tolist()
n_gaps = len(gap_inds)

first_gap = gap_inds.pop(0)
last_block = np.where(disk != -1)[0][-1]

while first_gap < last_block:
    disk[first_gap] = disk[last_block]
    disk[last_block] = -1
    first_gap = gap_inds.pop(0)
    last_block = np.where(disk != -1)[0][-1]

# %%
compacted_disk = disk[disk != -1]

checksum = (np.arange(compacted_disk.shape[0]) * compacted_disk).sum()
print(checksum)
