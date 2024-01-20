FROM python:3.11.5
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Ajoutez la clé GPG de Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Ajoutez le référentiel Microsoft aux sources de paquets
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/msprod.list

# Installez le pilote ODBC MSODBCSQL17
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]