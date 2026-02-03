import streamlit as st
from services.blob_service import upload_file_to_blob
from services.credit_card_service import analyze_credit_card


def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_container_width=True)
    st.write("Resultados da Validação:")

    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown("<h1 style='color:green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info.get('card_name')}")
        st.write(f"Banco Emissor: {credit_card_info.get('bank_name')}")
        st.write(f"Data de Validade: {credit_card_info.get('expiry_date')}")
    else:
        st.markdown("<h1 style='color:red;'>Cartão Inválido</h1>", unsafe_allow_html=True)


def configure_interface():
    st.title("Upload de Arquivos DIO - Desafio 1 Azure AI Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo para fazer o upload", type=["png", "jpg", "jpeg"])

    if uploaded_file is None:
        st.info("Selecione um arquivo para fazer upload.")
        return

    file_name = uploaded_file.name

    blob_url = upload_file_to_blob(uploaded_file, file_name)

    if blob_url:
        st.write(f"Arquivo '{file_name}' enviado com sucesso para o Azure Blob Storage.")

        credit_card_info = analyze_credit_card(blob_url)

        if credit_card_info.get("error"):
            st.error(credit_card_info["error"])
            return

        show_image_and_validation(blob_url, credit_card_info)

    else:
        st.error(f"Falha ao enviar o arquivo '{file_name}' para o Azure Blob Storage.")

configure_interface()
