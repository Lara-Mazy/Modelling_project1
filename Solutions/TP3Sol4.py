# set up our KalmanFilter object and tell it which parameters we want to
# estimate
np.random.seed(1)

n_dim_obs = 2
n_dim_state = 2

kf = pykalman.KalmanFilter(
  n_dim_state=n_dim_state,
  n_dim_obs=n_dim_obs,
  em_vars=['transition_matrices', 'transition_covariance',
           'observation_matrices', 'observation_covariance']
)