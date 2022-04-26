

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_delivery_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete'), ('bulk', 'Bulk')], max_length=10),
        ),
    ]
