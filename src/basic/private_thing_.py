# Private Variable
#Single underscore (_)
class test:
    def __init__(self,num):
        self._num= num
#_privatemethod private method
    def _numfunc(self):
        print("Hello")
obj=test(156)
#_ attributes can be accessed as normal variables
obj._numfunc()