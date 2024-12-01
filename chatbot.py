import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

#Front-end 

st.set_page_config(page_title="Watch&Read Buddy")

st.title("Welcome Watch&Read Buddy!")
st.subheader("Discover books, movies, and series tailored to your favorite picks!")
st.subheader("📺  🎬 🎞  📚 ")
st.write("""
    Girdiğiniz kitap, film ya da diziye göre size benzer içerikler öneriyoruz.
    Örneğin, Hamlet seviyorsanız Shakespeare tarzında başka bir eser ya da onun temalarını işleyen bir film/dizi önerisi alabilirsiniz.
    Başlamak için favori bir eser ismi yazın!
""")

#LLM part


@st.cache_resource
def gemini_response(prompt):
    generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
            }

    model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            )
    response = model.generate_content(prompt)

    return response

##text_area widgetını dene 
user_input = st.text_input("En sevdiğiniz kitap, film veya dizi hangisi? 😉")

if user_input is not None and user_input != "":
                with st.spinner(text="Öneriler hazırlanıyor..."):
                        prompt = f"""
                        Sen sinema, televizyon ve edebiyat dünyasındaki her eser hakkında bilgiye sahip bir uzmansın. 
                        Kullanıcı sevdiği türü ya da sevdiği eseri verdi: "{user_input}". 
                        Bu esere benzer temalara, yazarlara veya türlere göre kitap, film ve dizi önerisi yap. 
                        Kullanıcının sevdiği temaya göre diğer kategorilerdeki arkadaş canlısı bir tavır ile önerilerini yazdır.
                        Kullanıcı eksik input girmiş olabilir, harfe basıp enter demiş olabilir, kontrol et.
                        Eğer eksik bir input ise "lütfen bana sevdiğin eseri tam olarak söyle yoksa sana yardımcı olamam" uyarı mesajını ver
                        
                        """
                        response = gemini_response(prompt)
                        #st.success("İşte önerileriniz hazır!")
                        st.write(response.text)
