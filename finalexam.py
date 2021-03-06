# -*- coding: utf-8 -*-
"""Final_Exam-VisualisasiData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J1c2s5jY-g8kDV6wSvL9QNgiU5Gtl1It

# Tugas Besar Visualisasi Data

**Interaktif Fluktuasi Harga Saham**

Helmi Sunjaya Ramadhan / 1301194404

Muhammad Iqbal / 1301194032

Ibrahim Muhammad / 130119

IF 42-Gab04

# Import Library dan Data
"""

from bokeh.io import output_notebook, curdoc
from bokeh.plotting import figure, show
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import ColumnDataSource, GroupFilter, CDSView, HoverTool, Div
from bokeh.layouts import column, widgetbox
import pandas as pd
import numpy as np

# Commented out IPython magic to ensure Python compatibility.
# from google.colab import drive
# drive.mount('/content/drive/', force_remount = True)
# %cd /content/drive/MyDrive/datasetvisdat

#import data
df = pd.read_csv('stock_market.csv', parse_dates=['Date'])
# df = pd.read_csv("stock_market.csv")
df = df.rename(columns = {'Adj Close': 'Adj_Close'}, inplace = False)
df.head()

"""# Sort Data"""

#sort data
source = ColumnDataSource(df)

filter_hs = [GroupFilter(column_name='Name', group='HANG SENG')]
source_hs = CDSView(source=source,filters=filter_hs)

filter_nk = [GroupFilter(column_name='Name', group='NIKKEI')]
source_nk = CDSView(source=source,filters=filter_nk)

filter_nd = [GroupFilter(column_name='Name', group='NASDAQ')]
source_nd = CDSView(source=source,filters=filter_nd)

#set circle info
circle_data = {'source': source, 'size': 3, 'alpha': 0.7, 'selection_color':'black'}

circle_hs = {'view': source_hs, 'color': 'red', 'legend_label': 'HANG SENG'}

circle_nk = {'view': source_nk, 'color': 'green', 'legend_label': 'NIKKEI'}

circle_nd = {'view': source_nd, 'color': 'blue', 'legend_label': 'NASDAQ'}

"""# Adj Close (lvl 1)"""

#create figure
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
figure1 = figure(title= 'Adj Close Data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Adj Close',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
figure1.circle(x='Date', y='Adj_Close', **circle_data, **circle_hs)
figure1.circle(x='Date', y='Adj_Close', **circle_data, **circle_nk)
figure1.circle(x='Date', y='Adj_Close', **circle_data, **circle_nd)

#add hover
tooltips= [ ('Name','@Name'),('Adj_Close', '@Adj_Close') ]
hover_glyph = figure1.circle(x='Date', y= 'Adj_Close' , source=source,size=3, alpha=0, hover_fill_color='black', hover_alpha=0.5)
figure1.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

"""# Volume (lvl 2)"""

#create figure
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
figure2 = figure(title= 'Volume Data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Volume',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
figure2.circle(x='Date', y='Volume', **circle_data, **circle_hs)
figure2.circle(x='Date', y='Volume', **circle_data, **circle_nk)
figure2.circle(x='Date', y='Volume', **circle_data, **circle_nd)

#add hover
tooltips= [ ('Name','@Name'),('Volume', '@Volume') ]
hover_glyph = figure2.circle(x='Date', y= 'Volume' , source=source,size=3, alpha=0,hover_fill_color='black', hover_alpha=0.5)
figure2.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

"""# Day Perc Change (lvl 2)"""

#create figure
output_notebook()
select_tools = ['pan', 'box_select', 'wheel_zoom', 'tap', 'reset']
figure3 = figure(title= 'Day_Perc_Change Data',x_axis_type='datetime',x_axis_label='Date', y_axis_label= 'Day_Perc_Change',
              plot_height=500, plot_width=800, toolbar_location="right",tools=select_tools)

#add data circle
figure3.circle(x='Date', y='Day_Perc_Change', **circle_data, **circle_hs)
figure3.circle(x='Date', y='Day_Perc_Change', **circle_data, **circle_nk)
figure3.circle(x='Date', y='Day_Perc_Change', **circle_data, **circle_nd)

#add hover
tooltips= [ ('Name','@Name'),('Day_Perc_Change', '@Day_Perc_Change') ]
hover_glyph = figure3.circle(x='Date', y= 'Day_Perc_Change' , source=source,size=3, alpha=0,hover_fill_color='black', hover_alpha=0.5)
figure3.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

"""# Hide Index (lvl 3)"""

#hide data via legend
figure1.legend.click_policy = 'hide'
figure1.legend.location= 'top_right'

figure2.legend.click_policy = 'hide'
figure2.legend.location= 'top_right'

figure3.legend.click_policy = 'hide'
figure2.legend.location= 'top_right'

"""# Configure Panel"""

#add title
isi = """<h1>Visualisasi Data Interaktif Fluktuasi Harga Saham</h1>
<h3><i>Click Legend to HIDE Data</i><h3>"""
title = Div(text=isi)
#add widget panel and tab
figure1_panel = Panel(child=figure1, title='Adj Close Data')
figure2_panel = Panel(child=figure2, title='Volume Data')
figure3_panel = Panel(child=figure3, title='Day_Perc_Change Data')
tab = Tabs(tabs=[figure1_panel, figure2_panel, figure3_panel])
#add layout
# show(column(title,tab))
curdoc().add_root(tab)