import openai

openai.api_key = "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"

def whisper_api(file_path):
    try:
        file = open(file_path, "rb")
        transcription = openai.Audio.transcribe("whisper-1", file)

        print(transcription.text)
        return transcription.text
    except:
        return "Server Error"