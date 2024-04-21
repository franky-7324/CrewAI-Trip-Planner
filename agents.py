from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI


from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal.
- Define which experts the captain needs to communicate with and delegate tasks to.
- Build a top down structure of the crew.

Goal:
- Create a 7-day itinerary with detailed per-day plans including:
    - Budget,
    - packing suggestions,
    - safety tips.

Captain/Manager/Boss:
- Expert Travel Agent
- 

Employees/Experts to hire:
- City Selection Expert
- Local Tour guide

Notes:
- agents should be result driven and have a clear goal in mind.
- Role is their job title.
- Goal should be actionable.
- Backstory should be their resume.

"""


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TravelAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        # self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent(f"""
                        Expert in travel planning and logistics.
                        I have decades of experience making travel itineraries.
                        """),
            goal=dedent(f"""
                        Create a 7-day travel itinerary with detailed per-day plans,
                        include budget, packing and safety tips.
                        """),
            tools=[
                 SearchTools.search_internet,
                 CalculatorTools.calculate
                 ],
            # allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent(f"""Expert at analyzing travel date to pick ideal destinations."""),
            goal=dedent(f"""Select the best cities based on weather, prices, season and traveler interests."""),
            tools=[SearchTools.search_internet],
            # allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
            return Agent(
                role="Local Tour Guide",
                backstory=dedent(f"""ledgeable local guide with extensive information
                                 about the city, its attractions and customs."""),
                goal=dedent(f"""Provides best insights about the selected city."""),
                tools=[SearchTools.search_internet],
                # allow_delegation=False,
                verbose=True,
                llm=self.OpenAIGPT35,
            )