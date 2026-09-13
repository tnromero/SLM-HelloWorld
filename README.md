# Explorando o uso de SLM com Ollama

## Pré-Requisito

- Instalar WSL 
    - Instalar o `Python 3.13` no WSL
    - Instalar o `UV` instalado para gerenciar ambiente Python
        1. Instalar UV: `curl -LsSf https://astral.sh/uv/install.sh | sh`
        2. Depois feche e abra novamente o Ubuntu ou carregue o perfil: `source ~/.bashrc`
    - Instalar ferramentas básicas:
        ```
        sudo apt install -y \
            curl \
            git \
            build-essential \
            ca-certificates \
            jq
        ``` 

## Preparação do ambiente

1. Acessar o `wsl`

1. Instalar o Ollama: 
    
    `curl -fsSL https://ollama.com/install.sh | sh`

    `ollama --version`

1. Baixar o modelo desejado:

    `ollama pull qwen3:1.7b`

5. Verificar modelos instalados:

    `ollama list`

6. Iniciar SLM:

    `ollama run qwen3:1.7b`

    `ollama run qwen3:1.7b --think=false`

7. Faça sua pergunta de teste

8. Abra uma segunda sessão do `wsl` e teste a chamada da API do Ollama

    - Tags
    
        `curl http://localhost:11434/api/tags`

    - Prompt
        ```
        curl http://localhost:11434/api/chat \
            -d '{
                "model": "qwen3:4b",
                "messages": [
                {
                    "role": "user",
                    "content": "Classifique: SUPERMERCADO ABC"
                }
                ],
                "stream": false
            }'
        ```

### Testando via Python

1. Inicializar projeto Python com UV:

    `uv init --python 3.13`

1. Adicionar o ollama ao projeto:

    `uv add ollama`

1. Executar código:

    `uv run python main.py`

## Acompanhar uso da GPU

1. Processos em exeução do Ollama:
    
    `ollama ps`

1. Consumo da GPU pela Nvidia:

    `nvidia-smi` ou `watch -n 1 nvidia-smi`
