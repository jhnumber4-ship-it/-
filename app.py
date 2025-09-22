import pandas as pd
import streamlit as st
from openai import OpenAi

client = OpenAi()

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

st.chat_message('ai').write(answer.choices[0].message.content)
        


