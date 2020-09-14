def calculate_posterior_array(prior_array, likelihood_array):
    """
    This function computes the posterior distribution from the prior & the likelihood

    Inputs : prior_array (numpy array) is the prior distribution
             likelihood_array (numpy array) is the likelihood distribution
             For both these arrays, each line correspond to a different input stimulus
    Outputs : posterior_array (numpy array) that contains the posterior distribution for the different
              input stimulus (each line corresponds to a different input)
    """

    ###########################
    ### your code goes here ###
    ###########################
    posterior_array = prior_array * likelihood_array
    posterior_array /= posterior_array.sum(axis=1, keepdims=True)  # normalize each row separately

    return posterior_array


posterior_array = calculate_posterior_array(prior_array, likelihood_array)

fig = plt.figure()
ax = fig.add_subplot(111)
colormap = ax.imshow(posterior_array, extent=[-10, 10, 8, -8])
cbar = plt.colorbar(colormap, ax=ax)
cbar.set_label('probability')
ax.invert_yaxis()
ax.set_ylabel('Brain encoded Stimulus $\~x$')
ax.set_title('Posterior as a fcn of $\~x$ : $p(x | \~x)$')
ax.set_xlabel('Hypothesized Position $x$')
ax.set_aspect('auto')

