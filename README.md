![Logo](https://i.ibb.co/1RGz0VH/PIM-2.jpg)

# NeuralChat

This Chatbot is created in Python using NLTK, Tensorflow, keras, numpy and FastAPI.

**NOTE:**
(CURRENTLY OPTIMIZED FOR MAC OS (ARM64 CHIPS) ONLY DUE TO DIFFERENT GPU ARCHITECTURE IN WINDOWS)

## Features

- Train for custom datasets.
- Uses 3 layer Neural Network.
- Fast & Efficient.
- Can be integrated anywhere via REST API. (Web, Mobile App, Iot etc)

## API Reference

#### Get API Endpoints Docs

```http
  GET /docs
```

#### Ask Chatbot

```http
  POST /chatbot
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text`    | `string` | **Required**. Text to ask chatbot |

## Author

- [@ProgrammingInBlood](https://www.github.com/ProgrammingInBlood)

## Run Locally

Clone the project

```bash
  git clone https://github.com/ProgrammingInBlood/NeuralChat
```

Go to the project directory

```bash
  cd NeuralChat
```

Install dependencies

```bash
   pip install requirements.txt
```

Train Chatbot & Create Model

```bash
   python src/train_chatbot.py
```

Start the server

```bash
  python main.py
```

## Tech Stack

**Language:** Python (v3.9)

**Server:** FastAPI, Uvicorn

**Machine Learning:** NLTK, Tensorflow, Keras
