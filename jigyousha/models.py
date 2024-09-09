from django.db import models


class Jigyousha(models.Model):
    todofuken_code = models.BigIntegerField(db_column='都道府県コード又は市町村コード')
    no = models.TextField(db_column='No',primary_key=True)
    todofuken_name = models.TextField(db_column='都道府県名')
    shichoson_name = models.TextField(db_column='市区町村名')
    jigyousho_name = models.TextField(db_column='事業所名')
    jigyousho_name_kana = models.TextField(db_column='事業所名カナ')
    service_type = models.TextField(db_column='サービスの種類')
    address = models.TextField(db_column='住所')
    building_name = models.TextField(db_column='方書（ビル名等）', blank=True, null=True)
    latitude = models.FloatField(db_column='緯度', blank=True, null=True)
    longitude = models.FloatField(db_column='経度', blank=True, null=True)
    phone_number = models.TextField(db_column='電話番号', blank=True, null=True)
    fax_number = models.TextField(db_column='FAX番号', blank=True, null=True)
    houjin_number = models.FloatField(db_column='法人番号', blank=True, null=True)
    houjin_name = models.TextField(db_column='法人の名称', blank=True, null=True)
    jigyousho_number = models.TextField(db_column='事業所番号', blank=True, null=True)
    available_days = models.TextField(db_column='利用可能曜日', blank=True, null=True)
    special_notes = models.TextField(db_column='利用可能曜日特記事項', blank=True, null=True)
    capacity = models.FloatField(db_column='定員', blank=True, null=True)
    url = models.TextField(db_column='URL', blank=True, null=True)
    kogei_shogaisha_taiyo = models.TextField(db_column='高齢者の方と障害者の方が同時一体的に利用で', blank=True, null=True)
    kaigo_hoken = models.TextField(db_column='介護保険の通常の指定基準を満たしている', blank=True, null=True)
    shogai_fukushi = models.TextField(db_column='障害福祉の通常の指定基準を満たしている', blank=True, null=True)
    notes = models.TextField(db_column='備考', blank=True, null=True)

    class Meta:
        db_table = 'jigyousha'  # 既存のテーブル名を指定

    def __str__(self):
        return self.jigyousho_name


class SJigyousha(models.Model):
    todofuken_code = models.BigIntegerField(db_column="都道府県コード又は市区町村コード")  # 都道府県コード又は市区町村コード
    no = models.IntegerField(primary_key=True, db_column="NO（※システム内の固有の番号、連番）")  # NO（※システム内の固有の番号、連番）
    shitei_kikan_name = models.TextField(db_column="指定機関名")  # 指定機関名
    houjin_name = models.TextField(db_column="法人の名称")  # 法人の名称
    houjin_name_kana = models.TextField(db_column="法人の名称_かな")  # 法人の名称_かな
    houjin_number = models.BigIntegerField(db_column="法人番号")  # 法人番号
    houjin_address_city = models.TextField(db_column="法人住所（市区町村）")  # 法人住所（市区町村）
    houjin_address_street = models.TextField(db_column="法人住所（番地以降）")  # 法人住所（番地以降）
    houjin_phone_number = models.CharField(max_length=20, db_column="法人電話番号")  # 法人電話番号
    houjin_fax_number = models.CharField(max_length=20, null=True, blank=True, db_column="法人FAX番号")  # 法人FAX番号
    houjin_url = models.URLField(null=True, blank=True, db_column="法人URL")  # 法人URL
    service_type = models.TextField(db_column="サービス種別")  # サービス種別
    jigyousho_name = models.TextField(db_column="事業所の名称")  # 事業所の名称
    jigyousho_name_kana = models.TextField(db_column="事業所の名称_かな")  # 事業所の名称_かな
    jigyousho_number = models.CharField(max_length=255, db_column="事業所番号")  # 事業所番号
    jigyousho_address_city = models.TextField(db_column="事業所住所（市区町村）")  # 事業所住所（市区町村）
    jigyousho_address_street = models.TextField(db_column="事業所住所（番地以降）")  # 事業所住所（番地以降）
    jigyousho_phone_number = models.CharField(max_length=20, db_column="事業所電話番号")  # 事業所電話番号
    jigyousho_fax_number = models.CharField(max_length=20, null=True, blank=True, db_column="事業所FAX番号")  # 事業所FAX番号
    jigyousho_url = models.URLField(null=True, blank=True, db_column="事業所URL")  # 事業所URL
    jigyousho_latitude = models.FloatField(null=True, blank=True, db_column="事業所緯度")  # 事業所緯度
    jigyousho_longitude = models.FloatField(null=True, blank=True, db_column="事業所経度")  # 事業所経度
    available_time_weekdays = models.TextField(null=True, blank=True, db_column="利用可能な時間帯（平日）")  # 利用可能な時間帯（平日）
    available_time_saturday = models.TextField(null=True, blank=True, db_column="利用可能な時間帯（土曜）")  # 利用可能な時間帯（土曜）
    available_time_sunday = models.TextField(null=True, blank=True, db_column="利用可能な時間帯（日曜）")  # 利用可能な時間帯（日曜）
    available_time_holiday = models.TextField(null=True, blank=True, db_column="利用可能な時間帯（祝日）")  # 利用可能な時間帯（祝日）
    closed_days = models.TextField(null=True, blank=True, db_column="定休日")  # 定休日
    available_days_note = models.TextField(null=True, blank=True, db_column="利用可能曜日特記事項（留意事項）")  # 利用可能曜日特記事項（留意事項）
    capacity = models.IntegerField(null=True, blank=True, db_column="定員")  # 定員

    class Meta:
        db_table = 'sjigyousha'  # 既存のテーブル名を指定

    def __str__(self):
        return self.jigyousho_name
