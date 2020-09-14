x = np.arange(-10, 10, 0.1)


def calculate_prior_array(x_points, stim_array, p_center,
                          prior_mean_center=.0, prior_sigma_center=.5,
                          prior_mean_corner=3, prior_sigma_corner=1):
    """
    This function computes the prior distribution based on the mixture of gaussians

    Inputs : x_points (numpy array) is the set of points on which we want to evaluate the prior
             stim_array (numpy array) is the array of stimulus input
             p_center (float) is the probability that the ball lands in center of the court
             mean_center (float) mean value of the center ball landing site
             mean_corner (float) mean value of the corner ball landing site
             sigma_center (float) std deviation of the center ball landing site
             sigma_corner (float) std deviation of the corner ball landing site

    Outputs : prior array (numpy array) contains the prior in a len(stim_array) x len(x_points) array
        'indep' stands for independent
    """

    ###########################
    ### your code goes here ###
    ###########################
    prior_center = my_gaussian(x_points, prior_mean_center, prior_sigma_center)
    prior_corner = my_gaussian(x_points, prior_mean_corner, prior_sigma_corner)

    prior_mixed = (p_center) * prior_center + ((1 - p_center) * prior_corner)
    prior_mixed /= np.sum(prior_mixed)  # normalize
    prior_array = np.tile(prior_mixed, len(stim_array)).reshape(len(stim_array), -1)
    return prior_array


# Run the lines below to test your code


p_center = .5
hypothetical_stim = np.linspace(-8, 8, 1000)
prior_array = calculate_prior_array(x, hypothetical_stim, p_center)

###########################
### your code goes here ###
###########################
fig = plt.figure()
ax = fig.add_subplot(111)
colormap = ax.imshow(prior_array, extent=[-10, 10, 8, -8])
cbar = plt.colorbar(colormap, ax=ax)
cbar.set_label('probability')
ax.invert_yaxis()
ax.set_xlabel("$x$ : Potential true stimulus $x$")
ax.set_title("Prior as a function of $\~x$ : $p(\~x|x)$")
ax.set_ylabel("Possible brain encoding $\~x$")
ax.set_aspect('auto')