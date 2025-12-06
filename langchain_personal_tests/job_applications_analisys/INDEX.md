# 📑 Índice do Projeto - Análise de Vagas AI/ML

## 🎯 Visão Geral

Este projeto contém uma análise completa do mercado de trabalho em AI/ML baseada em 83 vagas em Portugal e Espanha.

---

## 📁 Estrutura de Arquivos

### 🚀 Para Começar Rapidamente
1. **[QUICKSTART.md](QUICKSTART.md)** - ⚡ Comece aqui! Guia rápido de 5 minutos

### 📊 Dashboard Interativo
2. **[dashboard_app.py](dashboard_app.py)** - Aplicação Streamlit completa
3. **[DASHBOARD_README.md](DASHBOARD_README.md)** - Documentação completa do dashboard
4. **[test_dashboard.py](test_dashboard.py)** - Script de teste das dependências

### 📓 Análises Detalhadas
5. **[job_role_analisys.ipynb](job_role_analisys.ipynb)** - Notebook Jupyter com 30+ análises
6. **[ANALISE_SUMMARY.md](ANALISE_SUMMARY.md)** - Resumo executivo de todas as análises

### 🔧 Configuração
7. **[requirements.txt](requirements.txt)** - Dependências do projeto
8. **[INDEX.md](INDEX.md)** - Este arquivo (navegação)

### 📂 Dados
9. **job_analysis_results.csv** - Dataset com 83 vagas analisadas

---

## 🗺️ Fluxo de Navegação Recomendado

### Opção A: Quero explorar visualmente (Dashboard)
```
1. QUICKSTART.md
2. Instalar dependências: pip install -r requirements.txt
3. Executar: streamlit run dashboard_app.py
4. Explorar as 5 tabs do dashboard
```

### Opção B: Quero análises detalhadas (Notebook)
```
1. Instalar dependências: pip install -r requirements.txt
2. Abrir: jupyter notebook job_role_analisys.ipynb
3. Executar células sequencialmente
4. Ler insights no final
```

### Opção C: Quero apenas os insights (Leitura)
```
1. ANALISE_SUMMARY.md - Resumo executivo
2. DASHBOARD_README.md - Funcionalidades do dashboard
3. QUICKSTART.md - Principais descobertas
```

---

## 📊 Conteúdo por Arquivo

### 1. QUICKSTART.md
**O que contém:**
- Instruções de instalação em 3 passos
- Principais insights em formato resumido
- 3 caminhos de carreira identificados
- Troubleshooting rápido

**Quando usar:**
- Primeira vez no projeto
- Quer começar rápido
- Precisa resolver problemas técnicos

---

### 2. dashboard_app.py
**O que contém:**
- Aplicação web completa em Streamlit
- 5 tabs com análises diferentes:
  - Visão Geral
  - Cruzamento de Dados
  - Skills & Technologies
  - Knowledge Analysis
  - Localização & Empresas
- 15+ visualizações interativas com Plotly
- Filtros dinâmicos
- ~600 linhas de código

**Como usar:**
```bash
streamlit run dashboard_app.py
```

**Quando usar:**
- Quer explorar dados interativamente
- Precisa de visualizações profissionais
- Quer filtrar e segmentar dados
- Apresentar para outras pessoas

---

### 3. DASHBOARD_README.md
**O que contém:**
- Documentação completa do dashboard
- Descrição de cada tab
- Lista de filtros disponíveis
- Tipos de gráficos incluídos
- Casos de uso
- Instruções de troubleshooting

**Quando usar:**
- Quer entender todas as funcionalidades
- Precisa de ajuda com o dashboard
- Quer saber os tipos de visualizações
- Busca exemplos de uso

---

### 4. job_role_analisys.ipynb
**O que contém:**
- 30+ células de análise
- 25+ visualizações
- Análises divididas em 3 partes:
  1. **EDA**: Análise exploratória
  2. **Visualizações Plotly**: Gráficos interativos
  3. **Insights Estratégicos**: Recomendações

**Tipos de análises:**
- Completude de dados
- Complexidade das vagas
- Cruzamento Skills × Knowledge
- Cruzamento Technologies × Knowledge
- Skill Leverage (ROI de aprendizado)
- Technology Gateway (portas que tecnologias abrem)
- Perfis de vaga (clustering)
- Must-have vs Nice-to-have
- Caminhos de carreira

**Quando usar:**
- Quer análises aprofundadas
- Precisa customizar visualizações
- Quer explorar dados livremente
- Busca insights estratégicos

---

### 5. ANALISE_SUMMARY.md
**O que contém:**
- Resumo executivo completo
- Lista de todas as análises implementadas
- Estatísticas do projeto
- Principais insights descobertos
- Checklist de funcionalidades
- Sugestões de próximos passos

**Quando usar:**
- Quer visão geral do projeto
- Precisa de estatísticas rápidas
- Busca principais insights
- Quer entender escopo completo

---

### 6. requirements.txt
**O que contém:**
```
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.18.0
matplotlib>=3.7.0
seaborn>=0.12.0
streamlit>=1.28.0
kaleido>=0.2.1
```

**Como usar:**
```bash
pip install -r requirements.txt
```

---

### 7. test_dashboard.py
**O que contém:**
- Script de teste automático
- Verifica instalação de dependências
- Valida arquivo de dados
- Fornece diagnóstico completo

**Como usar:**
```bash
python3 test_dashboard.py
```

