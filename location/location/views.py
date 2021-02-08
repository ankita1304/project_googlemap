from django.shortcuts import render , HttpResponse
import pandas as pd
import requests
from import_export.admin import ImportExportModelAdmin
import openpyxl
from geopy.geocoders import Nominatim
import googlemaps


def home(request):
    if request.method == "POST":
        file = request.FILES["myFile"]
        wb = openpyxl.load_workbook(file)
        active_sheet = wb.active
        excel_data = list()
        for row in active_sheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        gmaps_key = googlemaps.Client(key ="AIzaSyDmHr39todYYu2unRk-3nsvuwNpCEmiUhY")
        excel = pd.read_excel(file)
        excel["latitude"] = None
        excel["longitude"] = None
        for i in range(0, len(excel),1):
            geocode_result = gmaps_key.geocode(excel.iat[i,0])
            try:
                lat= geocode_result[0]["geometry"]["location"]["lat"]
                lon= geocode_result[0]["geometry"]["location"]["colon"]
                excel.iat[i ,excel.columns.get_loc("LAT")] = lat
                excel.iat[i ,excel.columns.get_loc("LON")] = lon
            except:
                lat = None
                lon = None
        return render(request, 'index.html', {"something": True,  "excel_data":excel})
    else: 

        return render(request , "fileupload.html")

#def upload(request):
 #   return render(request , "fileupload.html")