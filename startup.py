from crewai import Agent, Task, Crew
from transformers import AutoModelForCausalLM, AutoTokenizer

# Konfiguracja modelu Hugging Face
model_name = "distilgpt2"  # Możesz zmienić na dowolny model dostępny na Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Przykład użycia modelu Hugging Face
def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    attention_mask = inputs['attention_mask']
    outputs = model.generate(
        inputs['input_ids'], 
        attention_mask=attention_mask, 
        max_length=50, 
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Przykładowe użycie funkcji generate_text
prompt = "Once upon a time"
generated_text = generate_text(prompt)
print(generated_text)

# Konfiguracja agenta z modelem Hugging Face
class HuggingFaceAgent(Agent):
    def __init__(self, role, goal, backstory, verbose=True, allow_delegation=True):
        super().__init__(role=role, goal=goal, backstory=backstory, verbose=verbose, allow_delegation=allow_delegation)
        self._model_name = model_name
        self._tokenizer = tokenizer
        self._model = model

    def generate_response(self, prompt):
        return generate_text(prompt)

# Ensure the required fields are passed correctly
trener = HuggingFaceAgent(
    role="Trener Kulturystyki",
    goal="Przyrost masy mięśniowej",
    backstory="Sprawdził wszystkie rodzaje diety i najlepsze efekty uzyskał na carnivore diet"
)

# Utwórz zadanie i przypisz do niego agenta
zadanie_treningowe = Task(
    name="Trening",
    description="Przygotuj plan treningowy",
    expected_output="Plan treningowy dostosowany do przyrostu masy mięśniowej",
    agents=[trener]  # Upewnij się, że agenci są przypisani prawidłowo
)

# Utwórz załogę
crew = Crew(
    agents=[trener],
    tasks=[zadanie_treningowe],
    verbose=2,
)

# Dodanie logowania przed wywołaniem kickoff
print('###################################')
print('Agents:', crew.agents)
print('Tasks:', crew.tasks)
print('Process:', crew.process)
print('Verbose:', crew.verbose)

result = crew.kickoff()

print('###################################')
print(result)
