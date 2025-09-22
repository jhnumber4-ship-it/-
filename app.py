import base64
import streamlit as st
from openai import OpenAI

client = OpenAI()

audio = st.audio_input('음성을 입력하세요')

if audio:
    button = st.button('음성 인식 시작')
    if button :
        user_script = client.audio.transcriptions.create(
            model = 'whisper-1',
            file = audio
            )
        st.chat_message('user').write(user_script.text)

        answer = client.chat.completions.create(
            model = 'gpt-4o',
            messages = [{'role':'user','content':user_script.text}]
            )
        answer_text = answer.choices[0].message.content
        st.chat_message('ai').write(answer_text)

        answer_text-to-audio = client.audio.speech.create(model = 'tts-1', voice = 'nova', input = answer_text)

        b64_audio = base64.b64encode(answer_text-to-audio.content).decode()

        st.html(
            f'''<audio autoplaystyle = "display:none">
                <source src = "data:audio/mp3; base64, (b64_audio)" type= "audio/mp3">
                </audio>
            ''')
        
            
                

        
        


