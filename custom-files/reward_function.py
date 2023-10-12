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
            steps_reward=0
            if waypoint<19 or waypoint>202  or (waypoint>160 and waypoint<171):
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
                if(params["is_left_of_center"]):
                        corner_reward=30
            elif (waypoint>116 and waypoint<132) :
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
                if(not params["is_left_of_center"]):
                        corner_reward=30
            elif (waypoint > 28 and waypoint < 44) or (waypoint >180 and waypoint< 189 ):
                if steering_angle == 0 or steering_angle == 10:
                    if speed == 4 :
                        bonus = 20
                    else:
                        bonus = 10
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                else:
                    if speed == 4:
                        bonus = 15
                    elif speed>3:
                        bonus = 8
                    elif speed>2.5:
                        bonus= 4
                    elif speed>2:
                        bonus = 2
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                if(params["is_left_of_center"]):
                        corner_reward=30
            elif (waypoint >56 and waypoint< 65 ):
                if  steering_angle <= 0:
                    if speed  > 3 :
                        bonus = 20
                    elif speed > 2.5:
                        bonus = 15
                    elif speed > 2:
                        bonus=12
                    elif speed>1.5:
                        bonus= 7
                    else:
                        bonus = 5
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                    if(not params["is_left_of_center"]):
                        corner_reward=100
            elif (waypoint > 98 and waypoint < 145):
                if  steering_angle < -10:
                    if speed >3:
                        bonus =5 
                    if speed  > 2.5:
                        bonus = 20
                    elif speed >2:
                        bonus = 18
                    elif speed >1.5:
                        bonus = 16
                    else:
                        bonus = 14
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                    if(not params["is_left_of_center"]):
                        corner_reward=100
            elif (waypoint >= 145 and waypoint<160):
                if  steering_angle > 10:
                    if speed >3:
                        bonus =5 
                    if speed  > 2.5:
                        bonus = 20
                    elif speed >2:
                        bonus = 18
                    elif speed >1.5:
                        bonus = 16
                    else:
                        bonus = 14
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                    if(params["is_left_of_center"]):
                        corner_reward=100
            else:
                if  steering_angle >= 0:
                    if speed  > 3 :
                        bonus = 20
                    elif speed > 2.5:
                        bonus = 15
                    elif speed > 2:
                        bonus=10
                    elif speed>1.5:
                        bonus= 5
                    else:
                        bonus = 2
                    if(steering_angle==self.previous_steering_angle):
                        steering_bonus=10*min(20,self.count)
                    if(params["is_left_of_center"]):
                        corner_reward=100
            if(steering_angle==self.previous_steering_angle):
                self.count=self.count+1
            else:
                self.previous_steering_angle=steering_angle
                self.count=0
            
            if params['progress'] ==100 and params['steps']<375:
                steps_reward=30000
            elif params['progress'] ==100 and params['steps']<400:
                steps_reward=25000
            elif params['progress'] ==100 and params['steps']<425:
                steps_reward=20000
            elif params['progress'] ==100 and params['steps']<450:
                steps_reward=15000
            elif params['progress'] ==100 and params['steps']<500:
                steps_reward=10000
            
            if params['progress'] >=55 and params['progress'] <56 and  params['steps']<200:
                steps_reward=5000
            elif params['progress'] >=55 and params['progress'] <56 and params['steps']<205:
                steps_reward=3000
            elif params['progress'] >=55 and params['progress'] <56 and params['steps']<210:
                steps_reward=2000
            elif params['progress'] >=55 and params['progress'] <56 and params['steps']<215:
                steps_reward=1000
            elif params['progress'] >=55 and params['progress'] <56 and params['steps']<220:
                steps_reward=500
                
            if (bonus*10  + corner_reward + steering_bonus+steps_reward) ==0:
                return 0.00001
            else:
                return float(bonus*10  + corner_reward + steering_bonus+steps_reward)
        return (0.00001)
reward = Reward()
def reward_function(params):
    return reward.get_reward(params)