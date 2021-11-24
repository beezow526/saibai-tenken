# Generated by Django 2.1.2 on 2021-11-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211119_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sample_5_1',
            field=models.FloatField(blank=True, null=True, verbose_name='「機械室 2F」 空気槽\u3000槽圧（kg/cm2)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_5_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「機械室 2F」 空気槽\u3000吸入圧（Mpa)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_5_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「機械室 2F」 空気槽\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_1_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア1\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_1_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア1\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_1_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室中央棟」\u3000ブロア1\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_2_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア2\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_2_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア2\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_2_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室中央棟」\u3000ブロア2\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_3_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア3\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_3_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア3\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_3_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室中央棟」\u3000ブロア3\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_4_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア4\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_4_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア4\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_4_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室中央棟」\u3000ブロア4\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_5_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア5\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_5_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ブロア5\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_5_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室中央棟」\u3000ブロア5\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_6_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000圧縮機1\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_6_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000圧縮機1\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_6_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室中央棟」\u3000圧縮機1\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_7_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000圧縮機2\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_7_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000圧縮機2\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_7_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室中央棟」\u3000圧縮機2\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_6_8',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室中央棟」\u3000ヘッダー圧（Mpa)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_1_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア1\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_1_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア1\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_1_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア1\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_2_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア2\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_2_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア2\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_2_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア2\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_3_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア3\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_3_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア3\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_3_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア3\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_4_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア4\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_4_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア4\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_4_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア4\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_5_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア5\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_5_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア5\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_7_5_3',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「ブロア室アユ棟」\u3000ブロア5\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_1_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ1\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_1_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ1\u3000周波数（Hz)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_1_3',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ1\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_1_4',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ1\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_1_5',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ1\u3000ワット（kw)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_1_6',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ1\u3000cosθ'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_2_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ2\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_2_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ2\u3000周波数（Hz)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_2_3',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ2\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_2_4',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ2\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_2_5',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ2\u3000ワット（kw)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_2_6',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ2\u3000cosθ'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_3_1',
            field=models.IntegerField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ3\u3000電流（A)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_3_2',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ3\u3000周波数（Hz)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_3_3',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ3\u3000稼働時間（hr)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_3_4',
            field=models.IntegerField(blank=True, choices=[(1, '正常'), (2, '異常')], null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ3\u3000異常の有無'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_3_5',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ3\u3000ワット（kw)'),
        ),
        migrations.AddField(
            model_name='item',
            name='sample_8_3_6',
            field=models.FloatField(blank=True, null=True, verbose_name='「海水ポンプ室」\u3000海水取水ポンプ3\u3000cosθ'),
        ),
    ]
