import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")

st.image("logo.png", width=200)

st.title("Gerenciamento de Produto")

#Função auxiliar para exibir mensagem de erro detalhada
def show_response_message(response):
    if response.status_code == 200:
        st.success("Operação realizada com sucesso!")
    else:
        try:
            data = response.json()
            # Se o erro for uma lista, extraia as mensagens de cada erro
            if isinstance(data["detail"], list):
                errors = "\n".join([error["msg"] for error in data["detail"]])
                st.error(f"Erro: {errors}")
            else:
                # Caso contrario, mostre a mensagem de erro diretamente
                st.error(f"Erro: {data['detail']}")
        except ValueError:
            st.error("Erro desconhecido. Não foi possível decodificar a resposta")

# Adicionar Produto
with st.expander("Adicionar um Novo Produto"):
    with st.form("new_product"):
        name = st.text_input("Nome do Produto")
        description = st.text_area("Descrição do Produto")
        price = st.number_input("Preço", min_value=0.01, format="%f")
        category = st.selectbox(
            "Categoria",
            ["Eletronico", "Eletrodomestico", "Móveis", "Roupas","Calçados"],)            
        supplier_email = st.text_input("Email do Fornecedor")
        submit_button = st.form_submit_button("Adicionar Produto")

        if submit_button:
            response = requests.post(
                "http://backend:8000/products/",
                json={
                    "name": name,
                    "description":description,
                    "price": price,
                    "category": category,
                    "supplier_email": supplier_email,
                },
            )
            show_response_message(response)

# Visualizar Produtos
with st.expander("Visualizar Produtos"):
    if st.button("Exibir Todos os produtos"):
        response = requests.get("http://backend:8000/products/")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame(product)

            df = df[
                [
                    "id",
                    "name",
                    "description",
                    "price",
                    "category",
                    "supplier_email",
                    "created_at",
                ]
            ]
            # Exibe o DataFrame sem o indice
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Obter Detalhes de um Propduto

with st.expander("Obter detalhes de um Produto"):
    get_id = st.number_input("ID do Produto", min_value=1, format="%d")
    if st.button("Buscar Produto"):
        response = requests.get(f"http://backend:8000/products/{get_id}")
        if response.status_code == 200:
            product = response.json()
            df = pd.DataFrame([product])

            df = df[
                    [
                        "id",
                        "name",
                        "description",
                        "price",
                        "category",
                        "supplier_email",
                        "created_at",
                    ]
            ]
            # Exibe o DataFrame sem o indice
            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)

# Deletar Produto

with st.expander("Deletar Produto"):
    delete_id = st.number_input("ID do Produto para Deletar", min_value=1, format="%d")
    if st.button("Deletar Produto"):
        response = requests.delete(f"http://backend:8000/products/{delete_id}")
        show_response_message(response)

# Atualizar Produto
with st.expander("Atualizar Produto"):
    with st.form("update_product"):
        update_id = st.number_input("ID do Produto", min_value=1, format="%d")
        new_name = st.text_input("Novo Nome do Produto")
        new_description = st.text_area("Nova Descrição do Produto")
        new_price = st.number_input("Novo Preço", min_value=0.01, format="%f")
        new_category = st.selectbox(
            "Nova Categoria",
            ["Eletronico", "Eletrodomestico", "Móveis", "Roupas","Calçados"],)    
        new_supplier_email = st.text_input("Novo e-mail Fornecedor")

        update_button = st.form_submit_button("Atualizar Produto")
        if update_button:
            upddate_data = {}
            if new_name:
                upddate_data["name"] = new_name
            if new_description:
                upddate_data["description"] = new_description
            if new_price:
                upddate_data["price"] = new_price
            if new_supplier_email:
                upddate_data["supplier_email"] = new_supplier_email
            if new_category:
                upddate_data["category"] = new_category

            if upddate_data:
                response = requests.put(
                    f"http://backend:8000/products/{update_id}", json=upddate_data
                )
                show_response_message(response)