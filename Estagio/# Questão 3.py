# Questão 3
import json
import xml.etree.ElementTree as ET

def carregar_dados_json(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo JSON não encontrado: {caminho}")
        return []
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return []

def carregar_dados_xml(caminho):
    try:
        tree = ET.parse(caminho)
        root = tree.getroot()
        dados_xml = []
        for row in root.findall('row'):
            dia = int(row.find('dia').text)
            valor = row.find('valor').text
            if valor:  # Ignorar dias sem faturamento
                dados_xml.append({'dia': dia, 'valor': float(valor)})
        return dados_xml
    except FileNotFoundError:
        print(f"Arquivo XML não encontrado: {caminho}")
        return []
    except ET.ParseError as e:
        print(f"Erro ao fazer parsing do arquivo XML: {e}")
        return []


def processar_dados_faturamento(dados):
    # (ignorar dias com valor 0)
    faturamento_valido = [d['valor'] for d in dados if d['valor'] > 0]
    
    # Se não tiver numeros validos retornar o erro
    if not faturamento_valido:
        print("Nenhum faturamento válido encontrado.")
        return
    #Calculo
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_faturamento = sum(faturamento_valido) / len(faturamento_valido)
    
    # Conta quantos dias o faturamento foi maior que a média
    dias_acima_media = sum(1 for v in faturamento_valido if v > media_faturamento)
    
    # Exibe os resultados
    print(f"Menor faturamento: {menor_faturamento:.2f}")
    print(f"Maior faturamento: {maior_faturamento:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")

caminho_json = 'C:/Users/Dudu/Downloads/Estagio/dados.json'
caminho_xml = 'C:/Users/Dudu/Downloads/Estagio/dados (2).xml'

dados_json = carregar_dados_json(caminho_json)
dados_xml = carregar_dados_xml(caminho_xml)

# Verifica se os dados foram carregados corretamente e processa
if dados_json:
    print("Processando dados JSON...")
    processar_dados_faturamento(dados_json)
elif dados_xml:
    print("Processando dados XML...")
    processar_dados_faturamento(dados_xml)
else:
    print("Nenhum dado válido encontrado nos arquivos JSON ou XML.")
