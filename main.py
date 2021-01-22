import discord
import random
import json

class Client(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$losuj') or message.content.startswith('$pseudolosuj'):
            with open('data.json') as file:
                data = json.load(file)
                num = random.randint(1, int(data['liczba osob']))
                while data[str(num)] == 'wykreslony':
                    num = random.randint(1, int(data['liczba osob']))
                print(f'{num} - {data[str(num)]}')
                await message.channel.send(f'{num} - {data[str(num)]}')

client = Client()
client.run('token')
