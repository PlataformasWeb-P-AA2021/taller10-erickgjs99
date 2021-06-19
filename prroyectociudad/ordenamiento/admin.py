from django.contrib import admin

# Importar las clases del modelo
from ordenamiento.models import Parroquia, Barrio_Ciudadela
from import_export.admin import ImportExportModelAdmin

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Parroquia

class ParroquiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'tipo')

    
# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase ParroquiaAdmin
admin.site.register(Parroquia, ParroquiaAdmin)

# admin.site.register(Modulo)

class Barrio_CiudadelaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'numViviendas', 'numParques', 'numEdif', 'parroquia')
    search_fields = ('nombre', 'parroquia')

admin.site.register(Barrio_Ciudadela, Barrio_CiudadelaAdmin)