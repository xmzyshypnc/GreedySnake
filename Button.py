class Button(object):

    def __init__(self,lefttop_x,lefttop_y,rightbottom_x,rightbottom_y):
        self.left_top_x = lefttop_x
        self.left_top_y = lefttop_y
        self.right_bottom_x = rightbottom_x
        self.right_bottom_y = rightbottom_y

    def judge(self,point_x,point_y):

        if self.left_top_x < point_x and self.right_bottom_x > point_x:
            if self.left_top_y < point_x and self.right_bottom_y > point_y:
                return True
            else:
                return False
        else:
            return False
