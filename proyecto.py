import discord
import random
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot= commands.Bot(command_prefix="/",intents=intents)

datos=["1. Plantar un árbol puede absorber hasta 22 kg de CO₂ al año", 
      "2. Reciclar una lata de aluminio ahorra suficiente energía para ver televisión durante 3 horas",
      "3. Ducharse durante 5 minutos consume menos agua que llenar una bañera",
      "4. Reducir el consumo de carne una vez a la semana puede salvar hasta 7.000 litros de agua",
      "5. Una bolsa de tela puede reemplazar más de 700 bolsas de plástico al año",
      "6. Usar energía solar en casa puede reducir hasta un 80 porciento las emisiones de carbono domésticas",
      "7. Ir en bici en vez de coche reduce más de 200 gramos de CO₂ por kilómetro",
      "8. Apagar tus dispositivos por la noche puede ahorrar hasta 10 porciento de energía eléctrica mensual",
      "9. Hacer tus propios productos de limpieza ecológicos evita químicos contaminantes",
      "10. Las abejas polinizan el 75 porciento de los cultivos alimentarios del mundo"]

url="https://www.ecologiaverde.com/ecologia/"

@bot.event
async def on_ready():
    print(f"iniciando{bot.user}")


@bot.command()
async def dato_curioso (ctx):
    dtos= random.choice(datos)
    await ctx.send (f"Aquí tienes tu dato curioso 😉:{dtos}")

@bot.command()
async def imagen(ctx):
    listaimagenes= os.listdir("img")
    enviarimagen=random.choice(listaimagenes)
    with open(f'img\{enviarimagen}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def aprender(ctx):
    await ctx.send(f"claro dirigite aqui: {url}")

@bot.command()
async def clasificacion(ctx,*,objeto:str):
    reciclable=["botellas", "latas", "periódicos", "cartón", "revistas", "envases", "papel", "tetrapak", "plásticos", "vidrio", "hojas", "cajas", "folletos", "tapas", "empaques", "tubos", "archivadores", "sobres", "bolsas", "libros", "latas de aluminio", "frascos de vidrio", "papel de oficina", "cajas de cereales", "tetrabriks", "bandejas de plástico", "bolsas plásticas", "tapitas de botellas", "papel kraft", "papel periódico", "cajas de zapatos", "botellas de detergente", "envases de yogur", "papel higiénico sin usar", "papel de envolver", "papel bond", "revistas viejas", "catálogos", "folletos publicitarios", "cartones de huevo", "cajas de pizza limpias", "papel de cuadernos", "libretas", "cuadernos", "archivos manila", "sobres manila", "tubos de cartón", "bandejas de aluminio", "latas de conserva", "latas de refresco", "botellas de agua", "botellas de gaseosa", "botellas de jugo", "envases de productos de limpieza", "tarros de vidrio", "frascos de comida", "recipientes plásticos", "botellas de aceite vacías", "bolsas de supermercado reutilizables", "empaques de cartón corrugado", "papel para imprimir usado por una cara", "hojas de examen usadas", "papel reciclado"]
    no_reciclables=["pañuelos usados", "papel higiénico sucio", "servilletas sucias", "papeles con grasa", "envases con restos de comida", "cajas de pizza sucias", "espejos rotos", "vidrios rotos", "cerámica", "vajilla rota", "bombillas", "focos", "tubos fluorescentes", "pañales", "toallas sanitarias", "preservativos", "mascarillas", "guantes desechables", "jeringas", "hisopos", "cepillos de dientes", "esponjas", "colillas de cigarro", "cintas adhesivas", "cinta aislante", "cinta de embalar", "etiquetas plásticas", "bolsas metalizadas", "papel carbón", "papel plastificado", "fotos", "CDs", "DVDs", "disquetes", "juguetes rotos", "bolígrafos", "lapiceros vacíos", "marcadores", "brochas con pintura", "envases contaminados con químicos", "tubos de pasta dental", "tetrabriks sucios", "plásticos termoformados sucios", "espuma flex", "unicel", "poliestireno", "envoltorios de golosinas", "envoltorios de snacks", "envoltorios metalizados", "ropa interior usada", "zapatos rotos", "alfombras", "cintas de video", "cintas de cassette", "celofán", "piedras", "tierra", "cenizas", "residuos de jardinería", "residuos orgánicos cocidos", "excremento de mascotas", "basura de aspiradora", "pelos", "uñas", "plásticos combinados con metal o papel"]
 
    objeto=objeto.lower()
    
    if objeto in reciclable:
        await ctx.send(f"el {objeto}  es reciclable")
    elif objeto in  no_reciclables:
        await ctx.send(f"el {objeto } no es reciclabe")
    else :
        await ctx.send(f"desconosco información del {objeto}")

bot.run()
