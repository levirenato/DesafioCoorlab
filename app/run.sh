#!/bin/bash

frontend_dir="frontend/"

# Diretório do backend
backend_dir="backend/"

# Comandos para o backend
echo "Iniciando o backend..."
(cd "$backend_dir" && python -m pip install virtualenv && \
    python -m virtualenv venv && \
    source venv/bin/activate && \
    pip install -r requirements.txt && \
    python3 run.py &)


# Comandos para o frontend (executados em segundo plano)
echo "Iniciando o frontend..."
cd "$frontend_dir" && npm install && npm run dev