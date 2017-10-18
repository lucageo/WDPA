# Elevation profile
# 
# A virtual elevation profile for each terrestrial Protected Area (PA)
# of minimum size 50 km2 (WDPA) using the terrestrial relief (SRTM).
# The computed statistics are minimum, maximum, median and mean elevations. 


# Import arcpy 
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")


# Local variables:
WDPA = "WDPA"
mosaic_vrt = "E:\\xxx\\mosaic.vrt"
elevation_wdpa_all = "E:\\xxx\\ELEVATION.gdb\\elevation_wdpa_all"
WDPA_wdpa_id_text = "WDPA_wdpa_id_text"
ele__Value_ = "E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%"

# Process: Loop through the features
arcpy.IterateFeatureSelection_mb(WDPA, "wdpa_id_text #", "false")

# Process: Zonal Statistics
arcpy.gp.ZonalStatisticsAsTable_sa(WDPA_wdpa_id_text, "wdpa_id_text", mosaic_vrt, ele__Value_, "DATA", "ALL")

# Process: Append
arcpy.Append_management("E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%", elevation_wdpa_all, "NO_TEST", "COUNT \"COUNT\" true true false 4 Long 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Count,-1,-1;AREA \"AREA\" true true false 8 Double 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Area,-1,-1;MIN \"MIN\" true true false 4 Long 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Min,-1,-1;MAX \"MAX\" true true false 4 Long 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Max,-1,-1;RANGE \"RANGE\" true true false 4 Long 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Range,-1,-1;MEAN \"MEAN\" true true false 8 Double 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Mean,-1,-1;STD \"STD\" true true false 8 Double 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Std,-1,-1;SUM \"SUM\" true true false 8 Double 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Sum,-1,-1;VARIETY \"VARIETY\" true true false 4 Long 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Variety,-1,-1;MAJORITY \"MAJORITY\" true true false 4 Long 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Majority,-1,-1;MINORITY \"MINORITY\" true true false 4 Long 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Minority,-1,-1;MEDIAN \"MEDIAN\" true true false 4 Long 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,Median,-1,-1;ident \"ident\" true true false 4 Long 0 0 ,First,#; wdpa_id_text \"wdpa_id_text\" true true false 50 Text 0 0 ,First,#, \n
                        E:\\xxx\\ELEVATION_OUTPUT.gdb\\ele_%Value%,wdpa_id_text,-1,-1", "") 

