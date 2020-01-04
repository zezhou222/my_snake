

# 矩形碰撞检测
def collision_detection(obj1, obj2):
    # 矩形的碰撞检测
    if obj2.x < obj1.x + obj1.return_surface().get_width() and obj2.y < obj1.y + obj1.return_surface().get_height() and obj2.x + obj2.return_surface().get_width() > obj1.x and obj2.y + obj2.return_surface().get_height() > obj1.y:
        return True
    return False

