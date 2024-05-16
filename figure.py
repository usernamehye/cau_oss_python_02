"""
__length의 기본값은 1이다.
생성자를 통해 지정받은 __length의 값이 int 혹은 float 타입이 아니거나 0 이하일 경우 기본/이전 값을 유지한다.
매개변수의 타입 Line 클래스가 아닌 경우 값으로 0을 반환한다.
n은 __length로 받는 값이다.
"""
import math
class Line:
    __length=1

    def __init__(self,initial_value):
        if (type(initial_value)== int or type(initial_value)==float) and initial_value>0:
            self.__length=initial_value
        else:
            pass


    def set_length(self, value):
        if (type(value)== int or type(value)==float) and value>0:
            self.__length = value
        else:
            pass

    def get_length(self):
        return self.__length

def area_square (n):     
    """
    length^2의 넓이 반환
    """
    if type(n)!=Line:
        return 0
    else:
        num = n.get_length()
        return num**2

def area_circle (n):    
    """
    length^2*파이의 원의 넓이 반환
    """
    if type(n)!=Line:
        return 0
    else:
        num = n.get_length()
        return (num**2)*math.pi

def area_regular_triangle (n):   
    """
    (루트3)/4*length^2의 정삼각형의 넓이 반환
    """
    if type(n)!=Line:
        return 0
    else:
        num = n.get_length()
        return (math.sqrt(3)/4)*(num**2)
