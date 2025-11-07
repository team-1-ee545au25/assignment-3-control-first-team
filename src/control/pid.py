from __future__ import division
import numpy as np

from control.controller import BaseController
from control.controller import compute_position_in_frame


class PIDController(BaseController):
    def __init__(self, **kwargs):
        self.kp = kwargs.pop("kp")
        self.kd = kwargs.pop("kd")

        # Get the keyword args that we didn't consume with the above initialization
        super(PIDController, self).__init__(**kwargs)


    def get_error(self, pose, reference_xytv):
        """Compute the PD error.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed

        Returns:
            error: across-track and cross-track error
        """
        return compute_position_in_frame(pose, reference_xytv[:3])

    def get_control(self, pose, reference_xytv, error):
        """Compute the PD control law.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed
            error: error vector from get_error

        Returns:
            control: np.array of velocity and steering angle
                (velocity should be copied from reference velocity)
        """
        # QUESTION 2.1
	cross_track_error = error[1]
	heading_error = pose[2] - reference_xytv[2]
	heading_error = np.arctan2(np.sin(heading_error), np.cos(heading_error))

	# Velocity gains
	v_ref = reference_xytv[3]
	kp_scaled = self.kp * v_ref
        
	# PD control law
	steering_angle = -kp_scaled * cross_track_error - self.kd * heading_error

	# Saturation limits
	max_steering = np.deg2rad(30)
	steering_angle = np.clip(steering_angle, -max_steering, max_steering)

	velocity = v_ref
	
	return np.array([velocity, steering_angle])
        # END QUESTION 2.1
