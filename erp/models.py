from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)


class Client(models.Model):
    name = models.CharField(max_length=250)
    tax_id = models.CharField(max_length=10)
    zip_code = models.CharField('ZIP code', max_length=6)
    city = models.CharField('City', max_length=250)
    street = models.CharField('Street and number', max_length=250)


class Window(models.Model):
    width = models.IntegerField(
        'Width [mm]',
        validators=[MinValueValidator(500), MaxValueValidator(2500)],
        default=500,
    )
    height = models.IntegerField(
        'Height [mm]',
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


class Offer(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    offer_date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    windows = models.ManyToManyField(Window)
    accepted = models.BooleanField('Accepted by client?')


class Bom(models.Model):
    """ 'Bom' means Bill of materials """
    window = models.ForeignKey(Window, on_delete=models.CASCADE)
    cost_of_materials = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    cost_of_work = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )


class CategoryOfMaterial(models.Model):
    category = models.CharField(max_length=100)


class Supplier(models.Model):
    name = models.CharField(max_length=250)
    zip_code = models.CharField('ZIP code', max_length=6)
    city = models.CharField('City', max_length=250)
    street = models.CharField('Street and number', max_length=250)
    category = models.ForeignKey(CategoryOfMaterial, on_delete=models.CASCADE)


class Material(models.Model):
    code = models.CharField(max_length=4, unique=True)
    description = models.CharField(max_length=250)
    unit = models.CharField(max_length=5)
    quantity = models.IntegerField
    cost_per_unit = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    trade_markup = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text='the percentage that is added to the costs to get the selling price and create a profit'
    )
    weight_by_unit = models.DecimalField(max_digits=8, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryOfMaterial, on_delete=models.CASCADE)


class Order(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[
            ('to_do', 'To do'),
            ('in_progress', 'Production in progress'),
            ('done', 'Produced and ready for delivery'),
            ('delivered', 'Delivered to client')
        ],
        default='to_do',
    )


class Purchase(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        default=1,
        validators=[MinValueValidator(0)],
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class Api(models.Model):
    endpoint = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
