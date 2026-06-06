import scipy.stats as stats
n = 10

p = 0.5

probability = (
    stats.binom.pmf(2, n, p) +
    stats.binom.pmf(3, n, p) +
    stats.binom.pmf(4, n, p)
)

print("Probability of getting between 2 and 4 heads:")
print(probability)