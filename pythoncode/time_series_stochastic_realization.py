import random
import matplotlib.pyplot as plt

# Set the seed for reproducibility
random.seed(42)

# Generate the two random series
series1 = [random.uniform(8, 10) for _ in range(24)]
series2 = [random.uniform(8, 10) for _ in range(24)]
series3 = [random.uniform(8, 10) for _ in range(24)]

# Plot the results
plt.plot(series1, label='y1')
plt.plot(series2, label='Y2')
plt.plot(series3, label='Y3')
plt.xlabel('Z(t)')
plt.ylabel('t')
plt.legend()
plt.grid(True)
plt.ylim((0,10))
plt.title("Três realizações de Uma Série Temporal")
plt.show()