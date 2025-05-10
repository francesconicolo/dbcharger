# Usa una base image Python
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del codice nella directory di lavoro
COPY . .

# Imposta il comando di esecuzione del programma
CMD ["python","-u","app.py"]
