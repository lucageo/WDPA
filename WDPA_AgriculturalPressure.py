# Agricultural Pressure
# 
# The Agricultural Pressure index is based on the average percentage of cropland in 1 km raster cells within 
# protected areas of size ≥ 50 km2 extracted from the WDPA. 



# Import arcpy 
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")


# Local variables:
WDPA = "WDPA"
Agri_raster = "E:\\xxx\\CROPLAND2005.tif"
agri_wdpa_all = "E:\\xxx\\precipitation.gdb\\agri_wdpa_all"
WDPA_wdpa_id_text = "WDPA_wdpa_id_text"
agri__Value_ = "E:\\xxx\\AGRI_OUTPUT.gdb\\ele_%Value%"

# Process: Loop through the features
arcpy.IterateFeatureSelection_mb(WDPA, "wdpa_id_text #", "false")

# Process: Zonal Statistics
arcpy.gp.ZonalStatisticsAsTable_sa(WDPA_wdpa_id_text, "wdpa_id_text", Agri_raster, agri__Value_, "DATA", "ALL")

# Process: Append
arcpy.Append_management("E:\\xxx\\AGRI_OUTPUT.gdb\\ele_%Value%", agri_wdpa_all, "NO_TEST", "COUNT \"COUNT\" true true false 4 Long 0 0 ,First,#,\
                        E:\\xxx\\AGRI_OUTPUT.gdb\\ele_%Value%,Range,-1,-1;MEAN \"MEAN\" true true false 8 Double 0 0 ,First,#, wdpa_id_text \"wdpa_id_text\" true true false 50 Text 0 0 ,First,#, \
                        E:\\xxx\\AGRI_OUTPUT.gdb\\ele_%Value%,wdpa_id_text,-1,-1", "")
