# first install pip. Pip is a separate python file . Recommended websites are https://pip.pypa.io/en/stable/installing/
#https://matthewhorne.me/how-to-install-python-and-pip-on-windows-10/
import pip 

# Check if pip is installed by running this on command line
# pip
# You might have to set environment variables for python. 

#See the difference below

#*** Run from command line*** #pip install pandas
#After running pandas you will see packages being downloaded
import pandas as pd
#ex
s=pd.Series([1, 3, 5, 6, 8]) 
# To automate the process if we deploy this on our servers
import os

# It sends commands to command prompt
os.system('pip install numpy')
os.system('pip list')

import numpy as np
import scipy as sp
from scipy import special, optimize
f = lambda x: -special.jv(3, x)
sol = optimize.minimize(f, 1.0)


x=np.linspace(0,10,5)

# above code was an indication that we successfully installed 





