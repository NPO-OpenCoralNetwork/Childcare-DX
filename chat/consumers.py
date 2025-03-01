import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, Message
from django.utils import timezone  # タイムスタンプ用
import logging

logger = logging.getLogger(__name__)
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            # 早期にacceptを実行
            await self.accept()
            
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'

            if self.scope["user"].is_anonymous:
                logger.warning("Anonymous user connection rejected")
                await self.close()
                return

            # グループへの追加を試みる
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            
            logger.info(f"WebSocket connected: {self.room_group_name}")

        except Exception as e:
            logger.error(f"Connection error: {str(e)}", exc_info=True)
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