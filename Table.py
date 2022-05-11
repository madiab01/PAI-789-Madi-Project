# -*- coding: utf-8 -*-
"""
Created on Mon May  2 12:21:03 2022

@author: Madi
"""
import pandas as pd 

survey_q_v = ['CLG','CLC','DIV','CLH','RSI','FSI','FSG','FSV','FSP','FSC','MSI','MSH','MSD','MSS','MSM','ESA','ESI','GPS','GPT','GPE','RFS']

cdc_name_v = ['EPL_POV','EPL_UNEMP','EPL_PCI','SPL_THEME1','EPL_NOHSDP','RPL_THEME1','EPL_AGE65','EPL_AGE17','EPL_DISABL','SPL_THEME2','EPL_SNGPNT','RPL_THEME2','EPL_MINRTY','EPL_LIMENG','RPL_THEME3','EPL_MUNIT','EPL_MOBILE','EPL_CROWD','EPL_NOVEH','EPL_GROUPQ','SPL_THEME3']

max_value_v = [1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,3,3,3,2]

headers = pd.DataFrame({'survey_q': survey_q_v, 'max_value': max_value_v, 'cdc_name': cdc_name_v})

print(headers)

headers.to_csv('cols_vals.csv', index=False)

