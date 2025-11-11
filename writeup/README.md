# Project 3: Control [![tests](../../../badges/submit-proj3/pipeline.svg)](../../../pipelines/submit-proj3/latest)

Replace this with your own writeup! Please place all figures in this directory.

Q2:
pid:
  kp: 0.05
  kd: 0.95


Q3:
pid:
  kp: 0.05
  kd: 0.95
pp:
  distance_lookahead: 0.7
mpc:
  K: 2
  T: 1

In order to reduce the curvature of robot following the reference path, I had to increase the distance_lookahead step by step. Initial Ld value was 0.1, and i increased to 0.5. THis value had less curvature error, but keep spinning around at the end of reference path. I had to increase to 0.7, which gave us small curvature and good stopping point at the end of the reference path.

Additional Answer:
PP_small (distance lookahead = 0.1): The model became very responsive where it takes aggressive turns. It seems like its overreacting to every curves.

pp_large (distance lookahead = ): The model became smoother and more stable to track. but wider turning radius.

Circle Radius Answer:
While 5m radius gave a proper modeling, 0.5 radius was not feasible to track. When the radius is big enough, then prediction doesn't oversteer. s