x_vector = np.arange(-10,10,0.1)

def compute_posterior_pointwise(prior, likelihood):
    ''' Author: Florence Blondiaux
    Returns the normalized posterior probability based on the prior and the likelihood
    Prior: The prior probabilities
    Likelihood: The likelihood probabilities
    '''
    posterior = prior * likelihood
    posterior /= posterior.sum()
    return posterior

likelihood = my_gaussian(x_vector,3,1.5)
prior = my_gaussian(x_vector,-1,1.5)
posterior = compute_posterior_pointwise(prior,likelihood)

plt.plot(x_vector, likelihood, 'r',Linewidth=2.5,label='likelihood')
plt.plot(x_vector,prior,'g',Linewidth=2.5,label='prior')
plt.plot(x_vector, posterior, 'b',Linewidth=2.5,label='posterior')
plt.legend()
plt.show()