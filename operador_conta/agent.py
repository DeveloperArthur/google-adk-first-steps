from google.adk.agents import Agent
from .tools import listar_faturas, cancelar_assinatura, consultar_assinatura
from .prompt import prompt

root_agent = Agent(
    name="operador_conta",
    instruction=prompt,
    model="gemini-3.5-flash-lite",
    tools=[
        listar_faturas, 
        consultar_assinatura,
        cancelar_assinatura
    ]
)