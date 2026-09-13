from ollama import chat

LANGUAGE_MODEL = {
    "QWEN-3-1.7B": "qwen3:1.7b",
    "QWEN-3-4B": "qwen3:4b",
}

PROMPT = """
Classifique estas despesas nas categorias Alimentação, Transporte, Moradia, Saúde, Entretenimento ou Outros:

1. Uber para o trabalho
2. Supermercado Carrefour
3. Netflix
4. Farmácia
5. Conta de energia
"""
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("PROMPT:")
print("-----------------------------------------------------------")
print(PROMPT)
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")


response = chat(
    model=LANGUAGE_MODEL["QWEN-3-1.7B"],
    messages=[
        {
            "role": "user",
            "content": PROMPT,
        }
    ],
)

print("RESPOSTA:")
print("-----------------------------------------------------------")
print(response.message.content)
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("MODELO", LANGUAGE_MODEL["QWEN-3-1.7B"])
