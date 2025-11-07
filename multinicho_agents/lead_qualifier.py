from .base import Agent
class LeadQualifier(Agent):
    name = "lead_qualifier"
    def run(self, input: dict) -> dict:
        return {"qualified": True, "notes": "MVP"}
