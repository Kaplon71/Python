import multiprocessing
import random
import time
import matplotlib.pyplot as plt


class complex_Number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        return complex_Number(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return complex_Number(self.real - other.real, self.imaginary - other.imaginary)

class fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.current_Value = 0
        self.next_Value = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.steps:
            raise StopIteration

        if(self.count == 1):
            self.current_Value = 0

        fib = self.current_Value + self.next_Value
        self.current_Value = self.next_Value
        self.next_Value = fib
        self.count += 1
        return fib

def quick_Sort(data):
        if len(data) <= 1:
            return data

        pivot = data[len(data)//2]
        left = []
        middle = []
        right = []

        for i in range(0, len(data)):
            if data[i] < pivot:
                left.append(data[i])
            elif data[i] == pivot:
                middle.append(data[i])
            else:
                right.append(data[i])

        return quick_Sort(left) + middle + quick_Sort(right)

def parallel_Quick_Sort(data, processes):
    if len(data) <= 1:
        return data

    pivot = data[len(data)//2]
    left = []
    middle = []
    right = []

    for i in range(0, len(data)):
        if data[i] < pivot:
            left.append(data[i])
        elif data[i] == pivot:
            middle.append(data[i])
        else:
            right.append(data[i])
    with multiprocessing.Pool(processes) as p:
        sorted_left, sorted_right = p.map(quick_Sort, [left, right])
    return sorted_left + middle + sorted_right


if __name__ == '__main__':
    multiprocessing.freeze_support()
    fib = fibonacci(20)
    for num in fib:
        print(num)

    data_sizes = [100, 2000, 30000, 400000]
    num_processes_list = [1, 2, 4, 8]
    results = {}

    for size in data_sizes:
        results[size] = []
        data = [random.randint(1, 10000) for _ in range(size)]
        for num_processes in num_processes_list:
            start_time = time.time()
            parallel_Quick_Sort(data, num_processes)
            elapsed_time = time.time() - start_time
            results[size].append(elapsed_time)

    plt.figure(figsize=(12, 8))
    for size in data_sizes:
        plt.plot(num_processes_list, results[size], marker='o', label=f"Data size: {size}")

    plt.legend()
    plt.grid(True)
    plt.xlabel("Number of Processes")
    plt.ylabel("Time [s]")

    plt.show()
