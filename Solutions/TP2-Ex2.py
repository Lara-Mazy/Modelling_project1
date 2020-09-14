def compare_computational_analytical_means():
    x = np.arange(-10, 11, 0.1)
    ##########################
    ##### Your code here #####
    ##########################
    # Fixed likelihood
    mu_likelihood = 3
    sigma_likelihood = 1.5
    likelihood = my_gaussian(x, mu_likelihood, sigma_likelihood)
    # Varying prior
    mu_priors = np.linspace(-10, 10)
    sigma_prior = 1.5

    # Accumulate results here
    mus_by_integration = []
    mus_analytical = []
    for mu_prior in mu_priors:
        prior = my_gaussian(x, mu_prior, sigma_prior)
        posterior = compute_posterior_pointwise(prior, likelihood)
        mu_integrated = np.sum(x*posterior)
        mu_analytical = ((mu_likelihood / sigma_likelihood ** 2 + mu_prior / sigma_prior ** 2) /
                  (1 / sigma_likelihood ** 2 + 1 / sigma_prior ** 2))

        mus_by_integration.append(mu_integrated)
        mus_analytical.append(mu_analytical)

    return mu_priors, mus_analytical, mus_by_integration

mu_visuals, mu_analytical, mu_computational = compare_computational_analytical_means()
##########################
##### Your code here #####
##########################
#Visualize the results
plt.plot(mu_visuals,mu_analytical,'r', label= 'Analytical')
plt.plot(mu_visuals,mu_computational,'b--', label= 'Computational')
plt.legend()
plt.xlabel('Mean of the prior distribution')
plt.ylabel('Mean of the posterior distribution')
plt.show()