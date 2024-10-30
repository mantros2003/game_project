import math

def detect_collision_2d_tol(obj1x, obj1y, obj2x, obj2y, tol):
    if math.pow(obj1x - obj2x, 2) + math.pow(obj1y - obj2y, 2) < pow(tol, 2):
        return True
    return False

def detect_collision_edge(rect1, rect2):
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