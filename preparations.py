# Import libraries
## Basic libs
import pandas as py
import numpy as np
import warnings

## Data visualisation
import seaborn as sns
import matplotlib.pyplot as plt 

# Configure libraries
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = (10,10)
plt.style.use('seaborn-v0_8-darkgrid')
print(f"pandas version: {py.__version__}")