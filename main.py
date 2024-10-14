import speech_recognition as sr
import keyboard
from gtts import gTTS
import pygame
import io
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain



pygame.mixer.init()
language = "en"
text = ""
history = ""
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
base_prompt = """You are a helpful AI Assistant, just answer the user questions in a friendly manner, just keep the answer very consice and short, dont use any emojis, here im using your response as speech so focus on giving the text in more speech format
                This is our conversation so far.. {conversation_history}
                User Query: {query}
                Response:
               """
prompt_template1 = PromptTemplate(
    input_variables=["conversation_history", "query"],
    template=base_prompt,
)
llm_chain1 = LLMChain(llm=llm, prompt=prompt_template1)



while True:
    if keyboard.is_pressed('q'):
        print("Exiting...")
        break
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("litsening..")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Transcription - ", text)
    except:
        print("no audio")
    if text:
        history += text
        response = llm_chain1.run({"conversation_history": history,"query": text})
        print("yea text is there")
        speech = gTTS(text=response, lang=language, slow=False, tld="co.in")
        speech_buffer = io.BytesIO()
        speech.write_to_fp(speech_buffer)
        speech_buffer.seek(0)
        pygame.mixer.music.load(speech_buffer, 'mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        history += response
        text = None
    else:
        continue
    if keyboard.is_pressed('q'):
        print("Exiting...")
        break
