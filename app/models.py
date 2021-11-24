from django.db import models

from users.models import User

from django.utils import timezone


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

     # サンプル項目9 選択肢（マスタ連動）
    """
    sample_10 = models.ForeignKey(
        User,
        verbose_name='点検者',
        blank=True,
        null=True,
        related_name='sample_10',
        on_delete=models.SET_NULL,
    )
    """
    sample_1 = models.CharField(verbose_name='点検者',max_length=20,blank=True,null=True,)


     # サンプル項目7 日付
    sample_7 = models.DateField(
        verbose_name='日付',
        blank=True,
        null=True,
    )
    """
    # サンプル項目8 日時
    sample_8 = models.TimeField(
        verbose_name='点検時間',
        blank=True,
        null=True,
    )
    """
    #天気の項目
    weather_choice = (
        (1, '晴れ'),
        (2, '曇り'),
        (3, '雨'),
        (4, 'その他'),
    )

    sample_9 = models.IntegerField(
        verbose_name='天気',
        choices=weather_choice,
        blank=True,
        null=True,
    )




    #項目異常の選択
    ABNOMAL_CHOICE = (
        (1,'正常'),
        (2,'異常'),
    )

    # 項目1-1-1 淡水取水ポンプ1電流
    sample_1_1_1 = models.IntegerField(
        verbose_name='「淡水ポンプ室」淡水取水ポンプ1　電流（A)',
        blank=True,
        null=True,
    )

    # 項目1-1-2 淡水取水ポンプ1稼働時間
    sample_1_1_2 = models.FloatField(
        verbose_name='「淡水ポンプ室」淡水取水ポンプ1　稼働時間（hr)',
        blank=True,
        null=True,
    )

    #　項目1-1-3 淡水取水ポンプ1の異常有無

    sample_1_1_3 = models.IntegerField(
        verbose_name='「淡水ポンプ室」淡水取水ポンプ1　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

     # 項目1-2-1 淡水取水ポンプ2電流
    sample_1_2_1 = models.IntegerField(
        verbose_name='「淡水ポンプ室」淡水取水ポンプ2　電流（A)',
        blank=True,
        null=True,
    )

    # 項目1-2-2 淡水取水ポンプ1稼働時間
    sample_1_2_2 = models.FloatField(
        verbose_name='「淡水ポンプ室」淡水取水ポンプ2　稼働時間（hr)',
        blank=True,
        null=True,
    )

    #　項目1-2-3 淡水取水ポンプ1の異常有無
    sample_1_2_3 = models.IntegerField(
        verbose_name='「淡水ポンプ室」淡水取水ポンプ2　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目２−１-1　調餌室の冷蔵庫の温度
    sample_2_1_1 = models.FloatField(
        verbose_name='「調餌室」冷蔵庫　庫内温度（℃)',
        blank=True,
        null=True,
    )

    #　項目２−１−２　冷蔵庫の異常有無
    sample_2_1_2 = models.IntegerField(
        verbose_name='「調餌室」冷蔵庫　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目２−２−１冷凍庫の温度
    sample_2_2_1 = models.FloatField(
        verbose_name='「調餌室」冷凍庫　庫内温度（℃)',
        blank=True,
        null=True,
    )

    #　項目２−２−２　冷凍庫の異常有無
    sample_2_2_2 = models.IntegerField(
        verbose_name='「調餌室」冷凍庫　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目3-1 海水受水槽　水位
    sample_3_1 = models.IntegerField(
        verbose_name='「研究室」海水受水槽　水位（cm)',
        blank=True,
        null=True,
    )

    #　項目3-2　淡水受水槽　水位
    sample_3_2 = models.IntegerField(
        verbose_name='「研究室」淡水受水槽　水位（cm)',
        blank=True,
        null=True,
    )

    # 項目４−１−１海水揚水ポンプ１　電流
    sample_4_1_1 = models.IntegerField(
        verbose_name='「機械室 2F」 海水揚水ポンプ1　電流（A)',
        blank=True,
        null=True,
    )

    # 項目４−１−2 海水揚水ポンプ１　稼働時間
    sample_4_1_2 = models.FloatField(
        verbose_name='「機械室 2F」 海水揚水ポンプ1　稼働時間（hr)',
        blank=True,
        null=True,
    )

    #　項目4-1-3 海水揚水ポンプ１の異常有無
    sample_4_1_3 = models.IntegerField(
        verbose_name='「機械室 2F」 海水揚水ポンプ1　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目４−2−１海水揚水ポンプ2　電流
    sample_4_2_1 = models.IntegerField(
        verbose_name='「機械室 2F」 海水揚水ポンプ2　電流（A)',
        blank=True,
        null=True,
    )

    # 項目４−2−2 海水揚水ポンプ１　稼働時間
    sample_4_2_2 = models.FloatField(
        verbose_name='「機械室 2F」 海水揚水ポンプ2　稼働時間（hr)',
        blank=True,
        null=True,
    )

    #　項目4-2-3 海水揚水ポンプ１の異常有無
    sample_4_2_3 = models.IntegerField(
        verbose_name='「機械室 2F」 海水揚水ポンプ2　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目４−3−１海水揚水ポンプ3　電流
    sample_4_3_1 = models.IntegerField(
        verbose_name='「機械室 2F」 海水揚水ポンプ3　電流（A)',
        blank=True,
        null=True,
    )

    # 項目４−3−2 海水揚水ポンプ3　稼働時間
    sample_4_3_2 = models.FloatField(
        verbose_name='「機械室 2F」 海水揚水ポンプ3　稼働時間（hr)',
        blank=True,
        null=True,
    )

    #　項目4-3-3 海水揚水ポンプ１の異常有無
    sample_4_3_3 = models.IntegerField(
        verbose_name='「機械室 2F」 海水揚水ポンプ3　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目5-1 空気槽の槽圧
    sample_5_1 = models.FloatField(
        verbose_name='「機械室 2F」 空気槽　槽圧（kg/cm2)',
        blank=True,
        null=True,
    )

    # 項目5-２ 空気槽の吸入圧
    sample_5_2 = models.FloatField(
        verbose_name='「機械室 2F」 空気槽　吸入圧（Mpa)',
        blank=True,
        null=True,
    )

    #　項目５-3 空気槽の異常有無
    sample_5_3 = models.IntegerField(
        verbose_name='「機械室 2F」 空気槽　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目６−１−１　ブロアー１の電流
    sample_6_1_1 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア1　電流（A)',
        blank=True,
        null=True,
    )

    # 項目6−1−2 ブロアー１の稼働時間
    sample_6_1_2 = models.FloatField(
        verbose_name='「ブロア室中央棟」　ブロア1　稼働時間（hr)',
        blank=True,
        null=True,
    )

    # 項目6−1−3 ブロアー１の稼働時間
    sample_6_1_3 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア1　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目６−2−１　ブロアー2の電流
    sample_6_2_1 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア2　電流（A)',
        blank=True,
        null=True,
    )

    # 項目6−2−2 ブロアー１の稼働時間
    sample_6_2_2 = models.FloatField(
        verbose_name='「ブロア室中央棟」　ブロア2　稼働時間（hr)',
        blank=True,
        null=True,
    )

    # 項目6−2−3 ブロアー１の稼働時間
    sample_6_2_3 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア2　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目６−3−１　ブロアー3の電流
    sample_6_3_1 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア3　電流（A)',
        blank=True,
        null=True,
    )

    # 項目6−2−2 ブロアー3の稼働時間
    sample_6_3_2 = models.FloatField(
        verbose_name='「ブロア室中央棟」　ブロア3　稼働時間（hr)',
        blank=True,
        null=True,
    )

    # 項目6−2−3 ブロアー3の稼働時間
    sample_6_3_3 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア3　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目６−4−１　ブロアー4の電流
    sample_6_4_1 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア4　電流（A)',
        blank=True,
        null=True,
    )

    # 項目6−4−2 ブロアー4の稼働時間
    sample_6_4_2 = models.FloatField(
        verbose_name='「ブロア室中央棟」　ブロア4　稼働時間（hr)',
        blank=True,
        null=True,
    )

    # 項目6−4−3 ブロアー3の稼働時間
    sample_6_4_3 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア4　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目６−5−１　ブロアー5の電流
    sample_6_5_1 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア5　電流（A)',
        blank=True,
        null=True,
    )

    # 項目6−5−2 ブロアー5の稼働時間
    sample_6_5_2 = models.FloatField(
        verbose_name='「ブロア室中央棟」　ブロア5　稼働時間（hr)',
        blank=True,
        null=True,
    )

    # 項目6−5−3 ブロアー5の稼働時間
    sample_6_5_3 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　ブロア5　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目６−6−１　圧縮機１の電流
    sample_6_6_1 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　圧縮機1　電流（A)',
        blank=True,
        null=True,
    )

    # 項目6−6−2 ブロアー4の稼働時間
    sample_6_6_2 = models.FloatField(
        verbose_name='「ブロア室中央棟」　圧縮機1　稼働時間（hr)',
        blank=True,
        null=True,
    )

    # 項目6−6−3 ブロアー3の稼働時間
    sample_6_6_3 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　圧縮機1　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    # 項目６−7−１　圧縮機2の電流
    sample_6_7_1 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　圧縮機2　電流（A)',
        blank=True,
        null=True,
    )

    # 項目6−7−2 圧縮機2の稼働時間
    sample_6_7_2 = models.FloatField(
        verbose_name='「ブロア室中央棟」　圧縮機2　稼働時間（hr)',
        blank=True,
        null=True,
    )

    # 項目6−7−3 圧縮機2の稼働時間
    sample_6_7_3 = models.IntegerField(
        verbose_name='「ブロア室中央棟」　圧縮機2　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    #項目6-8　ヘッダー圧
    sample_6_8 = models.FloatField(
        verbose_name='「ブロア室中央棟」　ヘッダー圧（Mpa)',
        blank=True,
        null=True,
    )

    
    # 項目７−１−１　ブロアー１の電流
    sample_7_1_1 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア1　電流（A)',
        blank=True,
        null=True,
    )

    # 項目7−1−2 ブロアー１の稼働時間
    sample_7_1_2 = models.FloatField(
        verbose_name='「ブロア室アユ棟」　ブロア1　稼働時間（hr)',
        blank=True,
        null=True,
    )

    # 項目7−1−3 ブロアー１の稼働時間
    sample_7_1_3 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア1　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    sample_7_2_1 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア2　電流（A)',
        blank=True,
        null=True,
    )

    sample_7_2_2 = models.FloatField(
        verbose_name='「ブロア室アユ棟」　ブロア2　稼働時間（hr)',
        blank=True,
        null=True,
    )

    sample_7_2_3 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア2　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    sample_7_3_1 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア3　電流（A)',
        blank=True,
        null=True,
    )

    # 項目7−1−2 ブロアー１の稼働時間
    sample_7_3_2 = models.FloatField(
        verbose_name='「ブロア室アユ棟」　ブロア3　稼働時間（hr)',
        blank=True,
        null=True,
    )

    # 項目6−1−3 ブロアー１の稼働時間
    sample_7_3_3 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア3　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )


    sample_7_4_1 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア4　電流（A)',
        blank=True,
        null=True,
    )

    # 項目7−1−2 ブロアー１の稼働時間
    sample_7_4_2 = models.FloatField(
        verbose_name='「ブロア室アユ棟」　ブロア4　稼働時間（hr)',
        blank=True,
        null=True,
    )

    sample_7_4_3 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア4　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    sample_7_5_1 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア5　電流（A)',
        blank=True,
        null=True,
    )

    sample_7_5_2 = models.FloatField(
        verbose_name='「ブロア室アユ棟」　ブロア5　稼働時間（hr)',
        blank=True,
        null=True,
    )

    sample_7_5_3 = models.IntegerField(
        verbose_name='「ブロア室アユ棟」　ブロア5　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    #　項目８−１−１海水取水ポンプ１の電流
    sample_8_1_1 = models.IntegerField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ1　電流（A)',
        blank=True,
        null=True,
    )

    #　項目８−１−2 海水取水ポンプ１のヘルツ
    sample_8_1_2 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ1　周波数（Hz)',
        blank=True,
        null=True,
    )

    #項目８−１−３　海水取水ポンプ１の稼働時間
    sample_8_1_3 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ1　稼働時間（hr)',
        blank=True,
        null=True,
    )

    #項目８−１−４　海水取水ポンプ１の異常有無
    sample_8_1_4 = models.IntegerField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ1　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    #項目８−１−5　海水取水ポンプ１のkw
    sample_8_1_5 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ1　ワット（kw)',
        blank=True,
        null=True,
    )

    #項目８−１−６　海水取水ポンプ１のcosθ
    sample_8_1_6 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ1　cosθ',
        blank=True,
        null=True,
    )

    #海水取水ポンプ2の電流
    sample_8_2_1 = models.IntegerField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ2　電流（A)',
        blank=True,
        null=True,
    )

    #　項目８−１−2 海水取水ポンプ１のヘルツ
    sample_8_2_2 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ2　周波数（Hz)',
        blank=True,
        null=True,
    )

    #項目８−2−３　海水取水ポンプ１の稼働時間
    sample_8_2_3 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ2　稼働時間（hr)',
        blank=True,
        null=True,
    )

    #項目８−2−４　海水取水ポンプ１の異常有無
    sample_8_2_4 = models.IntegerField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ2　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    #項目８−１−5　海水取水ポンプ１のkw
    sample_8_2_5 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ2　ワット（kw)',
        blank=True,
        null=True,
    )

    #項目８−2−６　海水取水ポンプ１のcosθ
    sample_8_2_6 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ2　cosθ',
        blank=True,
        null=True,
    )

     #　項目８−3−１海水取水ポンプ１の電流
    sample_8_3_1 = models.IntegerField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ3　電流（A)',
        blank=True,
        null=True,
    )

    #　項目８−１−2 海水取水ポンプ１のヘルツ
    sample_8_3_2 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ3　周波数（Hz)',
        blank=True,
        null=True,
    )

    #項目８−１−３　海水取水ポンプ１の稼働時間
    sample_8_3_3 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ3　稼働時間（hr)',
        blank=True,
        null=True,
    )

    #項目８−１−４　海水取水ポンプ１の異常有無
    sample_8_3_4 = models.IntegerField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ3　異常の有無',
        choices=ABNOMAL_CHOICE,
        blank=True,
        null=True,
    )

    #項目８−１−5　海水取水ポンプ１のkw
    sample_8_3_5 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ3　ワット（kw)',
        blank=True,
        null=True,
    )

    #項目８−3−６　海水取水ポンプ１のcosθ
    sample_8_3_6 = models.FloatField(
        verbose_name='「海水ポンプ室」　海水取水ポンプ3　cosθ',
        blank=True,
        null=True,
    )

    # サンプル項目2 メモ
    sample_2 = models.TextField(
        verbose_name='備考',
        blank=True,
        null=True,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
