import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


number_of_elements = [] # Create list with the number of elements for each benchmark
limit = 22
for i in range(7, limit, 3):
    number_of_elements.append(2**i)


names = ["heapsort",
         "mergesort",
         "quicksort",
         "python_sorted",
         "numpy_sort"] # name of algorithms

name_element_ordering = ["Random", "Reverse", "Sorted"] # sorted/reverse/random
name_element_ordering = name_element_ordering[0]
#markers = ["-", "--", ":"]
n_ar = 15 # number of executions

#for j, k in zip(names, markers):
for j in names:
    time_list = [] # Create list that will hold time for benchmarks
    std_list = [] # Create list that will hold std of time for benchmarks
    for i in number_of_elements:
        times = pd.read_pickle("./benchmarks/"+j+"-"+name_element_ordering
                               +"-"+str(i)+"-"+str(n_ar)+".pkl")
        times_array = times.values
        time = np.mean(times_array)
        std = np.std(times_array)
        time_list.append(time)
        std_list.append(std)
    plt.errorbar(number_of_elements, time_list, std_list)
plt.xscale("log", basex=2)
plt.yscale("log", basey=10)

plt.show()

