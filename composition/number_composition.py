composition_set = set()

def numbers_generator(k_pos,tup,n):
    if k_pos > len(tup)-1:
        return
    tup[k_pos]=1
    while tup[k_pos]<= n:
        gen(k_pos+1,tup,n)
        #print(tup)
        check_for_sum(tup,n)
        if tup[k_pos]+1 <= n:
            tup[k_pos] = tup[k_pos]+1
        else:
            return

def check_for_sum(arr,n):
    if sum(arr) == n:
        composition_set.add(tuple(arr))


def compositions(k, n):
    # inputs: k and n are of type 'int'
    # output: a set of tuples
    numbers_generator(0,np.ones([1,k],dtype=np.int8).ravel(),n)
    return composition_set
    
print(compositions(3, 7))
len(composition_set)


#################################################################################################

# finding number of compositions for a given number with binomial theorm

import math
def binomial(k,n):
    fun = math.factorial
    return fun(n-1)/(fun(k-1)*fun(n-1-k+1))
    
print(binomial(3,10))    
