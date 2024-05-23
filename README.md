# Multiclass text classificator
This app is playground for multiple-class text clasificator task where we wanna classify text (title and perex of article) into predefine categories. Its build as conteinered app on `python 3.11`, `fast api` and some jupyter notebooks.

## Requirements
Let's make sure you have Docker and the NVIDIA Container Toolkit installed. Also check if your system support make (but this is not nessesary)

## Local development
If you want to run this code on your machine, you have 2 options:

1. Easy way - use the `tensorflow/tensorflow:latest-gpu-jupyter` dev container in your code editor with arguments that allow you to use GPU and
   setup this container to auto install `requirements.txt`. For VS Code `devcontainer.json`, it should look like this:

   ```json
   {
     "name": "transformers",
     "image": "tensorflow/tensorflow:latest-gpu-jupyter",
     "forwardPorts": [
       8888
     ],
     "containerEnv": {
       "PYTHONPATH": "${containerEnv:PYTHONPATH}:/env",
       "PATH": "/usr/local/cuda/bin:${localEnv:PATH}",
       "LD_LIBRARY_PATH": "/usr/local/cuda/lib64:${localEnv:LD_LIBRARY_PATH}"
     },
     "remoteUser": "root",
     "customizations": {
       "vscode": {
         "extensions": [
           "ms-python.python",
           "ms-toolsai.jupyter"
         ]
       }
     },
     "postCreateCommand": "pip install -r requirements.txt",
     "postStartCommand": "export PYTHONPATH=$PYTHONPATH:/env",
     "runArgs": [
       "--gpus",
       "all"
     ]
   }
2. Harder way - install CUDA directly on your machine, create virtual enviroment and install tensorflow, pytorch, flash-attn and rest of sweets

## Run app
1) Create a .env file with the following structure:

  ```bash
  OPENAI_API_KEY=your_open_ai_api_keys
  OPENAI_MODEL=gpt-3.5-turbo-instruct
  OLLAMA_MODEL=mistral:instruct # check official pages of ollama and pick what you preffer
  CUSTOM_MODEL=my_model # name it as you want in case that you will train your own model
  LABELS_FILE=labels/labels.csv
  ```

2) Go into the project directory and in the terminal type `make cheers`. If you see a response, you are on the right track.
3) To run containers, execute `make run`. For the rest of the commands, check the Makefile. If your system does not support `make`, then use direct Docker commands.
4) After a successful build, run the following command in your terminal: `docker exec -it ollama ollama run mistral:instruct`
5) Have fun on `localhost:8000`

## Training custom model
1) Create a `data` directory in the root. Inside that, add `processed` and `raw` directories. Add your dataset in the `raw` directory. Also, create a `labels` directory in the root and keep it empty.
2) Check the `preprocessing.ipynb` file. If it works on your dataset, feel free to use it as is. Otherwise, update it as needed. Ensure that at the end of data processing, you have two files in `processed` - `train.csv` and `test.csv `with columns `text` and `label`. The `preprocessing.ipynb` will also create a `labels.csv` file in the `labels` directory.
3) You can choose between TensorFlow and PyTorch implementations for training, but the PyTorch version is not fully implemented yet. Ensure that the directory with the new model has the same name as the `CUSTOM_MODEL` parameter in the `.env` file.
4) Use the `custom_model` route in your browser to interact with this model.

# Usage
The app contains three endpoints: one for OpenAI API calls, one for Ollama implementation for local running of LLMs, and the third for custom models driven by the Hugging Face/Transformers library. Be free to play with different models, try another training methods and / or contribute on this repo as you want.