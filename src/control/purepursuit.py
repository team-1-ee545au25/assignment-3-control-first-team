from __future__ import division
import numpy as np

from control.controller import BaseController
from control.controller import compute_position_in_frame


class PurePursuitController(BaseController):
    def __init__(self, **kwargs):
        self.car_length = kwargs.pop("car_length")

        # Get the keyword args that we didn't consume with the above initialization
        super(PurePursuitController, self).__init__(**kwargs)


    def get_error(self, pose, reference_xytv):
        """Compute the Pure Pursuit error.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed

        Returns:
            error: Pure Pursuit error
        """
        return compute_position_in_frame(reference_xytv[:3], pose)

    def get_control(self, pose, reference_xytv, error):
        """Compute the Pure Pursuit control law.

        Args:
            pose: current state of the vehicle [x, y, heading]
            reference_xytv: reference state and speed
            error: error vector from get_error

        Returns:
            control: np.array of velocity and steering angles
        """
        # BEGIN QUESTION 3.1
        v_ref = max(float(reference_xytv[3]), self.min_speed)

        x_L = float(error[0])
        y_L = float(error[1])

        L_d2 = x_L * x_L + y_L * y_L
        if L_d2 < 1e-9:
            return np.array([v_ref, 0.0])

        delta = np.arctan( (2.0 * self.car_length * y_L) / L_d2 )

        return np.array([v_ref, delta])


        # END QUESTION 3.1
