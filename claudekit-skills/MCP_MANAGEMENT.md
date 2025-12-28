# No more context bloat with "mcp-manager" subagent + "mcp-management" skills!

When I finished reading [Anthropic’s “Code execution with MCP” article](https://www.anthropic.com/engineering/code-execution-with-mcp), a sudden idea flashed in my mind

As many people may already know, subagents have their own context windows, while using MCP as it currently does will bloat the main context (anyone who has used Chrome Devtools MCP or Playwright MCP knows how much their tools consume context from the start)

So then: **why don’t we load all MCP into the subagent’s context?**

*I tested it immediately...*

The idea is very simple: **“mcp-manager” subagent + “mcp-management” skills**

1/ **“mcp-management” skills** will have script snippets to initialize MCP Client from “.claude/.mcp.json” (I move the “.mcp.json” file here so the main agent doesn’t load them into context from the start)

2/ **“mcp-manager” subagent** is equipped with **“mcp-management” skills**

Whenever needing to call a tool -> summon “mcp-manager” subagent -> activate “mcp-management” skills -> load MCP servers -> subagent receives list of tools & analyzes to select the tool to use -> call tool & receive result -> return it back to main agent

***Voilà!***

Main context stays pristine and clean even if you use 80 MCP servers 👌

Look at this image and you’ll understand better:

![No more context bloat with "mcp-manager" subagent + "mcp-management" skills](https://github.com/mrgoonie/claudekit-skills/blob/main/assets/mcp-management.jpeg?raw=true)

Actually, after that I upgraded it a bit, because processing such a large number of MCP servers tools, while not polluting the main context, still… consumes tokens, leading to quickly hitting the limit.

So I transferred that MCP processing part to… `gemini-cli` 😂​​​​​​​​​​​​​​​​

I think Anthropic should adopt this approach as default, oc without the "gemini" part.

Apparently it's already available in [ClaudeKit.cc](https://claudekit.cc) 😁

If you find this useful, please support my project:
[![ClaudeKit Agent Skills](https://github.com/mrgoonie/claudekit-skills/blob/main/claudekit.png?raw=true)](https://claudekit.cc)

Cheers,
@mrgoonie