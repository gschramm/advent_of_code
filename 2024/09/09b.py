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

gap_starts = []
file_starts = []

for i_file, filesize in enumerate(filesizes):
    disk[curpos : curpos + filesize] = i_file
    file_starts.append(curpos)
    curpos += filesize

    if i_file < (len(filespaces) - 1):
        gaps = filespaces[i_file]
        disk[curpos : curpos + gaps] = -1
        gap_starts.append(curpos)
        curpos += gaps

#### HACK
# gap_starts.append(94788)

original_disk = disk.copy()

# %%
for file_id in range(filesizes.shape[0] - 1, -1, -1):
    file_size = filesizes[file_id]

    possible_gaps = np.where(filespaces >= file_size)[0]

    if len(possible_gaps) > 0:
        gap_id = possible_gaps[0]
        if gap_id < len(gap_starts):
            gap_start = gap_starts[gap_id]
            file_start = file_starts[file_id]

            if gap_start < file_start:
                disk[gap_start : gap_start + file_size] = file_id
                disk[file_start : file_start + file_size] = -1

                filespaces[gap_id] -= file_size
                gap_starts[gap_id] += file_size

# %%
# calculate the checksum
tmp = disk.copy()
tmp[tmp == -1] = 0
checksum = (tmp * np.arange(tmp.shape[0])).sum()

print(checksum)
