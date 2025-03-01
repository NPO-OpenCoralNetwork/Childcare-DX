import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, Message
from django.utils import timezone  # タイムスタンプ用

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'

            # ユーザー認証の確認を追加
            if self.scope["user"].is_anonymous:
                await self.close()
                return

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
            print(f"WebSocket connected: {self.room_group_name}")  # デバッグ用

        except Exception as e:
            print(f"Connection error: {str(e)}")  # デバッグ用
            await self.close()

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

            if not message.strip():  # 空メッセージのチェック
                return

            chat = await self.get_chat()
            user = self.scope['user']
            await self.save_message(chat, user, message)

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': user.username,
                    'timestamp': timestamp
                }
            )

        except Exception as e:
            print(f"Message handling error: {str(e)}")  # デバッグ用