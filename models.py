# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsOtp(models.Model):
    id = models.BigAutoField(primary_key=True)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField()
    user = models.ForeignKey('AccountsUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_otp'


class AccountsUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    user_type = models.CharField(max_length=10)
    email = models.CharField(unique=True, max_length=254)
    bio = models.TextField(blank=True, null=True)
    inquiry_history = models.TextField(blank=True, null=True)
    response_history = models.TextField(blank=True, null=True)
    chat_history = models.TextField(blank=True, null=True)
    profile_image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accounts_userprofile'


class AccountsUserprofileGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    userprofile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_userprofile_groups'
        unique_together = (('userprofile', 'group'),)


class AccountsUserprofileUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    userprofile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_userprofile_user_permissions'
        unique_together = (('userprofile', 'permission'),)


class Allowed(models.Model):
    法人等の種類 = models.TextField(blank=True, null=True)
    法人等の名称_ふりがな_field = models.TextField(db_column='法人等の名称(ふりがな)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    法人等の名称 = models.TextField(blank=True, null=True)
    法人等の主たる事務所の所在地_郵便番号 = models.TextField(blank=True, null=True)
    法人等の主たる事務所の所在地_都道府県 = models.TextField(blank=True, null=True)
    法人等の主たる事務所の所在地_市区町村 = models.TextField(blank=True, null=True)
    法人等の主たる事務所の所在地_町名_番地 = models.TextField(db_column='法人等の主たる事務所の所在地_町名・番地', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    法人等の主たる事務所の所在地_建物名_部屋 = models.TextField(db_column='法人等の主たる事務所の所在地_建物名・部屋', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    法人等の連絡先_電話番号 = models.TextField(blank=True, null=True)
    法人等の連絡先_その他連絡先 = models.TextField(blank=True, null=True)
    法人等代表者の氏名 = models.TextField(blank=True, null=True)
    法人等代表者の職名 = models.TextField(blank=True, null=True)
    法人等の設立年月日 = models.TextField(blank=True, null=True)
    法人が教育_保育を提供し_又は提供しようと = models.TextField(db_column='法人が教育・保育を提供し、又は提供しようと', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設類型 = models.TextField(blank=True, null=True)
    施設の名称_ふりがな_field = models.TextField(db_column='施設の名称(ふりがな)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    施設の名称 = models.TextField(blank=True, null=True)
    事業所番号 = models.TextField(blank=True, null=True)
    郵便番号 = models.TextField(blank=True, null=True)
    施設の所在地_都道府県 = models.TextField(db_column='施設の所在地 都道府県', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設の所在地_市区町村 = models.TextField(db_column='施設の所在地 市区町村', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設の所在地_町名_番地 = models.TextField(db_column='施設の所在地 町名・番地', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設の所在地_建物名_部屋番号等 = models.TextField(db_column='施設の所在地 建物名・部屋番号等', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設の連絡先_電話番号 = models.TextField(db_column='施設の連絡先 電話番号', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設の連絡先_その他連絡先 = models.TextField(db_column='施設の連絡先 その他連絡先', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設の設置主体 = models.TextField(blank=True, null=True)
    施設_管理者氏名 = models.TextField(db_column='施設 管理者氏名', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設_管理者職名 = models.TextField(db_column='施設 管理者職名', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    事業の認可年月日 = models.TextField(blank=True, null=True)
    事業の開始年月日 = models.TextField(blank=True, null=True)
    事業の確認年月日 = models.TextField(blank=True, null=True)
    営業状況 = models.TextField(blank=True, null=True)
    保育教諭_従業者数_常勤 = models.TextField(blank=True, null=True)
    保育教諭_従業者数_非常勤 = models.TextField(blank=True, null=True)
    保育教諭_労働時間 = models.TextField(blank=True, null=True)
    保育教諭_平均経験年数_常勤 = models.TextField(blank=True, null=True)
    保育教諭_平均経験年数_非常勤 = models.TextField(blank=True, null=True)
    教諭又は保育士_従業者数_常勤 = models.TextField(blank=True, null=True)
    教諭又は保育士_従業者数_非常勤 = models.TextField(blank=True, null=True)
    教諭又は保育士_労働時間 = models.TextField(blank=True, null=True)
    教諭又は保育士_平均経験年数_常勤 = models.TextField(blank=True, null=True)
    教諭又は保育士_平均経験年数_非常勤 = models.TextField(blank=True, null=True)
    保育士_従業者数_常勤 = models.TextField(blank=True, null=True)
    保育士_従業者数_非常勤 = models.TextField(blank=True, null=True)
    保育士_労働時間 = models.TextField(blank=True, null=True)
    保育士_平均経験年数_常勤 = models.TextField(blank=True, null=True)
    保育士_平均経験年数_非常勤 = models.TextField(blank=True, null=True)
    保育従事者_従業者数_常勤 = models.TextField(blank=True, null=True)
    保育従事者_従業者数_非常勤 = models.TextField(blank=True, null=True)
    保育従事者_労働時間 = models.TextField(blank=True, null=True)
    保育従事者_平均経験年数_常勤 = models.TextField(blank=True, null=True)
    保育従事者_平均経験年数_非常勤 = models.TextField(blank=True, null=True)
    教諭_従業者数_常勤 = models.TextField(blank=True, null=True)
    教諭_従業者数_非常勤 = models.TextField(blank=True, null=True)
    教諭_労働時間 = models.TextField(blank=True, null=True)
    教諭_平均経験年数_常勤 = models.TextField(blank=True, null=True)
    教諭_平均経験年数_非常勤 = models.TextField(blank=True, null=True)
    家庭的保育者_常勤 = models.TextField(blank=True, null=True)
    家庭的保育補助者_非常勤 = models.TextField(blank=True, null=True)
    家庭的保育者_労働時間 = models.TextField(blank=True, null=True)
    家庭的保育者_平均経験年数_常勤 = models.TextField(blank=True, null=True)
    家庭的保育者_平均経験年数_非常勤 = models.TextField(blank=True, null=True)
    看護師_従業者数_常勤 = models.TextField(blank=True, null=True)
    看護師_従業者数_非常勤 = models.TextField(blank=True, null=True)
    看護師_労働時間 = models.TextField(blank=True, null=True)
    看護師_平均経験年数_常勤 = models.TextField(blank=True, null=True)
    看護師_平均経験年数_非常勤 = models.TextField(blank=True, null=True)
    合計_従業者数_常勤 = models.TextField(blank=True, null=True)
    合計_従業者数_非常勤 = models.TextField(blank=True, null=True)
    職員一人当たりの子どもの数 = models.TextField(blank=True, null=True)
    有する免許_資格 = models.TextField(db_column='有する免許・資格', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    有する免許_資格_その他 = models.TextField(db_column='有する免許・資格_その他', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    開所日_開所曜日 = models.TextField(blank=True, null=True)
    開所日_平日開所時間 = models.TextField(blank=True, null=True)
    開所日_平日閉所時間 = models.TextField(blank=True, null=True)
    開所日_土曜日開所時間 = models.TextField(blank=True, null=True)
    開所日_土曜日閉所時間 = models.TextField(blank=True, null=True)
    開所日_日祝日開所時間 = models.TextField(blank=True, null=True)
    開所日_日祝日閉所時間 = models.TextField(blank=True, null=True)
    開所日_延長保育午前開所時間 = models.TextField(blank=True, null=True)
    開所日_延長保育午前閉所時間 = models.TextField(blank=True, null=True)
    開所日_延長保育午後開所時間 = models.TextField(blank=True, null=True)
    開所日_延長保育午後閉所時間 = models.TextField(blank=True, null=True)
    預かり保育時間_平日開所 = models.TextField(blank=True, null=True)
    預かり保育時間_平日閉所 = models.TextField(blank=True, null=True)
    預かり保育時間_土曜日開所 = models.TextField(blank=True, null=True)
    預かり保育時間_土曜日閉所 = models.TextField(blank=True, null=True)
    預かり保育時間_日祝日開所 = models.TextField(blank=True, null=True)
    預かり保育時間_日祝日閉所 = models.TextField(blank=True, null=True)
    number_0歳_利用定員数 = models.TextField(db_column='0歳_利用定員数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_0歳_利用者数 = models.TextField(db_column='0歳_利用者数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_0歳_学級数 = models.TextField(db_column='0歳_学級数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1歳_利用定員数 = models.TextField(db_column='1歳_利用定員数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1歳_利用者数 = models.TextField(db_column='1歳_利用者数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1歳_学級数 = models.TextField(db_column='1歳_学級数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2歳_利用定員数 = models.TextField(db_column='2歳_利用定員数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2歳_利用者数 = models.TextField(db_column='2歳_利用者数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2歳_学級数 = models.TextField(db_column='2歳_学級数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3歳_利用定員数 = models.TextField(db_column='3歳_利用定員数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3歳_利用者数 = models.TextField(db_column='3歳_利用者数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3歳_学級数 = models.TextField(db_column='3歳_学級数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4歳_利用定員数 = models.TextField(db_column='4歳_利用定員数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4歳_利用者数 = models.TextField(db_column='4歳_利用者数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4歳_学級数 = models.TextField(db_column='4歳_学級数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5歳_利用定員数 = models.TextField(db_column='5歳_利用定員数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5歳_利用者数 = models.TextField(db_column='5歳_利用者数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5歳_学級数 = models.TextField(db_column='5歳_学級数', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    合計_利用定員数 = models.TextField(blank=True, null=True)
    合計_利用者数 = models.TextField(blank=True, null=True)
    合計_学級数 = models.TextField(blank=True, null=True)
    運営方法 = models.TextField(blank=True, null=True)
    教育_保育の内容等 = models.TextField(db_column='教育・保育の内容等', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    給食の実施状況_実施状況 = models.TextField(blank=True, null=True)
    給食の実施状況_提供日 = models.TextField(blank=True, null=True)
    障害児の受け入れ体制 = models.TextField(blank=True, null=True)
    一時預かり事業の実施 = models.TextField(blank=True, null=True)
    病児保育事業の実施 = models.TextField(blank=True, null=True)
    居室面積 = models.TextField(blank=True, null=True)
    園舎面積 = models.TextField(blank=True, null=True)
    園庭面積 = models.TextField(blank=True, null=True)
    利用手続き = models.TextField(blank=True, null=True)
    選考基準 = models.TextField(blank=True, null=True)
    その他の利用 = models.TextField(blank=True, null=True)
    苦情に対する窓口状況 = models.TextField(blank=True, null=True)
    賠償すべき事故への対応 = models.TextField(blank=True, null=True)
    提供内容の特色 = models.TextField(blank=True, null=True)
    利用料_実費徴収_実費徴収の有無 = models.TextField(blank=True, null=True)
    利用料_実費徴収_理由 = models.TextField(blank=True, null=True)
    利用料_実費徴収_金額 = models.TextField(blank=True, null=True)
    利用料_上乗せ徴収_上乗せ徴収の有無 = models.TextField(blank=True, null=True)
    利用料_上乗せ徴収_理由 = models.TextField(blank=True, null=True)
    利用料_上乗せ徴収_金額 = models.TextField(blank=True, null=True)
    提供開始時の説明 = models.TextField(blank=True, null=True)
    利用者の同意 = models.TextField(blank=True, null=True)
    利用者負担の利用料に関する説明 = models.TextField(blank=True, null=True)
    相談_苦情等の対応のための取組 = models.TextField(db_column='相談、苦情等の対応のための取組', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    事故発生の防止及び発生時の対応 = models.TextField(blank=True, null=True)
    個人情報等の取組状況 = models.TextField(blank=True, null=True)
    第三者評価等の実施_結果の公表状況 = models.TextField(db_column='第三者評価等の実施・結果の公表状況', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    第三者評価等の結果 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allowed'


class AllowedFacilityData(models.Model):

    class Meta:
        managed = False
        db_table = 'allowed_facility_data'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AccountsUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class ChatChat(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'chat_chat'


class ChatChatParticipants(models.Model):
    id = models.BigAutoField(primary_key=True)
    chat = models.ForeignKey(ChatChat, models.DO_NOTHING)
    userprofile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat_chat_participants'
        unique_together = (('chat', 'userprofile'),)


class ChatMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField()
    chat = models.ForeignKey(ChatChat, models.DO_NOTHING)
    sender = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chat_message'


class Disallowed(models.Model):
    施設_事業所名 = models.TextField(db_column='施設・事業所名', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    設置者_法人格_field = models.TextField(db_column='設置者（法人格）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    設置者名 = models.TextField(blank=True, null=True)
    管理者 = models.TextField(blank=True, null=True)
    郵便番号 = models.TextField(blank=True, null=True)
    施設の所在地_都道府県 = models.TextField(db_column='施設の所在地 都道府県', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設の所在地_市区町村 = models.TextField(db_column='施設の所在地 市区町村', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設の所在地_町名_番地 = models.TextField(db_column='施設の所在地 町名・番地', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    施設の所在地_建物名_部屋番号等 = models.TextField(db_column='施設の所在地 建物名・部屋番号等', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    電話番号 = models.TextField(blank=True, null=True)
    交通手段_最寄り駅_線 = models.TextField(blank=True, null=True)
    交通手段_最寄り駅_駅 = models.TextField(blank=True, null=True)
    交通手段_バス = models.TextField(blank=True, null=True)
    交通手段_徒歩 = models.TextField(blank=True, null=True)
    事業の開始年月日 = models.TextField(blank=True, null=True)
    届け出受理日 = models.TextField(blank=True, null=True)
    施設類型 = models.TextField(blank=True, null=True)
    施設の設置主体 = models.TextField(blank=True, null=True)
    企業主導型保育事業 = models.TextField(blank=True, null=True)
    指導監督基準適合証明書交付_交付年月日_field = models.TextField(db_column='指導監督基準適合証明書交付（交付年月日）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    営業状況 = models.TextField(blank=True, null=True)
    備考 = models.TextField(blank=True, null=True)
    建物構造 = models.TextField(blank=True, null=True)
    建物構造_階層_field = models.TextField(db_column='建物構造（階層）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    建物形態 = models.TextField(blank=True, null=True)
    保育室_部屋数 = models.TextField(blank=True, null=True)
    保育室_面積 = models.TextField(blank=True, null=True)
    調理室_部屋数 = models.TextField(blank=True, null=True)
    調理室_面積 = models.TextField(blank=True, null=True)
    医務室_部屋数 = models.TextField(blank=True, null=True)
    医務室_面積 = models.TextField(blank=True, null=True)
    便所_部屋数 = models.TextField(blank=True, null=True)
    便所_面積 = models.TextField(blank=True, null=True)
    その他_部屋数 = models.TextField(blank=True, null=True)
    その他_面積 = models.TextField(blank=True, null=True)
    合計_面積 = models.TextField(blank=True, null=True)
    備考_1 = models.TextField(db_column='備考.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    利用定員の有無 = models.TextField(blank=True, null=True)
    number_0歳_利用定員数 = models.TextField(db_column='0歳-利用定員数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_0歳_利用児童数 = models.TextField(db_column='0歳-利用児童数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1歳_利用定員数 = models.TextField(db_column='1歳-利用定員数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1歳_利用児童数 = models.TextField(db_column='1歳-利用児童数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2歳_利用定員数 = models.TextField(db_column='2歳-利用定員数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2歳_利用児童数 = models.TextField(db_column='2歳-利用児童数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3歳_利用定員数 = models.TextField(db_column='3歳-利用定員数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3歳_利用児童数 = models.TextField(db_column='3歳-利用児童数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4歳_利用定員数 = models.TextField(db_column='4歳-利用定員数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4歳_利用児童数 = models.TextField(db_column='4歳-利用児童数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5歳_利用定員数 = models.TextField(db_column='5歳-利用定員数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5歳_利用児童数 = models.TextField(db_column='5歳-利用児童数', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    合計_利用定員数 = models.TextField(db_column='合計-利用定員数', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    合計_利用児童数 = models.TextField(db_column='合計-利用児童数', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    備考_2 = models.TextField(db_column='備考.2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    開所閉所時間_平日開所 = models.TextField(blank=True, null=True)
    開所閉所時間_平日閉所 = models.TextField(blank=True, null=True)
    開所閉所時間_土曜開所 = models.TextField(blank=True, null=True)
    開所閉所時間_土曜閉所 = models.TextField(blank=True, null=True)
    開所閉所時間_日祝日開所 = models.TextField(blank=True, null=True)
    開所閉所時間_日祝日閉所 = models.TextField(blank=True, null=True)
    延長保育_有無 = models.TextField(blank=True, null=True)
    延長保育_時間 = models.TextField(blank=True, null=True)
    一時保育 = models.TextField(blank=True, null=True)
    夜間保育 = models.TextField(blank=True, null=True)
    number_24時間保育 = models.TextField(db_column='24時間保育', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    病児保育 = models.TextField(blank=True, null=True)
    保育料_月極額_0歳 = models.TextField(blank=True, null=True)
    保育料_月極額_1歳 = models.TextField(blank=True, null=True)
    保育料_月極額_2歳 = models.TextField(blank=True, null=True)
    保育料_月極額_3歳 = models.TextField(blank=True, null=True)
    保育料_月極額_4歳 = models.TextField(blank=True, null=True)
    保育料_月極額_5歳 = models.TextField(blank=True, null=True)
    保育料_定期契約_0歳 = models.TextField(blank=True, null=True)
    保育料_定期契約_1歳 = models.TextField(blank=True, null=True)
    保育料_定期契約_2歳 = models.TextField(blank=True, null=True)
    保育料_定期契約_3歳 = models.TextField(blank=True, null=True)
    保育料_定期契約_4歳 = models.TextField(blank=True, null=True)
    保育料_定期契約_5歳 = models.TextField(blank=True, null=True)
    保育料_一時預かり_0歳 = models.TextField(blank=True, null=True)
    保育料_一時預かり_1歳 = models.TextField(blank=True, null=True)
    保育料_一時預かり_2歳 = models.TextField(blank=True, null=True)
    保育料_一時預かり_3歳 = models.TextField(blank=True, null=True)
    保育料_一時預かり_4歳 = models.TextField(blank=True, null=True)
    保育料_一時預かり_5歳 = models.TextField(blank=True, null=True)
    保育料以外の実費_食事代 = models.TextField(blank=True, null=True)
    保育料以外の実費_入会金 = models.TextField(blank=True, null=True)
    保育料以外の実費_キャンセル料 = models.TextField(blank=True, null=True)
    保育料以外の実費_その他 = models.TextField(blank=True, null=True)
    変更を生じたことがある場合にあっては当該変 = models.TextField(blank=True, null=True)
    備考_3 = models.TextField(db_column='備考.3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    保育従事者数_常勤 = models.TextField(blank=True, null=True)
    保育従事者数_非常勤 = models.TextField(blank=True, null=True)
    有資格者数_保育者士 = models.TextField(blank=True, null=True)
    有資格者数_看護師 = models.TextField(blank=True, null=True)
    有資格者数_家庭的保育者等 = models.TextField(blank=True, null=True)
    研修受講者数_居宅訪問型保育研修 = models.TextField(blank=True, null=True)
    研修受講者数_子育て支援員研修 = models.TextField(blank=True, null=True)
    研修受講者数_家庭的保育者等研修 = models.TextField(blank=True, null=True)
    研修受講者数_その他 = models.TextField(blank=True, null=True)
    保育士その他の職員の配置予定 = models.TextField(blank=True, null=True)
    備考_4 = models.TextField(db_column='備考.4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    前年度年次報告提出実績 = models.TextField(blank=True, null=True)
    前年度監査実績_改善事項の有無_field = models.TextField(db_column='前年度監査実績（改善事項の有無）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    過去の事業停止命令_施設閉鎖命令の歴有無 = models.TextField(db_column='過去の事業停止命令・施設閉鎖命令の歴有無', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    行政処分歴_01_処分を行った自治体 = models.TextField(db_column='行政処分歴(01)_処分を行った自治体', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    行政処分歴_01_処分の種類 = models.TextField(db_column='行政処分歴(01)_処分の種類', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    行政処分歴_01_処分年月日 = models.TextField(db_column='行政処分歴(01)_処分年月日', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    保険_01_保険の種類 = models.TextField(db_column='保険(01)_保険の種類', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    保険_01_保険事故_内容_field = models.TextField(db_column='保険(01)_保険事故(内容)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    保険_01_保険金額 = models.TextField(db_column='保険(01)_保険金額', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    保険_02_保険の種類 = models.TextField(db_column='保険(02)_保険の種類', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    保険_02_保険事故_内容_field = models.TextField(db_column='保険(02)_保険事故(内容)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    保険_02_保険金額 = models.TextField(db_column='保険(02)_保険金額', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    保険_03_保険の種類 = models.TextField(db_column='保険(03)_保険の種類', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    保険_03_保険事故_内容_field = models.TextField(db_column='保険(03)_保険事故(内容)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    保険_03_保険金額 = models.TextField(db_column='保険(03)_保険金額', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    緊急時等における対応方法 = models.TextField(blank=True, null=True)
    非常災害対策 = models.TextField(blank=True, null=True)
    虐待の防止のための措置に関する事項 = models.TextField(blank=True, null=True)
    備考_6 = models.TextField(db_column='備考.6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    マッチングサイト関係_ベビーシッターのみ = models.TextField(db_column='マッチングサイト関係（※ベビーシッターのみ', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    備考_7 = models.TextField(db_column='備考.7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    無償化に係る確認申請の提出状況 = models.TextField(blank=True, null=True)
    幼児教育_保育の無償化に係る確認申請の提出 = models.TextField(db_column='幼児教育・保育の無償化に係る確認申請の提出', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    子ども_子育て支援施設等確認の有無 = models.TextField(db_column='子ども・子育て支援施設等確認の有無', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    幼児教育_保育の無償化について = models.TextField(db_column='幼児教育・保育の無償化について', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    情報入力更新日 = models.TextField(blank=True, null=True)
    直近の立入調査日_field = models.TextField(db_column='直近の立入調査日\u3000', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    連絡用メールアドレス = models.TextField(blank=True, null=True)
    直近の立ち入り調査日 = models.TextField(blank=True, null=True)
    施設の紹介 = models.TextField(blank=True, null=True)
    ホームページ = models.TextField(blank=True, null=True)
    市町から確認を受けた日 = models.TextField(blank=True, null=True)
    立入調査年月日 = models.TextField(blank=True, null=True)
    指摘事項の有無 = models.TextField(blank=True, null=True)
    立入調査指摘事項の内容 = models.TextField(blank=True, null=True)
    指導監督基準を満たす旨の証明書の有無 = models.TextField(blank=True, null=True)
    指導監督基準を満たす旨の証明書取得年月日_field = models.TextField(db_column='指導監督基準を満たす旨の証明書取得年月日\t', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    無償化対象施設 = models.TextField(blank=True, null=True)
    備考2 = models.TextField(blank=True, null=True)
    企業主導型保育事業助成決定の有無 = models.TextField(blank=True, null=True)
    地方裁量型認定こども園の認定の有無 = models.TextField(blank=True, null=True)
    久留米市が開催する保育施設等職員研修の受講 = models.TextField(blank=True, null=True)
    field_認可外保育施設指導監督基準を満たす旨の証 = models.TextField(db_column='「認可外保育施設指導監督基準を満たす旨の証', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'disallowed'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DonationDonation(models.Model):
    id = models.BigAutoField(primary_key=True)
    donation_type = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_frequency = models.CharField(max_length=10, blank=True, null=True)
    is_anonymous = models.BooleanField()
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'donation_donation'


class InquiriesInquiry(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    user = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    title = models.CharField(max_length=255)
    views = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inquiries_inquiry'


class InquiriesInquiryTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    inquiry = models.ForeignKey(InquiriesInquiry, models.DO_NOTHING)
    tag = models.ForeignKey('InquiriesTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inquiries_inquiry_tags'
        unique_together = (('inquiry', 'tag'),)


class InquiriesReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    reason = models.TextField()
    created_at = models.DateTimeField()
    reported_user = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    reporter = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING, related_name='inquiriesreport_reporter_set')

    class Meta:
        managed = False
        db_table = 'inquiries_report'


class InquiriesResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    inquiry = models.ForeignKey(InquiriesInquiry, models.DO_NOTHING)
    user = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inquiries_response'


class InquiriesSavedinquiry(models.Model):
    id = models.BigAutoField(primary_key=True)
    saved_at = models.DateTimeField()
    inquiry = models.ForeignKey(InquiriesInquiry, models.DO_NOTHING)
    responder = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inquiries_savedinquiry'
        unique_together = (('responder', 'inquiry'),)


class InquiriesSavedresponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    saved_at = models.DateTimeField()
    response = models.ForeignKey(InquiriesResponse, models.DO_NOTHING)
    user = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inquiries_savedresponse'


class InquiriesTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'inquiries_tag'


class MainAnnouncement(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'main_announcement'
