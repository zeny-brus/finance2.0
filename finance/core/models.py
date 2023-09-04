from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria

    class Meta:      
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Conta(models.Model):
    BANCO_CHOICES = (
        ('NU', 'Nubank'),
        ('CX','Caixa Economica'),
        ('BB','Banco do Brasil'),
        ('BR','Bradesco'),
        ('IT','Itau'),
        ('SC','Sicred cooperativa'),
        ('SI','Sicoob'),
        ('SA','Satander'),
    )
    TIPO_PESSOA = (
        ('pf','pessoa fisica'),
        ('pj','pessoa juridica'),
    )

    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=BANCO_CHOICES)
    tipo = models.CharField(max_length=2,choices=TIPO_PESSOA)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    icone = models.ImageField(upload_to='icones')


    def __str__(self):
        return self.apelido

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'