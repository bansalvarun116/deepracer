def reward_function(params):
    if (not params['is_offtrack']) and params['steps']>0 :
        reward = params['progress']/params['steps']*100 + (params['speed']**2)*5
        if params['speed'] == 4:
            bonus = 200
        elif params['speed'] >3 :
            bonus = 150
        elif params['speed'] > 2 :
            bonus = 100
        else:
            bonus = 0 
        return float(reward+bonus)
    return (0.00001)