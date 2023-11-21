from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader
import openai, sys

CLIENT = openai.OpenAI(api_key="OPENAI_API_KEY")

def GenerateStory(client : openai.OpenAI) -> str:
    """
    Generates a short story using OpenAI's GPT-3.5 Turbo model.

    Parameters:
        client (openai.OpenAI): An instance of the openai.OpenAI class with the API key set.

    Returns:
        str: A string representing the generated short story.

    Raises:
        Exception: If an exception occurs during the API call, the function prints an error message and exits the application.
    """
    
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
    """
    Generates an audio file (MP3) by converting the text content of a given PDF file using OpenAI's TTS-1 model.

    Parameters:
        client (openai.OpenAI): An instance of the openai.OpenAI class with the API key set.
        filename (str): The name of the input PDF file (including extension) located in the root directory.

    Returns:
        None

    Raises:
        FileNotFoundError: If the input PDF file is not found, the function prints an error message and exits the application.
        Exception: If an exception occurs during the API call or file handling, the function prints an error message and exits the application.
    """
    
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
    """
    Generates a PDF file containing a short story and saves it in the output/ directory.

    Parameters:
        None

    Returns:
        None
    """
    
    pdf = canvas.Canvas(filename="output/output.pdf")
    pdf.drawString(10, 10, text=GenerateStory(client=CLIENT))
    pdf.save()
    print("A pdf containing the short story was saved to output/output.pdf!")

def main() -> None:
    """
    The main function that controls the user interaction loop.

    Parameters:
        None

    Returns:
        None
    """
    
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