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
        # BEGIN QUESTION 2.1
        v_ref = reference_xytv[3]
        e_ct = error[1]
        theta = pose[2]
        theta_ref = reference_xytv[2]
        # heading difference wrapped to (-pi, pi)
        heading_err = np.arctan2(np.sin(theta - theta_ref), np.cos(theta - theta_ref))

        # analytic derivative: ȧe_ct = v * sin(theta - theta_ref)
        e_ct_dot = v_ref * np.sin(heading_err)
        delta = (-self.kp * e_ct) - (self.kd * e_ct_dot)
        return np.array([v_ref, delta])
        # END QUESTION 2.1
