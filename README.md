# ToolMate AI

ToolMate AI, formerly known as FreeGenius AI, is a cutting-edge AI companion that seamlessly integrates agents, tools, and plugins to excel in conversations, generative work, and task execution. With the ability to perform multi-step actions, users can customize workflows to tackle complex projects with ease.

![ToolMateAI](https://github.com/user-attachments/assets/64525e6c-0e01-4316-bd3e-06c1f06ec5dd)

# Background

https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/LetMeDoIt%20Mode.md

# Documentation

https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/000_Home.md

# Latest changes

https://github.com/eliranwong/toolmate/blob/main/latest_changes.md

# Supported Platforms

Windows, macOS, Linux, ChromeOS, Android (upcoming)

# AI Backends and Models

ToolMate AI supports a wide range of AI backends and models, including [Ollama, Llama.cpp, Llama-cpp-python (default), Groq Cloud API, OpenAI API, and Google Gemini via Vertex AI](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Supported%20Backends%20and%20Models.md). Llama-cpp-python is selected as the default backend because it is completely free and requires no additional setup. However, users can switch backends at any time.

Our recommendations:
* For backend selection, we consider [Ollama](https://ollama.com/) as the best friendly free `offline` option and [Groq Cloud API](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Groq%20API%20Setup.md) as the best freiendly and free `online` option.
* Regarding AI models, we have found that `wizardlm2` and `mixtral` work well with ToolMate AI, though many others are well-supported.

Read more at https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Supported%20Backends%20and%20Models.md

# Distinctive Features

[NEW! Tool Selection Agent](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Tool%20Selection%20Configurations.md)

[NEW! Deep Reflection Agents](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Reflection%20Agents.md)

[NEW! Risk Management Agent](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Risk%20Management%20Agent.md)

[NEW! Running Multiple Tools in One Go](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Running%20Multiple%20Tools%20in%20One%20Go.md)

[Plentiful Built-in Tools](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Tool%20Descriptions.md)

[Highly Customisable Plugins](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/000_Home.md#plugins)

[Savable, Searchable and Sharable Records](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Chat%20Record%20Management.md)

[Integration with Popular AI Tools](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/000_Home.md#integration)

# Quick Tool Calling

Starting with version 0.2.86+, users can utilize the `@` symbol to designate a specific tool within the application. The `toolmate` package now comes with a suite of pre-built tools:

@add_google_calendar_event @add_outlook_calendar_event @analyze_audio @analyze_files @analyze_images_chatgpt @analyze_images_gemini @analyze_images_llamacpp @analyze_images_ollama @analyze_web_content @append_command @append_fabric @append_instruction @ask_chatgpt @ask_codey @ask_gemini @ask_groq @ask_llama3_1 @ask_llamacpp @ask_llamacppserver @ask_ollama @ask_palm2 @build_agents @chat @command @context @convert_relative_datetime @copy_to_clipboard @correct_python_code @create_image_dalle3 @create_image_sd @create_map @create_qrcode @create_statistical_graphics @datetimes @deep_reflection @download_web_content @download_youtube_audio @download_youtube_video @execute_computing_task @extract_python_code @fabric @improve_writing @install_package @integrate_google_searches @list_current_directory_contents @load_conversations @modify_images @open_browser @paste_from_clipboard @pronunce_words @recommend_tool @reflection @remove_image_background @retrieve_memory @run_python_code @save_memory @search_conversations @search_finance @search_latest_news @search_sqlite @search_weather_info @send_gmail @send_outlook @send_tweet @workflow

For those interested in expanding the capabilities of ToolMate AI, [custom tools can be added to the system via plugins](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Plugins%20-%20How%20to%20Write%20a%20Custom%20Plugin.md).

Tips: 

* Type the `@` symbol to launch a drop-down menu listing all available tools for selection..
* Enter the `@` symbol to display a list of all available tools and their descriptions
* `@chat` is regarded as a single tool.  If you just want a direct response generated by LLM, simply use `@chat`.
* `@execute_computing_task` is like a magic tool designed to execute computing tasks upon user requests.
* `@recommend_tool` is designed to help users to find an appropriate tool to resolve a given request.

# Selectie Screenshots

## Brand New Tool Selection Agent

![tool_selection_agent_compressed](https://github.com/user-attachments/assets/c963ca48-cb01-4eb7-b40d-57e2a4a92eaf)

[Read more ...](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Tool%20Selection%20Configurations.md)

## Multiple Tools in One Go

From version 0.2.87+, ToolMate AI supports use of multiple tools in a single request. It enables individual tools to work on results, generated by running previous tools.

![multiple_tools_in_single_prompt](https://github.com/user-attachments/assets/7bdc63cd-beca-44c9-bfb0-27596a5e0632)

Read more at: https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Running%20Multiple%20Tools%20in%20One%20Go.md

## Customizable Plugins

![plugins](https://github.com/eliranwong/toolmate/assets/25262722/6bb4b2f6-5684-42c1-95e3-7b12c3a38db6)

## System Command and Fabric Integration

System Command Integration: https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/System%20Command%20Integration.md

Fabric Integration: https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Fabric%20Integration.md

## Support GPU Offloading

![llamacpp_with_gpu_offloading_compressed](https://github.com/eliranwong/toolmate/assets/25262722/2d607fc1-e6b5-4c62-be14-325d73866fce)

## Access to Real-time Data

![realtime_information](https://github.com/eliranwong/toolmate/assets/25262722/d94fd9c3-f242-4c8c-8564-308f866e9adb)

## Access to Device Information

![access_device_information](https://github.com/eliranwong/toolmate/assets/25262722/6e3386a4-7314-4ce5-a64f-fffe35dff92e)

## Task Execution

![toolmate_ai_screenshot](https://github.com/eliranwong/toolmate/assets/25262722/1e9dd18e-aa4b-4e2c-8d76-386af7ba00ea)

## Content Creation

![content_creation](https://github.com/eliranwong/toolmate/assets/25262722/5582d519-b925-4e1b-8fd8-ecaa8422d391)

# Installation - an example

Install ToolMate AI, by running:

To set up virtual environment (recommended):

> mkdir -p ~/apps/toolmate

> cd ~/apps/toolmate

> python3 -m venv toolmate

> source toolmate/bin/activate

To install:

> pip install --upgrade toolmate

To set up an alias:

> echo "alias toolmate=~/apps/toolmate/bin/toolmate" >> ~/.bashrc

Remarks: Auto-upgrade is supported in macOS and Linux versions, but not in Windows version.  Windows users need to manually upgrade to get the latest features.

To run:

> toolmate

To start up with a particular backend, you may use parameter `-b`, e.g.:

> toolmate -b groq

Read more at https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/000_Home.md#installation

# GPU Acceleration

[GPU Acceleration](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/GPU%20Acceleration.md)

[GPU Acceleration with Llama.cpp Server](https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/GPU%20Acceleration%20with%20Llama_cpp%20server.md)

# Quick Guide

https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/Quick%20Guide.md

# More

Documentation https://github.com/eliranwong/toolmate/blob/main/package/toolmate/docs/000_Home.md

# Welcome Contributions

You are welcome to make contributions to this project by:

* joining the development collaboratively

* donations to show support and invest for the future

Support link: https://www.paypal.me/letmedoitai

Please kindly report of any issues at https://github.com/eliranwong/toolmate/issues
