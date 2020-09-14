x = np.arange(-10, 10, 0.1)
hypothetical_stim = np.linspace(-8, 8, 1000)


def compute_likelihood_array(x_points, stim_array, sigma=1.):
    """
    This function computes the likelihood array of a given stimulus

    Inputs : x_points (numpy array) is the set of points on which one wants to evaluate the likelihood
             stim_array (numpy array) contains the mean position of every possible stimulus
             sigma (float) is the standard deviation of the gaussian distribution

    Outputs : likelihood array (numpy array) is a len(stim_array) x len(x_points) that contains the evaluation of
              the likelihood for every possible stimulus on the the set x_points. Each line of this array corresponds
              to a single simulus (stim_array[i]).
    """
    #########################
    ## your code goes here ##
    #########################

    # initializing likelihood_array
    likelihood_array = np.zeros((len(stim_array), len(x_points)))

    # looping over stimulus array
    for i in range(len(stim_array)):
        likelihood_array[i, :] = my_gaussian(x_points, stim_array[i], sigma)

    return likelihood_array


# Run the line below to test your code
likelihood_array = compute_likelihood_array(x, hypothetical_stim)

# Plot the results
#########################
## your code goes here ##
#########################
fig = plt.figure()
ax = fig.add_subplot(111)
colormap = ax.imshow(likelihood_array, extent=[-10, 10, 8, -8])
cbar = plt.colorbar(colormap, ax=ax)
cbar.set_label('probability')
ax.invert_yaxis()
ax.set_xlabel("$x$ : Potential true stimulus $x$")
ax.set_title("Likelihood as a function of $\~x$ : $p(\~x | x)$")
ax.set_ylabel("Possible brain encoding $\~x$")
ax.set_aspect('auto')