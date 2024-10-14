# TTS_STT_using_LLM-s-Complete-Converstational-Chatbot

This project implements a complete conversational chatbot that mimics human-like conversation. The chatbot allows users to communicate via voice messages, receiving voice replies in return. It integrates advanced Speech-to-Text (STT) and Text-to-Speech (TTS) technologies to enable seamless voice interactions. Additionally, the chatbot is powered by Google Generative AI (Gemini 1.5 Pro) for intelligent, context-aware responses.

## Features

- **Voice Input and Output**: Users can send voice messages, and the chatbot replies with synthesized voice using `gTTS`.
- **STT and TTS Integration**: Utilizes `speech_recognition` for speech-to-text conversion and `gTTS` for text-to-speech synthesis.
- **Real-time Conversations**: The chatbot maintains conversation history, ensuring responses are relevant and contextually aware.
- **LLM-Driven Responses**: The system uses Google Generative AI (Gemini 1.5 Pro) through Langchain to generate concise and natural responses, focusing on speech-friendly formatting.

## Technologies Used

- **Google Generative AI (Gemini 1.5 Pro)**: For intelligent response generation.
- **gTTS (Google Text-to-Speech)**: For converting text responses to speech.
- **SpeechRecognition**: For capturing and transcribing user speech.
- **Pygame**: For handling audio playback.
- **Langchain**: To manage prompt templates and chain the LLM with conversation history.
