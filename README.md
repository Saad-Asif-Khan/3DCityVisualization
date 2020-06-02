# Overview
This repo contains automated tool that is created using python, which can automatically convert large set of cityGML files to Cesium 3D Tiles. 
Second major part in this project is an IIS server which contains webpages that are capable of visualization of large amount of 3D city data.

# 3D City Visualization
* With advancements in the field of computer graphics, role of 3D Geo-Visualization has increased ever since.
* CityGML is xml based official format of OGC for 3D city and landscape models.
* However CityGML is not optimized to be visualized on Web.
* For faster rendering of 3D data on web, Cesium 3D tiles is a better option.

# Objective
* Data collection/ auto-downloading from the source i.e. GitHub repository. 
* Automation of the conversion of CityGML to 3D Tiles.
* Building a GUI for automation of tasks.
* Visualize 3D city model of the whole USA (nearly 125 million buildings) with LOD1 building models on a Web-Based platform to access and examine it effortlessly. 

# Data Used in this project
* This study is conducted for data of “The United States”. 
* Source of Data: https://github.com/opencitymodel/opencitymodel


# Prerequisites
There are certain prerequirements that needs to be fulfilled. These are as follows: 
1. **FME** 
2. **Python** 
3. **JavaScript**
4. **HTML**
