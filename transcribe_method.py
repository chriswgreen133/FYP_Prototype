import argparse
import os
import utils

# api_key == 0f5426b53f9548b0b2c3536a302bee24

def transcribe_audio(audio_file):
    try:
        # parser = argparse.ArgumentParser()
        # parser.add_argument('audio_file', help='url to file or local audio filename')
        # parser.add_argument('--local', action='store_true', help='must be set if audio_file is a local filename')
        # parser.add_argument('--api_key', action='store', help='<YOUR-API-KEY>')

        # args = parser.parse_args()

        # if args.api_key is None:
        #     args.api_key = os.getenv("AAI_API_KEY")
        #     if args.api_key is None:
        #         raise RuntimeError("AAI_API_KEY environment variable not set. Try setting it now, or passing in your "
        #                            "API key as a command line argument with `--api_key`.")

        # Create header with authorization along with content-type
        header = {
            'authorization': "0f5426b53f9548b0b2c3536a302bee24",
            'content-type': 'application/json'
        }

        # if args.local:
        #     # Upload the audio file to AssemblyAI
        #     upload_url = utils.upload_file(args.audio_file, header)
        # else:
        #     upload_url = {'upload_url': args.audio_file}

        print('upload_url')

        upload_url = utils.upload_file(audio_file, header)

        # Request a transcription
        transcript_response = utils.request_transcript(upload_url, header)

        print('transcript_response')

        # Create a polling endpoint that will let us check when the transcription is complete
        polling_endpoint = utils.make_polling_endpoint(transcript_response)

        print('polling_endpoint')

        # Wait until the transcription is complete
        utils.wait_for_completion(polling_endpoint, header)

        print('utils')

        # Request the paragraphs of the transcript
        paragraphs = utils.get_paragraphs(polling_endpoint, header)

        print('paragraphs')

        # Save and print transcript
        # with open('transcript.txt', 'w') as f:
        #     for para in paragraphs:
        #         print(para['text'] + '\n')
        #         f.write(para['text'] + '\n')

        return paragraphs
    except:
        return False