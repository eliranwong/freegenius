"""
ToolMate AI Plugin - search Tavily

search Tavily

[TOOL_CALL]
"""


from toolmate import config, getTavilyClient, print1

def search_tavily(function_args):
    query = function_args.get("query") # required
    config.currentMessages[-1] = {"role": "user", "content": query}
    context = getTavilyClient().get_search_context(query=query)
    config.stopSpinning()
    return context

functionSignature = {
    "examples": [
        "Search Tavily",
    ],
    "name": "search_tavily",
    "description": "Search Tavily for online information",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The original request in detail, including any supplementary information",
            },
        },
        "required": ["query"],
    },
}

config.addFunctionCall(signature=functionSignature, method=search_tavily)
config.inputSuggestions.append("Search Tavily: ")