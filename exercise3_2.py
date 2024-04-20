# Import the library
from pybloom_live import ScalableBloomFilter
import math

# Define the parameters
n = 10**9 # total number of items
n_4 = 0.0347 * n # number of items that appear four or more times
fpr = 0.001 # false positive rate
k = 3 # number of hash functions
b = -n_4 * math.log(fpr) / (k * math.log(2)) # number of bits in the CBF
threshold = 4 # frequency threshold

# Create the CBF
cbf = ScalableBloomFilter(initial_capacity=n_4, error_rate=fpr, mode=ScalableBloomFilter.SMALL_SET_GROWTH)

# Create a dictionary to store the exact frequencies of the items that exceed the threshold
freq_dict = {}

# Simulate the input stream of items
# For simplicity, we assume that the items are integers from 1 to n
# and that their frequencies follow the given distribution
import random
random.seed(42) # for reproducibility
items = list(range(1, n+1))
freqs = [1] * int(0.8364 * n) + [2] * int(0.0978 * n) + [3] * int(0.0311 * n) + [4] * int(0.01735 * n) + [5] * int(0.008675 * n) + [6] * int(0.0043375 * n) + [7] * int(0.00216875 * n) + [8] * int(0.001084375 * n) + [9] * int(0.0005421875 * n) + [10] * int(0.00027109375 * n)
random.shuffle(freqs) # randomize the order of the frequencies

# Process each item in the stream
for i in range(n):
  item = items[i]
  freq = freqs[i]
  # Update the CBF and the dictionary for each occurrence of the item
  for j in range(freq):
    # Add the item to the CBF
    cbf.add(item)
    # Estimate the frequency of the item from the CBF
    est_freq = min([cbf.counters[i][item % cbf.counters[i].num_slices] for i in range(len(cbf.counters))])
    # If the estimated frequency is equal to the threshold, store the item and its exact frequency in the dictionary
    if est_freq == threshold:
      freq_dict[item] = freq
    # If the estimated frequency is greater than the threshold, update the exact frequency in the dictionary
    elif est_freq > threshold:
      freq_dict[item] += 1

# Print the results
print("The number of items that appear four or more times is:", len(freq_dict))
print("The items and their frequencies are:")
for item, freq in freq_dict.items():
  print(item, freq)
