import discord
import requests
import json
import pycoingecko
from discord.ext import commands
from discord.ext.commands import Bot
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

client = commands.Bot(command_prefix = '$', case_insensitive = True)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="$cryptohelp"))
    print("Bot is on and is using {0.user} ".format(client))
    print(str(len(client.guilds)))

@client.command()
async def cryptohelp(ctx):
    embed=discord.Embed(title="Help", description="A list of all the supported Cryptocurrencies")
    embed.add_field(name="Aave", value="Value of aave", inline=True)
    embed.add_field(name="Avalanche", value="Value of avalanche", inline=True)
    embed.add_field(name="BinanceCoin", value="Value of binancecoin", inline=True)
    embed.add_field(name="Bitcoin", value="Value of bitcoin", inline=True)
    embed.add_field(name="BitcoinCash", value="Value of bitcoincash", inline=True)
    embed.add_field(name="BitcoinSV", value="Value of bitcoinsv", inline=True)
    embed.add_field(name="Cardano", value="Value of cardano", inline=True)
    embed.add_field(name="Chainlink", value="Value of chainlink", inline=True)
    embed.add_field(name="Cosmos", value="Value of cosmos", inline=True)
    embed.add_field(name="Dogecoin", value="Value of dogecoin", inline=True)
    embed.add_field(name="Eos", value="Value of eos", inline=True)
    embed.add_field(name="Ethereum", value="Value of ethereum", inline=True)
    embed.add_field(name="EthereumClassic", value="Value of ethereumclassic", inline=True)
    embed.add_field(name="FTXToken", value="Value of ftxtoken", inline=True)
    embed.add_field(name="Filecoin", value="Value of filecoin", inline=True)
    embed.add_field(name="IOTA", value="Value of iota", inline=True)
    embed.add_field(name="Kusama", value="Value of kusama", inline=True)
    embed.add_field(name="Litecoin", value="Value of litecoin", inline=True)
    embed.add_field(name="Maker", value="Value of maker", inline=True)
    embed.add_field(name="Neo", value="Value of neo", inline=True)
    embed.add_field(name="Orfano", value="Value of orfano", inline=True)
    embed.add_field(name="PancakeSwap", value="Value of pancakeswap", inline=True)
    embed.add_field(name="Polygon", value="Value of polygon", inline=True)
    embed.add_field(name="Ripple", value="Value of ripple", inline=True)
    embed.add_field(name="ShibaInu", value="Value of shibainu", inline=True)
    embed.add_field(name="Solana", value="Value of solana", inline=True)
    embed.add_field(name="Stellar", value="Value of stellar", inline=True)
    embed.add_field(name="Terra", value="Value of terra", inline=True)
    embed.add_field(name="Tezos", value="Value of tezos", inline=True)
    embed.add_field(name="Theta", value="Value of theta", inline=True)
    embed.add_field(name="Tron", value="Value of tron", inline=True)
    embed.add_field(name="Uniswap", value="Value of uniswap", inline=True)
    embed.add_field(name="UsdCoin", value="Value of usdcoin", inline=True)
    embed.add_field(name="Vechain", value="Value of vechain", inline=True)
    embed.add_field(name="Venus", value="Value of venus", inline=True)
    embed.add_field(name="WrappedBitcoin", value="Value of wrappedbitcoin", inline=True)
    await ctx.author.send(embed=embed)
    await ctx.send("Help sent in DM's.")

@client.command()
async def ping(ctx):
    await ctx.send(f'My ping is {client.latency}!')

