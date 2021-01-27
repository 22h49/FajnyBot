import discord
import random
import json

from decouple import config

class Client(discord.Client):
    data = {}
    chosenIDs = []

    async def on_ready(self):
        print('Logged on as {}!'.format(self.user))

        dataFromFile = json.load(open('data.json'))
        self.data = {
            key: dataFromFile[key]
            for key in dataFromFile
            if dataFromFile[key] != None
        }

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$losuj') or message.content.startswith('$pseudolosuj'):
            notChosen = {
                key: self.data[key]
                for key in self.data
                if key not in self.chosenIDs
            }

            chosen = random.choice(list(notChosen.items()))
            if (len(self.chosenIDs) < len(self.data)):
                self.chosenIDs.append(chosen[0])
            else:
                self.chosenIDs = []

            print('{} - {}'.format(chosen[0], chosen[1]))
            await message.channel.send('{} - {}'.format(chosen[0], chosen[1]))

client = Client()
client.run(config('BOT_TOKEN'))