
# Vinheria Microservices

Simulação da arquitetura da Vinheria Agnello com foco em DevOps, segurança e automação utilizando Docker e Jenkins.

## Microserviços disponíveis

- **auth_service:** cadastro e autenticação de usuários via JWT
- **orders_service:** cadastro e consulta de pedidos protegidos por JWT

---

## Requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Jenkins (incluso no compose, acessível via navegador)

---

## Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/brenoDataEngineer/vinheria-microservices.git
cd vinheria-microservices
```

### 2. Build e iniciação dos serviços

```bash
docker-compose up --build -d
```

- Serviços sobem nos containers: **auth_service**, **orders_service**, **jenkins**
- Jenkins acessível em: [http://localhost:8080](http://localhost:8080)

### 3. Acesse Jenkins (opcional)

Para acessar Jenkins pela primeira vez:

```bash
docker exec vinheria-microservices-jenkins-1 cat /var/jenkins_home/secrets/initialAdminPassword
```
Use essa senha para login inicial e configurar jobs.

---

## Testando os microserviços

### Auth Service

**Cadastrar usuário:**
```bash
curl -X POST http://localhost:5000/register      -H "Content-Type: application/json"      -d '{"username":"user1","password":"senha123"}'
```

**Login (JWT):**
```bash
curl -X POST http://localhost:5000/login      -H "Content-Type: application/json"      -d '{"username":"user1","password":"senha123"}'
```

### Orders Service

**Criar pedido (JWT):**
```bash
curl -X POST http://localhost:5001/pedidos      -H "Content-Type: application/json"      -H "Authorization: Bearer SEU_JWT_AQUI"      -d '{"item":"Vinho Tinto","quantidade":2}'
```

**Listar pedidos (JWT):**
```bash
curl -X GET http://localhost:5001/pedidos      -H "Authorization: Bearer SEU_JWT_AQUI"
```

---

## DevSecOps e Segurança

- Comunicação protegida por JWT
- Pipeline CI/CD automatizado no Jenkins
- Sugestão: analise pacotes via Wireshark para fins didáticos

---

## Estrutura do projeto

```
├── auth_service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── orders_service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── Jenkins.Dockerfile
├── Jenkinsfile
├── docker-compose.yml
```

---

## Referências

- [Docker Documentation](https://docs.docker.com/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Wireshark](https://www.wireshark.org/)

---
