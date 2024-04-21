from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions and practical travel advice.

Key Steps for task creation:
1. Identify the desired outcome: Define what success looks like for your project.
    - A detailed 7 day travel itinerary

2. Task Breakdown: Divied the goal into smaller, manageable tasks that agent can execute.
    - Itinerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analyze and pick the best cities to visit.
    - Local tour guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expetise.
4. Task Description Template:
    - Use this template as a guide to define each task into your CrewAI application.
    - This template helps ensure that each task is clearly defined, actionable and aligned with the specific

    Template:
    ---------

        def [task_name](self, agent, [parameters]):
        return Task(description=dedent(f'''
        **Task**: [Provide a concise name or summary of the task.]
        **Description**: [Detailed description of what the agent is expected to do, including actionable steps and ]

        **Parameters**:
        - [Parameter 1]: [Description]
        - [Parameter 2]: [Description]
        ... [Add more parameters as needed.]                            
        
        **Note**: [Optional section for incentives or encouragement for high-quality work.]
        '''), agent=agent)

"""




# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a 7-day Travel itinerary
            **Description**: Expand the city guide into a full 7-day travel itinerary with detailed
                per day plans, including weather forecasts, places to eat, packing suggestions,
                and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay,
                and actual restaurents to go to. This itinerary should cover all aspecrs of the trip,
                from arrival to departure, integrating the city guide information with practical travel logistics.

            **Parameters**:
            - City: {city}
            - Trip Date: {travel_dates}
            - Traveler_Interests: {interests}

                
        
            **Note**: {self.__tip_section()}

            
            """
            ),
            agent=agent,
        )

    def identify_city(self, agent, origin, cities, interests, date_range):
        return Task(
            description=dedent(
                f"""
            **Task**: Identify the best cities
            **Description**: Analyze and select the best city for the trip based on specific
                criteria such as weather, seasonal events, and travel costs.
                This task involves comparing multiple cities, considering factors like current weather
                conditions, upcoming cultural or seasonal events, and overall travel expenses.
                Your final answer must be a detailed report on the chosen city, including actual flight costs, weather forecasts and attractions.

            **Parameters**:
            - origin: {origin}
            - Cities: {cities}
            - Interests: {interests}
            - Travel Date: {date_range}

                                      
        
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )
    
    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Gather in-depth City guide information
            **Description**: Compile an in-depth guide for the selected city, gathering information about
                key attracttions, local customes, special events, and daily activity recommendations.
                This guide should provide a thorough overview of what city has to offer, including
                hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high level cost information.

            **Parameters**:
            - City: {city}
            - Interests: {interests}
            - Travel Date: {travel_dates}

                                      
        
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )
