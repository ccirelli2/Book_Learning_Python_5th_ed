# Notes for Chapter 26



# Classes Described______________________________________________________________
'''
Description:         They are packages of functions that use and process built-in object types.
                     Containers for variables and where we can attach attributes. 
                     Similar to modules accept for the fact that objects in classes have auto-
                     matically searched links to other namespace objects, and
                     classes correspond to statements, not entire files. 
                     They are designed to create and manage new objects and support 'inheritance'
                     Another compartment to package logic and data.
                     Much like modules, classes define new namespaces. 
3 Critical Distinctions:
                     1.) Multiple Instances:  Classes are factories for generating one or
                         more objects. Every time we call a class we generate a new namespace. 
                         Each object created from a class has access to the class's attributes. 

                     2.) Customization via Inheritance:  Classes can build up namespace hierarchies
                         which define names to be used by objects create from classes in the 
                         hierarchy. 
                     3.) Operator Overloading:  By providing special protocol methods, classes can
                         define objects that respond to built-in-types. 

Object Model:        Classes and the instances you generate from them are two distinct object types. 

Inheritance:         Create an attribute for a class that can be inherited by all subclasses.
                     object.attribute:  'Find the first occurrence of attribute by looking in 'object'
                                        then in all classes above it, from bottom to top and left
                                        to right.'
                     In other words, attribute fetches are simply tree searches. 
Composition:         Composition is where one object contains other objects that it activates
                     to carry out tasks. Each component may be coded as a class, which in turn
                     defines its own behavior. 
                     
Methods:             Functions attached to classes as attributes.  
                     In the book the use the example of a class called I2 with an mothod .w. 
                     If this method '.w' is a function call, it is a function that is called on 
                     I2.  * This is an important concept.  The function is called on the object
                     itself.  Ex:  string.lowercase().  The function lowercase is called on the 
                     object, which belonds to the object class 'string'.
                     Call:  Methods can be called on either an instance of the class or the class
                     object itself. Ex:  'Today'.lowercase() and String.lowercase('Today')

OOP:                 Whenever we call a function attached to a class in this fashion, an instance
                     of the class is always implied.  "This implied subject or context is part
                     of the reason we refer to this as an 'object-orientated-model'.
                     This implied subject is passed by Ptyhon using a specia lfirst argument in the 
                     method called 'self'. 



__init__             https://micropyramid.com/blog/
                     understand-self-and-__init__-method-in-python-class/
                     - Looks like the initial attributes of the class that are input by the user
                     when first creating an instance of the clas object. 
'''


# Coding Class Trees______________________________________________________________________
'''
Method:             Function defined inside a class. 
                    Automatically receives a first argument called 'self'
                    ex:  def setname(self, who):
                            self.name = who

'''


# Creating A Class Method____________________________________________________________
'''
C1:                 The below code creates a class call C1.
                    It defines a method called set name, whose first input is self, and second
                    is who.  Inside this medthod, self has an attribute called name that refers
                    to who.  
                    Note that self is the object to which we are calling the name method. 
                    I1 we create an instance of the object C1().  
                    Then we call its method setname and define who as 'sue'. 
def                 def inside a class is called a method. 
'''

class C1():
    def set_first_name(self, who):
        self.first_name = who               # first_name is an attribute of C1. 
                                            # like recursively assigning a value to the class object. 
    def set_last_name(self, who):
        self.last_name = who

I1 = C1()

# Use the Method to Assign a Value to the Attribute 'first_name' & 'last_name'
I1.set_first_name('sue')         # calling the C1 method 'set_first_name' and passing to it a
                                 # value for who. 
I1.set_last_name('ford')

# Call the Attribute of the Class by its name and get the value back of that attribute
print(I1.first_name, I1.last_name)

'''
Method:             Instructions for how an attribute works and is assigned a value. . 
Attribute:          Value that has been assigned to our class and can be called upon after created to 
                    return this value. 

'''




















