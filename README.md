# 🤖 Bot de Telegram – Proyecto Administración de Proyectos de Software

Este proyecto implementa un **bot de Telegram** desarrollado en Python, ejecutado dentro de Docker y que consume la **API pública de Binance** para obtener precios de criptomonedas.  
Fue realizado como parte de la materia *Administración de Proyectos de Software*.

## 📌 Funcionalidades del Bot

### ✅ 1. Comando `/start`
Da la bienvenida y explica las funciones disponibles.

### ✅ 2. Comando `/precio`
Muestra al usuario un teclado con tres opciones:

- **Bitcoin**
- **Ether**
- **Pepe**

Al elegir una, el bot consulta:

```
https://api.binance.com/api/v3/ticker/price?symbol=<SYMBOL>
```

y responde con el precio actual en USDT en un formato legible.

### ✅ 3. Echo automático
Cualquier mensaje que no sea un comando es reflejado:

> Usuario: hola  
> Bot: hola

### 🔐 4. Token seguro mediante `.env`
El bot no tiene el token escrito en el código.  
El token se pasa mediante variables de entorno dentro del contenedor.

### 🐳 5. Dockerizado completamente
El bot corre en un contenedor Docker usando:

- Python 3.12 slim
- requirements.txt
- long polling (no requiere puertos abiertos)

## 🗂️ Estructura del Proyecto

```
/telegram-bot
│── mi-bot.py
│── requirements.txt
│── Dockerfile
│── .env
│── .dockerignore
│── README.md
```

## ⚙️ Instalación y Ejecución

### 1️⃣ Clonar repositorio

```bash
git clone <URL-del-repo>
cd telegram-bot
```

### 2️⃣ Crear archivo `.env`

```env
BOT_TOKEN=TU_TOKEN_AQUI
```

### 3️⃣ Construir la imagen

```bash
docker build -t proyecto:latest .
```

### 4️⃣ Ejecutar el contenedor

```bash
docker run --name proyecto --env-file .env proyecto:latest
```

Verás:

```
Bot corriendo con long polling...
```

## 🧪 Cómo Probar el Bot

1. Abre Telegram y busca tu bot por su **@nombre**.  
2. Escribe `/start` → el bot responde.  
3. Escribe `/precio` → aparece un teclado con monedas.  
4. Selecciona una → el bot da el precio en Binance.  
5. Escribe cualquier mensaje normal → el bot lo refleja.

## 🌐 API Consumida

Se usa la API pública de Binance:

```url
GET https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
```

La respuesta se procesa para mostrar el precio de forma clara.

## 📦 Dependencias (requirements.txt)

```
python-telegram-bot>=21.0
requests>=2.0
```

## 💬 Autor

**Ortega Novoa Octavio**

## 📘 Notas

- El bot solo funciona mientras el contenedor Docker está encendido.  
- No requiere puertos abiertos porque usa *long polling*.  
