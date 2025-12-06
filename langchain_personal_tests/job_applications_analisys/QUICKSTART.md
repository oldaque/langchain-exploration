# 🚀 Guia Rápido - Dashboard de Análise de Vagas AI/ML

## ⚡ Início Rápido (5 minutos)

### 1️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

**Ou instalar individualmente:**
```bash
pip install pandas numpy plotly streamlit matplotlib seaborn
```

### 2️⃣ Testar Instalação (Opcional)

```bash
python3 test_dashboard.py
```

Se tudo estiver OK, você verá:
```
✅ Todas as dependências estão instaladas!
✅ Arquivo de dados está OK!
🚀 TUDO PRONTO!
```

### 3️⃣ Executar Dashboard

```bash
streamlit run dashboard_app.py
```

O dashboard abrirá automaticamente em: **http://localhost:8501**

---

## 📊 O que você encontrará no Dashboard

### 🎯 Tab 1: Visão Geral
- Métricas principais (total de vagas, médias)
- Top 10 skills e tecnologias
- Distribuição de complexidade

### 🔗 Tab 2: Cruzamento de Dados
- Heatmap interativo (Skills × Knowledge)
- Scatter 3D (visualização multidimensional)

### 🎯 Tab 3: Skills & Technologies
- Treemap de skills
- Sunburst de tecnologias
- Top 10 combinações

### 🧠 Tab 4: Knowledge Analysis
- Top 20 conhecimentos técnicos
- Distribuição por categoria (Pie chart)

### 📍 Tab 5: Localização & Empresas
- Top 10 localizações
- Top 10 empresas
- Tabela completa de vagas

---

## 🔧 Usando os Filtros

**No sidebar à esquerda:**

1. **📍 Localização**: Selecione uma ou várias cidades
2. **🏢 Empresas**: Filtre por empresas específicas
3. **📊 Requisitos Mínimos**: Ajuste o slider para vagas mais/menos complexas

**Dica:** Clique em "Clear All" para resetar os filtros!

---

## 📓 Análises Avançadas no Jupyter Notebook

Se preferir análises mais detalhadas, abra o notebook:

```bash
jupyter notebook job_role_analisys.ipynb
```

**O notebook inclui:**
- ✅ 30+ células de análise
- ✅ 25+ visualizações
- ✅ Insights estratégicos
- ✅ Recomendações de carreira

---

## 💡 Principais Insights (Spoiler!)

### Must-Have
- **Python**: 90% das vagas
- **Model Deployment**: 64% das vagas
- **Docker**: 39% das vagas

### Em Alta
- **LLMs**: 46% das vagas
- **Generative AI**: 31% das vagas
- **MLOps**: 30% das vagas

### Combinações Vencedoras
1. Python + Docker + AWS
2. Python + LLMs + Cloud
3. Python + Kubernetes + MLOps

---

## 🎓 3 Caminhos de Carreira Identificados

### 1. MLOps Engineer
```
Python → SQL → Git → Docker → Kubernetes → AWS
→ Model Deployment → MLOps → CI/CD
```

### 2. ML/AI Specialist
```
Python → Matemática → SQL → PyTorch/TensorFlow
→ LLMs → Generative AI → RAG → NLP
```

### 3. Data Engineer
```
Python → SQL → Cloud → Databases → Spark/Airflow
→ Data Pipelines → ETL/ELT → Data Warehousing
```

---

## ❓ Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'streamlit'"
**Solução:**
```bash
pip install streamlit
```

### Dashboard não abre
**Solução:**
```bash
# Verifique se o Streamlit está instalado
streamlit --version

# Se não estiver, instale:
pip install streamlit

# Execute novamente:
streamlit run dashboard_app.py
```

### Erro: "FileNotFoundError: job_analysis_results.csv"
**Solução:**
- Certifique-se de estar no diretório correto
- Verifique se o arquivo CSV existe
- Execute: `ls -la job_analysis_results.csv`

### Gráficos não aparecem
**Solução:**
```bash
# Reinstale o Plotly
pip install --upgrade plotly

# Limpe o cache do Streamlit
streamlit cache clear
```

---

## 📸 Recursos Visuais

### Interatividade dos Gráficos Plotly
- **Hover**: Passe o mouse para ver detalhes
- **Zoom**: Clique e arraste para zoom
- **Pan**: Segure Shift + arrastar
- **Reset**: Clique duplo para resetar view
- **Download**: Botão de câmera para exportar PNG

### Scatter 3D
- **Rotacionar**: Clique e arraste
- **Zoom**: Scroll do mouse
- **Pan**: Shift + arrastar

---

## 🎯 Casos de Uso

### Para Candidatos
1. Identifique skills mais demandadas
2. Planeje seu stack tecnológico
3. Encontre combinações vencedoras
4. Veja caminhos de carreira

### Para Recrutadores
1. Benchmark de requisitos
2. Análise de competitividade
3. Identificação de talentos raros
4. Planejamento de JDs

### Para Educadores
1. Alinhamento curricular
2. Priorização de tecnologias
3. Skills em alta demanda
4. Tendências do mercado

---

## 📚 Documentação Completa

- **DASHBOARD_README.md**: Documentação detalhada do dashboard
- **ANALISE_SUMMARY.md**: Resumo executivo de todas as análises
- **requirements.txt**: Dependências do projeto

---

## 🆘 Suporte

Se encontrar problemas:

1. ✅ Verifique se todas as dependências estão instaladas
2. ✅ Execute o script de teste: `python3 test_dashboard.py`
3. ✅ Consulte a documentação: `DASHBOARD_README.md`
4. ✅ Verifique logs de erro no terminal

---

## 🎉 Pronto para Começar!

```bash
# Passo 1: Instalar
pip install -r requirements.txt

# Passo 2: Testar (opcional)
python3 test_dashboard.py

# Passo 3: Executar
streamlit run dashboard_app.py

# 🎊 Divirta-se explorando os dados!
```

---

**Desenvolvido com ❤️ usando Claude Code**
