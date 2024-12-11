
import os 
from dotenv import  load_dotenv
from crewai import Agent, Task, Process, Crew

load_dotenv()

#load GPT4
api = os.environ.get("OPENAI_API_KEY")

#DEFINE AGENTS

#Market Reseach Agent
marketer = Agent(
    role="Market Research Analyst",
    goal="Find out how big is the demand for my products and suggest how to reach the widest possible customer base",
    backstory="""You are an expert at understanding the market demand, target audience and competiton. This is crucial for 
    validating whether an idea fulfills a markett need and has the potential to attract a wider audience. You are good 
    at coming up with ideas to appeal to widest possible audience.""",
      verbose=True, #help agents create detailed outputs
      allow_delegation=True, #allow agents to collaborte
)

#Technologist Agent
technologist = Agent(
    role="Technology Expert",
    goal="Make assessment on how technologically feasible the company is and what type of technologies the companiy needs in order to succeed",
    backstory="""You are a visionary in the realm of technology, with a deep understanding of the current and emerging 
    technological trends. Your expertise lise in not only knowing the technology but in foreseeing how it can be leveraged to solve real world problems
    and drive business innovation. You have a knack for identifying which technological solutions best fit different business models
    and needs, ensuring that companies stay ahead of the curve. Your insights are crucial in aligning technology with business strategies 
    , ensuring that the technological adoption not only enhances operatinoal efficiency but also provides a competetive edge in 
    the market.""",
      verbose=True, #help agents create detailed outputs
      allow_delegation=True, #allow agents to collaborte
)

#Business Consultant Agent
businessguy = Agent(
    role="Business Development Consultant",
    goal="Evaluate and advise on the business model, scalability and potential revenue streams to ensure long-term sustainability and profitability",
    backstory="""You are a seasoned professional with expertise in shaping business strategies. Your insight is essential for turning innovative ideas
    into viable business models. You have a keen understanding of various industries and are adept at identifying and developing potential
    revenue streams. Your experience in scalability ensures that a business can grow without comprimising its values or operational efficiency.
    Your advice is not just about immediate gains but about building a resilient and adaptable business that can thrive in a changing market.
      """,
      verbose=True, #help agents create detailed outputs
      allow_delegation=True, #allow agents to collaborte
)

reserachtask = Task(
    description="""Analyze what is the market demand for "personalized AI Agents with contextual memory in India". Write a detailed report 
                    with description of what the ideal customer profile might look like, and how to reach the widest possbile
                    audience.                                                                        
                    """,
    expected_output="""The report has to be concise with atleast 10 bullet points in a tabular format, and it has to address the most 
                    important areas when it comes to marketing this type of business.""",             
    agent= marketer,
)

technologytask= Task(
    description="""Analyze how to develop "personalized AI Agents with contextual memory in India", with minimum resources. Write a detailed report 
                    with description of which technologies the business needs to use for a successful buinsess implementation.                                                                       
                    """,
    expected_output="""The report has to be concise with atleast 10 bullet points in a tabular format, and it has to address the most 
                    important areas when it comes to developing technologies for this type of business.""",
    agent= technologist,
)

businesstask = Task(
    description="""Analyze and summarize marketing and technological report, and write a detailed business plan with description of 
    how to make a sustainable and profitable "personalized AI Agents with contextual memory in India" business.                                                                       
                    """,
    expected_output="""The business plan 
    has to be concise with atleast 10 bullet points with : 4 Ideal customer profiles, Total Addressable Market in dollars, Top 5 goals 
    and it needs to have a timeline for which goal needs to be completed by when.
    """,
    agent= businessguy,
)

crew = Crew(
    agents=[marketer, technologist, businessguy],
    tasks=[reserachtask, technologytask, businesstask],
    verbose=True,
    process=Process.sequential,
)

result = crew.kickoff()
print("************************************")
print(result)