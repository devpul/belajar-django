# function , definition
def my_function():
    print('my_function berhasil jalan.')
    
# arguments *args
def my_function(*kids):
    print("The younges child is " + kids[2])
    
# arguments **kwargs
def my_function(nilai1, nilai2, nilai3):
    print('halo')
    
my_function(nilai3=100, nilai2=50, nilai3=25)