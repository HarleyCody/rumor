# Generated by Django 3.0.2 on 2020-02-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rumor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rumor', models.CharField(max_length=200, null=True)),
                ('isReal', models.BooleanField(default=True)),
                ('province', models.CharField(choices=[('HB', '湖北'), ('BJ', '北京'), ('SH', '上海'), ('CQ', '重庆'), ('HuN', '湖南'), ('SC', '四川'), ('HeN', '河南'), ('AH', '安徽'), ('JS', '江苏'), ('SD', '山东'), ('ZJ', '浙江'), ('FJ', '福建'), ('GD', '广东'), ('AM', '澳门'), ('HaiN', '海南'), ('GX', '广西'), ('YN', '云南'), ('GZ', '贵州'), ('SX', '陕西'), ('NX', '宁夏'), ('SaX', '山西'), ('HeB', '河北'), ('TJ', '天津'), ('LN', '辽宁'), ('GL', '吉林'), ('HLJ', '黑龙江'), ('NMG', '内蒙古'), ('XJ', '新疆'), ('JX', '江西'), ('GS', '甘肃'), ('XG', '香港'), ('TW', '台湾'), ('QH', '青海'), ('XZ', '西藏')], default='HB', max_length=4)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
