# Given an integral number, determine if it's a square number:
# In mathematics, a square number or perfect square is an integer that is the square of an integer; 
# in other words, it is the product of some integer with itself.
# 
# The tests will always use some integral number, so don't worry about that in dynamic typed languages.

def is_square(n):

    square_flag = False

    if(n < 0):
        return False
    elif(n==0):
        return True
    else:
        for num in range(1,n):
            
            if ( (num * num) > n):
                break
            elif((num * num) == n):
                square_flag = True
    return square_flag # fix me