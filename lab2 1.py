import numpy as np
import time

# Информация об авторе
AUTHOR = "Красников Владимир"
GROUP = "090301-ПОВа-о24"

N = 1024
BLOCK_SIZE = 128  # Размер блока для оптимизации

def generate_matrix():
    return np.random.rand(N, N)

def multiply_matrices_block(A, B, C):
    for i in range(0, N, BLOCK_SIZE):
        for j in range(0, N, BLOCK_SIZE):
            for k in range(0, N, BLOCK_SIZE):
                i_end = min(i + BLOCK_SIZE, N)
                j_end = min(j + BLOCK_SIZE, N)
                k_end = min(k + BLOCK_SIZE, N)
                C[i:i_end, j:j_end] += np.dot(A[i:i_end, k:k_end], B[k:k_end, j:j_end])

def main():
    print(f" \n Автор: {AUTHOR}")
    print(f"Группа: {GROUP}")

    A = generate_matrix()
    B = generate_matrix()
    C = np.zeros((N, N), dtype=np.float64)

    start = time.time()
    multiply_matrices_block(A, B, C)
    end = time.time()

    duration = end - start
    complexity = 2.0 * N ** 3
    performance = complexity / duration * 1e-6  # MFlops

    print(f"Сложность: {complexity}")
    print(f"Время: {duration:.2f} секунд")
    print(f"Производительность: {performance:.2f} MFlops")

if __name__ == "__main__":
    main()