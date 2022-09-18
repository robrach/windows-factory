from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Window(models.Model):
    width = models.IntegerField(
        validators=[MinValueValidator(500), MaxValueValidator(2500)],
        default=500,
    )
    height = models.IntegerField(
        validators=[MinValueValidator(500), MaxValueValidator(2500)],
        default=500,
    )
    type = models.CharField(
        max_length=20,
        choices=[
            ('openable_type1', 'obenable - type 1'),
            ('openable_type2', 'openable - type 2'),
            ('openable_type3', 'openable - tyle 3'),
            ('unopenable', 'unopenable'),
        ],
        default='openable_type1',
    )
    direction_of_opening = models.CharField(
        max_length=20,
        choices=[
            ('to_the_inside', 'to the inside'),
            ('to_the_outside', 'to the outside'),
            ('unopenable', 'unopenable'),
        ],
        default='to_the_inside',
    )
    acoustics = models.CharField(
        max_length=20,
        choices=[
            ('standard_acoustics', 'standard'),
            ('super_acoustics', 'super'),
        ],
        default='standard_acoustics',
    )
    thermics = models.CharField(
        max_length=20,
        choices=[
            ('standard_thermics', 'standard'),
            ('super_thermics', 'super'),
        ],
        default='standard_thermics',
    )
    additional_options = models.CharField(
        max_length=20,
        choices=[
            ('additional_vent', 'additional vent'),
            ('security_lock', 'security lock in the handle'),
            ('rc2', 'fittings with increased resistance to burglary (RC2)')
        ],
        default='additional_vent',
    )


class Material(models.Model):
    pass


class BillOfMaterials(models.Model):
    pass


class Offer(models.Model):
    pass


class Order(models.Model):
    pass


class Warehouse(models.Model):
    pass


class Client(models.Model):
    pass


class Purchase(models.Model):
    pass


class Employee(models.Model):
    pass
