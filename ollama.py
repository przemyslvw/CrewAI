import os
from ollama import Ollama

# Ustawienie ścieżki do danych
data_path = "ścieżka/do/twoich/danych"

# Funkcja wczytująca dane
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

# Inicjalizacja modelu
model = Ollama("llama2")

# Wczytanie danych
file_path = os.path.join(data_path, "nazwa_pliku.txt")
data = load_data(file_path)

# Przekazanie danych do modelu
response = model.generate(prompt=data)

print(response)