# Source

https://medium.com/@ianmcintyre_38849/creating-custom-conda-environments-in-an-arcgis-pro-workflow-1e4a0648f691

# Create a clone of your environement using the command line.


 - Go to the root of your conda installation: `cd C:\Program Files\ArcGIS\Pro\bin\Python\Scripts`
 - Activate the environement you have created: `activate arcgispro-py3-update-agol`
 - Remove the pinned dependency on pyshp: `conda install --no-pin arcgis=1.8.0`