import question_1
import question_2

uniform = question_1.PRNG()


class Modulation:
    def __init__(self, bits, numM):
        self.total = bits
        self.bits = []
        self.symbols = []
        self.transmitted = []
        self.SNR = 0
        self.Eb = 0
        self.N0 = 0
        self.sigma = 0
        self.M = numM

    def binary(self):
        temp = uniform.randomUniform()
        if temp > 0.5:
            self.bits.append(1)
        else:
            self.bits.append(0)


BPSK = Modulation(100, 2)
QAM4 = Modulation(100, 4)
PSK8 = Modulation(100, 8)
QAM16 = Modulation(100, 16)


def mapBPSK():
    for i in range(0, BPSK.total):
        BPSK.binary()
        length = len(BPSK.bits)
        if BPSK.bits[length - 1] == 1:
            BPSK.symbols.append(1)
        else:
            BPSK.symbols.append(-1)

    print(BPSK.bits)
    print(BPSK.symbols)


def map4QAM():
    pass


#
# def map8PSK():
#
# def map16QAM():
#
# def addNoise():

mapBPSK()
