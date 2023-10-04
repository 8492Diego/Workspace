import math

class Shape():
    def __init__(self, n):
        self._n = n

    def getNumber(self):
        return self._n
    
class Point(Shape):

    def __init__(self,n,x,y):
        self._n= n
        self._x= x
        self._y= y


    def updateCoord(self,x,y):
        self._x= x
        self._y= y

    
    def getType(self):
        return 'Point_'
    

    def printCoord(self):
        print(f'\nO ponto {self._n} possui as coord: ({self._x}, {self._y}).')

    def distance(self, other):
        return math.sqrt((self._x-other._x)**2 + (self._y-other._y)**2)
    
    def __str__(self):
        return f'({self._x}, {self._y})'



class Circle(Point):
    
    """ O círculo herda do ponto suas funcionalidades e adiciona raio"""
    """ É necessário definir as funções membro para o círculo operar"""
    
    def __init__(self,n,x,y,radius):
        
        super().__init__(n, x, y)
        self.radius= radius
        
    
    def getType(self):
        """ Atencção!!! Polimorfismo aplicado"""
        return 'Circle_'
        
    
    def updateCoord(self,x,y,radius):
        
        super().updateCoord(x, y)
        self.radius= radius

    
    def printCoord(self):
        
        print(f'\nO círculo {self._n} possui origem em: ({self._x}, {self._y})')
        print(f'E o seu raio é {self.radius}')
        
    
    def pointIn(self,pt):
        """ Verifica se o ponto está dentro deste círculo"""
        return self.distance(pt) < self.radius
            
    
    
    def area(self):
        """ calcula a área deste circulo e mostra no terminal"""
        return math.pi*self.radius**2
    

    def perimeter(self):
        return 2*math.pi*self.radius
    
    
    def my_function(self):
        """ defina mais funções de seu interesse aqui"""
        pass
    

class Line(Shape):
    
    """ implementar a linha com dois pontos internos"""
    def __init__(self, n, x1, x2, y1, y2):
        self._p1 = Point(1,x1,y1)
        self._p2 = Point(2,x2,y2)
        self._n = n

    """ definir funções membro e quaisquer outros atributos da classe""" 
    def getType(self):
        return 'Line_'
    

    def updateCoord(self, x1, x2, y1, y2):
        self._p1.updateCoord(x1,y1)
        self._p2.updateCoord(x2,y2)
        return
     
    def slope(self):
        return (self._p1._y-self._p2._y)/(self._p1._x-self._p2._x)

    
    def lenght(self):
        return self._p1.distance(self._p2)
    
    def printCoord(self):
        print(f'\nA linha {self._n} é definida pelos pontos: ({self._p1}, {self._p2}).')
    

class Triangle(Shape):

    def __init__(self, n, x1, y1, x2, y2, x3, y3):
        self._p1 = Point(1,x1,y1)
        self._p2 = Point(2,x2,y2)
        self._p3 = Point(3,x3,y3)
        self._n = n
    
    def perimeter(self):
        return self._p1.distance(self._p2) + self._p2.distance(self._p3) + self._p3.distance(self._p1)
    
    def area(self):
        p = self.perimeter()/2
        return math.sqrt(p*(p-self._p1.distance(self._p2))*(p-self._p2.distance(self._p3))*self._p3.distance(self._p1))
    
    def getType(self):
        return 'Triangle_'