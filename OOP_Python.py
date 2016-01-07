print "Class and object practice"

class Person(object):
    def getGender(self):
        return self.__class__.__name__

class Male( Person ):
    def getGender( self ):
        return self.__class__.__name__

class Female( Person ):
    def getGender( self ):
        return self.__class__.__name__

male = Male()
female = Female()
person = Person()

print male.getGender()
print female.getGender()
