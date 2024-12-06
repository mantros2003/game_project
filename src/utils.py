import math

def detect_collision_2d_tol(obj1x, obj1y, obj2x, obj2y, tol) -> bool:
    if math.pow(obj1x - obj2x, 2) + math.pow(obj1y - obj2y, 2) < pow(tol, 2):
        return True
    return False

def detect_collision_circle_2d(obj1_dict, obj2_dict) -> bool:
    center1 = (obj1_dict['x'] + obj1_dict['width']/2, obj1_dict['y'] + obj1_dict['height']/2)
    center2 = (obj2_dict['x'] + obj2_dict['width']/2, obj2_dict['y'] + obj2_dict['height']/2)

    if (center1[0] - center2[0])**2 + (center1[1] - center2[1])**2 <= ((obj1_dict['width'] + (obj2_dict['width']))**2)/4:
        return True
    return False

def detect_collision_edge(rect1, rect2) -> bool:
    # Calculate edges of rect1
    rect1_left = rect1['x']
    rect1_right = rect1['x'] + rect1['width']
    rect1_top = rect1['y']
    rect1_bottom = rect1['y'] + rect1['height']
    
    # Calculate edges of rect2
    rect2_left = rect2['x']
    rect2_right = rect2['x'] + rect2['width']
    rect2_top = rect2['y']
    rect2_bottom = rect2['y'] + rect2['height']

    # Check if there is any collision
    if (rect1_right > rect2_left and rect1_left < rect2_right and
        rect1_bottom > rect2_top and rect1_top < rect2_bottom):
        
        # Determine which edge is colliding based on minimal overlap distance
        overlap_left = rect1_right - rect2_left
        overlap_right = rect2_right - rect1_left
        overlap_top = rect1_bottom - rect2_top
        overlap_bottom = rect2_bottom - rect1_top

        # Find the smallest overlap to determine the edge of collision
        min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

        if min_overlap == overlap_left:
            return "right"
        elif min_overlap == overlap_right:
            return "left"
        elif min_overlap == overlap_top:
            return "bottom"
        elif min_overlap == overlap_bottom:
            return "top"
    
    return None

def detect_collsiosion_circular(px, py, objx, objy, r):
    if  math.pow(px - objx, 2) + math.pow(py - objy, 2) <  math.pow(r, 2) :
        return True
    else :
        return False

def dist(px, py, objx, objy):
    return (math.pow(px - objx, 2) + math.pow(py - objy, 2))**(0.5)


def solve_quadratic( a , b , c):
    D = b**2 - 4*a*c
    if D >= 0 :
        x1 = (-b + (D)**(0.5))/(2*a)
        x2 = (-b - (D)**(0.5))/(2*a)
        return (x1,x2)


def collision_correct( px, py, objx, objy, r  ):
    
    if (objx - px ) != 0 : 
        m =  (objy - py)/(objx - px)
        c1 = py - m*px

        a = 1+ m**2
        b = -2*objx + 2*m*(c1 - objy)
        c = objx**2 + (c1-objy)**2 - r**2
        
        Roots = solve_quadratic(a,b,c)

        y1 = m*Roots[0] + c1
        y2 = m*Roots[1] + c1
        
        if( ( dist( px , py , Roots[0], y1 ) < dist( px , py , Roots[1], y2 ) ) ):
                return ( Roots[0] , y1 )
        else :
                return ( Roots[1] , y2 )
      
    else :
        y1 = objy - r
        y2 = objy + r
        if( abs( py - y1) <= abs( py - y2) ):
                return ( px , y1 )
        else :
                return ( px , y2 )
      
def attack_direction(A,S,D,W):
    x = 0 
    y = 0 
    if( A ):
        x = x - 1 
    if( S ):
        y = y - 1
    if( D ):
        x = x + 1 
    if( W ):
        y = y + 1 
    return (x,y)
    
def is_valid_point( Screen_x , Screen_Y, given_x , given_y  ):
    
     print(given_x)
     if(given_x >=  0    ):
         return True 
     return False

def on_screen(x: int, y: int, display_size) -> bool:
    if x < -64 or x > display_size[0] or y < -64 or y > display_size[1]:
        return False
    return True