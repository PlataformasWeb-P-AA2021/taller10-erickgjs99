from django.db import models

# Create your models here.


class Parroquia(models.Model):
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Las Parroquias"


    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s" % (self.nombre,
                            self.tipo
                            )


class Barrio_Ciudadela(models.Model):
    class Meta:
        ordering = ["nombre", "parroquia"]
        verbose_name_plural = "Barrios / Ciudadelas"

    opciones_parques = (
        ('1', '1 Parque'),
        ('2', '2 Parques'),
        ('3', '3 Parques'),
        ('4', '4 Parques'),
        ('5', '5 Parques'),
        ('6', '6 Parques'),
    )

    nombre = models.CharField(max_length=30)
    numViviendas = models.CharField(max_length=30)
    numParques = models.CharField(max_length=30, choices=opciones_parques)
    numEdif = models.CharField(max_length=30)

    parroquia = models.ForeignKey(Parroquia, related_name='lasparroquias',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - %s - %s - %s" % (self.nombre,
                                           self.numViviendas,
                                           self.numParques,
                                           self.numEdif,
                                           self.parroquia
                                           )
