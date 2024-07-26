import os
from crewai import Agent, Task, Process, Crew
from crewai.agent import ChatOpenAI  # Poprawiony import

openai_api_key = "A4gZRQMCjEBpsFiNxwaT3BlbkFJqxmNhlpRiz2B0ORcTvvc"

# Ustawienie zmiennej środowiskowej
os.environ['OPENAI_API_KEY'] = openai_api_key

api = os.environ.get('OPENAI_API_KEY')


Trener = Agent(
    role="Trener Kulturystyki",
    model=ChatOpenAI(openai_api_key=openai_api_key),
    goal="Przyrost masy mięściowej",
    backstory="Sprawdził wszystkie rodzaje diety i najlepsze efekty uzyskał na carnivore diet",
    verbose=True,
    allow_delegation=True,
)
Programista = Agent(
    role="Trener Programowania",
    model=ChatOpenAI(openai_api_key=openai_api_key),
    goal="Uzyskanie crtyfkatu ISTQB",
    backstory="Posiada wszystkie niezbędne szkolenia, chce zdobyć certyfikat",
    verbose=True,
    allow_delegation=True,
)

task = Task(
    name="Trening",
    description="Przygotuj plan treningowy",
    duration=60,
    priority=5,
    deadline="2021-12-31",
    agent=Trener,
    expected_output="Plan treningowy na 4 tygodnie"  # Dodanie wymaganego pola
)

task1 = Task(
    name="Dieta",
    description="Przygotuj plan dietetyczny",
    duration=60,
    priority=5,
    deadline="2021-12-31",
    agent=Trener,
    expected_output="Plan dietetyczny na 4 tygodnie"  # Dodanie wymaganego pola
)

task2 = Task(
    name="Szkolenie",
    description="Przygotuj się do egzaminu",
    duration=60,
    priority=5,
    deadline="2021-12-31",
    agent=Programista,
    expected_output="Plan szkoleniowy na 4 tygodnie"  # Dodanie wymaganego pola
)

crew = Crew(    
    agents=[Programista, Trener],
    tasks=[task, task1, task2],
    verbose=2,
    process=Process.sequential,
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
