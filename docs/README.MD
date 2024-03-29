<div align="center">
    <img src="https://static.otta.com/uploads/images/company-logos/17023-r1fn8E7CIWJX0L-iFw8YivXD9C37itYuFvVWW_xFh5k.svg" width="50%" height="50%">
</div>
    
<p align="center">The open source repository for Mistral AI Discord chatbot.</p>

<div align="center">

<a href="https://github.com/ibnaleem/mistral-discord/stargazers"><img src="https://img.shields.io/github/stars/ibnaleem/mistral-discord.svg?style=for-the-badge"></a>
<a href="https://github.com/ibnaleem/gnupg-discord/blob/main/docs/LICENSE"><img src="https://img.shields.io/github/license/ibnaleem/mistral-discord?style=for-the-badge"></a>
</div>

## Invite Mistral AI:
```
https://discord.com/api/oauth2/authorize?client_id=1202215160954228766&permissions=0&scope=bot
```

## Purpose
Mistral Discord facilitates user interaction with the Large Language Model (LLM) through Discord chat functionality. Users can invite Mistral AI to their Discord server and engage in conversations immediately, equivalent to ChatGPT. Currently, Mistral's 7.3B parameter LLM can:
- Outperform Llama 2 13B on all benchmarks
- Outperform Llama 1 34B on many benchmarks
- Approach CodeLlama 7B performance on code, while remaining good at English tasks
- Use Grouped-query attention (GQA) for faster inference
- Use Sliding Window Attention (SWA) to handle longer sequences at smaller cost

([Mistral AI, 2024](https://mistral.ai/news/announcing-mistral-7b/))

Mistral Discord does not have any commands, though could in the future. Therefore, Mistral Discord does not require any permissions to function properly. It is recommended for admins to create a separate (no-permission) role for Mistral AI Discord and place it near the top of the server so server members can easily message the bot. 

## Privacy
This project does not collect or store your chats with Mistral AI; all chats are stored in random access memory (RAM) temporarily. See lines [9](https://github.com/ibnaleem/mistral-discord/blob/main/main.py#L9), [39](https://github.com/ibnaleem/mistral-discord/blob/main/main.py#L39), and [43](https://github.com/ibnaleem/mistral-discord/blob/main/main.py#L43) in [main.py](https://github.com/ibnaleem/mistral-discord/blob/main/main.py)

## Acknowledgements
- [Mistral AI](https://mistral.ai)
- [ollama/ollama-python](https://github.com/ollama/ollama-python)

## Support Server
```
https://discord.gg/JX4XgrQSeV
```