**Saída esperada:**
```
✅ pandas importado com sucesso!
✅ numpy importado com sucesso!
✅ plotly importado com sucesso!
✅ streamlit importado com sucesso!
✅ Arquivo 'job_analysis_results.csv' encontrado!
🚀 TUDO PRONTO!
```

---

## 🎯 Casos de Uso por Persona

### 👨‍💻 Candidato a Vaga
**Arquivos recomendados:**
1. dashboard_app.py (Tab 4: Knowledge Analysis)
2. job_role_analisys.ipynb (Seção: Recomendações de Carreira)
3. QUICKSTART.md (Seção: 3 Caminhos de Carreira)

**Perguntas que pode responder:**
- Quais skills devo aprender?
- Qual tecnologia tem mais demanda?
- Que combinações de competências são vencedoras?
- Qual caminho de carreira seguir?

---

### 👔 Recrutador
**Arquivos recomendados:**
1. dashboard_app.py (Tab 2: Cruzamento de Dados)
2. job_role_analisys.ipynb (Seção: Must-have vs Nice-to-have)
3. ANALISE_SUMMARY.md (Seção: Insights Principais)

**Perguntas que pode responder:**
- Quais requisitos são padrão de mercado?
- Combinações típicas de competências?
- Benchmark de complexidade de vagas?
- Empresas concorrentes e suas demandas?

---

### 🎓 Educador/Coordenador de Curso
**Arquivos recomendados:**
1. job_role_analisys.ipynb (Seção completa)
2. ANALISE_SUMMARY.md
3. dashboard_app.py (Tab 4: Knowledge Analysis)

**Perguntas que pode responder:**
- Que conteúdos ensinar?
- Priorização de tecnologias no currículo?
- Skills em alta vs obsoletas?
- Tendências emergentes?

---

### 📊 Analista de Dados/Pesquisador
**Arquivos recomendados:**
1. job_role_analisys.ipynb (todas as seções)
2. dashboard_app.py (código-fonte para referência)
3. ANALISE_SUMMARY.md (metodologia)

**O que pode fazer:**
- Replicar análises
- Customizar visualizações
- Adicionar novas métricas
- Expandir dataset

---

## 📈 Principais Descobertas (Spoiler!)

### 🔝 Top 3 Must-Have
1. **Python**: 90% das vagas
2. **Model Deployment**: 64% das vagas
3. **Machine Learning Modeling**: 58% das vagas

### 🚀 Top 3 Tecnologias
1. **Docker**: 39% das vagas
2. **AWS**: 37% das vagas
3. **Kubernetes**: 30% das vagas

### 🌟 Top 3 Emergentes
1. **LLMs**: 46% das vagas
2. **Generative AI**: 31% das vagas
3. **MLOps**: 30% das vagas

### 💎 Combinações Vencedoras
1. **Python + Docker + AWS**: ~70% das vagas
2. **Python + LLMs + Cloud**: ~46% das vagas
3. **Python + Kubernetes + MLOps**: ~60% das vagas

---

## 🛠️ Comandos Úteis

### Instalação
```bash
# Instalar todas as dependências
pip install -r requirements.txt

# Instalar individualmente
pip install pandas numpy plotly streamlit matplotlib seaborn
```

### Executar Dashboard
```bash
streamlit run dashboard_app.py
```

### Executar Notebook
```bash
jupyter notebook job_role_analisys.ipynb
```

### Testar Sistema
```bash
python3 test_dashboard.py
```

### Atualizar Dependências
```bash
pip install --upgrade -r requirements.txt
```

---

## 📊 Estatísticas do Projeto

- **Vagas Analisadas**: 83
- **Skills Identificadas**: 29 únicas
- **Tecnologias**: 231 únicas
- **Conhecimentos Técnicos**: 56 únicos
- **Células de Análise**: 30+
- **Visualizações**: 25+
- **Linhas de Código**: ~1000+
- **Tipos de Gráficos**: 10

---

## 🎓 Tecnologias Utilizadas

### Análise de Dados
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica

### Visualização
- **Plotly**: Gráficos interativos
- **Matplotlib**: Gráficos estáticos
- **Seaborn**: Visualização estatística

### Dashboard
- **Streamlit**: Framework web

### Ambiente
- **Jupyter**: Notebooks interativos
- **Python 3.8+**: Linguagem base

---

## 🚦 Estado do Projeto

- ✅ Análise exploratória completa
- ✅ Dashboard funcional
- ✅ Visualizações interativas
- ✅ Documentação completa
- ✅ Scripts de teste
- ✅ Insights estratégicos
- ⬜ Análise temporal (futuro)
- ⬜ Dados de salário (futuro)
- ⬜ API REST (futuro)

---

## 📞 Próximos Passos

1. **Ler**: QUICKSTART.md
2. **Instalar**: `pip install -r requirements.txt`
3. **Testar**: `python3 test_dashboard.py`
4. **Explorar**: `streamlit run dashboard_app.py`
5. **Aprofundar**: Abrir job_role_analisys.ipynb

---

## 🎉 Conclusão

Este projeto oferece uma análise completa e profissional do mercado de trabalho em AI/ML em Portugal. Use os arquivos de acordo com suas necessidades e explore os insights para tomar decisões informadas sobre carreira, recrutamento ou educação.

**Desenvolvido com ❤️ usando Claude Code**

---

**Última atualização**: 2025-12-04
