




# A First Example:
'''
def:            Assigns function objects to the names setdata and display in the class' scope. 
methods:        Functions defined inside a class. 
self.data:      Ensures that the attribute value 'data' is assigned to 'self', which refers to 
                each instance of the class created.  This means that the value we assigned to 
                data exists only in the namespace of each instance of the class and not the
                class itself. 
'''

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)


# Instance Creation Example
'''
():             By calling the class with paranthesis we are creating instances of that class. 
'''
x = FirstClass()
y = FirstClass()
print(type(x))


# Assign Value to Attribute
x.setdata('King Arthur')
x.display()



# Super Classes:
'''
Creation:       By passing other class objects to the super class in the class header. 
Ex              def superclass(subclass1, subclass2, subclass3): 


Customization:  By redefining superclass names in subclasses lower in the hierarchy (class tree)
                subclasses replace and thus customize inherited behavior. 
'''


# Second Example:
'''
Customization:  This is an example of customization and inheritance.  
                By giving 'display' the same name as the method in the super class, we have
                modified this function for the SecondClass. This approach of redefining
                methods of a class is sometimes call ''overloading''.

Important:      Why didn't we define setdata in SecondClass?  What data will SecondClass display?
                Answer:  We don't need to define it as setdata is inherited from FirstClass. 
                By passing FirstClass at the top level of SecondClass we ensure that SecondClass
                inherits these attributes from FirstClass. 

'''


class SecondClass(FirstClass):
    def display(self):
        print('Current value = {}'.format(self.data))

x = SecondClass()
x.setdata('Shit balls')
x.display()




# Continue page 831 'Classes Can Intercept Python Operators'









