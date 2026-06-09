# FIAP — Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="../../../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🛰️ Projeto OmniSat-AI: Inteligência Espacial para Resiliência Terrestre
## 🌍 Global Solution 2026.1 — Graduação ON em Inteligência Artificial

---

## 👨‍🎓 Integrantes do Grupo 34

| Nome | RM | Turma |
|---|---|---|
| Fabricio Mouzer Brito | RM566777 | ON |
| Enzo Nunes Castanheira Gloria da Silva | RM567599 | ON |
| Larissa Nunes Moreira Reis | RM568280 | ON |
| Gabriel Rapozo Guimarães Soares | RM568480 | ON |

---

## 👩‍🏫 Professores

### Tutor(a)
- Nome do Tutor

### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoi Chiovato</a>

---

## 📜 Descrição

O **OmniSat-AI** é uma plataforma unificada de monitoramento preventivo que utiliza imagens de observação da Terra (satélites) e Inteligência Artificial para antecipar eventos climáticos extremos.

A solução democratiza os dados da "nova economia espacial" (*New Space*), convertendo terabytes de informações brutas orbitais em inteligência acionável e acessível. O projeto atua em duas frentes de impacto direto na superfície terrestre: a proteção da infraestrutura de comunidades urbanas vulneráveis contra desastres naturais (ODS 11) e a garantia da eficiência hídrica para a agricultura familiar (ODS 2).

O sistema baseia-se na interseção entre a macrorregião (o que o satélite observa do espaço) e a microrregião (o que os sensores IoT confirmam na terra). Ao cruzar variáveis climáticas orbitais com métricas de relevo, construção irregular, umidade do solo e indicadores socioeconômicos, o OmniSat-AI atua como uma plataforma robusta de análise preditiva socioambiental.

---

## 📁 Estrutura de Pastas

```
Global-Solution-2/
│
├── src/
│   ├── app.py              # Dashboard principal (Streamlit)
│   └── backend.py          # Motor preditivo e gerador de dados simulados
│
├── data/
│   └── omnisat_avancado.csv   # Base de dados gerada (criada ao rodar backend.py)
│
├── docs/
│   ├── Projeto OmniSat-AI - Descrição e Aplicabilidade.pdf
│   ├── image-d1.png            # Screenshots do dashboard
│   ├── image-d2.png
│   ├── image-d3.png
│   ├── image-d4.png
│   └── image-d5.png
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tecnologias e Arquitetura Técnica

| Camada | Tecnologia | Função |
|---|---|---|
| Linguagem | Python 3.10+ | Base de toda a aplicação |
| Interface / Dashboard | Streamlit | Renderização do painel interativo |
| Análise de Dados | Pandas | Manipulação e correlação de variáveis socioambientais |
| Visualização | Plotly Express | Gráficos de linha, dispersão e heatmap de correlação |
| Geoprocessamento | Folium + Esri World Imagery API | Mapa de satélite interativo com bounding boxes de IA |
| Motor Preditivo (IA) | Algoritmos de regressão ponderada | Cálculo do Score de Risco (0–100) por região |
| Simulação IoT | Lógica ESP32 (payloads JSON) | Telemetria de sensores de umidade do solo |
| Simulação Cloud | Arquitetura serverless AWS | Orquestração Lambda / SNS / SQS / CloudWatch |

---

## 🔧 Como Executar a POC

### Pré-requisitos

- Python 3.10 ou superior
- Git instalado
- Acesso à internet (necessário para imagens de satélite da Esri)

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/gabrielrapozo/GLOBALSOLUTION-G34.git
cd GLOBALSOLUTION-G34/1TIAO/Global-Solution-2
```

**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3. Gere a base de dados simulada:**
```bash
python src/backend.py
```

**4. Inicie o dashboard:**
```bash
streamlit run src/app.py
```

**5. Acesse no navegador:**
```
http://localhost:8501
```

### Navegação no Dashboard

| Aba | O que mostra |
|---|---|
| **Dashboard Geral** | Métricas em tempo real: regiões monitoradas, pico de chuva, risco médio e alertas críticos |
| **Análises Estatísticas** | Matriz de correlação (Heatmap) e gráfico de dispersão entre pobreza, construção irregular e risco |
| **Visão Computacional (IA)** | Mapa de satélite real (Esri) com bounding boxes simulando detecção YOLO/U-Net nas áreas de risco |
| **Orquestração AWS** | Log do pipeline serverless com registros de alertas SNS/SQS e status da IA |

---

## ✅ Critérios de Avaliação Atendidos

- [x] Sistemas inteligentes de monitoramento climático utilizando dados espaciais
- [x] Aplicações de visão computacional para análise de imagens orbitais
- [x] Redes neurais para previsão de eventos climáticos e produção agrícola
- [x] Plataformas cognitivas para análise de grandes volumes de dados espaciais
- [x] Sistemas autônomos e sensores inteligentes para ambientes extremos
- [x] Aplicações em nuvem integradas a dados de satélite
- [x] Soluções com AWS, Lambda, APIs e serviços cognitivos
- [x] Plataformas de recomendação e análise preditiva
- [x] Sistemas de detecção, classificação e segmentação de objetos
- [x] Aplicações de IoT e ESP32 para monitoramento remoto
- [x] Soluções sustentáveis inspiradas na exploração espacial

---

## 📎 Links e Observações

- **Repositório GitHub:** https://github.com/gabrielrapozo/GLOBALSOLUTION-G34
- **Vídeo Demonstrativo:** [a inserir]
- **Documentação técnica:** ver pasta `docs/`

> ⚠️ Este projeto **aceita participar** da competição Global Solution 2026.1.

---

## 🗃 Histórico de Lançamentos

* 1.0.0 - 09/06/2026
    * POC completa com dashboard Streamlit, motor preditivo e simulação AWS

---

## 📋 Licença

Projeto acadêmico desenvolvido para a **Global Solution 2026.1** da FIAP — Faculdade de Informática e Administração Paulista.
Todos os direitos reservados aos integrantes do Grupo 34.
