import streamlit as st
import pandas as pd
import plotly.express as px
import statsmodels.api as sm

st.title('teste')
bar = st.sidebar
opcoes = list(range(1, 193))
escolhas = bar.multiselect('seleciona', opcoes)
opcoes2 = []
for num in opcoes:
    if num not in escolhas:
        opcoes2.append(num)
escolhas2 = bar.multiselect('seleciona2', opcoes2)
selecionados = pd.DataFrame()
selecionados2 = pd.DataFrame()
selecionados_nao = pd.DataFrame()
base_orig = pd.read_excel('mastervida_pa_db_19_22_.xlsx').dropna()
base = base_orig.loc[base_orig['ano'] == 2022]

escolhas_nao = []
for num in opcoes2:
    if num not in escolhas2:
        escolhas_nao.append(num)

for valor in escolhas:
    escolhido_valor = base.loc[base['nome_id'] == valor]
    selecionados = pd.concat([selecionados, escolhido_valor], ignore_index=True)

for valor in escolhas2:
    escolhido_valor2 = base.loc[base['nome_id'] == valor]
    selecionados2 = pd.concat([selecionados2, escolhido_valor2], ignore_index=True)

for valor in escolhas_nao:
    escolhido_valor_nao = base.loc[base['nome_id'] == valor]
    selecionados_nao = pd.concat([selecionados_nao, escolhido_valor_nao], ignore_index=True)

# listadescb = listaids1.groupby('nome_id').mês.value_counts()
listadescb = base.df_pas_.value_counts()
st.dataframe(listadescb)

st.dataframe(base)

if not selecionados.empty:
    # fig = px.bar(selecionados, x='data', y=['pre_pas_', 'pos_pas_'], barmode='group')
    # st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    fig2 = px.scatter(selecionados, x='data', y='pre_pas_', trendline="ols")
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    # st.dataframe(selecionados)

    # fig12 = px.bar(selecionados, x='data', y=['pre_pas_', 'pos_pas_'], barmode='group')
    # st.plotly_chart(fig12, theme="streamlit", use_container_width=True)

    fig22 = px.scatter(selecionados2, x='data', y=['pre_pas_'], trendline="ols")
    st.plotly_chart(fig22, theme="streamlit", use_container_width=True)
    # st.dataframe(selecionados)

    # fig_nao = px.bar(selecionados_nao, x='data', y=['pre_pas_', 'pos_pas_'], barmode='group')
    # st.plotly_chart(fig_nao, theme="streamlit", use_container_width=True)

    fig_nao2 = px.scatter(selecionados_nao, x='data', y=['pre_pas_'], trendline="ols")
    st.plotly_chart(fig_nao2, theme="streamlit", use_container_width=True)
    # st.dataframe(selecionados_nao)

    listausers = selecionados.groupby('nome_id').describe()
    st.dataframe(listausers)
    listausers2 = selecionados2.groupby('nome_id').describe()
    st.dataframe(listausers2)
    listausers_nao = selecionados_nao.groupby('nome_id').describe()
    st.dataframe(listausers_nao)

    # results = px.get_trendline_results(fig2)
    # print(results.px_fit_results.iloc[0].summary())
    # results2 = px.get_trendline_results(fig22)
    # print(results2.px_fit_results.iloc[0].summary())
    # results_nao = px.get_trendline_results(fig_nao2)
    # print(results_nao.px_fit_results.iloc[0].summary())
