# greenspace

### **ILM Greenspace Project**

**Objective:**
The goal of the Greenspace Project is to use digital imagery to calculate how greenspace varies throughout New Hanover County, and ultimately how urban landscapes are linked to heat islands and nuisance flooding. 

**Methods:** 
The basic methodology is simple, 1 km2 images were downloaded from Google Earth and then analyzed using Open CV. Each image pixel was converted from RGB - Red Green Blue - to HSV - Hue Saturated Value - and then analyzed for presence of gray color to distinguish concrete or other impervious surfaces (easier to distinguish than different shades of green). All pixels showing a positive and negative detection for gray were converted to white and black colors, respectively. To calculate the percentage of greenspace, the total amount of black pixels were counted and divided by the total number of pixels in each image.

**Python files:** 
[ILM_Greenspace.py ](https://github.com/mnemiopsis007/greenspace/blob/main/ILM_Greenspace.py)was used to analyze the images for % greenspace.
[ILM_greenspacemap.py](https://github.com/mnemiopsis007/greenspace/blob/main/ILM_greenspacemap.py) plots the amount of greenspace in NHC in Plotly using different shades of green to represent % greenspace in each image relative to its location.
[Azy_data.csv ](https://github.com/mnemiopsis007/greenspace/blob/main/Azy_data.csv)contains the summary data used in the map for greenspace and impervious surface, and central latitude and longitude points for each image.
<img width="1064" alt="Screen Shot 2021-08-09 at 12 24 38 AM" src="https://user-images.githubusercontent.com/30030810/135296240-f115ce51-f13d-42cb-9850-37ccd4a1aa30.png">


### **Tasks For Code Niñas**

The following tasks need to be completed by the group. McKenzie will help you work through these but please ask questions if you get stuck. Divvy up the tasks and enjoy the collaboration!

1) Update Map: in the original version, images were approximately 1 km2 but it would be great to have finer neighborhood scale measurements. Let's repeat the analysis but each image being no bigger than 0.4km x 0.4km.

2) Automate the analysis: let's update the image analysis code so that all the files are automatically analyzed and the data saved into a csv file. Let's also include the map code in the image analysis file so that it automatically maps the data using the csv file data.

3) Comparisons with other small cities: It would be good to compare how ILM shapes up to other similar sized cities. Let's repeat the analysis to see how ILM shapes up against Raleigh, Asheville, Greenville or any city you can think of.....why not NYC or LAX?

4) Rates of change in greenspace: Google Earth has timelines of images which might make an analysis of how greenspace has changed over time in NHC possible. If there is time let's see how the NHC landscape has changed over the past 20 years.
