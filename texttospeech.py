from googletrans import Translator
from gtts import gTTS

def translate_and_text_to_speech(text, src_lang='en', dest_lang='kn', slow=False):
    try:

        translator = Translator()
        translated_text = translator.translate(text, src=src_lang, dest=dest_lang)

        language = dest_lang
        text_to_speak = translated_text.text

        text_segments = text_to_speak.split('. ')
        audio_filenames = []

        for idx, segment in enumerate(text_segments):
            speech = gTTS(text=segment, lang=language, slow=slow)
            audio_filename = f'segment_{idx + 1}.mp3'
            speech.save(audio_filename)
            audio_filenames.append(audio_filename)

        return audio_filenames

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    text_to_translate = """Any content you upload to our Site will be considered non-confidential and non-proprietary.
      You retain all of your ownership rights in your content, but by providing content to the Site,
        you are granting us and other users permission to use that content for the purposes that it is provided,
          including publishing the content on the Site and as otherwise permitted in accordance with these Terms."""

    audio_files = translate_and_text_to_speech(text_to_translate, src_lang='en', dest_lang='kn', slow=False)

    if audio_files:
        print("Audio files saved:")
        for filename in audio_files:
            print(filename)
