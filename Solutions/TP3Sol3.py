def my_kalman_filter(nsteps,x0,A,H,omega_motor,omega_sensory,seed=2060):
  """
  my_kalman_filter computes and applies the Kalman filter to the system seen above
  Inputs : nsteps is the number of time steps to model
           x0 is the initial state (where we are starting from)
           A is the state-transition matrix
           H is the observation matrix
  Outputs : latent_state is a numpy array that contains the time-evolution of 
             the state vector : (state size * nsteps)
            observed_state is a numpy array that contains the time-evolution of 
             the observation of the state vector : (state size * nsteps)
            estimated_state is a numpy array that contains the time-evolution of 
              the estimation of the state vector : (state size * nsteps)
            K kalman gains: (state size * state size * nsteps)
  """
  np.random.seed(seed)

  K = np.zeros((len(x0),len(x0),nsteps))
  Sigma = np.zeros((len(x0),len(x0),nsteps))
  latent_state = np.zeros((len(x0),nsteps))
  observed_state = np.zeros((len(x0),nsteps))
  estimated_state = np.zeros((len(x0),nsteps))
  estimated_state[:,0]= x0
  observed_state[:,0] = x0
  latent_state[:,0] = x0

  motor_noise = np.random.multivariate_normal(np.zeros(len(x0)) ,omega_motor,nsteps).T
  sensory_noise = np.random.multivariate_normal(np.zeros(len(x0)) ,omega_sensory,nsteps).T

  for ii in range(nsteps-1):
    K[:,:,ii] = A @ Sigma[:,:,ii] @ H.T @ np.linalg.inv(H @ Sigma[:,:,ii] @ H.T + omega_motor)
    Sigma[:,:,ii+1] = omega_sensory + (A - K[:,:,ii] @ H) @ Sigma[:,:,ii] @ A.T
    latent_state[:,ii+1] = A @ latent_state[:,ii] + motor_noise[:,ii] #Needed to compute observed state
    observed_state[:,ii] = H @ latent_state[:,ii] + sensory_noise[:,ii]

    estimated_state[:,ii+1]= A @ estimated_state[:,ii] + K[:,:,ii] @ (observed_state[:,ii]-H @ estimated_state[:,ii])

  return latent_state,observed_state, estimated_state, K


# Run the lines below to test your code

# Parameters definition
x0 = np.array([1,1]).T
omega_motor = 0.05 * np.eye(len(x0))
omega_sensory = 0.02 * np.eye(len(x0))
latent_state,observed_state, estimated_state, K = my_kalman_filter(nsteps,x0,A,H,omega_motor,omega_sensory)
# plot --> see function preamble
# call the function
plot_my_kalman_filter(latent_state,observed_state, estimated_state)

