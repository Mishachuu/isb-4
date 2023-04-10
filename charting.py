import multiprocessing as mp
import time

import matplotlib.pyplot as plt
import numpy as np

from check_hash import check_hash

if __name__ == '__main__':
    print('start')
    times = np.empty(shape=0)
    for i in range(1, 36):
        start = time.time()
        with mp.Pool(i) as p:
            for result in p.map(check_hash, range(99999, 10000000)):
                if result:
                    end = time.time() - start
                    times = np.append(times, end)
                    p.terminate()
                    break
                else:
                    print('Solution not found')
    plt.bar(range(len(times)), np.round(times, 2).tolist())
    plt.xlabel("Number of pools")
    plt.ylabel("Time, s")
    plt.title("Dependence of time on the number of pool")
    plt.show()
