from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader
import openai, sys

CLIENT = openai.OpenAI(api_key="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")

def GenerateStory(client : openai.OpenAI) -> str:
    response            = client.chat.completions.create(
        model           = "gpt-3.5-turbo-1106",
        response_format = {"type":"text"},
        messages =[
            {"role" : "system", "content": "You are en english writer specializing in short stories."},
            {"role" : "user",   "content": "Write a short story consisting of not more than 4000 characters."}
        ]
    )
    return str(response.choices[0].message.content)

def GenerateAudio(client : openai.OpenAI, filename : str) -> None:
    text : str = ""
    for page in PdfReader(filename).pages:
        text += page.extract_text()
    try:
        response  = client.audio.speech.create(
            model = "tts-1",
            voice = "alloy",
            input = text
        )
    except Exception as e:
        input(f"An exception {e} was raised. Press any key to exit the application...")
        sys.exit(0)
    response.stream_to_file("output.mp3")

def main() -> None:
    pass

if __name__ == "__main__":
    main()