@client.command()
async def Ethereum(ctx):
    ETH = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=aud").text
    ETH = json.loads(ETH)
    ETHCHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=aud&include_24hr_change=true").text
    ETHCHANGE = json.loads(ETHCHANGE)
    test = round(ETHCHANGE["ethereum"]["aud_24h_change"], 2)
    embed=discord.Embed(title="ETH", description="The value of Ethereum!", color=0x0294c4)
    embed.set_thumbnail(url="https://icons.iconarchive.com/icons/cjdowner/cryptocurrency-flat/1024/Ethereum-ETH-icon.png")
    embed.set_author(name = "Ethereum")
    embed.add_field(name=ETH["ethereum"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Bitcoin(ctx):
    BTC = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=aud").text
    BTC = json.loads(BTC)
    BTCCHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=aud&include_24hr_change=true").text
    BTCCHANGE = json.loads(BTCCHANGE)
    test = round(BTCCHANGE["bitcoin"]["aud_24h_change"], 2)
    embed=discord.Embed(title="BTC", description="The value of Bitcoin!", color=0xFF9900)
    embed.set_thumbnail(url="https://miro.medium.com/max/410/1*U7phpu7aKKrU05JvMvs-wA.png")
    embed.set_author(name = "Bitcoin")
    embed.add_field(name=BTC["bitcoin"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Dogecoin(ctx):
    DOGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=aud").text
    DOGE = json.loads(DOGE)
    DOGECHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=aud&include_24hr_change=true").text
    DOGECHANGE = json.loads(DOGECHANGE)
    test = round(DOGECHANGE["dogecoin"]["aud_24h_change"], 2)
    embed=discord.Embed(title="DOGE", description="The value of Dogecoin!", color=0xCB9800)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/d/d0/Dogecoin_Logo.png")
    embed.set_author(name = "Dogecoin")
    embed.add_field(name=DOGE["dogecoin"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def EthereumClassic(ctx):
    ETC = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum-classic&vs_currencies=aud").text
    ETC = json.loads(ETC)
    ETCCHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum-classic&vs_currencies=aud&include_24hr_change=true").text
    ETCCHANGE = json.loads(ETCCHANGE)
    test = round(ETCCHANGE["ethereum-classic"]["aud_24h_change"], 2)
    embed=discord.Embed(title="ETC", description="The value of Ethereum Classic!", color=0x8CC43C)
    embed.set_thumbnail(url="https://www.benzinga.com/files/images/story/2012/1321.png")
    embed.set_author(name = "Ethereum Classic")
    embed.add_field(name=ETC["ethereum-classic"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ShibaInu(ctx):
    SHIB = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=aud").text
    SHIB = json.loads(SHIB)
    SHIBCHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=aud&include_24hr_change=true").text
    SHIBCHANGE = json.loads(SHIBCHANGE)
    test = round(SHIBCHANGE["shiba-inu"]["aud_24h_change"], 2)
    embed=discord.Embed(title="SHIB", description="The value of Shiba Inu!", color=0x8E3C24)
    embed.set_thumbnail(url="https://styles.redditmedia.com/t5_3uvocd/styles/communityIcon_qgoetx3njan61.png?width=256&s=b32baf76be1c50fe7d04a6a2d7544878798d5255")
    embed.set_author(name = "Shiba Inu")
    embed.add_field(name=SHIB["shiba-inu"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Ripple(ctx):
    XRP = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=aud").text
    XRP = json.loads(XRP)
    XRPCHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=aud&include_24hr_change=true").text
    XRPCHANGE = json.loads(XRPCHANGE)
    test = round(XRPCHANGE["ripple"]["aud_24h_change"], 2)
    embed=discord.Embed(title="XRP", description="The value of Ripple!", color=0x434C54)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/xrp-xrp-logo.png")
    embed.set_author(name = "Ripple")
    embed.add_field(name=XRP["ripple"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Orfano(ctx):
    ORFAN = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=orfano&vs_currencies=aud").text
    ORFAN = json.loads(ORFAN)
    ORFANCHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=orfano&vs_currencies=aud&include_24hr_change=true").text
    ORFANCHANGE = json.loads(ORFANCHANGE)
    test = round(ORFANCHANGE["orfano"]["aud_24h_change"], 2)
    embed=discord.Embed(title="ORFANO", description="The value of Orfano!", color=0xC81CFC)
    embed.set_thumbnail(url="https://www.orfano.io/img/core-img/favicon.ico")
    embed.set_author(name = "Orfano")
    embed.add_field(name=ORFAN["orfano"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Litecoin(ctx):
    LTC = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=aud").text
    LTC = json.loads(LTC)
    LTCCHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=aud&include_24hr_change=true").text
    LTCCHANGE = json.loads(LTCCHANGE)
    test = round(LTCCHANGE["litecoin"]["aud_24h_change"], 2)
    embed=discord.Embed(title="LTC", description="The value of Litecoin!", color=0x333333)
    embed.set_thumbnail(url="https://cdn.freelogovectors.net/wp-content/uploads/2021/01/litecoin-logo-freelogovectors.net_.png")
    embed.set_author(name = "Litecoin")
    embed.add_field(name=LTC["litecoin"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Cardano(ctx):
    ADA = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=aud").text
    ADA = json.loads(ADA)
    ADACHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=aud&include_24hr_change=true").text
    ADACHANGE = json.loads(ADACHANGE)
    test = round(ADACHANGE["cardano"]["aud_24h_change"], 2)
    embed=discord.Embed(title="ADA", description="The value of Cardano!", color=0x0377FC)
    embed.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/crypto-currency-and-coin-2/256/cardano_ada-512.png")
    embed.set_author(name = "Cardano")
    embed.add_field(name=ADA["cardano"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def BinanceCoin(ctx):
    BNB = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=aud").text
    BNB = json.loads(BNB)
    BNBCHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=aud&include_24hr_change=true").text
    BNBCHANGE = json.loads(BNBCHANGE)
    test = round(BNBCHANGE["binancecoin"]["aud_24h_change"], 2)
    embed=discord.Embed(title="BNB", description="The value of Binance Coin!", color=0xF3BA2F)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/binance-coin-bnb-logo.png")
    embed.set_author(name = "Binance Coin")
    embed.add_field(name=BNB["binancecoin"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Venus(ctx):
    XVS = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=venus&vs_currencies=aud").text
    XVS = json.loads(XVS)
    XVSCHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=venus&vs_currencies=aud&include_24hr_change=true").text
    XVSCHANGE = json.loads(XVSCHANGE)
    test = round(XVSCHANGE["venus"]["aud_24h_change"], 2)
    embed=discord.Embed(title="XVS", description="The value of Venus!", color=0xF3BA2F)
    embed.set_thumbnail(url="https://research.binance.com/static/images/projects/venus/logo.png")
    embed.set_author(name = "Venus")
    embed.add_field(name=XVS["venus"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def IOTA(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=iota&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=iota&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["iota"]["aud_24h_change"], 2)
    embed=discord.Embed(title="MIOTA", description="The value of IOTA!", color=0x000000)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/iota-miota-logo.png")
    embed.set_author(name = "IOTA")
    embed.add_field(name=PRICE["iota"]["aud"], value="AUD", inline=False)
    embed.add_field(name=CHANGE["iota"]["aud_24h_change"], value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def FTXToken(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ftx-token&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ftx-token&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["ftx-token"]["aud_24h_change"], 2)
    embed=discord.Embed(title="FTT", description="The value of FTX Token!", color=0x00D0FF)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/ftx-token-ftt-logo.png")
    embed.set_author(name = "FTX Token")
    embed.add_field(name=PRICE["ftx-token"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Tezos(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=tezos&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=tezos&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["tezos"]["aud_24h_change"], 2)
    embed=discord.Embed(title="XTZ", description="The value of Tezos!", color=0x0088FF)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/tezos-xtz-logo.png?v=010")
    embed.set_author(name = "Tezos")
    embed.add_field(name=PRICE["tezos"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Cosmos(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cosmos&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=cosmos&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["cosmos"]["aud_24h_change"], 2)
    embed=discord.Embed(title="ATOM", description="The value of Cosmos!", color=0x050052)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/cosmos-atom-logo.png?v=010")
    embed.set_author(name = "Cosmos")
    embed.add_field(name=PRICE["cosmos"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def PancakeSwap(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=pancakeswap-token&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=pancakeswap-token&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["pancakeswap-token"]["aud_24h_change"], 2)
    embed=discord.Embed(title="CAKE", description="The value of PancakeSwap!", color=0xD47726)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/pancakeswap-cake-logo.png?v=010")
    embed.set_author(name = "PancakeSwap")
    embed.add_field(name=PRICE["pancakeswap-token"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Maker(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=maker&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=maker&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["maker"]["aud_24h_change"], 2)
    embed=discord.Embed(title="MKR", description="The value of Maker!", color=0x00ADA2)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/maker-mkr-logo.png?v=010")
    embed.set_author(name = "Maker")
    embed.add_field(name=PRICE["maker"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Avalanche(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=avalanche&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=avalanche&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["avalanche"]["aud_24h_change"], 2)
    embed=discord.Embed(title="AVAX", description="The value of Avalanche!", color=0xFF4D00)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/avalanche-avax-logo.png?v=010")
    embed.set_author(name = "Avalanche")
    embed.add_field(name=PRICE["avalanche"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Kusama(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=kusama&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=kusama&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["kusama"]["aud_24h_change"], 2)
    embed=discord.Embed(title="KSM", description="The value of Kusama!", color=0x000000)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/kusama-ksm-logo.png?v=010")
    embed.set_author(name = "Kusama")
    embed.add_field(name=PRICE["kusama"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Filecoin(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=filecoin&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=filecoin&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["filecoin"]["aud_24h_change"], 2)
    embed=discord.Embed(title="FIL", description="The value of Filecoin!", color=0x00B3FF)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/filecoin-fil-logo.png?v=010")
    embed.set_author(name = "Filecoin")
    embed.add_field(name=PRICE["filecoin"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Polygon(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=matic-network&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["matic-network"]["aud_24h_change"], 2)
    embed=discord.Embed(title="MATIC", description="The value of Polygon!", color=0x77299E)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/polygon-matic-logo.png?v=010")
    embed.set_author(name = "Polygon")
    embed.add_field(name=PRICE["matic-network"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Terra(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=terra-luna&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=terra-luna&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["terra-luna"]["aud_24h_change"], 2)
    embed=discord.Embed(title="LUNA", description="The value of Terra!", color=0x3700FF)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/terra-luna-luna-logo.png?v=010")
    embed.set_author(name = "Terra")
    embed.add_field(name=PRICE["terra-luna"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Solana(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["solana"]["aud_24h_change"], 2)
    embed=discord.Embed(title="SOL", description="The value of Solana!", color=0x00FFE5)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/solana-sol-logo.png?v=010")
    embed.set_author(name = "Solana")
    embed.add_field(name=PRICE["solana"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def BitcoinSV(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin-cash-sv&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin-cash-sv&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["bitcoi-cash-sv"]["aud_24h_change"], 2)
    embed=discord.Embed(title="BSV", description="The value of Bitcoin SV!", color=0xFF9900)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/bitcoin-sv-bsv-logo.png?v=010")
    embed.set_author(name = "Bitcoin SV")
    embed.add_field(name=PRICE["bitcoin-cash-sv"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Tron(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["tron"]["aud_24h_change"], 2)
    embed=discord.Embed(title="TRX", description="The value of Tron!", color=0xFC1703)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/tron-trx-logo.png?v=010")
    embed.set_author(name = "Tron")
    embed.add_field(name=PRICE["tron"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Uniswap(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=uniswap&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=uniswap&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["uniswap"]["aud_24h_change"], 2)
    embed=discord.Embed(title="UNI", description="The value of Uniswap!", color=0xFC1703)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/uniswap-uni-logo.png?v=010")
    embed.set_author(name = "Uniswap")
    embed.add_field(name=PRICE["uniswap"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Chainlink(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=chainlink&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=chainlink&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["chainlink"]["aud_24h_change"], 2)
    embed=discord.Embed(title="LINK", description="The value of Chainlink!", color=0x0062FF)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/chainlink-link-logo.png?v=010")
    embed.set_author(name = "Chainlink")
    embed.add_field(name=PRICE["chainlink"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Vechain(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=vechain&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=vechain&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["vechain"]["aud_24h_change"], 2)
    embed=discord.Embed(title="VET", description="The value of VeChain!", color=0x00D0FF)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/vechain-vet-logo.png?v=010")
    embed.set_author(name = "VeChain")
    embed.add_field(name=PRICE["vechain"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Stellar(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=stellar&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=stellar&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["stellar"]["aud_24h_change"], 2)
    embed=discord.Embed(title="XLM", description="The value of Stellar!", color=0x000000)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/stellar-xlm-logo.png?v=010")
    embed.set_author(name = "Stellar")
    embed.add_field(name=PRICE["stellar"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Neo(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=neo&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=neo&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["neo"]["aud_24h_change"], 2)
    embed=discord.Embed(title="NEO", description="The value of Neo!", color=0x00FF99)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/neo-neo-logo.png?v=010")
    embed.set_author(name = "Neo")
    embed.add_field(name=PRICE["neo"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Aave(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=aave&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=aave&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["aave"]["aud_24h_change"], 2)
    embed=discord.Embed(title="AAVE", description="The value of Aave!", color=0xB300FF)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/aave-aave-logo.png?v=010")
    embed.set_author(name = "Aave")
    embed.add_field(name=PRICE["aave"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Eos(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=eos&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=eos&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["eos"]["aud_24h_change"], 2)
    embed=discord.Embed(title="EOS", description="The value of Eos!", color=0x000000)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/eos-eos-logo.png?v=010")
    embed.set_author(name = "Eos")
    embed.add_field(name=PRICE["eos"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def Theta(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=theta-token&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=theta-token&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["theta-token"]["aud_24h_change"], 2)
    embed=discord.Embed(title="THETA", description="The value of Theta!", color=0x00FF99)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/theta-theta-logo.png?v=010")
    embed.set_author(name = "Theta")
    embed.add_field(name=PRICE["theta-token"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def BitcoinCash(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin-cash&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin-cash&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["bitcoin-cash"]["aud_24h_change"], 2)
    embed=discord.Embed(title="BCH", description="The value of Bitcoin Cash!", color=0x00FF44)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/bitcoin-cash-bch-logo.png?v=010")
    embed.set_author(name = "Bitcoin Cash")
    embed.add_field(name=PRICE["bitcoin-cash"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def UsdCoin(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["usd-coin"]["aud_24h_change"], 2)
    embed=discord.Embed(title="USDC", description="The value of Usd Coin!", color=0x0062FF)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/usd-coin-usdc-logo.png?v=010")
    embed.set_author(name = "Usd Coin")
    embed.add_field(name=PRICE["usd-coin"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def WrappedBitcoin(ctx):
    PRICE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=wrapped-bitcoin&vs_currencies=aud").text
    PRICE = json.loads(PRICE)
    CHANGE = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=wrapped-bitcoin&vs_currencies=aud&include_24hr_change=true").text
    CHANGE = json.loads(CHANGE)
    test = round(CHANGE["wrapped-bitcoin"]["aud_24h_change"], 2)
    embed=discord.Embed(title="WBTC", description="The value of Wrapped Bitcoin!", color=0xFF9900)
    embed.set_thumbnail(url="https://cryptologos.cc/logos/wrapped-bitcoin-wbtc-logo.png?v=010")
    embed.set_author(name = "Wrapped Bitcoin")
    embed.add_field(name=PRICE["wrapped-bitcoin"]["aud"], value="AUD", inline=False)
    embed.add_field(name=test, value="Change percent in last 24 hours", inline=False)
    await ctx.send(embed=embed)

client.run("put token in here")
