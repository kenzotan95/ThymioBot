from pythymiodw import *
from pythymiodw import io
from pythymiodw.sm import *
from libdw import sm
from boxworld import thymio_world

class MySMClass(sm.SM):
    start_state= 0.05
    def get_next_values(self, state, inp):
        # These two lines is to stop the robot
        # by pressing the backward button.
        # This only works when using the real robot.
        # It will not work in simulator.
        if inp.button_backward:
            return 'halt', io.Action(0,0)
        #####################################

        #ground = inp.prox_ground.reflected
        #ground = inp.prox_ground.ambiant

        #ground = inp.prox_ground.delta
        #left = ground[0]
        #right = ground[1]
        #print(left,right)
        output = io.Action(fv = state, rv = -0.5)
        next_state = state + 0.005**9
        return next_state, output

    #########################################
    # Don't modify the code below.
    # this is to stop the state machine using
    # inputs from the robot
    #########################################
    def done(self,state):
        if state=='halt':
            return True
        else:
            return False

MySM=MySMClass()

############################

m=ThymioSMSim(MySM, thymio_world)
try:
    m.start()
except KeyboardInterrupt:
    m.stop()
