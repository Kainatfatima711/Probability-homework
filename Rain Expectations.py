import scipy.stats as stats

lambda_value = 10

prob_12_or_more = 1 - stats.poisson.cdf(11, lambda_value)

print("Probability of observing 12 or more rainy days:")
print(prob_12_or_more)

prob_12_to_18 = (
    stats.poisson.pmf(12, lambda_value) +
    stats.poisson.pmf(13, lambda_value) +
    stats.poisson.pmf(14, lambda_value) +
    stats.poisson.pmf(15, lambda_value) +
    stats.poisson.pmf(16, lambda_value) +
    stats.poisson.pmf(17, lambda_value) +
    stats.poisson.pmf(18, lambda_value)
)

print("\nProbability of observing between 12 and 18 rainy days:")
print(prob_12_to_18)
