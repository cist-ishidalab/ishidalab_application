import streamlit as st


# Streamlit ページの設定
st.set_page_config(
    page_title="石田研究室アプリケーション",
    layout="wide",
    initial_sidebar_state="expanded"
)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# サイドバーにメッセージを表示
st.header("石田研究室アプリケーション")
st.write("石田研究室の研究活動を助けるアプリケーションです。")

st.write("左に表示されているサイドバーから行いたい分析項目を選択してください。")

st.subheader('各項目説明')

with st.expander("テキスト可視化アプリ"):
  st.markdown("""
    - アップロードされたcsvファイルの、選択した列のテキストを可視化・分析できる   
    - csvであればあらゆるcsvに対応したつもり  
  """)

with st.expander("ポータルアンケートCSV結合アプリ"):
  st.markdown("""
    - ポータルのアンケートの集計結果は設問別にCSVファイルが分かれていますが、それを一つのCSVに結合することができる      
    - ※学籍番号や氏名の列はこの2列を特別使う方以外は残さないで作業するよう注意してください。（石田先生より）        
  """)
