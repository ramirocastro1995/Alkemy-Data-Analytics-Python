import requests
import csv

datosArgentinaMuseosURL = 'https://docs.google.com/spreadsheets/d/1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA/edit'
datosArgentinaSalasDeCineURL ='https://docs.google.com/spreadsheets/d/1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM/edit?pli=1#gid=1691373423'
datosArgentinaBiblotecasPopularesURL = 'https://docs.google.com/spreadsheets/d/1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk/edit#gid=1605800889'

def obtenerDatosMuseos():
    datosArgentinaMuseos = requests.get(datosArgentinaMuseosURL, allow_redirects=True)
def obtenerDatosSalasDeCine():
    datosArgentinaSalasDeCine = requests.get(datosArgentinaSalasDeCineURL, allow_redirects=True)

def obtenerDatosBiblotecasPopulares():
    datosArgentinaBiblotecasPopulares = requests.get(datosArgentinaBiblotecasPopularesURL,allow_redirects=True)
    
    
obtenerDatosBiblotecasPopulares()
