from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0001_initial'),  # 既存のマイグレーションに依存
    ]

    operations = [
        migrations.RunSQL("""
            CREATE TABLE IF NOT EXISTS channels_postgres_message (
                id SERIAL PRIMARY KEY,
                channel TEXT NOT NULL,
                message TEXT NOT NULL,
                created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                expires TIMESTAMP WITH TIME ZONE
            );
            CREATE INDEX IF NOT EXISTS channels_postgres_message_channel_idx 
            ON channels_postgres_message(channel);
            
            CREATE TABLE IF NOT EXISTS channels_postgres_group (
                group_name TEXT PRIMARY KEY,
                created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );
        """, """
            DROP TABLE IF EXISTS channels_postgres_message;
            DROP TABLE IF EXISTS channels_postgres_group;
        """)
    ]