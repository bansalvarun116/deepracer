class Reward:
    def __init__(self):
        self.previous_steering_angle=0
        self.count=0

    def get_reward(self,params):
        if (not params['is_offtrack']) and params['steps']>0 :
            bonus=0 
            steering_bonus=0
            corner_reward=0
            waypoint = params['closest_waypoints'][0]
            speed= params['speed']
            steering_angle = params['steering_angle']
            if waypoint<18 or waypoint>204  or (waypoint>116 and waypoint<131) or (waypoint>160 and waypoint<169):
                if steering_angle == 0 :
                    if speed == 4 :
                        bonus = 20
                    else:
                        bonus = 10
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                else:
                    if speed == 4:
                        bonus = 10
                    elif speed>3:
                        bonus = 5
                    elif speed>2:
                        bonus = 1
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
            elif (waypoint > 28 and waypoint < 44) or (waypoint >180 and waypoint< 189 ):
                if steering_angle == 0 or steering_angle == 10:
                    if speed == 4 :
                        bonus = 20
                    else:
                        bonus = 15
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                else:
                    if speed == 4:
                        bonus = 15
                    elif speed>3:
                        bonus = 10
                    elif speed>2:
                        bonus = 2
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
            elif (waypoint >56 and waypoint< 65 ):
                if  steering_angle <= 0:
                    if speed  > 3 :
                        bonus = 20
                    elif speed > 2:
                        bonus = 15
                    else:
                        bonus = 5
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                    if(not params["is_left_of_center"]):
                        corner_reward=100
            elif (waypoint > 98 and waypoint < 145):
                if  steering_angle <= 0:
                    if speed  > 3 :
                        bonus = 20
                    elif speed > 2:
                        bonus = 15
                    else:
                        bonus = 5
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
            else:
                if  steering_angle >= 0:
                    if speed  > 3 :
                        bonus = 20
                    elif speed > 2:
                        bonus = 15
                    else:
                        bonus = 5
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                    if(params["is_left_of_center"]):
                        corner_reward=100
            if(steering_angle==self.previous_steering_angle):
                self.count=self.count+1
            else:
                self.previous_steering_angle=steering_angle
                self.count=0
            return   float(bonus*10  + corner_reward + steering_bonus)
        return (0.00001)
reward = Reward()
def reward_function(params):
    return reward.get_reward(params)