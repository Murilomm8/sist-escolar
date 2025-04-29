# API de Gestão Escolar - Back-end (Projeto sis-esco)

Este é o back-end do sistema de gestão escolar, desenvolvido com Python e Flask, utilizando SQLite para persistência dos dados (ideal para desenvolvimento e testes). A API implementa os seguintes recursos:
- Gerenciamento de Pagamentos (GET/POST em /payments)
- Registros de Presenças (GET/POST em /attendances)
- Registro de Atividades (GET/POST em /activities)
- Registro de Atividades (GET/POST em /students)
- Endpoint para inicialização do banco de dados (/initdb) – **use com cautela em ambiente de desenvolvimento**

## Instruções para Execução

### Sem Docker

1. Certifique-se de ter o Python 3.9 ou superior instalado.
2. Navegue até a pasta `sis-esco/App`:
   ```bash
   cd sis-esco/App

### com Docker
1. Navegue até a pasta da API Abra seu terminal/PowerShell e vá para o diretório onde está o Dockerfile da aplicação. Por exemplo:
cd sis-esco/App

2. Construir a Imagem Docker Construa a imagem Docker utilizando o comando abaixo. Isso compacta o projeto e instala todas as dependências (incluindo o Flasgger, Flask, etc.):
docker build -t sis-esco .

3. Iniciar o Container Após a construção bem-sucedida da imagem, inicie a aplicação dentro de um container utilizando:
docker run -d -p 5000:5000 sis-esco
A opção -d indica que o container será iniciado em modo detached (em segundo plano).
A opção -p 5000:5000 mapeia a porta 5000 do container para a porta 5000 do host.
Assim, a API estará acessível em http://localhost:5000.

4. Verificar se o Container Está Rodando Você pode listar os containers ativos com o comando:
docker ps
Verifique se há um container com o nome ou imagem sis-esco ativo.

5. Acessar a API e a Documentação Swagger
No navegador acesse: http://localhost:5000/ – para confirmar que a aplicação está em execução; http://localhost:5000/api/docs – para visualizar a interface interativa do Swagger com a documentação dos endpoints.

6. Visualizar Logs (opcional) Caso deseje ver os logs da aplicação, utilize o comando, substituindo <container_id> pelo ID do container listado pelo docker ps:
docker logs <container_id>

7. Encerrar o Container Para parar o container, execute:
docker stop <container_id>
