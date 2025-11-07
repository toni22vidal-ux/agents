from multinicho_agents.lead_qualifier import LeadQualifier
def test_lead_qualifier_runs():
    out = LeadQualifier().run({"message": "hola"})
    assert "qualified" in out
