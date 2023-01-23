

import statistics as stats

data = [364, 373, 358, 394, 378, 379, 357, 364, 350, 363, 392, 368, 359, 375, 399, 365, 379, 357, 380]


# Find the mean
mean = stats.mean(data)
print("Mean: ", mean)

# Find the median
median = stats.median(data)
print("Median: ", median)


# Find the mode
try:
    mode = stats.mode(data)
    print("Mode: ", mode)
except stats.StatisticsError:
    print("Mode: None")


# Find the stdev
stdev = stats.stdev(data)
print("Standard deviation: ", stdev)