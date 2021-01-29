import io
from discord.ext import commands
import discord
from discord.ext.commands import Bot

intents = discord.Intents.default()
intents.members = True
client = discord.Client()
bot = commands.Bot(command_prefix='/', description='Hola, soy EternalBot programado para ayudar a los nuevos jugadores! aqui abajo tienes diferentes comandos que te pueden servir de ayuda', intents=intents)

def field(parm1, parm2, parm3):
    return parm1.add_field(name=parm2, value=parm3)   

@bot.command(pass_context=True)
async def info(ctx, tipo):
    if tipo == "minecraft":
        em1 = discord.Embed(title="Eternity craft come back", description="Un servidor de minecraft técnico", color= discord.Color.dark_gold())
        field(em1, "IP", "190.210.218.26:25565")
        em1.set_image(url='https://media.discordapp.net/attachments/666358207614156801/803389835419058237/Logo_Eternity_craft_Come_Back.JPG')
        await ctx.send(embed = em1)
        await ctx.send("Reglas del servidor: ",file=discord.File('Reglas_eternity.docx'))
    if tipo == "discord":
        em2 = discord.Embed(title="Eternity craft come back", description="Servidor de discord para minecraft", color= discord.Color.dark_gold())
        field(em2, "Creado por:", "MaxiTaxi#5252" )
        field(em2,"Hoster:", "ElPro00F#1899" )
        field(em2, "admin:", "luc#9977")
        field(em2, "Mod:","giovacra#2591" )
        field(em2, "Helper:","TLONOXS_P#2993" )
        em2.set_image(url='https://media.discordapp.net/attachments/666358207614156801/803389835419058237/Logo_Eternity_craft_Come_Back.JPG')
        await ctx.send(embed=em2 )
    if tipo == "bot":
        em = discord.Embed(title="Eternity bot", description="Un bot creado con el fin de servir al servidor de minecraft", color=discord.Color.purple())
        field(em, "Creado por: ", "luc#9977" )
        field(em, "Logo creado por", "MaxiTaxi#5252")
        em.set_image(url="https://cdn.discordapp.com/attachments/666358207614156801/803385275615019018/Eternal_BOT_logo.JPG")
        await ctx.send(embed=em)
    if tipo !="bot" and tipo!="discord" and tipo != "minecraft":
        await ctx.send("Para ver la info del server de minecraft, discord o del bot, coloque el comando /info seguido de lo que quieres saber (minecraft/discord/bot)")
@bot.command()
async def rules(ctx):
    await ctx.send("```\n Reglas basicas: \n - No grifiar \n - No usar archivos externos al juego \n - No modificar parametros del juego. \n mas informacion en /info minecraft \n```")
'''
    obtener la Id de un servidor
    @bot.command(pass_context=True)
    async def getguild(ctx):
    id = ctx.message.guild.id
    print(id)
'''
@bot.command()
async def Ban_list(ctx):
    baned= await ctx.message.guild.bans()
    await ctx.send(baned)
@bot.command()
async def factions(ctx):
    fac = open("fac.txt", "r")
    await ctx.send(fac.read())
    fac.close()
@bot.command()
async def createfacction(ctx, nombre,in2,in3,in4):
    await ctx.guild.create_role(name= nombre)
    dueño =ctx.message.author
    fac = open("fac.txt", "a")
    fac.write('\nFacción {} dueño: {}. Integrantes: {}, {}, {}'.format(nombre, dueño, in2,in3,in4))
    rol = discord.utils.get(dueño.guild.roles, name=nombre)
    await bot.get_channel(803612218339885057).send("!una nueva faccion se unio a nuestro server¡ \n Nombre: {} \n Dueño:{}\n integrantes:{},{},{}".format(nombre, dueño, in2,in3,in4))
    await ctx.guild.create_voice_channel(name=nombre)
    await dueño.add_roles(rol)
    try:
        await ctx.guild.get_member_named(in2).add_roles(rol)
    except:
        pass
    try:
        await ctx.guild.get_member_named(in3).add_roles(rol)
    except:
        pass
    try:
        await ctx.guild.get_member_named(in4).add_roles(rol)
    except:
        pass
    fac.close()

@bot.command()
async def report(ctx, nombre, reporte):
    reporter = ctx.message.author
    await bot.get_channel(804089108217462806).send("El usuario {} a reportado a {} por {}".format(reporter, nombre, reporte ))
    await ctx.send("Tu reporte a sido enviado, muchas gracias")
    await ctx.message.delete()

@bot.command()
async def ruleacept(ctx, minname):
    await bot.get_channel(804089108217462806).send("El usuario {} acepto las reglas".format(minname))
    await ctx.send("En breve seras agregado a la lista blanca")
    

@bot.event
async def on_member_join(member):
    print("{} se a unido al servidor".format(member))
    await member.add_roles(discord.utils.get(member.guild.roles, name="Jugador"))
    await member.send("Hola, soy el bot de Eternity Craft y te voy a ayudar.\n Para empezar lo que debes hacer el leer estas reglas: ", file=discord.File('Reglas_eternity.docx'))
    await member.send("Cuando las termines de leer debes aceptarlas usando el comando /ruleacept [nombre de minecraft], esto te permite que puedas acceder al server.")
    await member.send("IMPORTANTE: el server de minecraft esta cerrado")
    await member.send("Para mas informacion existe el canal de bots update en el cual luc#9977 menciona las funciones que tiene este bot. \n Gracias")
    await bot.get_channel(804425234550620200).send("{} se unio a nuestro servidor.\n Disfruta de tu estadia.".format(member))
    
@bot.event
async def on_member_remove(member):
    print("{} se a ido del servidor".format(member))

@bot.event
async def on_ready():
    print("El bot se inicio correctamente")
bot.run('ODAzMzMzNjg5OTQ0OTY1MTQ5.YA8QzA.Ig0OSt2jMPa1canmvdouo_50SZk')
