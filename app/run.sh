#!/bin/bash

#!/bin/bash

# Diretório do frontend
frontend_dir="/app/frontend"

# Diretório do backend
backend_dir="/app/backend"

# Comandos para o frontend
echo "Iniciando o frontend..."
cd "$frontend_dir" && npm install # Navega até o diretório do frontend e instala as dependências
npm run dev # Executa o servidor de desenvolvimento do Vue.js

# Comandos para o backend
echo "Iniciando o backend..."
cd "$backend_dir" && pip install -r requirements.txt # Navega até o diretório do backend e instala as dependências
python run.py # Inicia o servidor do FastAPI
