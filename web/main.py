import streamlit as st
import requests


def main():
    st.title("Place Classifier")

    st.write(
        "The purpose of this application is to receive an image from a specific place as an upload and using an "
        "external API query, it is able to process and inform the place according to the image."
    )

    st.write({
        0: 'Trem',
        1: 'Armazem/Galpão',
        2: 'Restaurante',
        3: 'Cassino',
        4: 'Metrô',
        5: 'Bar',
        6: 'Aeroporto',
        7: 'Quarto',
        8: 'Sala de estar',
        9: 'Cozinha',
    })

    uploaded_file = st.file_uploader("Choose a image to classify", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()

        st.image(bytes_data, caption='Image to classify')

        with st.spinner(text="Processing..."):
            url = "https://place-classifier-api.onrender.com/predict"

            response = requests.post(url, files={"file": bytes_data})

            if response.status_code == 200:
                data = response.json()
                description = data.get("description")
                st.header(description)
                st.json(response.json())

            else:
                st.write("Error: ", response.status_code)

            st.success('Done!')


if __name__ == '__main__':
    main()
