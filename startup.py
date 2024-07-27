from crewai import Agent, Task, Process, Crew
from transformers import AutoModelForCausalLM, AutoTokenizer

# Konfiguracja modelu Hugging Face
model_name = "gpt2"  # Możesz zmienić na dowolny model dostępny na Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Przykład użycia modelu Hugging Face
def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Przykładowe użycie funkcji generate_text
prompt = "Once upon a time"
generated_text = generate_text(prompt)
print(generated_text)

# Konfiguracja agenta z modelem Hugging Face
class HuggingFaceAgent(Agent):
    def __init__(self, role, goal, backstory, verbose=True, allow_delegation=True):
        super().__init__(role=role, goal=goal, backstory=backstory, verbose=verbose, allow_delegation=allow_delegation)
        self.model_name = model_name
        self.tokenizer = tokenizer
        self.model = model

    def generate_response(self, prompt):
        return generate_text(prompt)

# Ensure the required fields are passed correctly
Trener = HuggingFaceAgent(
    role="Trener Kulturystyki",
    goal="Przyrost masy mięściowej",
    backstory="Sprawdził wszystkie rodzaje diety i najlepsze efekty uzyskał na carnivore diet",
    verbose=True,
    allow_delegation=True,
)

# Utwórz zadanie
zadanie_treningowe = Task(
    name="Trening",
    description="Przygotuj plan treningowy"
)

# Utwórz załogę
crew = Crew(    
    agents=[Trener],
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