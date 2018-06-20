import numpy as np

def bivariable_polinomial(coeficients, sample_size=100, x0=0, xmax=100, mu=0, sigma=1):
	""" 
	Returns x, y numpy arrays in the form of
	
	[3, 4] --> ax + b  -->  3x + 4
	[3, 4, 5] --> ax^2 + bx + c --> 3x^2 + 4x + 5

	"""

	# there has to be a better way than to use numbers from 0 to xmax divided by sample size
    x = np.linspace(x0, xmax, sample_size, endpoint=True)
    error = np.random.normal(mu, sigma, sample_size)



    #initialize y as a np array of size=sample_size
    y = error
    
    # here we get the list of coeficients and for each one we will do
    # coeficient[i]*x^degree
    # since the enumerate function does not go down, we can make degree as coef.len() - i - 1

    length = len(coeficients)
    for degree, coef in enumerate(coeficients):
    	if length - degree > 1 :
    		y += coef*np.power(x, (length - degree - 1))
    	else:
    		y+= coef
    return x, y