class Vector:
    '''
    Should take any number of args XOR an iterable
    Turn the iterable into args
    Have scalar + dot + cross product (cross product = 3D)
    '''

    '''
    Attibutes:
        components
        '''
    def __init__(self, name, x, y, z=None):
    '''TODO: implement many arg vectors'''

    def scalar_product(self, scalar):
        self.x = scalar * self.x
        self.y = scalar * self.y

    def dot_product(self, vec):
        '''take the dot product of self and another vector'''
        return self.x * vec.x + self.x * vec.y

    def cross_product(self, vec):
        '''take the cross product of self and another vector'''
    
class Matrix:
    '''
    Initialize as a nested array or (optional) nested iterable or a vector
    Have matrix multiplication (use dot product operator)
    Have scalar multiplication
    Have componentwise addition + multiplication 
    Have transposition as a property (learn how to use @property)
    Have class properties which generate idenity matricies
    (optional) Inversion of a matrix
    '''
    pass