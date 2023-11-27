# Importation library math
import math
# Super class Vector 2D
class Vector2D:

# Initialisation
    NBV = 0

# Parametric constracter 
    def __init__(self, X, Y):
        self.__X = X
        self.__Y = Y
        Vector2D.NBV += 1
    
# Method that compare the abscissa and the ordinates of vector
    def Equals(self):
        if(self.__X == self.__Y):
            return True
        else:
            return False 

# Method that return the value of the abscissa and the ordanates vector
    def ToString(self):
        return "X = "+str(self.__X)+"\nY = "+str(self.__Y  )
 
# Method that calculate the norm of vector
    def _Norm(self):
        return math.sqrt(pow(self.__X,2)+pow(self.__Y,2))

# Getters of abscissa and ordanates
    def GetX(self):
        return self.__X

    def GetY(self):
        return self.__Y
    
# Setters of abscissa and ordanates 
    def SetX(self, NewX):
        self.__X = NewX

    def SetY(self, NewY):
        self.__Y = NewY

# Child class Vector3D
class Vector3D(Vector2D):
    def __init__(self, X, Y, Z):
        Vector2D.__init__(self,X,Y)
        self.__Z = Z

# Method that compare the abscissa and the ordinates and dimension Z of vector
    def Equals(self):
        if(Vector2D.GetX(self) == Vector2D.GetY(self) == self.__Z):
            return True
        else:
            return False 

# Method that return the value of the aabscissa and the ordanates vector
    def ToString(self):
        return Vector2D.ToString(self)+"\nZ = "+str(self.__Z)

# Method that calculate the norm of vector
    def _Norm(self):
        return super()._Norm()


# Test of the program 
V1 = Vector2D(20,65)
print(V1.Equals())
print(V1.ToString())
print(V1._Norm())

V2 = Vector3D(10,10,10) 
print(V2.Equals())
print(V2.ToString())
print(V2._Norm())
