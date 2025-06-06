# Generated by Django 5.1.5 on 2025-02-06 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма оплаты')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('completed', 'Завершен'), ('failed', 'Ошибка')], default='pending', max_length=20, verbose_name='Статус платежа')),
                ('transaction_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='ID транзакции')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название устройства')),
                ('paper_count', models.PositiveIntegerField(default=100, verbose_name='Остаток бумаги (листов)')),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название терминала')),
                ('location', models.CharField(blank=True, max_length=255, verbose_name='Расположение')),
                ('supports_color', models.BooleanField(default=False, verbose_name='Поддержка цветной печати')),
                ('price_per_page_bw', models.DecimalField(decimal_places=2, default=5.0, max_digits=5, verbose_name='Цена за страницу (Ч/Б)')),
                ('price_per_page_color', models.DecimalField(decimal_places=2, default=15.0, max_digits=5, verbose_name='Цена за страницу (Цветная)')),
                ('main_wallet', models.CharField(max_length=255, verbose_name='Основной кошелек')),
                ('commission_wallet', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кошелек для комиссии')),
            ],
        ),
        migrations.DeleteModel(
            name='PrinterStatus',
        ),
        migrations.AddField(
            model_name='document',
            name='is_color',
            field=models.BooleanField(default=False, verbose_name='Цветная печать'),
        ),
        migrations.AddField(
            model_name='payment',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.document', verbose_name='Документ'),
        ),
        migrations.AddField(
            model_name='printer',
            name='terminal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printers', to='core.terminal', verbose_name='Терминал'),
        ),
        migrations.AddField(
            model_name='payment',
            name='terminal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.terminal', verbose_name='Терминал'),
        ),
        migrations.AddField(
            model_name='document',
            name='terminal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.terminal', verbose_name='Терминал'),
        ),
    ]
