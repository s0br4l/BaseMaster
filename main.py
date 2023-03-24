import streamlit as st
import pandas as pd
import plotly.express as px


st.title('teste')
bar = st.sidebar
# opcoes = list(range(1, 193))
# escolhas = bar.multiselect('Grupo 1', opcoes)
# opcoes2 = []

# for num in opcoes:
#     if num not in escolhas:
#         opcoes2.append(num)

# escolhas2 = bar.multiselect('Grupo 2', opcoes2)

freq_orig = pd.read_excel('frequencias_sessoes_22.xlsx').dropna()
base_orig = pd.read_excel('mastervida_pa_db_19_22_.xlsx').dropna()
base = base_orig.loc[base_orig['ano'] == 2022]
base_pos = base.loc[(base['df_pas_'] >= 0)]
base_pos2 = base_pos.loc[(base_pos['df_pad_'] >= 0)]


freq_mais = freq_orig.loc[freq_orig['group_freq'] == 'mais']['nome_id']
freq_med = freq_orig.loc[freq_orig['group_freq'] == 'med']['nome_id']
freq_menos = freq_orig.loc[freq_orig['group_freq'] == 'menos']['nome_id']

escolhas = list(freq_mais)
escolhas2 = list(freq_med)
escolhas_nao = list(freq_menos)


selecionados = pd.DataFrame()
selecionados2 = pd.DataFrame()
selecionados_nao = pd.DataFrame()

# escolhas_nao = []
# for num in opcoes2:
#     if num not in escolhas2:
#         escolhas_nao.append(num)

for valor in escolhas:
    escolhido_valor = base_pos2.loc[base_pos2['nome_id'] == valor]
    selecionados = pd.concat([selecionados, escolhido_valor], ignore_index=True)

for valor in escolhas2:
    escolhido_valor2 = base_pos2.loc[base_pos2['nome_id'] == valor]
    selecionados2 = pd.concat([selecionados2, escolhido_valor2], ignore_index=True)

for valor in escolhas_nao:
    escolhido_valor_nao = base_pos2.loc[base_pos2['nome_id'] == valor]
    selecionados_nao = pd.concat([selecionados_nao, escolhido_valor_nao], ignore_index=True)

# listadescb = listaids1.groupby('nome_id').mês.value_counts()
listadescb = base_pos2.describe()
st.dataframe(listadescb)

st.dataframe(base_pos2)


if not selecionados.empty:
    # fig = px.bar(selecionados, x='data', y=['pre_pas_', 'pos_pas_'], barmode='group')
    # st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    fig2 = px.scatter(selecionados, x='data', y='pre_pas_', trendline="ols")
    fig2.update_layout(scattermode="group")
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
    #
    # listausers = selecionados.groupby('nome_id').describe()
    # st.dataframe(listausers)
    # listausers2 = selecionados2.groupby('nome_id').describe()
    # st.dataframe(listausers2)
    # listausers_nao = selecionados_nao.groupby('nome_id').describe()
    # st.dataframe(listausers_nao)

    # results = px.get_trendline_results(fig2)
    # print(results.px_fit_results.iloc[0].summary())
    # results2 = px.get_trendline_results(fig22)
    # print(results2.px_fit_results.iloc[0].summary())
    # results_nao = px.get_trendline_results(fig_nao2)
    # print(results_nao.px_fit_results.iloc[0].summary())

    # listausers_mes = set(selecionados['mês'].astype(int))
    # print(listausers_mes)
    # listausers = selecionados.loc[selecionados['mês'] == 11]
    # resumo_mes = listausers.groupby('nome_id').describe()
    #
    # st.dataframe(resumo_mes)

    base_mes = pd.read_excel('results_22_mes_pos.xlsx').dropna()
    consulta_grup = base_mes.loc[base_mes['grupo_'] == 'menos']
    consulta = consulta_grup.groupby('hiperten').describe()
    st.dataframe(consulta)

    fig_mes_dfpas = px.scatter(consulta_grup, x='mês_max', y='df_pas__mean', symbol='nome_id', trendline='ols')
    st.plotly_chart(fig_mes_dfpas, theme="streamlit", use_container_width=True)
    fig_mes_dfpad = px.scatter(consulta_grup, x='mês_max', y='df_pad__mean', symbol='nome_id', trendline='ols')
    st.plotly_chart(fig_mes_dfpad, theme="streamlit", use_container_width=True)

    results = px.get_trendline_results(fig_mes_dfpad)
    for item in results.px_fit_results:
        print(item.rsquared)

    for item_id in results.nome_id:
        print(item_id)




