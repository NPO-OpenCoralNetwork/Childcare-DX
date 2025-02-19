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
    �@�l���̎�� = models.TextField(blank=True, null=True)
    �@�l���̖���_�ӂ肪��_field = models.TextField(db_column='�@�l���̖���(�ӂ肪��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �@�l���̖��� = models.TextField(blank=True, null=True)
    �@�l���̎傽�鎖�����̏��ݒn_�X�֔ԍ� = models.TextField(blank=True, null=True)
    �@�l���̎傽�鎖�����̏��ݒn_�s���{�� = models.TextField(blank=True, null=True)
    �@�l���̎傽�鎖�����̏��ݒn_�s�撬�� = models.TextField(blank=True, null=True)
    �@�l���̎傽�鎖�����̏��ݒn_����_�Ԓn = models.TextField(db_column='�@�l���̎傽�鎖�����̏��ݒn_�����E�Ԓn', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �@�l���̎傽�鎖�����̏��ݒn_������_���� = models.TextField(db_column='�@�l���̎傽�鎖�����̏��ݒn_�������E����', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �@�l���̘A����_�d�b�ԍ� = models.TextField(blank=True, null=True)
    �@�l���̘A����_���̑��A���� = models.TextField(blank=True, null=True)
    �@�l����\�҂̎��� = models.TextField(blank=True, null=True)
    �@�l����\�҂̐E�� = models.TextField(blank=True, null=True)
    �@�l���̐ݗ��N���� = models.TextField(blank=True, null=True)
    �@�l������_�ۈ��񋟂�_���͒񋟂��悤�� = models.TextField(db_column='�@�l������E�ۈ��񋟂��A���͒񋟂��悤��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�ݗތ^ = models.TextField(blank=True, null=True)
    �{�݂̖���_�ӂ肪��_field = models.TextField(db_column='�{�݂̖���(�ӂ肪��)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �{�݂̖��� = models.TextField(blank=True, null=True)
    ���Ə��ԍ� = models.TextField(blank=True, null=True)
    �X�֔ԍ� = models.TextField(blank=True, null=True)
    �{�݂̏��ݒn_�s���{�� = models.TextField(db_column='�{�݂̏��ݒn �s���{��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�݂̏��ݒn_�s�撬�� = models.TextField(db_column='�{�݂̏��ݒn �s�撬��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�݂̏��ݒn_����_�Ԓn = models.TextField(db_column='�{�݂̏��ݒn �����E�Ԓn', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�݂̏��ݒn_������_�����ԍ��� = models.TextField(db_column='�{�݂̏��ݒn �������E�����ԍ���', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�݂̘A����_�d�b�ԍ� = models.TextField(db_column='�{�݂̘A���� �d�b�ԍ�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�݂̘A����_���̑��A���� = models.TextField(db_column='�{�݂̘A���� ���̑��A����', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�݂̐ݒu��� = models.TextField(blank=True, null=True)
    �{��_�Ǘ��Ҏ��� = models.TextField(db_column='�{�� �Ǘ��Ҏ���', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{��_�Ǘ��ҐE�� = models.TextField(db_column='�{�� �Ǘ��ҐE��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ���Ƃ̔F�N���� = models.TextField(blank=True, null=True)
    ���Ƃ̊J�n�N���� = models.TextField(blank=True, null=True)
    ���Ƃ̊m�F�N���� = models.TextField(blank=True, null=True)
    �c�Ə� = models.TextField(blank=True, null=True)
    �ۈ狳�@_�]�ƎҐ�_��� = models.TextField(blank=True, null=True)
    �ۈ狳�@_�]�ƎҐ�_���� = models.TextField(blank=True, null=True)
    �ۈ狳�@_�J������ = models.TextField(blank=True, null=True)
    �ۈ狳�@_���όo���N��_��� = models.TextField(blank=True, null=True)
    �ۈ狳�@_���όo���N��_���� = models.TextField(blank=True, null=True)
    ���@���͕ۈ�m_�]�ƎҐ�_��� = models.TextField(blank=True, null=True)
    ���@���͕ۈ�m_�]�ƎҐ�_���� = models.TextField(blank=True, null=True)
    ���@���͕ۈ�m_�J������ = models.TextField(blank=True, null=True)
    ���@���͕ۈ�m_���όo���N��_��� = models.TextField(blank=True, null=True)
    ���@���͕ۈ�m_���όo���N��_���� = models.TextField(blank=True, null=True)
    �ۈ�m_�]�ƎҐ�_��� = models.TextField(blank=True, null=True)
    �ۈ�m_�]�ƎҐ�_���� = models.TextField(blank=True, null=True)
    �ۈ�m_�J������ = models.TextField(blank=True, null=True)
    �ۈ�m_���όo���N��_��� = models.TextField(blank=True, null=True)
    �ۈ�m_���όo���N��_���� = models.TextField(blank=True, null=True)
    �ۈ�]����_�]�ƎҐ�_��� = models.TextField(blank=True, null=True)
    �ۈ�]����_�]�ƎҐ�_���� = models.TextField(blank=True, null=True)
    �ۈ�]����_�J������ = models.TextField(blank=True, null=True)
    �ۈ�]����_���όo���N��_��� = models.TextField(blank=True, null=True)
    �ۈ�]����_���όo���N��_���� = models.TextField(blank=True, null=True)
    ���@_�]�ƎҐ�_��� = models.TextField(blank=True, null=True)
    ���@_�]�ƎҐ�_���� = models.TextField(blank=True, null=True)
    ���@_�J������ = models.TextField(blank=True, null=True)
    ���@_���όo���N��_��� = models.TextField(blank=True, null=True)
    ���@_���όo���N��_���� = models.TextField(blank=True, null=True)
    �ƒ�I�ۈ��_��� = models.TextField(blank=True, null=True)
    �ƒ�I�ۈ�⏕��_���� = models.TextField(blank=True, null=True)
    �ƒ�I�ۈ��_�J������ = models.TextField(blank=True, null=True)
    �ƒ�I�ۈ��_���όo���N��_��� = models.TextField(blank=True, null=True)
    �ƒ�I�ۈ��_���όo���N��_���� = models.TextField(blank=True, null=True)
    �Ō�t_�]�ƎҐ�_��� = models.TextField(blank=True, null=True)
    �Ō�t_�]�ƎҐ�_���� = models.TextField(blank=True, null=True)
    �Ō�t_�J������ = models.TextField(blank=True, null=True)
    �Ō�t_���όo���N��_��� = models.TextField(blank=True, null=True)
    �Ō�t_���όo���N��_���� = models.TextField(blank=True, null=True)
    ���v_�]�ƎҐ�_��� = models.TextField(blank=True, null=True)
    ���v_�]�ƎҐ�_���� = models.TextField(blank=True, null=True)
    �E����l������̎q�ǂ��̐� = models.TextField(blank=True, null=True)
    �L����Ƌ�_���i = models.TextField(db_column='�L����Ƌ��E���i', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �L����Ƌ�_���i_���̑� = models.TextField(db_column='�L����Ƌ��E���i_���̑�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �J����_�J���j�� = models.TextField(blank=True, null=True)
    �J����_�����J������ = models.TextField(blank=True, null=True)
    �J����_���������� = models.TextField(blank=True, null=True)
    �J����_�y�j���J������ = models.TextField(blank=True, null=True)
    �J����_�y�j�������� = models.TextField(blank=True, null=True)
    �J����_���j���J������ = models.TextField(blank=True, null=True)
    �J����_���j�������� = models.TextField(blank=True, null=True)
    �J����_�����ۈ�ߑO�J������ = models.TextField(blank=True, null=True)
    �J����_�����ۈ�ߑO������ = models.TextField(blank=True, null=True)
    �J����_�����ۈ�ߌ�J������ = models.TextField(blank=True, null=True)
    �J����_�����ۈ�ߌ������ = models.TextField(blank=True, null=True)
    �a����ۈ玞��_�����J�� = models.TextField(blank=True, null=True)
    �a����ۈ玞��_������ = models.TextField(blank=True, null=True)
    �a����ۈ玞��_�y�j���J�� = models.TextField(blank=True, null=True)
    �a����ۈ玞��_�y�j���� = models.TextField(blank=True, null=True)
    �a����ۈ玞��_���j���J�� = models.TextField(blank=True, null=True)
    �a����ۈ玞��_���j���� = models.TextField(blank=True, null=True)
    number_0��_���p����� = models.TextField(db_column='0��_���p�����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_0��_���p�Ґ� = models.TextField(db_column='0��_���p�Ґ�', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_0��_�w���� = models.TextField(db_column='0��_�w����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1��_���p����� = models.TextField(db_column='1��_���p�����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1��_���p�Ґ� = models.TextField(db_column='1��_���p�Ґ�', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1��_�w���� = models.TextField(db_column='1��_�w����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2��_���p����� = models.TextField(db_column='2��_���p�����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2��_���p�Ґ� = models.TextField(db_column='2��_���p�Ґ�', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2��_�w���� = models.TextField(db_column='2��_�w����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3��_���p����� = models.TextField(db_column='3��_���p�����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3��_���p�Ґ� = models.TextField(db_column='3��_���p�Ґ�', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3��_�w���� = models.TextField(db_column='3��_�w����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4��_���p����� = models.TextField(db_column='4��_���p�����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4��_���p�Ґ� = models.TextField(db_column='4��_���p�Ґ�', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4��_�w���� = models.TextField(db_column='4��_�w����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5��_���p����� = models.TextField(db_column='5��_���p�����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5��_���p�Ґ� = models.TextField(db_column='5��_���p�Ґ�', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5��_�w���� = models.TextField(db_column='5��_�w����', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    ���v_���p����� = models.TextField(blank=True, null=True)
    ���v_���p�Ґ� = models.TextField(blank=True, null=True)
    ���v_�w���� = models.TextField(blank=True, null=True)
    �^�c���@ = models.TextField(blank=True, null=True)
    ����_�ۈ�̓��e�� = models.TextField(db_column='����E�ۈ�̓��e��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ���H�̎��{��_���{�� = models.TextField(blank=True, null=True)
    ���H�̎��{��_�񋟓� = models.TextField(blank=True, null=True)
    ��Q���̎󂯓���̐� = models.TextField(blank=True, null=True)
    �ꎞ�a���莖�Ƃ̎��{ = models.TextField(blank=True, null=True)
    �a���ۈ玖�Ƃ̎��{ = models.TextField(blank=True, null=True)
    �����ʐ� = models.TextField(blank=True, null=True)
    ���ɖʐ� = models.TextField(blank=True, null=True)
    ����ʐ� = models.TextField(blank=True, null=True)
    ���p�葱�� = models.TextField(blank=True, null=True)
    �I�l� = models.TextField(blank=True, null=True)
    ���̑��̗��p = models.TextField(blank=True, null=True)
    ���ɑ΂��鑋���� = models.TextField(blank=True, null=True)
    �������ׂ����̂ւ̑Ή� = models.TextField(blank=True, null=True)
    �񋟓��e�̓��F = models.TextField(blank=True, null=True)
    ���p��_�����_������̗L�� = models.TextField(blank=True, null=True)
    ���p��_�����_���R = models.TextField(blank=True, null=True)
    ���p��_�����_���z = models.TextField(blank=True, null=True)
    ���p��_��悹����_��悹�����̗L�� = models.TextField(blank=True, null=True)
    ���p��_��悹����_���R = models.TextField(blank=True, null=True)
    ���p��_��悹����_���z = models.TextField(blank=True, null=True)
    �񋟊J�n���̐��� = models.TextField(blank=True, null=True)
    ���p�҂̓��� = models.TextField(blank=True, null=True)
    ���p�ҕ��S�̗��p���Ɋւ������ = models.TextField(blank=True, null=True)
    ���k_���̑Ή��̂��߂̎�g = models.TextField(db_column='���k�A���̑Ή��̂��߂̎�g', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ���̔����̖h�~�y�є������̑Ή� = models.TextField(blank=True, null=True)
    �l��񓙂̎�g�� = models.TextField(blank=True, null=True)
    ��O�ҕ]�����̎��{_���ʂ̌��\�� = models.TextField(db_column='��O�ҕ]�����̎��{�E���ʂ̌��\��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ��O�ҕ]�����̌��� = models.TextField(blank=True, null=True)

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
    �{��_���Ə��� = models.TextField(db_column='�{�݁E���Ə���', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �ݒu��_�@�l�i_field = models.TextField(db_column='�ݒu�ҁi�@�l�i�j', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ݒu�Җ� = models.TextField(blank=True, null=True)
    �Ǘ��� = models.TextField(blank=True, null=True)
    �X�֔ԍ� = models.TextField(blank=True, null=True)
    �{�݂̏��ݒn_�s���{�� = models.TextField(db_column='�{�݂̏��ݒn �s���{��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�݂̏��ݒn_�s�撬�� = models.TextField(db_column='�{�݂̏��ݒn �s�撬��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�݂̏��ݒn_����_�Ԓn = models.TextField(db_column='�{�݂̏��ݒn �����E�Ԓn', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �{�݂̏��ݒn_������_�����ԍ��� = models.TextField(db_column='�{�݂̏��ݒn �������E�����ԍ���', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �d�b�ԍ� = models.TextField(blank=True, null=True)
    ��ʎ�i_�Ŋ��w_�� = models.TextField(blank=True, null=True)
    ��ʎ�i_�Ŋ��w_�w = models.TextField(blank=True, null=True)
    ��ʎ�i_�o�X = models.TextField(blank=True, null=True)
    ��ʎ�i_�k�� = models.TextField(blank=True, null=True)
    ���Ƃ̊J�n�N���� = models.TextField(blank=True, null=True)
    �͂��o�󗝓� = models.TextField(blank=True, null=True)
    �{�ݗތ^ = models.TextField(blank=True, null=True)
    �{�݂̐ݒu��� = models.TextField(blank=True, null=True)
    ��Ǝ哱�^�ۈ玖�� = models.TextField(blank=True, null=True)
    �w���ē�K���ؖ�����t_��t�N����_field = models.TextField(db_column='�w���ē�K���ؖ�����t�i��t�N�����j', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �c�Ə� = models.TextField(blank=True, null=True)
    ���l = models.TextField(blank=True, null=True)
    �����\�� = models.TextField(blank=True, null=True)
    �����\��_�K�w_field = models.TextField(db_column='�����\���i�K�w�j', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �����`�� = models.TextField(blank=True, null=True)
    �ۈ玺_������ = models.TextField(blank=True, null=True)
    �ۈ玺_�ʐ� = models.TextField(blank=True, null=True)
    ������_������ = models.TextField(blank=True, null=True)
    ������_�ʐ� = models.TextField(blank=True, null=True)
    �㖱��_������ = models.TextField(blank=True, null=True)
    �㖱��_�ʐ� = models.TextField(blank=True, null=True)
    �֏�_������ = models.TextField(blank=True, null=True)
    �֏�_�ʐ� = models.TextField(blank=True, null=True)
    ���̑�_������ = models.TextField(blank=True, null=True)
    ���̑�_�ʐ� = models.TextField(blank=True, null=True)
    ���v_�ʐ� = models.TextField(blank=True, null=True)
    ���l_1 = models.TextField(db_column='���l.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ���p����̗L�� = models.TextField(blank=True, null=True)
    number_0��_���p����� = models.TextField(db_column='0��-���p�����', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_0��_���p������ = models.TextField(db_column='0��-���p������', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1��_���p����� = models.TextField(db_column='1��-���p�����', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_1��_���p������ = models.TextField(db_column='1��-���p������', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2��_���p����� = models.TextField(db_column='2��-���p�����', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_2��_���p������ = models.TextField(db_column='2��-���p������', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3��_���p����� = models.TextField(db_column='3��-���p�����', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_3��_���p������ = models.TextField(db_column='3��-���p������', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4��_���p����� = models.TextField(db_column='4��-���p�����', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_4��_���p������ = models.TextField(db_column='4��-���p������', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5��_���p����� = models.TextField(db_column='5��-���p�����', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_5��_���p������ = models.TextField(db_column='5��-���p������', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    ���v_���p����� = models.TextField(db_column='���v-���p�����', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ���v_���p������ = models.TextField(db_column='���v-���p������', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ���l_2 = models.TextField(db_column='���l.2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �J��������_�����J�� = models.TextField(blank=True, null=True)
    �J��������_������ = models.TextField(blank=True, null=True)
    �J��������_�y�j�J�� = models.TextField(blank=True, null=True)
    �J��������_�y�j�� = models.TextField(blank=True, null=True)
    �J��������_���j���J�� = models.TextField(blank=True, null=True)
    �J��������_���j���� = models.TextField(blank=True, null=True)
    �����ۈ�_�L�� = models.TextField(blank=True, null=True)
    �����ۈ�_���� = models.TextField(blank=True, null=True)
    �ꎞ�ۈ� = models.TextField(blank=True, null=True)
    ��ԕۈ� = models.TextField(blank=True, null=True)
    number_24���ԕۈ� = models.TextField(db_column='24���ԕۈ�', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    �a���ۈ� = models.TextField(blank=True, null=True)
    �ۈ痿_���Ɋz_0�� = models.TextField(blank=True, null=True)
    �ۈ痿_���Ɋz_1�� = models.TextField(blank=True, null=True)
    �ۈ痿_���Ɋz_2�� = models.TextField(blank=True, null=True)
    �ۈ痿_���Ɋz_3�� = models.TextField(blank=True, null=True)
    �ۈ痿_���Ɋz_4�� = models.TextField(blank=True, null=True)
    �ۈ痿_���Ɋz_5�� = models.TextField(blank=True, null=True)
    �ۈ痿_����_��_0�� = models.TextField(blank=True, null=True)
    �ۈ痿_����_��_1�� = models.TextField(blank=True, null=True)
    �ۈ痿_����_��_2�� = models.TextField(blank=True, null=True)
    �ۈ痿_����_��_3�� = models.TextField(blank=True, null=True)
    �ۈ痿_����_��_4�� = models.TextField(blank=True, null=True)
    �ۈ痿_����_��_5�� = models.TextField(blank=True, null=True)
    �ۈ痿_�ꎞ�a����_0�� = models.TextField(blank=True, null=True)
    �ۈ痿_�ꎞ�a����_1�� = models.TextField(blank=True, null=True)
    �ۈ痿_�ꎞ�a����_2�� = models.TextField(blank=True, null=True)
    �ۈ痿_�ꎞ�a����_3�� = models.TextField(blank=True, null=True)
    �ۈ痿_�ꎞ�a����_4�� = models.TextField(blank=True, null=True)
    �ۈ痿_�ꎞ�a����_5�� = models.TextField(blank=True, null=True)
    �ۈ痿�ȊO�̎���_�H���� = models.TextField(blank=True, null=True)
    �ۈ痿�ȊO�̎���_����� = models.TextField(blank=True, null=True)
    �ۈ痿�ȊO�̎���_�L�����Z���� = models.TextField(blank=True, null=True)
    �ۈ痿�ȊO�̎���_���̑� = models.TextField(blank=True, null=True)
    �ύX�𐶂������Ƃ�����ꍇ�ɂ����Ă͓��Y�� = models.TextField(blank=True, null=True)
    ���l_3 = models.TextField(db_column='���l.3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �ۈ�]���Ґ�_��� = models.TextField(blank=True, null=True)
    �ۈ�]���Ґ�_���� = models.TextField(blank=True, null=True)
    �L���i�Ґ�_�ۈ�Ҏm = models.TextField(blank=True, null=True)
    �L���i�Ґ�_�Ō�t = models.TextField(blank=True, null=True)
    �L���i�Ґ�_�ƒ�I�ۈ�ғ� = models.TextField(blank=True, null=True)
    ���C��u�Ґ�_����K��^�ۈ猤�C = models.TextField(blank=True, null=True)
    ���C��u�Ґ�_�q��Ďx�������C = models.TextField(blank=True, null=True)
    ���C��u�Ґ�_�ƒ�I�ۈ�ғ����C = models.TextField(blank=True, null=True)
    ���C��u�Ґ�_���̑� = models.TextField(blank=True, null=True)
    �ۈ�m���̑��̐E���̔z�u�\�� = models.TextField(blank=True, null=True)
    ���l_4 = models.TextField(db_column='���l.4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �O�N�x�N���񍐒�o���� = models.TextField(blank=True, null=True)
    �O�N�x�č�����_���P�����̗L��_field = models.TextField(db_column='�O�N�x�č����сi���P�����̗L���j', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ߋ��̎��ƒ�~����_�{�ݕ����߂̗�L�� = models.TextField(db_column='�ߋ��̎��ƒ�~���߁E�{�ݕ����߂̗�L��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �s��������_01_�������s���������� = models.TextField(db_column='�s��������(01)_�������s����������', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �s��������_01_�����̎�� = models.TextField(db_column='�s��������(01)_�����̎��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �s��������_01_�����N���� = models.TextField(db_column='�s��������(01)_�����N����', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �ی�_01_�ی��̎�� = models.TextField(db_column='�ی�(01)_�ی��̎��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �ی�_01_�ی�����_���e_field = models.TextField(db_column='�ی�(01)_�ی�����(���e)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ی�_01_�ی����z = models.TextField(db_column='�ی�(01)_�ی����z', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �ی�_02_�ی��̎�� = models.TextField(db_column='�ی�(02)_�ی��̎��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �ی�_02_�ی�����_���e_field = models.TextField(db_column='�ی�(02)_�ی�����(���e)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ی�_02_�ی����z = models.TextField(db_column='�ی�(02)_�ی����z', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �ی�_03_�ی��̎�� = models.TextField(db_column='�ی�(03)_�ی��̎��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �ی�_03_�ی�����_���e_field = models.TextField(db_column='�ی�(03)_�ی�����(���e)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �ی�_03_�ی����z = models.TextField(db_column='�ی�(03)_�ی����z', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �ً}�����ɂ�����Ή����@ = models.TextField(blank=True, null=True)
    ���ЊQ�΍� = models.TextField(blank=True, null=True)
    �s�҂̖h�~�̂��߂̑[�u�Ɋւ��鎖�� = models.TextField(blank=True, null=True)
    ���l_6 = models.TextField(db_column='���l.6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �}�b�`���O�T�C�g�֌W_�x�r�[�V�b�^�[�̂� = models.TextField(db_column='�}�b�`���O�T�C�g�֌W�i���x�r�[�V�b�^�[�̂�', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ���l_7 = models.TextField(db_column='���l.7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �������ɌW��m�F�\���̒�o�� = models.TextField(blank=True, null=True)
    �c������_�ۈ�̖������ɌW��m�F�\���̒�o = models.TextField(db_column='�c������E�ۈ�̖������ɌW��m�F�\���̒�o', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �q�ǂ�_�q��Ďx���{�ݓ��m�F�̗L�� = models.TextField(db_column='�q�ǂ��E�q��Ďx���{�ݓ��m�F�̗L��', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �c������_�ۈ�̖������ɂ��� = models.TextField(db_column='�c������E�ۈ�̖������ɂ���', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    �����͍X�V�� = models.TextField(blank=True, null=True)
    ���߂̗���������_field = models.TextField(db_column='���߂̗���������\u3000', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �A���p���[���A�h���X = models.TextField(blank=True, null=True)
    ���߂̗������蒲���� = models.TextField(blank=True, null=True)
    �{�݂̏Љ� = models.TextField(blank=True, null=True)
    �z�[���y�[�W = models.TextField(blank=True, null=True)
    �s������m�F���󂯂��� = models.TextField(blank=True, null=True)
    ���������N���� = models.TextField(blank=True, null=True)
    �w�E�����̗L�� = models.TextField(blank=True, null=True)
    ���������w�E�����̓��e = models.TextField(blank=True, null=True)
    �w���ē�𖞂����|�̏ؖ����̗L�� = models.TextField(blank=True, null=True)
    �w���ē�𖞂����|�̏ؖ����擾�N����_field = models.TextField(db_column='�w���ē�𖞂����|�̏ؖ����擾�N����\t', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    �������Ώێ{�� = models.TextField(blank=True, null=True)
    ���l2 = models.TextField(blank=True, null=True)
    ��Ǝ哱�^�ۈ玖�Ə�������̗L�� = models.TextField(blank=True, null=True)
    �n���ٗʌ^�F�肱�ǂ����̔F��̗L�� = models.TextField(blank=True, null=True)
    �v���Ďs���J�Â���ۈ�{�ݓ��E�����C�̎�u = models.TextField(blank=True, null=True)
    field_�F�O�ۈ�{�ݎw���ē�𖞂����|�̏� = models.TextField(db_column='�u�F�O�ۈ�{�ݎw���ē�𖞂����|�̏�', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.

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
