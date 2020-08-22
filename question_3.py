import question_1
import question_2
import math
import matplotlib.pyplot as plt

uniform = question_1.PRNG()


class Modulation:
    def __init__(self, bits, numM):
        self.total = bits
        self.bits = []
        self.symbols = []
        self.rk = []
        self.transmittedSymbols = []
        self.transmittedBits = []
        self.SNR = 0
        self.Eb = 0
        self.N0 = 0
        self.sigma = 0
        self.M = numM
        self.bitErrorCount = 0
        self.symErrorCount = 0
        self.BER = []
        self.SER = []

    def binary(self):
        temp = uniform.randomUniform()
        if temp > 0.5:
            self.bits.append(1)
        else:
            self.bits.append(0)

norm = question_2.GRNG()


BPSK = Modulation(10000, 2)
QAM4 = Modulation(100, 4)
PSK8 = Modulation(100, 8)
QAM16 = Modulation(100, 16)


# new comment
def mapBPSK():
    # Converts bits to symbols
    for i in range(0, BPSK.total):
        BPSK.binary()
        length = len(BPSK.bits)
        if BPSK.bits[length - 1] == 1:
            BPSK.symbols.append(1)
        else:
            BPSK.symbols.append(-1)

    for i in range(-4, 13):

        for j in range(0, BPSK.total):
            # Adding AWGN
            BPSK.sigma = 1/(math.sqrt(10**(i/10)*2*math.log(BPSK.M, 2)))
            BPSK.rk.append(BPSK.symbols[j] + BPSK.sigma*norm.randomNormal())

            # Decoding Received Bits
            if BPSK.rk[j] >= 0:
                BPSK.transmittedSymbols.append(1)
            else:
                BPSK.transmittedSymbols.append(-1)

            if BPSK.transmittedSymbols[j] == 1:
                BPSK.transmittedBits.append(1)
            else:
                BPSK.transmittedBits.append(0)

            if BPSK.transmittedSymbols[j] != BPSK.symbols[j]:
                BPSK.symErrorCount += 1

            if BPSK.transmittedBits[j] != BPSK.bits[j]:
                BPSK.bitErrorCount += 1

        BPSK.SER.append(BPSK.symErrorCount/BPSK.total)
        BPSK.BER.append(BPSK.bitErrorCount/BPSK.total)
        print(BPSK.SER)
        print(BPSK.BER)
        print()

        BPSK.bitErrorCount = 0
        BPSK.symErrorCount = 0
        BPSK.transmittedBits = []
        BPSK.transmittedSymbols = []
        BPSK.rk = []

    x = []
    for i in range(-4, 13):
        x.append(i)
    plt.semilogy(x, BPSK.SER)
    plt.show()


def map4QAM():
    pass


#
# def map8PSK():
#
# def map16QAM():
#
# def addNoise():

mapBPSK()
