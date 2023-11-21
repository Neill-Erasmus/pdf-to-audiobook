from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader
import openai, sys

CLIENT = openai.OpenAI(api_key="OPENAI_API_KEY")

def GenerateStory(client : openai.OpenAI) -> str:
    try:
        response            = client.chat.completions.create(
            model           = "gpt-3.5-turbo-1106",
            response_format = {"type":"text"},
            messages =[
                {"role" : "system", "content": "You are en english writer specializing in short stories."},
                {"role" : "user",   "content": "Write a short story consisting of not more than 4000 characters."}
            ]
        )
        return str(response.choices[0].message.content)
    except Exception as e:
        print(f"An exception {e} occured!")
        sys.exit(0)

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
    response.stream_to_file("output/output.mp3")
    print("A mp3 file narrating the short story has been saved to output/output.mp3!")
    sys.exit(0)

def CreatePDF() -> None:
    pdf = canvas.Canvas(filename="output/output.pdf")
    pdf.drawString(10, 10, text=GenerateStory(client=CLIENT))
    pdf.save()
    print("A pdf containing the short story was saved to output/output.pdf!")

def main() -> None:
    while True:
        prompt : str = input("Would you like to generate a story? (Y/n): ").lower()
        if prompt == "y":
            CreatePDF()
            GenerateAudio(client=CLIENT, filename="output/output.pdf")
        elif prompt == "n":
            while True:
                file = input("Enter the name of your file and ensure that it is in the root directory (example.pdf): ")
                try:
                    GenerateAudio(client=CLIENT, filename=file)
                except FileNotFoundError:
                    print("The file was not found! Ensure that you spelt it correctly and that it is in the correct directory.")
        else:
            print('Invalid Input! Type "Y" for Yes or "N" for No.')

if __name__ == "__main__":
    main()