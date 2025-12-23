"""
Auto migration to convert Producto.categoria and Producto.proveedor
from CharField to ForeignKey to Categoria and Proveedor respectively.
"""
from django.db import migrations, models


def forwards_func(apps, schema_editor):
    Producto = apps.get_model('ferreteria', 'Producto')
    Categoria = apps.get_model('ferreteria', 'Categoria')
    Proveedor = apps.get_model('ferreteria', 'Proveedor')

    for producto in Producto.objects.all():
        # Map categoria string to Categoria instance if exists
        cat_name = producto.categoria
        prov_name = producto.proveedor

        if cat_name:
            try:
                cat = Categoria.objects.get(nombre=cat_name)
                producto.categoria_new_id = cat.id
            except Categoria.DoesNotExist:
                producto.categoria_new_id = None

        if prov_name:
            try:
                prov = Proveedor.objects.get(nombre=prov_name)
                producto.proveedor_new_id = prov.id
            except Proveedor.DoesNotExist:
                producto.proveedor_new_id = None

        producto.save()


def reverse_func(apps, schema_editor):
    # No-op reverse: cannot reliably restore previous strings
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('ferreteria', '0002_categoria_producto_proveedor_delete_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria_new',
            field=models.ForeignKey(null=True, on_delete=models.deletion.CASCADE, to='ferreteria.categoria'),
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor_new',
            field=models.ForeignKey(null=True, on_delete=models.deletion.CASCADE, to='ferreteria.proveedor'),
        ),
        migrations.RunPython(forwards_func, reverse_func),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='proveedor',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categoria_new',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='proveedor_new',
            new_name='proveedor',
        ),
    ]
