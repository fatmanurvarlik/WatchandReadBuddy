# Watch & Read Buddy  

Bu proje, UP School - First AI Developer programı Capstone projesi kapsamında yapılmıştır. Text-to-text llm çalışması örneğidir.

Watch & Read Buddy, kişinin okuduğu kitap ya da izlediği film/dizi temasına göre diğer kategorilerde öneri sunan bir chatbottur.

• Proje, 'pyhton' dili ile hazırlanmıştır.

• Google Gemini API kullanılmıştır. 

• Streamlit kütüphanesinden faydalanılmıştır. 

**NOT: Daha iyi sonuç almak için prompt iyileştirmesi yapılmış chatbot_v.2.py dosyası olarak eklenmiştir. Bu versiyona ait sonuçlar aşağıdaki görsellerde yer almamaktadır!**

![](https://github.com/fatmanurvarlik/WatchandReadBuddy/blob/main/G%C3%B6rseller/Chatbot.png)

## Projeye Dair Videolar

Chatbotun kullanım şeklide dair videoları linkten izleyebilirsiniz: 
        https://drive.google.com/drive/folders/1JEK9AoSsPeYyKXopWmYCbrt5WayTk_34?usp=sharing


## Gerekli Kütüphaneler

```
import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

```
## Projeye Dair Görseller

Watch & Read Buddy chatbotuna dair görseller aşağıdaki gibidir. Kişinin girdiği inputa göre verdiği cevaplar için ipucu olması adına paylaşılmıştır, görseldeki promptlardan ve linkte paylaşılan videolardan yararlanarak chatbotu deneyebilirsiniz.

Chatbota ne kadar iyi bir prompt girerseniz o kadar iyi sonuç ürettiğini unutmayınız. 

![](https://github.com/fatmanurvarlik/WatchandReadBuddy/blob/main/G%C3%B6rseller/Chatbot_1.png)

İstenilen sonuca ulaşmak için örnek bir prompt.

![](https://github.com/fatmanurvarlik/WatchandReadBuddy/blob/main/G%C3%B6rseller/Chatbot_2.png)

Eksik bir prompt girdiğimizde cevaba bir örnek.

![](https://github.com/fatmanurvarlik/WatchandReadBuddy/blob/main/G%C3%B6rseller/Chatbot_3.png)

Sadece tema bilgisi girdiğimizde de istediğimiz sonucu alamayız.

![](https://github.com/fatmanurvarlik/WatchandReadBuddy/blob/main/G%C3%B6rseller/Chatbot_4.png)

