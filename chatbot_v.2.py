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

#user_input = st.text_input("En sevdiğiniz kitap, film veya dizi hangisi? 😉")
user_input = st.text_area("En sevdiğiniz kitap, film veya dizi hangisi? 😉")

if user_input is not None and user_input != "":
                with st.spinner(text="Öneriler hazırlanıyor..."):
                        prompt = f"""
                                Sen sinema, televizyon ve edebiyat dünyasındaki tüm eserler hakkında derin bilgiye sahip bir uzmansın. 
                                Kullanıcı, sevdiği bir tür, tema ya da eseri belirtti: "{user_input}". 

                                Senin görevin, bu girdiye dayanarak kullanıcının ilgisini çekebilecek, benzer temalara, yazarlara veya türlere sahip 
                                kitap, film ve dizi önerileri sunmak. 
                                - Eğer kullanıcı net bir eser veya tema belirtmişse, bu bilgiye dayanarak önerilerini yaz.
                                - Eğer kullanıcı eksik veya belirsiz bir bilgi girdiyse, tahmin yürüterek ona yardımcı ol. Örneğin, "Daha detaylı bilgi verirsen, önerilerimi geliştirebilirim!" diyebilirsin.

                                Önerilerini arkadaş canlısı, samimi bir üslupla yaz. Kullanıcının keşfetmekten keyif alacağı türden içerikler öner.

                                Eğer kullanıcı yalnızca boş bir mesaj ya da anlamlı olmayan bir giriş yaptıysa, şu mesajı ver:
                                "Lütfen bana sevdiğin bir eser, tema ya da tür hakkında biraz daha bilgi verir misin? Sana harika önerilerde bulunmak istiyorum! 😊"

                                Hazır olduğunda önerilerini kullanıcıya sun.
                                """
                        response = gemini_response(prompt)
                        #st.success("İşte önerileriniz hazır!")
                        st.write(response.text)
