# Usa imagem oficial do Python
FROM python:3.12-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 5000

# Comando para iniciar o Flask com as variáveis do .env
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
