# Box plots with custom fill colors

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

data40 =    [
[16754, 17019, 16672, 16281, 16702, 16047, 16406, 16054, 16600, 16834, 16650, 16368, 16236, 16830, 16218],
[18222, 19514, 18508, 19195, 17874, 18619, 18393, 18572, 18318, 18293, 18864, 19465, 17930, 19047, 18577],
            ]

data60 =    [
[20212, 17678, 16086, 16976, 18116, 17340, 17715, 17519, 18032, 16848, 16953, 17514, 18022, 15704, 19011],
[20202, 23934, 23367, 27286, 25666, 26065, 21689, 21077, 21257, 23501, 23820, 23688, 24058, 21860, 23724],
            ]

data80 =    [
[13873, 12647, 14327, 14053, 13974, 13995, 13478, 13141, 14321, 14558, 13567, 14723, 13763, 13451, 13850],
[31016, 28771, 31025, 26767, 29125, 31148, 27190, 30135, 25818, 28958, 27448, 27460, 27324, 26888, 29349],
            ]

data100 =   [
[8612, 9892, 9400, 9642, 9097, 9112, 9470, 10798, 9366, 10175, 11637, 10874, 10508, 11183, 11893],
[32032, 32635, 29965, 24493, 30721, 28771, 24047, 19286, 31502, 23992, 20014, 30783, 32530, 30378, 33467],
            ]


data40 = np.array(data40)/(500*40)
data40 = data40.tolist()

data60 = np.array(data60)/(500*60)
data60 = data60.tolist()

data80 = np.array(data80)/(500*80)
data80 = data80.tolist()

data100 = np.array(data100)/(500*100)
data100 = data100.tolist()

fig, ax = plt.subplots()
bplot60 = ax.boxplot(data60, vert=True, notch=False, patch_artist=True, positions=[0.75,1.25])
bplot100 = ax.boxplot(data100, vert=True, notch=False, patch_artist=True, positions=[1.75,2.25])


# fill with colors
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in [bplot60, bplot100]:
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

# adding horizontal grid lines
plt.xticks([1,2], ['60', '100'])
ax.set_ylabel('PDR')
ax.set_xlabel('Nodes')
ax.yaxis.grid(True)
ax.set_title('PDR with Link Check Frequency of 10s',y=1.02)
plt.xlim(0, 3)
plt.tick_params(pad=20) 

matplotlib.rcParams.update({'font.size':38})

plt.show()
