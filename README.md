![PDF to Audiobook](https://github.com/Neill-Erasmus/pdf-to-audiobook/assets/141222943/95363980-491c-4d7c-a351-ef97b28b0fa9)

# pdf-to-audiobook

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Output](#output)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python script empowers you to transform short stories into engaging audiobooks effortlessly. Leveraging the capabilities of OpenAI's GPT-3 and TTS-1 models, the converter not only generates captivating short stories but also converts them into beautifully formatted PDFs and narrates them in audio format.

## Prerequisites

- OpenAI API Key
- Python 3 installed on your system

## Setup

Follow these simple steps to set up and run the PDF to Audiobook Convertor:

1. Clone the Repository
   ```bash
   git clone https://github.com/your-username/pdf-to-audiobook.git

2. Navigate to the Project Directory:
   ```bash
   cd pdf-to-audiobook

3. Install Required Packages:
   ```bash
   pip install -r requirements.txt

4. Set OpenAI API Key:
   ```bash
   export OPENAI_API_KEY="your-api-key"

## Usage

Running the script is straighforward. Follow these steps:

1. Execute the main script:
   ```bash
   python main.py

2. Respond to the prompt:
   - To generate a new story, PDF, and audiobook, type "Y".
   - To convert an existing PDF to an audiobook, type "N" and provide the PDF filename.

## Output

- PDF: The generated PDF is saved in the output/ directory.
- Audiobook (MP3): The audio rendition is saved in the output/ directory.

## Notes

- The generated story is limited to 4000 characters.
- Ensure the input PDF is in the root directory and spelled correctly.

## Contributing

Currently, contributions are not accepted for this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.