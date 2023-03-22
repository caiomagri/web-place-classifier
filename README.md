# Aplicação Web para Predição de locais em Imagem

Aplicação construida utilizando o framework [Streamlit](https://streamlit.io/) para envio de imagem e envio para uma api que faz predição do local  da imagem.

## Como rodar

A aplicação foi feita utilizando Docker, então você pode executar seguindo os seguintes passos:

Criando/Buildando a aplicação.
```bash
 docker build -t web-place-classifier .
```

Para informar para aplicação em qual endpoint vamos enviar uma requisição, você deve definir essa URL dentro do arquivo .env na variavel CLASSIFIER_API_URL.

```env
CLASSIFIER_API_URL=https://place-classifier-api.onrender.com/predict
```

após definir a variável de ambiente, vamos rodar o container

```bash
docker run -d --name web -p 8501:8501 --env-file .env web-place-classifier
```

## Como acessar a aplicação?

A aplicação por default irá rodar na porta 8501 do seu localhost.

[http://localhost:8501 ](localhost:8501)

## Deploy

Você pode acessar um ambiente teste da aplicação em deploy:

[https://place-classifier-web.onrender.com](https://place-classifier-web.onrender.com)