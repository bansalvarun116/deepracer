class WRmapping():
    def __init__(self):
        self.waypoint_reward_mapping = {0: 1,
 1: 1,
 2: 1,
 3: 1,
 4: 1,
 5: 1,
 6: 1,
 7: 1,
 8: 1,
 9: 1,
 10: 1,
 11: 1,
 12: 1,
 13: 1,
 14: 1,
 15: 1,
 16: 1,
 17: 2,
 18: 2,
 19: 2,
 20: 3,
 21: 3,
 22: 3,
 23: 3,
 24: 3,
 25: 3,
 26: 3,
 27: 3,
 28: 3,
 29: 4,
 30: 4,
 31: 4,
 32: 4,
 33: 4,
 34: 4,
 35: 4,
 36: 4,
 37: 4,
 38: 4,
 39: 4,
 40: 4,
 41: 4,
 42: 2,
 43: 2,
 44: 2,
 45: 3,
 46: 3,
 47: 3,
 48: 3,
 49: 3,
 50: 3,
 51: 3,
 52: 5,
 53: 5,
 54: 5,
 55: 5,
 56: 5,
 57: 5,
 58: 6,
 59: 6,
 60: 6,
 61: 6,
 62: 6,
 63: 6,
 64: 2,
 65: 2,
 66: 2,
 67: 2,
 68: 2,
 69: 3,
 70: 3,
 71: 3,
 72: 3,
 73: 3,
 74: 3,
 75: 3,
 76: 3,
 77: 3,
 78: 3,
 79: 3,
 80: 3,
 81: 4,
 82: 4,
 83: 4,
 84: 4,
 85: 4,
 86: 2,
 87: 2,
 88: 2,
 89: 3,
 90: 3,
 91: 3,
 92: 3,
 93: 3,
 94: 3,
 95: 3,
 96: 5,
 97: 5,
 98: 5,
 99: 5,
 100: 6,
 101: 6,
 102: 6,
 103: 6,
 104: 6,
 105: 6,
 106: 6,
 107: 6,
 108: 6,
 109: 6,
 110: 6,
 111: 6,
 112: 6,
 113: 6,
 114: 1,
 115: 1,
 116: 1,
 117: 1,
 118: 1,
 119: 1,
 120: 1,
 121: 1,
 122: 1,
 123: 1,
 124: 1,
 125: 1,
 126: 1,
 127: 1,
 128: 1,
 129: 1,
 130: 1,
 131: 5,
 132: 5,
 133: 5,
 134: 5,
 135: 6,
 136: 6,
 137: 6,
 138: 6,
 139: 6,
 140: 6,
 141: 6,
 142: 6,
 143: 6,
 144: 3,
 145: 3,
 146: 3,
 147: 3,
 148: 3,
 149: 3,
 150: 3,
 151: 3,
 152: 3,
 153: 3,
 154: 3,
 155: 3,
 156: 3,
 157: 3,
 158: 1,
 159: 1,
 160: 1,
 161: 1,
 162: 1,
 163: 1,
 164: 1,
 165: 1,
 166: 1,
 167: 2,
 168: 2,
 169: 2,
 170: 2,
 171: 2,
 172: 3,
 173: 3,
 174: 3,
 175: 3,
 176: 3,
 177: 3,
 178: 3,
 179: 1,
 180: 1,
 181: 1,
 182: 1,
 183: 1,
 184: 1,
 185: 1,
 186: 1,
 187: 2,
 188: 2,
 189: 2,
 190: 3,
 191: 3,
 192: 3,
 193: 3,
 194: 3,
 195: 3,
 196: 5,
 197: 5,
 198: 5,
 199: 5,
 200: 5,
 201: 5,
 202: 5,
 203: 5,
 204: 1,
 205: 1,
 206: 1,
 207: 1,
 208: 1,
 209: 1,
 210: 1,
 211: 1,
 212: 1,
 213: 1,
 214: 1,
 215: 1,
 216: 1,
 217: 1,
 218: 1,
 219: 1,
 220: 1,
 221: 1,
 222: 1,
 223: 1,
 224: 1,
 225: 1,
 226: 1,
 227: 1,
 228: 1,
 229: 1,
 230: 1,
 231: 1,
 232: 1,
 233: 1,
 234: 1,
 235: 1,
 236: 1,
 237: 1,
 238: 1,
 239: 1,
 240: 1,
 241: 1,
 242: 1,
 243: 1,
 244: 1,
 245: 1,
 246: 1,
 247: 1,
 248: 1,
 249: 1,
 250: 1,
 251: 1,
 252: 1,
 253: 1,
 254: 1,
 255: 1,
 256: 1,
 257: 1,
 258: 1,
 259: 1,
 260: 1,
 261: 1,
 262: 1,
 263: 1,
 264: 1,
 265: 1,
 266: 1,
 267: 1,
 268: 1,
 269: 1,
 270: 1,
 271: 1,
 272: 1,
 273: 1,
 274: 1,
 275: 1,
 276: 1,
 277: 1,
 278: 1,
 279: 1,
 280: 1,
 281: 1,
 282: 1,
 283: 1,
 284: 1,
 285: 1,
 286: 1,
 287: 1,
 288: 1,
 289: 1,
 290: 1,
 291: 1,
 292: 1,
 293: 1,
 294: 1,
 295: 1,
 296: 1,
 297: 1,
 298: 1,
 299: 1}
 
 
