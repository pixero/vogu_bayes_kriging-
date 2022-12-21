# Name: EmpiricalBayesianKriging_Example_02.py
# Description: Bayesian kriging approach whereby many models created around the
#   semivariogram model estimated by the restricted maximum likelihood algorithm is used.
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
arcpy.env.workspace = "D:/ArcGisProj/Vogu"

# Set local variables
in_features = "voduData.shp"
z_field = "CND"
out_ga_layer = "outEBKVoguPython"
out_raster = None
cell_size = 3
transformation_type = "NONE"
max_local_points = 100
overlap_factor = 1
number_semivariograms = 100
# Set variables for search neighborhood
radius = 5.230788
search_neighborhood = arcpy.SearchNeighborhoodStandardCircular(radius)
outputType = "PREDICTION"
quantile_value = ""
threshold_type = ""
probability_threshold = ""
semivariogram_model_type = "POWER"
# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute EmpiricalBayesianKriging
res = arcpy.EmpiricalBayesianKriging_ga(in_features, z_field, out_ga_layer, out_raster,
                                        cell_size, transformation_type, max_local_points, overlap_factor, number_semivariograms,
                                        search_neighborhood, outputType, quantile_value, threshold_type, probability_threshold,
                                        semivariogram_model_type)
