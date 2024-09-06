from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Carro

# Mapeamento de cores de carros para cores CSS válidas
CORES_CSS = {
    'Preto': '#000000',
    'Branco': '#ffffff',
    'Prata': '#c0c0c0',
    'Cinza': '#808080',
    'Vermelho': '#ff0000',
    'Azul': '#0000ff',
    'Verde': '#008000',
    'Amarelo': '#ffff00',
    'Laranja': '#ffa500',
    'Bege': '#f5f5dc',
    'Marrom': '#a52a2a',
}


def home(request):
    return render(request, 'home/index.html')

def servico(request):
    return render(request, 'servicos/index.html')

def quemSomos(request):
    return render(request, 'quem_somos/index.html')

def detalhe_carro(request, carro_id):
    carro = get_object_or_404(Carro, carro_id=carro_id)
    return render(request, 'compra/index.html', {'carro': carro})

def catalogo(request):
    # Obter os dados do banco de dados
    carros = Carro.objects.all()
    marcas = Carro.objects.values_list('carro_marca', flat=True).distinct()
    anos = Carro.objects.values_list('carro_ano', flat=True).distinct()

    # Obter os valores de filtro da requisição GET
    marca_selecionada = request.GET.get('marca', 'todos')
    ano_selecionado = request.GET.get('ano', 'todos')
    condicao_selecionada = request.GET.get('condicao', 'todos')
    cor_selecionada = request.GET.get('cor', 'todos')

    # Verificar se nenhum filtro foi selecionado
    nenhum_filtro_selecionado = not any([
        marca_selecionada != 'todos',
        ano_selecionado != 'todos',
        condicao_selecionada != 'todos',
        cor_selecionada != 'todos'
    ])

    # Filtrar carros com base nos valores de filtro
    if marca_selecionada and marca_selecionada != 'todos':
        carros = carros.filter(carro_marca=marca_selecionada)
    if ano_selecionado and ano_selecionado != 'todos':
        carros = carros.filter(carro_ano=ano_selecionado)
    if condicao_selecionada and condicao_selecionada != 'todos':
        carros = carros.filter(carro_status=condicao_selecionada)
    if cor_selecionada and cor_selecionada != 'todos':
        carros = carros.filter(carro_cor=cor_selecionada)

    # Se nenhum filtro foi selecionado, retornar todos os carros
    if nenhum_filtro_selecionado:
        carros = Carro.objects.all()

    # Obter cores únicas dos carros
    cores_unicas = Carro.objects.values_list('carro_cor', flat=True).distinct()

    def cor_para_hex(cor):
        return CORES_CSS.get(cor, '#ffffff')

    # Aplicar o método a cada cor para obter o código hexadecimal
    cores_com_hex = [(cor, cor_para_hex(cor)) for cor in cores_unicas]

    # Lista de tuplas contendo códigos de status e suas descrições
    status_choices = Carro.STATUS_CARROS
    status_tuples = [(status[0], status[1]) for status in status_choices]

    # Passe os dados para o modelo HTML
    context = {
        'carros': carros,
        'cores': cores_com_hex,
        'marcas': marcas,
        'anos': anos,
        'condicoes': status_tuples,
        'marca_selecionada': marca_selecionada,
        'ano_selecionado': ano_selecionado,  # Certifique-se de incluir ano_selecionado aqui
        'condicao_selecionada': condicao_selecionada,
        'cor_selecionada': cor_selecionada,
    }
    return render(request, 'catalogo/index.html', context)


