# imports

import matplotlib.pyplot as plt
import pandas as pd

# import the html page
tables = pd.read_html(
    "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"
)
# grab the correct table
correct_table = tables[1]
# rename the columns
correct_table.columns = [
    "Country",
    "CO1990",
    "CO2005",
    "CO2017",
    "perc2017",
    "percchange",
    "perla",
    "perca",
    "total22",
    "total23",
]
# create the relevant dataframe with slicing
countries = correct_table.loc[3:, ["Country", "CO1990", "CO2005", "CO2017"]]

'''Graph 1:
5 biggest CO2 emitters'''


# Selecting the five biggest CO2 emitters in a dataframe


# Making a new variable for this graph's dataframe so we can sort it
# without changing the original dataframe 'countries'
graph_frame = countries

# Sorting the new dataframe
graph_frame.sort_values(by="CO1990", inplace=True, ascending=False)

# Saving the top five in a variable
graph_frame_sorted = graph_frame.iloc[0:5]

# Making nice x axis labels
graph_frame_sorted.columns = ["Country", "1990", "2005", "2017"]

# Making the graph

fig, ax = plt.subplots(figsize=(7, 7))

for index, row in graph_frame_sorted.iterrows():
    x = graph_frame_sorted.columns[1:]  # cutting column name out
    y = row[1:]  # cutting column data out
    plt.plot(x, y, label=row[0], marker="o")

# Editing the graph to make it readable

ax.set_title("Top 5 CO2 Emitters", size=22)
ax.set_xlabel("Year", size=15)
ax.set_ylabel("CO2 Emitted in Mt", size=15)
plt.legend(loc="center left", bbox_to_anchor=(1, 0.8))
plt.grid()

''' Graph 2:
3 biggest reductions and 3 smallest reductions'''

# Making a new variable for this graph's dataframe so we can sort it
# without changing the original dataframe 'countries'

graph2_frame = countries

# Adding the required columns to the dataframe
graph2_frame["Max1990"] = 100
graph2_frame["Rel2005"] = graph2_frame["CO2005"] / graph2_frame["CO1990"] * 100
graph2_frame["Rel2017"] = graph2_frame["CO2017"] / graph2_frame["CO1990"] * 100

# Sorting the dataframe
graph2_frame.sort_values(by="Rel2017", inplace=True, ascending=False)

# Defining the top 3 and bottom 3 relative changers
graph2_frame_head = graph2_frame.head(3)
graph2_frame_tail = graph2_frame.tail(3)

# Combining the two selected frames to create the desired graph dataframe
graph2_frame_topbot = pd.concat([graph2_frame_head, graph2_frame_tail])

# Selecting the relevant columns for the graph
graph2_frame_final = graph2_frame_topbot.loc[
    :, ["Country", "Max1990", "Rel2005", "Rel2017"]
]

# Making nice x axis labels
graph2_frame_final.columns = ["Country", "1990", "2005", "2017"]

# Making the graph

fig, ax = plt.subplots(figsize=(7, 10))

for index, row in graph2_frame_final.iterrows():
    x = graph2_frame_final.columns[1:]  # cutting column name out
    y = row[1:]  # cutting column data out
    plt.plot(x, y, label=row[0], marker="o")

# Editing the graph to make it readable
# The value for outlier "Greenland" is so big,
# the chart would have to be VERY long to make this readable

ax.set_title("Changes in relative CO2 emissions, Top 3 and bottom 3", size=22)
ax.set_xlabel("Year", size=15)
ax.set_ylabel("Relative change from 1990", size=15)
plt.legend(loc="center left", bbox_to_anchor=(1, 0.8))
plt.grid()

"""Graph 3:
Recreate graph 2 but only for countries with at least 5Mt CO2 emission
in 1990"""

# graph2_frame from the previous section contains the correct data
# I'll make a new variable to use it for graph 3 while filtering out the > 5Mt
# countries with a boolean mask
graph3_frame = graph2_frame.loc[graph2_frame.CO1990 >= 5]

# The rest of the code is the same, "graph2" is just replaced with "graph3"

# Defining the top 3 and bottom 3 relative changers
graph3_frame_head = graph3_frame.head(3)
graph3_frame_tail = graph3_frame.tail(3)

# Combining the two selected frames to create the desired graph dataframe
graph3_frame_topbot = pd.concat([graph3_frame_head, graph3_frame_tail])

# Selecting the relevant columns for the graph
graph3_frame_final = graph3_frame_topbot.loc[
    :, ["Country", "Max1990", "Rel2005", "Rel2017"]
]

# Making nice x axis labels
graph3_frame_final.columns = ["Country", "1990", "2005", "2017"]

# Making the graph

fig, ax = plt.subplots(figsize=(7, 10))

for index, row in graph3_frame_final.iterrows():
    x = graph3_frame_final.columns[1:]  # cutting column name out
    y = row[1:]  # cutting column data out
    plt.plot(x, y, label=row[0], marker="o")

# Editing the graph to make it readable

ax.set_title(
    "Changes in relative CO2 emissions Top 3 and Bottom 3. (Min. 5Mt emission)",
    size=15,
)
ax.set_xlabel("Year", size=15)
ax.set_ylabel("Relative change from 1990", size=15)
plt.legend(loc="center left", bbox_to_anchor=(1, 0.8))
plt.grid()
