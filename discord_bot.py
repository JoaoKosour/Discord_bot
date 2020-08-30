import discord
from discord.ext import commands
import random


client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('bot is ready')


@client.command(aliases = ['hg'])
async def hungerg(ctx, *, players):
    list = players.split()
    kills = [
            'morreu de fome tentando encontrar uma webnamorada', 'mamou', 
            'Sucumbiu', 'Foi pego com as calças arriadas', 'danou-se', 
            'gadeou tanto que foi pego pela friboi', 'foi pego na operação leva jato',
            'morreu tentando fazer o uber elder de wanderer', 'morreu pro red', 
            'foi abduzido pelo negoney', 'foi espancado na rua', 'foi banido da vida',
            'olhou para um enderman', 'se perdeu na floresta', 'foi atingido por uma flecha',
            'foi atacado por um urso', 'morreu de hipotermia',
            'desmaiou de intoxicação e foi comido por insetos', 'encontrou uma manada de lobos',
            'morreu por falta de sangue', 'foi atacado por um enxame de abelhas', 'caiu da arvore',
            'estava dormindo e foi atacado', 'esqueceu a fogueira acesa e morreu queimado',
            'morreu afogado tentando atravessar o rio', 'tentou lutar contra um time de jogadores',
            'teve um final tragico', 'levou uma flechada no peito', 'morreu esmagado por um tronco',
            'morreu de fome', 'morreu em combate, honras ao guerreiro',
            'ficou gravemente ferido e morreu no sono','foi envenenado por outro jogador',
            'perdeu a luta', 'caiu em um penhasco',  'foi atingido por uma jaca caindo', 
            'caiu em uma armadilha', 'caiu na armadilha de outro jogador', 'caiu em sua propria armadilha', 
            'foi empalado por um tronco caindo', 'foi empalado ao cair em uma armadilha', 'foi empalado quando caiu em um buraco',
            'ficou preso em uma caverna', 'morreu de frio dormindo em uma caverna', 'não achou comida, triste final',
            'tentou pegar um arco no monumento e foi atingido por tras', 'tentou pegar um isqueiro e outro jogador quebrou seu pescoço',
            'lutou bravamente com outro jogador, o feriu gravemente mas morreu', 'morreu de exaustao', 'morreu subitamente',
            'morreu de forma indefinida', 'foi achado morto em uma trincheira', 'foi encontrado congelado ao lado de uma arvore',
            'caiu ao descer de seu esconderijo e teve um final ruim', 'foi picado por uma cobra e nao sobreviveu', 'foi encontrado morto',
            'nao suportou a solidao e tirou a propria vida', 'foi encontrado pendurado em uma forca', 'foi encontrado com marcas de jacare',
            'ficou preso no pantano e teve um final ruim', 'foi intoxicado pelo ar do pantano', 'teve um final tragico', 'foi levado pelo frio',
            'perdeu a sanidade e comeu uma pedra', 'nunca mais foi encontrado', 'levou uma espadada no ombro e morreu',
            'foi esquartejado por outro jogador', 'foi multilado por outro jogador', 'foi assassinado durante a noite', 'foi levado pelo calor',
            'se perdeu em uma tempestade de areia e nao saiu vivo', 'lutou pela sua vida mas nao aguentou',
            'morreu de sua doença cronica', 'foi morto por cachorros', 'foi morto por piranhas selvagens no rio',
            'foi empalado por outro jogador', 'foi comido vivo por outro jogador faminto', 'morreu de desnutrição', 'foi destruido',
            'nao aguentou o jogo e tirou a propria vida'
            ]
    for i in range(len(list)):
        if(len(list) == 1):
            await ctx.send(f'{list[0]} foi o grande vencedor!') 
            break
        random.shuffle(list)
        morto = list.pop()
        await ctx.send(f'\n{morto} {random.choice(kills)}')


client.run('NzQ5NTIzODEyMjE0NzY3NjY2.X0tOcg.CoTu3Ap9zLri6_YLLwhdgIGtCZg')