
# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Load required toolboxes
arcpy.ImportToolbox("Model Functions")


# Local variables:
WDPA_poly_Oct2017_50_tbd = "WDPA_poly_Oct2017_50_tbd"
mosaic_vrt = "E:\\battluc\\elevation_processing\\mosaic.vrt"
elevation_wdpa_all = "E:\\battluc\\elevation_processing\\elevation\\FINAL_TAB_ELEVATION.gdb\\elevation_wdpa_all"
I_WDPA_poly_Oct2017_50_tbd_wdpa_id_text = "I_WDPA_poly_Oct2017_50_tbd_wdpa_id_text"
ele__Value_ = "E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%"

# Process: Iterate Feature Selection
arcpy.IterateFeatureSelection_mb(WDPA_poly_Oct2017_50_tbd, "wdpa_id_text #", "false")

# Process: Zonal Statistics as Table
arcpy.gp.ZonalStatisticsAsTable_sa(I_WDPA_poly_Oct2017_50_tbd_wdpa_id_text, "wdpa_id_text", mosaic_vrt, ele__Value_, "DATA", "ALL")

# Process: Append
arcpy.Append_management("E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%", elevation_wdpa_all, "NO_TEST", "COUNT \"COUNT\" true true false 4 Long 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Count,-1,-1;AREA \"AREA\" true true false 8 Double 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Area,-1,-1;MIN \"MIN\" true true false 4 Long 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Min,-1,-1;MAX \"MAX\" true true false 4 Long 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Max,-1,-1;RANGE \"RANGE\" true true false 4 Long 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Range,-1,-1;MEAN \"MEAN\" true true false 8 Double 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Mean,-1,-1;STD \"STD\" true true false 8 Double 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Std,-1,-1;SUM \"SUM\" true true false 8 Double 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Sum,-1,-1;VARIETY \"VARIETY\" true true false 4 Long 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Variety,-1,-1;MAJORITY \"MAJORITY\" true true false 4 Long 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Majority,-1,-1;MINORITY \"MINORITY\" true true false 4 Long 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Minority,-1,-1;MEDIAN \"MEDIAN\" true true false 4 Long 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,Median,-1,-1;ident \"ident\" true true false 4 Long 0 0 ,First,#;wdpa_id_text \"wdpa_id_text\" true true false 50 Text 0 0 ,First,#,E:\\battluc\\elevation_processing\\elevation\\diff_jan_oct.gdb\\ele_%Value%,wdpa_id_text,-1,-1", "")

