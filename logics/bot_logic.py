import asyncio
from telebot.async_telebot import AsyncTeleBot
from config.config import TOKEN
from logics.AI import return_ollama

class Bot:
    def __init__(self) -> None:
        self.bot = AsyncTeleBot(TOKEN)
        
    def command_processing(self):
        @self.bot.message_handler(func=lambda message : True)
        async def echo(message):
            result = await return_ollama(message.text)  
            await self.bot.reply_to(message, result)
            
    def run(self):
        asyncio.run(self.bot.polling())