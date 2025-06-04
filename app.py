import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=openai_api_key
)

expert_prompts = {
    "旅行プランナー": "あなたは優秀な旅行プランナーです。ユーザーの希望に合わせて最適な旅行プランを提案してください。",
    "栄養士": "あなたはプロの栄養士です。健康的な食事や栄養に関するアドバイスを的確に行ってください。",
    "キャリアコンサルタント": "あなたは経験豊富なキャリアコンサルタントです。キャリア相談に適切に助言してください。"
}

st.title("サンプルアプリ③: 専門家LLMアプリ")

st.write("##### 各専門家に相談できます")

selected_item = st.radio(
    "専門家を選択してください。",
    list(expert_prompts.keys())
)

st.divider()

user_input = st.text_area("相談内容を入力してください。")

if st.button("実行"):
    st.divider()

    if user_input:
        system_message = SystemMessage(content=expert_prompts[selected_item])
        user_message = HumanMessage(content=user_input)
        response = llm.invoke([system_message, user_message])
        st.write(f"AIの回答: {response.content}")
    else:
        st.error("相談内容を入力してください。")
