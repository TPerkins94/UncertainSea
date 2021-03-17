#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 07:33:37 2021

@author: joncka

Description: This code extracts the estimated "extreme sea levels" and 
corresponding confidence bounds for different return periods for the 
user-specified location with name 'loc_name'. It also extracts the same data 
for the user-specifed rcp (26, 45 or 85) and time (2025, 2055, 2100).
"""

import pandas as pd
import numpy as np

#----------------------------Parameters to specify----------------------------#
loc_name = 'TheMumbles' #location name ['Newport', 'TheMumbles']
t = 2025 #Time [2025, 2055, 2100] 
rcp = 45 #RCP [26,45,85] 
#-----------------------------------------------------------------------------#

#-------------------Extract present-time extreme sea levels-------------------#
#Get all data from github as (pandas multiindex dataframe)
url = 'https://raw.githubusercontent.com/TPerkins94/UncertainSea/main/' + loc_name + '_present_ea_sea_levels.pkl'
df_ea = pd.read_pickle(url)

#Put data into pandas dataframe
dat = np.concatenate((df_ea.loc[2.5].values, df_ea.loc[50].values, df_ea.loc[97.5].values), axis=1)
df_present = pd.DataFrame(index = df_ea.loc[2.5].index, columns = ['lower', 'middle', 'upper'], data=dat)
#-----------------------------------------------------------------------------#


#----------------------Extract future extreme sea levels----------------------#
#Get all data from github as (pandas multiindex dataframe)
url = 'https://raw.githubusercontent.com/TPerkins94/UncertainSea/main/' + loc_name + '_future_ea_plus_ukcp18_sea_levels.pkl'
df_ukcp = pd.read_pickle(url)

#Put data into pandas dataframe
dat = np.vstack((df_ukcp.loc[5,rcp,:][t].values, df_ukcp.loc[50,rcp,:][t].values, df_ukcp.loc[95,rcp,:][t].values)).transpose()
df_future = pd.DataFrame(index = df_ea.loc[2.5].index, columns = ['lower', 'middle', 'upper'], data=dat)
#-----------------------------------------------------------------------------#

#You can now access present day or future sea levels for a specified return 
#period using pandas indexing. e.g. to get the present-day upper-bound for a 
#return period of 200 years:
sea_level = df_present.loc[200,'upper']

#Or the middle estimate of the 75 year retrun period sea level for the future:
sea_level = df_future.loc[75,'middle']
