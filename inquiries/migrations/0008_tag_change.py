from django.db import migrations

def update_tags(apps, schema_editor):
    Tag = apps.get_model('inquiries', 'Tag')
    # 既存のタグをすべて削除（必要に応じてフィルタリングしてください）
    Tag.objects.all().delete()
    # 新しいタグのリスト
    new_tags = [
        '病気', '風邪', '嫌々期', '障碍児', '発達', '病院',
        '保育所', 'こども園', '幼稚園', '子育て支援', '発熱', '熱性けいれん', '子供',
        'スマホ'
    ]
    for tag_name in new_tags:
        Tag.objects.create(name=tag_name)

def reverse_update_tags(apps, schema_editor):
    Tag = apps.get_model('inquiries', 'Tag')
    # ロールバックのために新しいタグを削除し、元のタグを再作成する（元のデータが必要な場合）
    Tag.objects.all().delete()
    original_tags = [
        '認知症', 'せん妄', '身体障碍', '精神障碍', '昼夜逆転', '寝たきり',
        '施設', '家族間トラブル', '介護認定', '介護制度', '障碍者手帳', 'ヤングケアラー', '老々介護',
        '依存症', 'ギャンブル', '薬物', 'アルコール', '精神病', '終末期ケア', '居宅介護',
    ]
    for tag_name in original_tags:
        Tag.objects.create(name=tag_name)

class Migration(migrations.Migration):

    dependencies = [
        # 依存関係は適宜設定してください
        ('inquiries', '0007_report'),
    ]

    operations = [
        migrations.RunPython(update_tags, reverse_update_tags),
    ]
