from django.db import models

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    POSICIONES = [
        ('arquero', 'Arquero'),
        ('defensa', 'Defensa'),
        ('centro', 'Centro'),
        ('delantero', 'Delantero'),
    ]

    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=20, choices=POSICIONES)
    numero_camiseta = models.PositiveIntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class CampeonatoEquipos(models.Model):
    año = models.PositiveIntegerField()
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.año} - {self.equipo_futbol} - {self.campeonato}"
