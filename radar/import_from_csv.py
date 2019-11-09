import pandas as pd
from radar.models import BaseRadares,Trajetos, Viagens, Contagens


base_radar = pd.read_csv('data/')

for index, row in base_radar.iterrows():

    BaseRadares.objects.create(
        id = row['id'], 
        lote = row['lote'], 
        codigo = row['codigo'], 
        endereco = row['endereco'], 
        sentido = row['sentido'],
        referencia = row['referencia'], 
        tipo_equip = row['tipo_equip'], 
        enquadrame = row['enquadrame'], 
        qtde_fxs_f = row['qtde_fxs_f'],
        data_publi = row['data_publi'], 
        velocidade = row['velocidade'], 
        latitude_l = row['latitude_l'], 
        ligado = row['ligado'], 
        data_desli = row['data_desli'],
        motivo_des = row['motivo_des'], 
    )


trajetos = pd.read_csv('data/')

for index, row in trajetos.iterrows():

    Trajetos.objects.create(
        id = row['id'],
        viagem_id = row['viagem_id'],
        tipo = row['tipo'],
        data_inicio = row['data_inicio'],
        data_final = row['data_final'],
        origem = row['origem'],
        destino = row['destino'],
        v0 = row['v0'],
        v1 = row['v1'],
    )

Trajetos
Viagens
Contagens