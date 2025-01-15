<div align="center">
  <h1>Nectere</h1>
  <p>An open-source framework for adding blockchain tools to your AI agent</p>
  <p>
    <a href="https://nectere.dev">Website</a>
    ·
    <a href="https://nectere.dev/">Documentation</a>
    ·
    <a href="https://x.com/necteresdk">Twitter</a>
  </p>
</div>

<div align="center">
  <a href="https://x.com/necteresdk">
    <img src="https://img.shields.io/twitter/follow/necteresdk?style=social" alt="Twitter Follow">
  </a>
</div>

## Overview

Nectere is a powerful framework that enables AI agents to interact with blockchain networks. With primary support for Solana and additional support for EVM chains, Nectere provides a unified interface for blockchain operations. Whether you're building a DeFi trading bot, an NFT analytics agent, or integrating blockchain capabilities into your existing AI system, Nectere makes it simple and efficient.

## Features

### 🌞 Solana First
- Deep integration with Solana's ecosystem
- Native SPL token operations
- NFT minting, trading, and metadata handling
- Integration with major Solana DeFi protocols
- Support for Solana Program interactions

### 🔗 Multi-Chain Support
- EVM chain compatibility (Base, Polygon, Mode)
- Cross-chain operations
- Unified interface across chains
- Smart contract interactions
- Token standards support (ERC20, ERC721, ERC1155)

### 🔌 Plugin System
- Extensible architecture
- Easy-to-write custom plugins
- Rich ecosystem of pre-built plugins
- Protocol-specific integrations
- Community-driven plugin repository

### 🤖 AI Integration
- Seamless integration with popular AI frameworks
- LangChain compatibility
- Vercel AI SDK support
- Custom agent implementation support
- Structured tool definitions

## Quick Start

```python
from nectere import SolanaWalletClient, get_tools
from nectere_plugins import JupiterPlugin, SPLTokenPlugin

# Initialize wallet and tools
wallet = SolanaWalletClient()
tools = get_tools(wallet, [
    JupiterPlugin(),
    SPLTokenPlugin()
])

# Use tools in your agent
await tools["swap_tokens"]({
    "token_in": "SOL",
    "token_out": "USDC",
    "amount": 1.0
})
```

## Installation

```bash
# Using pip
pip install nectere-sdk

# Using poetry
poetry add nectere-sdk

# Optional plugins
pip install nectere-sdk-plugin-jupiter nectere-sdk-plugin-spl-token
```

## Advanced Examples

### Custom Tool Creation
```python
from nectere import Tool
from pydantic import BaseModel, Field

class SwapParameters(BaseModel):
    token_in: str = Field(description="Token to swap from")
    token_out: str = Field(description="Token to swap to")
    amount: float = Field(description="Amount to swap")

@Tool({
    "name": "swap_tokens",
    "description": "Swap tokens using Jupiter",
    "parameters": SwapParameters
})
async def swap_tokens(params: dict) -> str:
    # Implement swap logic here
    return f"Swapped {params['amount']} {params['token_in']} for {params['token_out']}"
```

### LangChain Integration
```python
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_structured_chat_agent, AgentExecutor

# Initialize LLM and tools
llm = ChatOpenAI(model="gpt-4")
agent = create_structured_chat_agent(llm=llm, tools=tools, prompt=prompt)

# Create executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Execute
response = await agent_executor.invoke({
    "input": "Swap 1 SOL for USDC using Jupiter"
})
```

## Plugin Ecosystem

Nectere comes with a growing collection of plugins:

- **Jupiter Plugin**: DEX aggregator for optimal token swaps
- **SPL Token Plugin**: Solana token operations
- **Metaplex Plugin**: NFT operations and metadata
- **Marinade Plugin**: Liquid staking operations
- **ERC20 Plugin**: Standard token operations on EVM chains
- **Uniswap Plugin**: DEX operations on EVM chains
- **Coingecko Plugin**: Price data and market information
- **Defillama Plugin**: TVL and analytics data

## Documentation

For detailed documentation and examples, visit [nectere.dev](https://nectere.dev). Our documentation includes:

- Getting Started Guide
- API Reference
- Plugin Development Guide
- Best Practices
- Example Projects
- Troubleshooting Guide

## Community

- Follow us on [Twitter](https://x.com/necteresdk) for updates
- Star us on [GitHub](https://github.com/nectere-sdk/nectere) to show your support


## License

Nectere is licensed under the [MIT License](LICENSE).
