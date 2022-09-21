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
    additional_vent = models.BooleanField('Additional vent')
    security_lock = models.BooleanField('Security lock in the handle')
    rc2 = models.BooleanField('Fittings with increased resistance to burglary (RC2)')


class Supplier(models.Model):
    name = models.CharField(max_length=250)
    address_zip_code = models.CharField('ZIP code', max_length=6)
    address_city = models.CharField('City', max_length=250)
    address_street = models.CharField('Street and number', max_length=250)
    description = models.CharField(max_length=250)


class Material(models.Model):
    code = models.CharField(max_length=4, unique=True)
    description = models.CharField(max_length=250)
    unit = models.CharField(max_length=5)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    markup = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='the percentage that is added to the costs to get the selling price and create a profit'
    )
    weight_by_unit = models.DecimalField(max_digits=5, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class BillOfMaterials(models.Model):
    pass


class Employee(models.Model):
    first_name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)


class Offer(models.Model):
    number = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateTimeField()
    # window = models.ManyToOneRel


class Order(models.Model):
    pass


class Warehouse(models.Model):
    pass


class Client(models.Model):
    pass


class Purchase(models.Model):
    pass


class Api(models.Model):
    pass
