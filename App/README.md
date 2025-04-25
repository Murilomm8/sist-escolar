# API de Gestão Escolar - Back-end (Projeto sis-esco)

Este é o back-end do sistema de gestão escolar, desenvolvido com Python e Flask, utilizando SQLite para persistência dos dados (ideal para desenvolvimento e testes). A API implementa os seguintes recursos:
- Gerenciamento de Pagamentos (GET/POST em /payments)
- Registros de Presenças (GET/POST em /attendances)
- Registro de Atividades (GET/POST em /activities)
- Endpoint para inicialização do banco de dados (/initdb) – **use com cautela em ambiente de desenvolvimento**

## Instruções para Execução

### Sem Docker

1. Certifique-se de ter o Python 3.9 ou superior instalado.
2. Navegue até a pasta `sis-esco/App`:
   ```bash
   cd sis-esco/App
