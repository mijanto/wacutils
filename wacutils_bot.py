import discord
import os

client = discord.Client()
token = '<INSERT TOKEN HERE>'

#operationToRuletable="and1xor6or7nor8nand14"
operationToRuletable=[["and",1],["xor",6],["or",7],["nor",8],["nand",14]]

def operationBit(a,b,rule):
	return bin(rule)[(2*a+b)]

def operationNumber(a,b,rule):
	binary1 = bin(a)
	binary2 = bin(b)

#	while len(binary1) > len(binary2):
#		binary2 = '0' + binary2
	if len(binary1) > len(binary2):
		binary2 = ('0'*(len(binary1)-len(binary2))) + binary2
	elif len(binary1) < len(binary2):
		binary1 = ('0'*(len(binary2)-len(binary1))) + binary1

	out=""
	for b1, b2 in zip(a,b):
		out += operationBit(bit,)
		
# Same as operationNumber(), except the rule can be a string like "and" or "xor", and they will map to their corresponding ruletables (0001 and 0110 for "and" and "xor")
# Maps stored in operationToRuletable list
def operationWithMap(a,b,rule):
	if type(rule) is str:
		return 

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('&hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('&status'):
        msg = 'Im fine, thank you. How are you? {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)

# python3.6 wacutils_bot.py
