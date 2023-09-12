# Atividade avaliativa 3 

Para a realização da atividade avaliativa 3, foi utilizado o dataset "Customer Segmentation". O dataset foi normalizado e todas as modificações e tratamentos realizados estão dispostos no notebook que está no repositório. Primeiramente, utilizei o pycaret para realizar o treinamento porém não foi possível dar continuidade e por essa maneira escolhi o modelo de "Random Forest", pois o dataset se trata de uma predição onde ao inputar determinados dados deveremos retornar uma previão de qual será o será o score do cliente.

## Dockerhub
A api containerizada está disponível no dockerhub através do seguinte link:
https://hub.docker.com/repository/docker/bialimac/ponderada3/general

## Como utilizar
Para utilizar, execute o comando abaixo em um terminal: </br>
```
docker run -p 5000:5000 bialimac/ponderada3
```

## Funcionamento da API

- /predict
Ao acessar o endereço abaixo aparecerá o Swagger UI onde você poderá utilizar a rota "/predict" para obter sua predição
```
http://127.0.0.1:5000/docs
```
## Exemplo de entrada
```
{
  "CustomerID": 201,
  "Gender": 0,
  "Age": 0.5,
  "Annual": 0.7
}
```
## Saída esperada
```
{
  "prediction": 0.24285714285714322
}
```

## Link do vídeo 
https://drive.google.com/drive/folders/1-CbwrJpxtwNlS_671y82l2SjbMlEycem?usp=sharing
