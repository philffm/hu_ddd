import handle_data
import pandas as pd

import justpy as jp
import plotly.express as px
import numpy as np


data_facebook = handle_data.output_data('frankfurt', 'data_facebook.csv')

df_pie = pd.DataFrame(data_facebook)


print('================================')