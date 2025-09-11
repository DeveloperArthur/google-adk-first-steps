from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import google_search

from .prompt import prompt

#instanciando um objeto da classe Agent
root_agent = Agent(
    name="previsao_do_tempo",
    # em um sistema multiagente, quando o agente principal precisar
    # identificar qual agente chamar, ele usará essa descrição, semelhança
    description="Agente para previsão do tempo",
    model=LiteLlm(model="ollama/gemma3:12b"),
    instruction=prompt,
    tools=[google_search],
)