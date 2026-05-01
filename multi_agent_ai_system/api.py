from fastapi import FastAPI
from pydantic import BaseModel
from agents import research_agent, planner_agent, writer_agent
from logger import log_data

app = FastAPI(title="Multi-Agent AI System")


class TopicRequest(BaseModel):
    topic: str


@app.get("/")
def home():
    return {"message": "Gemini Multi-Agent AI API Running"}


@app.post("/research")
def research(request: TopicRequest):
    result = research_agent(request.topic)
    log_data("Research Agent", result)
    return {"research": result}


@app.post("/plan")
def plan(request: TopicRequest):
    research = research_agent(request.topic)
    outline = planner_agent(research)

    log_data("Planner Agent", outline)
    return {"outline": outline}


@app.post("/generate-report")
def generate_report(request: TopicRequest):
    research = research_agent(request.topic)
    outline = planner_agent(research)
    report = writer_agent(outline)

    log_data("Final Report", report)

    return {
        "topic": request.topic,
        "research": research,
        "outline": outline,
        "report": report
    }