wrmapping =WRmapping()

def straight_path_super_fast(speed,steering_angle,is_left_of_center):
    bonus=0
    corner_reward=0
    if steering_angle == 0:
        if speed ==4:
            bonus =200
        else:
            bonus = 50
    elif abs(steering_angle) == 10:
        if speed == 4:
            bonus = 50
    else:
        return (True,0.0001)
    return (False, bonus)

def slowing_down_before_left_curve(speed,steering_angle,is_left_of_center):
    bonus=0
    corner_reward=0
    if steering_angle == 0 or steering_angle == 10:
        if speed ==4:
            bonus = 200
        elif speed >3:
            bonus = 150
        if(is_left_of_center):
            corner_reward=100
    elif steering_angle >10:
        if speed > 2:
            bonus = 50
        if(is_left_of_center):
            corner_reward=100
    elif steering_angle < 0:
        return (True,0.00001)
    return(False, bonus+corner_reward)

def slowing_down_before_right_curve(speed,steering_angle,is_left_of_center):
    bonus=0
    corner_reward=0
    if steering_angle == 0 or steering_angle == -10:
        if speed ==4:
            bonus = 200
        elif speed >3:
            bonus = 150
        if(not is_left_of_center):
            corner_reward=100
    elif steering_angle < -10:
        if speed > 2:
            bonus = 50
        if(not is_left_of_center):
            corner_reward=100
    elif steering_angle > 0:
        return (True,0.00001)
    return(False, bonus+corner_reward)

def left_turn(speed,steering_angle,is_left_of_center):
    bonus=0
    corner_reward=0
    if steering_angle > 10:
        if speed >2:
            bonus = 200
        else:
            bonus = 100
        if(is_left_of_center):
            corner_reward=100
    elif steering_angle == 10:
        if speed >3:
            bonus =100
        else:
            bonus = 50
        if(is_left_of_center):
            corner_reward=100
    elif steering_angle <0:
         return (True,0.00001)
    return(False, bonus+corner_reward)

def right_turn(speed,steering_angle,is_left_of_center):
    bonus=0
    corner_reward=0
    if steering_angle < -10:
        if speed >2:
            bonus = 200
        else:
            bonus = 100
        if(not is_left_of_center):
            corner_reward=100
    elif steering_angle == -10:
        if speed >3:
            bonus =100
        else:
            bonus = 50
        if(not is_left_of_center):
            corner_reward=100
    elif steering_angle <0:
         return (True,0.00001)
    return(False, bonus+corner_reward)

def slight_curved_path(speed,steering_angle,is_left_of_center):
    bonus=0
    corner_reward=0
    if steering_angle == 0 or steering_angle == 10:
        if speed ==4:
            bonus = 200
        elif speed >3:
            bonus = 150
    elif steering_angle >10:
        if speed > 2:
            bonus = 50
    elif steering_angle < 0:
        return (True,0.00001)
    return(False, bonus+corner_reward)
        
def reward_function(params):
    if (not params['is_offtrack']) and params['steps']>0 :
        waypoint_reward_mapping = wrmapping.waypoint_reward_mapping
        waypoint = params['closest_waypoints'][0]
        speed= params['speed']
        steering_angle = params['steering_angle']
        reward = params['progress']/params['steps']*100 + (params['speed']**2)*5
        bonus =0
        bonus_func_index= waypoint_reward_mapping.get(waypoint)
        if bonus_func_index ==1:
            punishment,bonus  = straight_path_super_fast(speed,steering_angle,params['is_left_of_center'])
            if punishment :
                return 0.00001
            else:
                return  reward + bonus
                
        elif bonus_func_index == 2:
            punishment,bonus  = slowing_down_before_left_curve(speed,steering_angle,params['is_left_of_center'])
                
            if punishment :
                return 0.00001
            else:
                return  reward + bonus
                
        elif bonus_func_index == 3:
            punishment,bonus  = left_turn(speed,steering_angle,params['is_left_of_center'],)
            
            if punishment :
                return 0.00001
            else:
                return  reward + bonus
        elif bonus_func_index == 4:
            punishment,bonus = slight_curved_path(speed,steering_angle,params['is_left_of_center'])
            if punishment :
                return 0.00001
            else:
                return  reward + bonus
        elif bonus_func_index == 5:
            punishment,bonus  = slowing_down_before_right_curve(speed,steering_angle,params['is_left_of_center'])
            
            if punishment :
                return 0.00001
            else:
                return  reward + bonus
        elif bonus_func_index == 6:
            punishment,bonus  = right_turn(speed,steering_angle,params['is_left_of_center'])
            
            if punishment :
                return 0.00001
            else:
                return  reward + bonus
        
        
        
    return 0.00001