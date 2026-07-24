EVIDENCE_EXAMPLE = """
{
  "company_name": "Example Co",
  "industry": "Finance",
  "headquarters": "New York, USA",
  "geographic_presence": ["North America"],
  "company_size": "Enterprise",
  "employee_count": "12000",
  "founded": "1998",
  "products_services": ["Retail Banking","Digital Payments"],
  "business_model":"Banking services.",
  "technologies_used":["Cloud","AI"],
  "recent_news": [{
      "title":"AI assistant launched",
      "summary":"Customer support AI.",
      "source":"TechCrunch"
    }],
  "key_observations": ["Strong brand", "AI adoption"]
}
"""

OVERVIEW_EXAMPLE = """
{
  "summary":"Global financial services company.",
  "mission":"Accessible finance.",
  "vision":"Leading digital bank.",
  "target_market":["Consumers","Businesses"],
  "competitive_position":"Strong market position.",
  "strengths": ["Brand","Technology","Customers"]
}
"""

BUSINESS_EXAMPLE = """
{
  "core_operations":["Retail Banking","Payments"],
  "revenue_streams": ["Interest","Transaction Fees"],
  "customer_segments": ["Consumers","Businesses"],
  "value_proposition": "Secure financial services.",
  "operational_workflow": ["Acquire","Serve","Support"]
}
"""

CHALLENGES_EXAMPLE = """
{
  "challenges": [{
      "title":"Legacy Systems",
      "description":"Slow innovation.",
      "impact":"High"
    }]
}
"""

AI_OPPORTUNITIES_EXAMPLE = """
{
  "opportunities":[{
      "title":"AI Support",
      "description":"Automate customer support.",
      "business_value":"Lower costs.",
      "implementation_complexity":"Medium",
      "priority":"High"
    }]
}
"""


CEO_PITCH_EXAMPLE = """
{
  "executive_summary":"AI can improve efficiency and growth.",
  "recommended_ai_initiatives":["AI customer support","Predictive analytics"],
  "expected_business_impact":["Lower costs","Better decisions"],
  "recommended_first_step":"Start with a pilot project.",
  "closing_statement":"Expand based on measurable results."
}
"""








































# One optimization I recommend for all downstream nodes

# You're currently passing the entire Evidence object to:

# Overview
# Business
# Challenges
# AI Opportunities
# CEO Pitch

# But think about what each node actually needs.

# For example:

# Overview needs:
# company_name
# industry
# headquarters
# founded
# business_model
# products_services
# key_observations

# It probably doesn't need the full recent_news array.

# Business needs:
# business_model
# products_services
# technologies_used
# key_observations

# It doesn't need:

# headquarters
# employee_count
# founded
# CEO Pitch mainly needs:
# Overview
# Business
# Challenges
# AI Opportunities

# Not the raw evidence again.















# EVIDENCE_EXAMPLE = """
# {
#   "company_name": "Example Company",
#   "industry": "Financial Services",
#   "headquarters": "New York, USA",
#   "geographic_presence": [
#     "North America",
#     "Europe"
#   ],
#   "company_size": "Enterprise",
#   "employee_count": "12000",
#   "founded": "1998",
#   "products_services": [
#     "Retail Banking",
#     "Digital Payments",
#     "Business Lending"
#   ],
#   "business_model": "Provides financial products and earns revenue through banking services and transaction fees.",
#   "technologies_used": [
#     "Cloud",
#     "AI",
#     "Mobile Applications"
#   ],
#   "recent_news": [
#     {
#       "title": "Company launches AI assistant",
#       "summary": "The company introduced an AI-powered assistant for customer support.",
#       "source": "TechCrunch"
#     }
#   ],
#   "key_observations": [
#     "Strong digital presence",
#     "Expanding AI initiatives",
#     "Growing international operations"
#   ]
# }
# """

# OVERVIEW_EXAMPLE = """
# {
#   "summary": "Example Company is a global financial services provider focused on digital banking.",
#   "mission": "Deliver accessible financial services.",
#   "vision": "Become the world's leading digital bank.",
#   "target_market": [
#     "Consumers",
#     "Small Businesses",
#     "Enterprises"
#   ],
#   "competitive_position": "Strong market position with growing digital adoption.",
#   "strengths": [
#     "Large customer base",
#     "Strong brand",
#     "Advanced technology"
#   ]
# }
# """

# BUSINESS_EXAMPLE = """
# {
#   "core_operations": [
#     "Retail Banking",
#     "Commercial Banking",
#     "Digital Payments"
#   ],
#   "revenue_streams": [
#     "Interest Income",
#     "Subscription Services",
#     "Transaction Fees"
#   ],
#   "customer_segments": [
#     "Individuals",
#     "Businesses",
#     "Corporations"
#   ],
#   "value_proposition": "Secure and convenient financial services.",
#   "operational_workflow": [
#     "Customer Acquisition",
#     "Service Delivery",
#     "Customer Support"
#   ]
# }
# """

# CHALLENGES_EXAMPLE = """
# {
#   "challenges": [
#     {
#       "title": "Legacy Infrastructure",
#       "description": "Existing systems slow innovation and integration.",
#       "impact": "High"
#     }
#   ]
# }
# """

# AI_OPPORTUNITIES_EXAMPLE = """
# {
#   "opportunities": [
#     {
#       "title": "AI Customer Support",
#       "description": "Deploy conversational AI for customer service.",
#       "business_value": "Reduced support costs and faster response times.",
#       "implementation_complexity": "Medium",
#       "priority": "High"
#     }
#   ]
# }
# """

# CEO_PITCH_EXAMPLE = """
# {
#   "executive_summary": "AI adoption presents a significant opportunity to improve operational efficiency and customer experience while creating measurable business value.",
#   "recommended_ai_initiatives": [
#     "Deploy an AI-powered customer support assistant",
#     "Implement predictive analytics for operational planning",
#     "Automate repetitive internal workflows"
#   ],
#   "expected_business_impact": [
#     "Lower operational costs",
#     "Faster customer response times",
#     "Improved strategic decision-making"
#   ],
#   "recommended_first_step": "Launch a pilot AI customer support project and measure ROI before expanding to other business functions.",
#   "closing_statement": "A phased AI adoption strategy focused on high-impact initiatives will maximize business value while minimizing implementation risk."
# }
# """
