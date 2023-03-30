import multiprocessing as mp
from matplotlib import pyplot as plt
import numpy as np
import hashlib
from cryptography.hazmat.primitives import hashes

# hash: 70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473		end: 1378	sha256
# bin 4466 74
# 446674**********%

# узнаем число доступных ядер
# в коллабе их мало, так что выполнять лабораторную придется на своем железе
cores = mp.cpu_count()
print(cores)  # 12


def algoritm_luna(number: str) -> bool:
    code = [int(i) for i in number]
    code = code[::-1]
    for i, num in enumerate(code):
        if i % 2 == 0:
            mul = num*2
            if mul > 10:
                mul -= 10
            code[i]=mul
    all_sum=10-sum(code)%10
