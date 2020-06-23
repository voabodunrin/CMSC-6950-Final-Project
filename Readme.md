# CMSC 6950: Computer Based Research Tools and Applications Final Project for Group 5
This project shows different ways to visualize the current canadaian covid-19 data with matplotlib. It also shows the use of Numpy and Pandas to process the data before visualizing.

## Technologies Used
This project was built with
* [Python] - Programming Language
* [Anaconda 3] - Development Environment
* [Latex] - Results of the Project
* [remark-js] - Presentation slides

## Features
* Q1: Within group5_notebook.ipynb. Downloads .csv file from the given URL and outputs content into Python list.
* Q4: Takes the data from the file and uses pandas dataframe to format, clean and filter the data before plotting it with pandas inbuilt .plot() function. It also makes use of subplots to represent different provinces
* Q5: q5_proj.py calculates the doubling rate of COVID-19 given 3 arguments: province, specification of cases or deaths, and date (dd-mm-yyyy). q5_shell runs q5_proj.py multiple times and directs output to files cases.dat and deaths.dat.
* Q6: q6.ipynb plots content from files cases.dat and deaths.dat using Pandas package in Python.
* Free Choice Task: This makes use of pandas and ipywidgets to produce and interactive plot. The pandas is used to format, clean and filter the data before plotting it with pandas inbuilt .plot() function while the ipywidgets is used to create datepicker and dropdown widgets. The value of the widgets are then plotted.

## Usage/ Installation Instructions
* Q3: creates a dictionary that contains all provinces in order to plot the number of individuals tested in each province over time.
* Q5: Run q5_proj.py from the command line. Example of command is 'python q5_proj.py "Newfoundland-and-Labrador" "cases" "19-05-2020" '.
* Q6: Run command 'bash q5_shell.sh' to output data files, then run jypter notebook Q6.ipynb to form and save plots.  
* Free Choice Tasks: Install ipywidgets with either 'pip install ipywidgets' or 'conda install -c conda-forge ipywidgets' commands. Run on jupyter notebook.

## Authors

* **Collins Bekoe**
* **Miranda Boutilier**
* **Victor Abodunrin**

## References

* [Coronavirus disease (COVID-19): Outbreak update](https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html?topic=tilelink#a1) Government of Canada, 2020. 
* [#Flattenthecurve, but by how much?](https://blog.datawrapper.de/weekly-chart-coronavirus-doublingtimes/), Data Wrapper.
* [Time Series Data Visualization with Python](https://machinelearningmastery.com/time-series-data-visualization-with-python/) Machine Learning Mastery, 2019. 
* [Interactive Controls in Jupyter Notebooks](https://towardsdatascience.com/interactive-controls-for-jupyter-notebooks-f5c94829aee6) towards data science, 2019. 

