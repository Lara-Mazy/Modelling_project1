def calculate_binary_decision_array(x_points, posterior_array):
    """
    This function computes the decision taken by the participants for every potential decision input

    Inputs : x_points (numpy array) is the set of points on which we evaluated the posterior
             posterior_array (numpy array) is the posterior distribution

    Outputs : binary_decision_array (numpy array) that contains the decision taken for every potential input stimulus
    """

    binary_decision_array = np.zeros_like(posterior_array)

    for i in range(len(posterior_array)):
        # calculate mean of the posterior 
        mean = np.sum(x_points * posterior_array[i])
        # find the postion of mean in x_points (closest position)
        idx = np.argmin(np.abs(x_points - mean))
        binary_decision_array[i, idx] = 1

    return binary_decision_array


binary_decision_array = calculate_binary_decision_array(x, posterior_array)

fig = plt.figure()
ax = fig.add_subplot(111)
colormap = ax.imshow(binary_decision_array, extent=[-10, 10, 8, -8])
cbar = plt.colorbar(colormap, ax=ax)
cbar.set_label('probability')
ax.invert_yaxis()
ax.set_ylabel('Brain encoded Stimulus $\~x$')
ax.set_title('Sample Binary Decision Array')
ax.set_xlabel('Chosen position $\hat x$')
ax.set_aspect('auto')