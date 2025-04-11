import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Chat, Message
from django.utils import timezone

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            # 早期にacceptを実行
            await self.accept()
            
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'chat_{self.room_name}'
    
            # グループへの追加をタイムアウト付きで実行
            from asyncio import wait_for
            await wait_for(
                self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name
                ),
                timeout=5.0
            )
            
        except Exception as e:
            logger.error(f"Connection error: {str(e)}")
            await self.close()

    async def disconnect(self, close_code):
        try:
            # グループから削除
            if hasattr(self, 'room_group_name'):
                await self.channel_layer.group_discard(
                    self.room_group_name,
                    self.channel_name
                )
            logger.info(f"WebSocket disconnected: {getattr(self, 'room_group_name', 'unknown')}")
        except Exception as e:
            logger.error(f"Disconnect error: {str(e)}")

    @database_sync_to_async
    def get_chat(self):
        return Chat.objects.get(id=self.room_name)

    @database_sync_to_async
    def save_message(self, chat, user, message_text):
        return Message.objects.create(
            chat=chat,
            sender=user,
            text=message_text
        )

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

            if not message.strip():
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
            logger.error(f"Message handling error: {str(e)}", exc_info=True)

    async def chat_message(self, event):
        try:
            await self.send(text_data=json.dumps({
                'message': event['message'],
                'sender': event['sender'],
                'timestamp': event['timestamp']
            }))
        except Exception as e:
            logger.error(f"Chat message error: {str(e)}", exc_info=True)