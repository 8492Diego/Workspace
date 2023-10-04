from Biblioteca.Formas import *
from Biblioteca.Plano_Cartesiano import *

def main():
    plano = CartesianBoard()
    plano.inserShape(Point(1,0,1))
    plano.inserShape(Circle(1,2,3,9))
    plano.inserShape(Line(1,7,8,9,3))
    plano.inserShape(Triangle(1,5,6,2,3,4,8))

    pt1= Point(1,12,54)
    pt1.printCoord()
    
    
    circ2= Circle(2, 13, 15, 4)
    circ2.printCoord()
    
   
    dashboard= CartesianBoard()
    dashboard.inserShape(pt1)
    dashboard.inserShape(circ2)
    
    dashboard.showShapes()
    
    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()
    
    print('\nRemoção de uma das formas!')
    
    dashboard.removeShape(pt1)
    dashboard.showShapes() 
    
    print('\nOs detalhes de cada forma podem ser observados abaixo:')
    dashboard.printDetails()
    
    
    print('\nVamos pegar uma das formas e atualizar:')
    
    my_copy_of_circ2= dashboard.getShape('Circle_2')
    my_copy_of_circ2.updateCoord(17,22,5)
    my_copy_of_circ2.printCoord()
    
    print('\nO objeto original:')
    circ2.printCoord()
    
    print('\nNote que a atualização da cópia alterou o objeto original!')    
    
    print("\nSuccessful exit")

if __name__ == "__main__":

    main()