import streamlit as st
import speech_recognition as sr

# Function to recognize Hindi speech
def recognize_hindi_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("कृपया बोलें...")
        # Adjust for ambient noise and record
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        st.write("आपकी आवाज़ को सुन लिया गया है, कृपया प्रतीक्षा करें...")

        try:
            # Use Google Speech Recognition for Hindi
            text = r.recognize_google(audio, language='hi-IN')
            st.success(f"आपने कहा: {text}")
        except sr.UnknownValueError:
            st.error("स्पीच को समझा नहीं जा सका। कृपया पुनः प्रयास करें।")
        except sr.RequestError:
            st.error("Google Speech Recognition API से अनुरोध में त्रुटि।")

def main():
    st.set_page_config(page_title="Hindi Voice Input App", layout="wide")
    st.title("हिंदी वॉयस इनपुट ऐप")

    if st.button("माइक से बोलें"):
        recognize_hindi_speech()

if __name__ == "__main__":
    main()
