import math
import numpy as np
import matplotlib.pyplot as plt


class PRNG:
    def __init__(self):
        self.x = 1
        self.y = 10000
        self.z = 300
        self.temp = 0
        self.random = 0

    def randomUniform(self):
        # X Component
        self.x = 171 * (self.x % 177) - 2 * (self.x / 177)
        if self.x < 0:
            self.x = self.x + 30269
        # Y Component
        self.y = 172 * (self.y % 176) - 35 * (self.y / 176)
        if self.y < 0:
            self.y = self.y + 30307
        # Z Component
        self.z = 170 * (self.z % 178) - 63 * (self.z / 178)
        if self.z < 0:
            self.z = self.z + 30323
        # Addition of X, Y and Z Variable
        self.temp = self.x / 30269 + self.y / 30307 + self.z / 30323
        self.random = self.temp - math.trunc(self.temp)

        return self.random


# CODE FOR THE PDF GRAPH (Leave out if not in use)
# UNCOMMENT UNTIL ----
# print("Start")
# rand = PRNG()
# a = np.array([])
# Max = 1000000
# total = 0
#
# for i in range(0, Max):
#     if i % 10000:
#         print(i, end=",\t")
#     value = rand.randomUniform()
#     total += value
#     TP = np.array([value])
#     a = np.append(a, TP)
#
# print(total / Max)
# plt.hist(a, bins=80)
# plt.show()
# ----
