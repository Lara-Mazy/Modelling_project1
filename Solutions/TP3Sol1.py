def my_system(nsteps,x0,A,omega_motor,seed=2060):
  """
  my_system is a function that model the time-evolution of a linear dynamical system
  with state transition matrix A.
  Inputs : nsteps is the number of time steps to model
           x0 is the initial state (where we are starting from)
           A is the state-transition matrix
  Outputs : state_evolution is a numpy array that contains the time-evolution of 
            the state vector : (state size * nsteps)
  """
  # Set the random generator seed
  np.random.seed(seed)

  state_evolution = np.zeros([len(x0),nsteps])
  state_evolution[:,0] = x0
  motor_noise = np.random.multivariate_normal(np.zeros(len(x0)) ,omega_motor,nsteps).T

  for ii in range(nsteps-1):
    state_evolution[:,ii+1] = A @ state_evolution[:,ii] + motor_noise[:,ii]
  return state_evolution

# Run the lines below to test your code

nsteps = 50
x0 = np.array([1,1]).T
A = np.array([[1., 1.], [-(2*np.pi/20.)**2., .9]])
sigma_motor = 0.05
omega_motor = [[sigma_motor , 0],[0, sigma_motor]]

state_evolution = my_system(nsteps,x0,A,omega_motor)
plot_my_system(state_evolution)
