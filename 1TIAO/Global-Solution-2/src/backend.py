import pandas as pd
import random
from datetime import datetime, timedelta

# ==========================================
# 1. Definição das Regiões (Com Dados Socioambientais)
# ==========================================
regioes = [
    {"regiao": "Comunidade Encosta Sul", "tipo": "Urbana", "inclinacao_graus": 45, "idh": 0.61, "indice_pobreza_pct": 42.0, "construcao_irregular_pct": 78.0, "historico_deslizamentos": 4},
    {"regiao": "Horta Familiar Leste", "tipo": "Agrícola", "inclinacao_graus": 12, "idh": 0.72, "indice_pobreza_pct": 25.0, "construcao_irregular_pct": 15.0, "historico_deslizamentos": 0},
    {"regiao": "Bairro Nobre Vale", "tipo": "Urbana", "inclinacao_graus": 5, "idh": 0.89, "indice_pobreza_pct": 5.0, "construcao_irregular_pct": 2.0, "historico_deslizamentos": 0}
]

# ==========================================
# 2. Motor de Geração e Correlação de Risco
# ==========================================
def gerar_base_dados():
    registros = []
    
    for i in range(100): # Gerando 100 horas de histórico simulado
        hora_simulada = datetime.now() - timedelta(hours=i)
        
        # Variáveis climáticas macros (Satélite simulado)
        temp_orbital = round(random.uniform(22.0, 38.0), 1)
        chuva_mm = round(random.uniform(0.0, 60.0), 1)
        
        for loc in regioes:
            # Variáveis micro (Sensores locais)
            umidade_solo = round(random.uniform(10.0, 95.0), 1)
            
            # Cálculo de Score de Risco Geológico (Fórmula Preditiva)
            # Pesos: Chuva (30%), Umidade Solo (30%), Inclinação (20%), Construção Irregular (20%)
            fator_chuva = (chuva_mm / 60) * 30
            fator_solo = (umidade_solo / 100) * 30
            fator_relevo = (loc["inclinacao_graus"] / 50) * 20
            fator_irregular = (loc["construcao_irregular_pct"] / 100) * 20
            
            score_risco = round(fator_chuva + fator_solo + fator_relevo + fator_irregular, 1)
            
            # Definição de Status
            if score_risco > 75:
                status = "CRÍTICO - Evacuação"
                alerta = f"[SNS] Risco eminente na {loc['regiao']}! Deslizamento provável."
            elif score_risco > 50:
                status = "ALERTA - Atenção"
                alerta = f"[SNS] Chuva e saturação elevadas na {loc['regiao']}."
            else:
                status = "Normal"
                alerta = "[SQS] Monitoramento estável."

            registros.append({
                "data_hora": hora_simulada.strftime("%Y-%m-%d %H:%M:%S"),
                "regiao": loc["regiao"],
                "tipo": loc["tipo"],
                "idh": loc["idh"],
                "indice_pobreza_pct": loc["indice_pobreza_pct"],
                "construcao_irregular_pct": loc["construcao_irregular_pct"],
                "inclinacao_graus": loc["inclinacao_graus"],
                "precipitacao_mm": chuva_mm,
                "umidade_solo_pct": umidade_solo,
                "score_risco": score_risco,
                "status_ia": status,
                "alerta_sns": alerta
            })
            
    df = pd.DataFrame(registros).sort_values(by="data_hora")
    df.to_csv("omnisat_avancado.csv", index=False)
    print("Base de dados com indicadores socioambientais gerada com sucesso!")

if __name__ == "__main__":
    gerar_base_dados()
    