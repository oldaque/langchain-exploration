"""
Script de teste para verificar se todas as dependências estão instaladas
e o dashboard pode ser executado sem erros.
"""

import sys

def test_imports():
    """Testa se todas as bibliotecas necessárias podem ser importadas"""
    print("🧪 Testando importações...\n")

    errors = []

    # Testar pandas
    try:
        import pandas as pd
        print("✅ pandas importado com sucesso!")
    except ImportError as e:
        errors.append(f"❌ pandas: {e}")

    # Testar numpy
    try:
        import numpy as np
        print("✅ numpy importado com sucesso!")
    except ImportError as e:
        errors.append(f"❌ numpy: {e}")

    # Testar plotly
    try:
        import plotly.express as px
        import plotly.graph_objects as go
        print("✅ plotly importado com sucesso!")
    except ImportError as e:
        errors.append(f"❌ plotly: {e}")

    # Testar streamlit
    try:
        import streamlit as st
        print("✅ streamlit importado com sucesso!")
    except ImportError as e:
        errors.append(f"❌ streamlit: {e}")

    # Testar matplotlib
    try:
        import matplotlib.pyplot as plt
        print("✅ matplotlib importado com sucesso!")
    except ImportError as e:
        errors.append(f"❌ matplotlib: {e}")

    # Testar seaborn
    try:
        import seaborn as sns
        print("✅ seaborn importado com sucesso!")
    except ImportError as e:
        errors.append(f"❌ seaborn: {e}")

    return errors

def test_data_file():
    """Verifica se o arquivo de dados existe"""
    print("\n📁 Testando arquivo de dados...\n")

    import os

    if os.path.exists('job_analysis_results.csv'):
        print("✅ Arquivo 'job_analysis_results.csv' encontrado!")

        # Tentar carregar
        try:
            import pandas as pd
            df = pd.read_csv('job_analysis_results.csv')
            print(f"✅ Arquivo carregado com sucesso! {len(df)} vagas encontradas.")
            return True
        except Exception as e:
            print(f"❌ Erro ao carregar arquivo: {e}")
            return False
    else:
        print("❌ Arquivo 'job_analysis_results.csv' NÃO encontrado!")
        print("   Por favor, certifique-se de que o arquivo está no mesmo diretório.")
        return False

def main():
    print("="*60)
    print("🎯 TESTE DO DASHBOARD DE ANÁLISE DE VAGAS")
    print("="*60)
    print()

    # Testar importações
    errors = test_imports()

    # Testar arquivo de dados
    data_ok = test_data_file()

    # Resultados finais
    print("\n" + "="*60)
    print("📊 RESULTADO DOS TESTES")
    print("="*60)

    if errors:
        print("\n❌ ALGUNS PACOTES NÃO ESTÃO INSTALADOS:\n")
        for error in errors:
            print(f"   {error}")
        print("\n💡 Execute: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ Todas as dependências estão instaladas!")

    if data_ok:
        print("✅ Arquivo de dados está OK!")
    else:
        print("❌ Problema com arquivo de dados!")
        return False

    print("\n" + "="*60)
    print("🚀 TUDO PRONTO! Você pode executar:")
    print("   streamlit run dashboard_app.py")
    print("="*60)

    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
