from typing import List, TypeVar, Any

from langchain_core.tools import BaseTool
from langchain_core.tools.structured import StructuredTool
from nectere import ToolBase, WalletClientBase, get_tools


def get_on_chain_tools(wallet: WalletClientBase, plugins: List[Any]) -> List[BaseTool]:
    """Create LangChain tools from Nectere tools.

    Args:
        wallet: A wallet client instance
        plugins: List of plugin instances

    Returns:
        List of LangChain Tool instances configured with the Nectere tools
    """
    tools: List[ToolBase] = get_tools(wallet=wallet, plugins=plugins)

    def _execute_tool(t: ToolBase, **args):
        return t.execute(args)

    langchain_tools = []
    for t in tools:
        # Create a LangChain Tool for each Nectere tool
        tool = StructuredTool(
            name=t.name,
            description=t.description,
            func=lambda t=t, **args: _execute_tool(t, **args),
            args_schema=t.parameters,
        )
        langchain_tools.append(tool)

    return langchain_tools
