#마우스의 객체를 만들어보자
class Mouse:
    def __init__(self, color,material):
        self.color =  color
        self.material = material
    def Mouse(self):
        print('마우스의 특징')
        myMouse = Mouse('black', 'steal')
        print('마우스 의 색상:{Mouse.black()}')
        print('마우스 의 재료:{Mouse.plastic()}')
