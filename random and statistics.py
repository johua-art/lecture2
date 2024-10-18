import random
import statistics

# a. Generate 100 random integers between 1 and 50
random_integers = [random.randint(1, 50) for _ in range(100)]

# b. Compute mean, median, mode, and standard deviation
mean = statistics.mean(random_integers)
median = statistics.median(random_integers)
try:
    mode = statistics.mode(random_integers)
except statistics.StatisticsError:
    mode = "No unique mode"

std_dev = statistics.stdev(random_integers)

# Print the results
print("Random Integers:", random_integers)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std_dev)
