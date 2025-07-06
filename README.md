# 🏐 Análise de Estatísticas do Vôlei Feminino – VNL 2021–2023

Este projeto realiza uma análise exploratória dos dados da Volleyball Nations League (VNL) entre 2021 e 2023, com foco nas seleções femininas do **Brasil**, **Estados Unidos** e **Itália**. A proposta é investigar o desempenho médio das jogadoras em métricas relevantes como **pontos totais**, **bloqueios**, **eficiência** e **sucesso no saque**, além de comparar os resultados entre países.

---

## 📊 O que foi analisado

- Evolução média anual das principais estatísticas das jogadoras brasileiras.
- Rankings das 10 melhores jogadoras do Brasil por:
  - Pontos totais
  - Eficiência média
  - Sucesso em bloqueios
- Comparação entre Brasil, EUA e Itália nas métricas:
  - Eficiência
  - Sucesso no bloqueio
  - Sucesso no saque
- Criação de um **índice comparativo** simples entre as seleções.
- Visualizações claras para facilitar a interpretação dos dados.

---

## 📁 Dataset

Os dados utilizados são do dataset [The 2021–2023 VNL Player Dataset](https://www.kaggle.com/datasets/zakirpasha/the-2021-2023-vnl-player-dataset), disponível gratuitamente no Kaggle.

> Obs.: O arquivo CSV (`df_womens_rosters_21_23.csv`) **já está incluído na pasta `/data`** deste repositório.

---

## 🛠️ Tecnologias e Bibliotecas

- Python 3.x
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn

---

## 🧠 Metodologia

- Limpeza de dados: conversão de colunas percentuais em valores numéricos.
- Agrupamento e ordenação de dados para gerar rankings.
- Visualizações com gráficos de linha, barras e boxplots.
- Comparação entre seleções a partir de métricas médias normalizadas.

---

## ⚠️ Limitações

- O índice comparativo entre seleções é **exploratório e simplificado**.
- Não foram consideradas variáveis de contexto como adversários, resultados dos jogos, forma física, etc.
- A análise se restringe às informações disponíveis no dataset (2021–2023).
- O projeto é **descritivo**, e não preditivo.

---

## 🚀 Como Executar

1. Clone o repositório:
   ```
   git clone https://github.com/ceciliagomes1/analise-vnl-feminino.git
   cd analise-vnl-feminino
   ```

2. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

3. Execute o script:

   ```
   python analise_vnl_2021_2023.py
   ```

---

## 📂 Estrutura do Projeto

   ```
/analise-vnl-feminino
├── /data
│   └── df_womens_rosters_21_23.csv     # Dataset com estatísticas das jogadoras
├── analise_vnl_2021_2023.py            # Código principal da análise
├── README.md                           # Descrição do projeto
├── requirements.txt                    # Dependências do projeto
   ```

---

## 📬 Contato

Fique à vontade para entrar em contato:

* 🔗 [LinkedIn: ceciliagomes1](https://www.linkedin.com/in/ceciliagomes1)
* 📧 Email: [ceciliaoliveira72@gmail.com](mailto:ceciliaoliveira72@gmail.com)

---

> *Este projeto tem fins educacionais e exploratórios. Não representa análises técnicas oficiais ou previsões especializadas sobre a VNL.*
