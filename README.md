# Assessing Vulnerability in Conflict Area X

Motivated by the lack of statistical indicators in Syria throughout the Syrian civil war. I designed a vulnerability evaluation survey and used Python to do the following:
-	Projected experimental randomized CDC data onto the survey variables.
-	Manipulated the data to establish the required indices in standardized form.
-	Plotted the results of the indices on corresponding individual histograms.
And used QGIS to:
-	Established a fictional Country X.
-	Spatially mapped the results of the previous indices onto Country X.


## Main Objectives
The repository is the output of the class individual project for PAI 789, Advanced Policy Analysis at the Maxwell School at Syracuse University. This project is motivated by the lack of information in Syria and other conflict areas. My objectives included a complete survey design and an experimental run of the survey variables interaction using a random data sample, in addition to plotting the data statistically and spatially to have a pilot of a ready to implement model.


## The Project:
For the purposes of civilian public use, the lack of crisis monitoring solutions in conflict areas (as in the Syrian civil war) prompted me to run this trial using experimental data and a fictional country of my creation, Country X.
The goal is to establish an adaptable survey and an analysis code that plots statistical histograms of the experiment variables and generates a dataset that is ready for spatial projection using QGIS.


## Disclaimer:
The project is purely fictional due to a lack of information on the Syrian crisis. 
The survey design is a personal effort guided by other classes in economics. No ready indicators were borrowed or adapted in this design. Please feel free to reach out with questions about the survey design part of the project.


## Data Source:
The data used to generate the required variable data is the CDC/ATSDR SVI Data, and is available for download here:
[I'm an inline-style link](https://www.atsdr.cdc.gov/placeandhealth/svi/data_documentation_download.html)
the same link can also be used to download the corresponding shapefile for the desired state. Using a same agency shapefile was done to avoid mismatching the random data with a shapefile from other sources. For this project, the data selection was based on the data available for the State of Florida on a census tract level for the year of 2018.


### Python – the Script:
A single script is used for the purpose of this assignment. However, the script is divided into three distinct parts:
1.	Aligning the survey and its columns with the targeted data
2.	Establishing the indices
3.	Plotting Indices Histograms
The modules used in the script are: 
	Pandas			numpy			matplotlib.pyplot

#### PART 1: Aligning the survey and metrics with the targeted data
This part of the script does the following:
First, it creates a table with the survey columns, max values for each of the columns, and the desired CDC column to correspond to that survey column. The survey columns and corresponding values are based on the survey design (check the disclaimer above for more information). Consequently, the script creates a variable that is limited (trimmed) to include only the desired columns from the CDC file, including the FIPS column to enable spatial mapping of the data. Then within that list, a function is designed to scale down the data to a standardized value ranging between “zero“ and “one“. The dataset headers are then relabeled to the correct survey columns which will be used in creating the required indicators (indices). 

#### PART 2: Establishing the indices
In this part, the data is manipulated to create the required indices, based on a prefix and suffix variable label design in the survey. The indices are designed as: 
(Index survey columns total sum) / (Index survey column maximum value sum). 
The labels starting with the following letters are used to formulate their corresponding indices:
F: Food Index
E: Education Index
M: Medical Index
G: Governmental Index
The labels ending with the following letters are used to formulate their corresponding indices:
SI: Income Security Index
This part of the script also scales down the results of the indices to “one” as a standardized value. The part is then concluded by exporting the resulting dataset to a comma separated file named “survey_q.csv”.

#### PART 3: Plotting Indices’ Histograms
This part uses the module “matplotlib.pyplot” to plot the indices using two layers, a histogram and a kernel density distribution. Either one would have been sufficiently, but this arrangement displays a good visibility and transparency into the data trend and individual bins if one wishes. 


### QGIS – Creating Fictional Country X: 
As mentioned above, I used the Florida shapefile from the same source as the CDC data. The file was used to select a random centroid point of a census tract and crop the surrounding area in a diameter of about 30 miles to frame a fictional country in that area. A coastal area was selected to give some natural shape of the desired fictional country X. The resulting country was then to spatially plot the different indices from the previously resulting file in Python, adding clarity to the spatial distribution of different concentrations or distributions of the mentioned indices.

The resulting maps are then organized with the matching statistical histogram and projected to audiences. (The presentation talks about potentially projecting the maps onto Tableau Public, which is a part planned in case the survey is really coming to life.)
One interesting observation was to see that within the frame of a randomly assigned artificial dataset, a local government located in the southeastern part of the central region was doing comparably better on all measured indices. This illustrates how powerful the projection of the data into an interactive map.


## Conclusions:
•	A Python script (PART 2) can readily be used to find the standardized results of the indices. 
•	Python script (PART 3) is readily available to plot the histograms of the resulting indices.
•	QGIS is perfectly suitable to projecting high quality data illustrations that are 
