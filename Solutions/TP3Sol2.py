def my_system_with_obs(nsteps,x0,A,H,omega_motor,omega_sensory):
  """
  my_system_with_obs is a function that model the time-evolution of the latent state 
  and its observation
  Inputs : nsteps is the number of time steps to model
           x0 is the initial state (where we are starting from)
           A is the state-transition matrix
           H is the observation matrix
           omega_motor is the variance of the motor noise
           sigma_sensory is the variance of the sensory noise
  Outputs : state_evolution is a numpy array that contains the time-evolution of 
            the state vector : (state size * nsteps)
            obs_evolution is a numpy array that contains the time-evolution of 
            the observation of the state vector : (state size * nsteps)
  """
  ######################
  ### your code here ###
  ######################
  state_evolution = np.zeros([len(x0),nsteps])
  obs_evolution = np.zeros((len(x0),nsteps))
  state_evolution[:,0] = x0
  obs_evolution[:,0] = x0

  motor_noise = np.random.multivariate_normal(np.zeros(len(x0)) ,omega_motor,nsteps).T
  sensory_noise = np.random.multivariate_normal(np.zeros(len(x0)) ,omega_sensory,nsteps).T
  for ii in range(nsteps-1):
    state_evolution[:,ii+1] = A @ state_evolution[:,ii] + motor_noise[:,ii]
    obs_evolution[:,ii+1] = H @ state_evolution[:,ii+1] + sensory_noise[:,ii]  
  return state_evolution,obs_evolution

# Run the lines below to test your code 
np.random.seed(2060)
nsteps = 50
x0 = np.array([1,1]).T
A = np.array([[1.,1.],[-(2*np.pi/20.)**2.,0.9]])
H = np.eye(2)
sigma_motor = 0.05
sigma_sensory = 0.02
omega_motor = [[sigma_motor , 0],[0, sigma_motor]]
omega_sensory = [[sigma_sensory , 0],[0, sigma_sensory]]
######################
### your code here ###
######################
state_evolution, obs_evolution = my_system_with_obs(nsteps,x0,A,H,omega_motor,omega_sensory)
plot_my_system_with_obs(state_evolution,obs_evolution)
