# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:13:32 2016

@author: juliaroquette

calcula amplitudes para manchas
"""
import numpy as np
#from astropy import units as u
from astropy.analytic_functions import blackbody_lambda#, blackbody_nu
# blackbody_lambda(in_x, temperature) return flux

Teff1=3000.
Teff2=4000.



def Aspot(Teff,Tspot,lb,f):
    return -2.5*np.log10(blackbody_lambda(lb,Teff)/(f*blackbody_lambda(lb,Tspot)+(1.-f)*blackbody_lambda(lb,Teff)))

def inclinations(Teff,Tspot,f):
    J=1.2483*(10**(4)) #em angstrom
    H=1.6313*(10**(4))
    K=2.2010*(10**(4))
    aJ=Aspot(Teff1,Tspot,J,f)
    aH=Aspot(Teff1,Tspot,H,f)
    aK=Aspot(Teff1,Tspot,K,f)
#    print 'J-H vs H-K inclination:',np.arctan((aJ-aH)/(aH-aK))*180./np.pi
#    print 'K vs H-K inclination:',np.arctan((aK)/(aH-aK))*180./np.pi    
#    print 'J vs J-H inclination:',np.arctan((aJ)/(aJ-aH))*180./np.pi
    return np.arctan((aJ-aH)/(aH-aK))*180./np.pi,np.arctan((aK)/(aH-aK))*180./np.pi,np.arctan((aJ)/(aJ-aH))*180./np.pi

#def AspotCarpenter(Teff,Tspot,lb,f):
#    return -2.5*np.log10(1-f*(1.0-blackbody_lambda(lb,Tspot)/blackbody_lambda(lb,Teff)))
    
J=1.2483*(10**(4)) #em angstrom
H=1.6313*(10**(4))
K=2.2010*(10**(4))


#Estrela com 3000K
Teff=3000.
Tspot=np.array([2000.,3000.,3800.,4200.,8000.,12000.])
f=np.array([.01,.05,.12,.3])

for i in range(len(Tspot)):
    for j in range(len(f)):
        

#
#print 'Star with:'
#print 'Teff= 3000K'
#print 'Spot coverage= 0.1'
#f=0.1
#print 'Tspot=8000'
#Tspot=8000. #(5000-12000)
##print 'J= ',Aspot(Teff1,Tspot,J,f),AspotCarpenter(Teff1,Tspot,J,f)
##print 'H= ',Aspot(Teff1,Tspot,H,f),AspotCarpenter(Teff1,Tspot,H,f)
##print 'K= ',Aspot(Teff1,Tspot,K,f),AspotCarpenter(Teff1,Tspot,K,f)
#print 'J= ',Aspot(Teff1,Tspot,J,f)
#print 'H= ',Aspot(Teff1,Tspot,H,f)
#print 'K= ',Aspot(Teff1,Tspot,K,f)
#inclinations(Teff1,Tspot,J,f)
#print 'Star with:'
#print 'Teff= 3000K'
#print 'Spot coverage= 0.3'
#f=0.3
#print 'Tspot=2000'
#Tspot=2000. #(5000-12000)
##print 'J= ',Aspot(Teff1,Tspot,J,f),AspotCarpenter(Teff1,Tspot,J,f)
##print 'H= ',Aspot(Teff1,Tspot,H,f),AspotCarpenter(Teff1,Tspot,H,f)
##print 'K= ',Aspot(Teff1,Tspot,K,f),AspotCarpenter(Teff1,Tspot,K,f)
#print 'J= ',Aspot(Teff1,Tspot,J,f)
#print 'H= ',Aspot(Teff1,Tspot,H,f)
#print 'K= ',Aspot(Teff1,Tspot,K,f)
#inclinations(Teff1,Tspot,J,f)