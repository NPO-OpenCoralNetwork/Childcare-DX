from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0002_rename_timestamp_chat_created_at_remove_chat_message_and_more'),
    ]

    operations = [
        migrations.RunSQL("""
            DROP TABLE IF EXISTS channels_postgres_groupchannel;
            DROP TABLE IF EXISTS channels_postgres_message;

            CREATE TABLE IF NOT EXISTS channels_postgres_message (
                id SERIAL PRIMARY KEY,
                channel TEXT NOT NULL,
                message TEXT NOT NULL,
                created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                expires TIMESTAMP WITH TIME ZONE
            );

            CREATE TABLE IF NOT EXISTS channels_postgres_groupchannel (
                group_name TEXT PRIMARY KEY,
                created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );

            CREATE INDEX IF NOT EXISTS channels_postgres_message_channel_idx 
            ON channels_postgres_message(channel);
        """, """
            DROP TABLE IF EXISTS channels_postgres_group;
            DROP TABLE IF EXISTS channels_postgres_message;
        """)
    ]