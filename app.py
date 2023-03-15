from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from werkzeug.utils import secure_filename
import os
import asyncio, json

import transcribe_method
import whisper

import openai

openai.api_key = "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"

app = Flask(__name__)

global page1, page2, page3
page1 = True
page2 = False
page3 = False

MIMETYPE = 'audio/wav'

@app.route("/transcribe", methods=["GET", "POST"])
async def transcribe():
    global page1, page2, page3

    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            # recognizer = sr.Recognizer()
            # audioFile = sr.AudioFile(file)
            # with audioFile as source:
            #     data = recognizer.record(source)
            # transcript = recognizer.recognize_google(data, key=None)

            file.save(file.filename)
            filepath = file.filename

            # file1 = open(filepath, "rb")
            # transcript = openai.Audio.transcribe("whisper-1", file1)
            # print(transcript.text)

            # file.save(file.filename)

            # audio = open('./{}'.format(file.filename), 'rb')

            # print('========== Filename ==========')
            # print(file.filename)
            # print('./{}'.format(file.filename))
            # print(request.files['file'].file.name)

            # # Set the source
            # source = {
            #     'buffer': audio,
            #     'mimetype': MIMETYPE
            # }

            # # source = {'url': AUDIO_URL}
            # source = {'url': file.filename}
            # options = { "punctuate": True, "model": "general", "language": "en-GB", "tier": "base" }
            # # response = dg_client.transcription.prerecorded(source, options)
            # response = await asyncio.create_task(
            #     dg_client.transcription.prerecorded(
            #         source, options
            #     )
            # )
            # print('================ Response ================')
            # # print(response)
            # print(json.dumps(response, indent=4))

            # result = transcribe_method.transcribe_audio('./{}'.format(file.filename))
            transcript = whisper.whisper_api(filepath)

            # if result:
            #     print('====== result =========')
            #     transcript = result
            #     print(transcript)

    return render_template('index.html', page1=page1, page2=page2, page3=page3, transcript=transcript)


@app.route("/", methods=["GET", 'POST'])
def index():
    global page1, page2, page3
    page1 = True
    page2 = False
    page3 = False
    return render_template('index.html', page1=page1, page2=page2, page3=page3);

@app.route("/page2", methods=["GET", 'POST'])
def page2():
    global page1, page2, page3
    page1 = False
    page2 = True
    page3 = False
    return render_template('index.html', page1=page1, page2=page2, page3=page3);

@app.route("/page3", methods=["GET", 'POST'])
def page3():
    global page1, page2, page3
    page1 = False
    page2 = False
    page3 = True
    return render_template('index.html', page1=page1, page2=page2, page3=page3);

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
