# Aqui tens os comandos necessários para rodar a API pelo docker.
docker run -it -p 8080:8080 payment-gateway-back-end_api


Puxar a imagem no docker hub:
docker push derciosinione/paymentgateway


Comando para rodar a api:
docker run -it -p 8000:8000 derciosinione/paymentgateway 

em seguida simplesmente terás que ir no navegador e acessar o seguinte endereço:
http://0.0.0.0:8000/

ou 

http://127.0.0.1:8000/