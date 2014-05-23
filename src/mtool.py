import numpy as np

def norpdf(x,mean, scaling, sigma):
    return (scaling/2)*np.exp(-0.5 * (1./sigma*(x - mean))**2)

def lorenpdf(x , mean, scaling, gamma):
	return (scaling/2)*1./(np.pi*gamma*(1+((x-mean)/gamma)**2))
