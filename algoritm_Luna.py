import multiprocessing as mp
from matplotlib import pyplot as plt
import numpy as np
import hashlib
from random import randint
import time
from tqdm import tqdm
wrong_pass = []
# hash: 70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473		end: 1378	sha256
# bin 4466 74
# 446674******137(8)

# узнаем число доступных ядер
# в коллабе их мало, так что выполнять лабораторную придется на своем железе


def algoritm_luna(number: int) -> bool:
    number = str(number)
    if len(number)!=6: 
        return False
    bin = [4, 4, 6, 6, 7, 4]
    end = [1, 3, 7]
    check = 8
    code = [int(i) for i in number]
    all_number = bin+code+end
    all_number = all_number[::-1]
    for i, num in enumerate(all_number):
        if i % 2 == 0:
            mul = num*2
            if mul > 9:
                mul -= 9
            all_number[i] = mul
    total_sum = sum(all_number)
    rem = total_sum % 10
    check_sum = 10 - rem if rem != 0 else 0
    return number if check_sum == check else False
    


def check_hash(x):
    all_n = '446674'+str(x)+'1378'
    h = all_n.encode()
    hash = hashlib.sha256(h).hexdigest()
    
    return hash == '70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473'


def sample_function(x):
    if algoritm_luna(x) != False:
        return x if check_hash(x) == True else False


if __name__ == "__main__":
    print('begin')
    start = time.time()
    with mp.Pool(36) as p:
        for result in p.map(sample_function, tqdm(range(99999, 10000000))):
            if result:
                end = time.time() - start
                print(f'we have found {result} and have terminated pool')
                print(end)
                p.terminate()
                break
    print('end')
