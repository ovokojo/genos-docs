# Genos Docs

⚡️ Quickly deploy an intelligent search engine for your private documentation.

We are developing open-source infrastructure to simplify the creation of chat interfaces for proprietary data. 

Our vision is a future where people and organizations can effortlessly upload their data, configure privacy settings, select language models, and swiftly deploy chat interfaces tailored to their needs.


##  Application Overview

Genos Docs is a Python web app built using robust open source frameworks that enable rapid prototyping. This approach to building an intelligent search engine prioritizes speed and simplicity.

### Core Technologies
- [Python](https://www.python.org/): The primary programming language used for both frontend and backend.
-  [Streamlit](https://streamlit.io/): A faster way to build & share data apps.
- [LlamaIndex](https://www.llamaindex.ai/): A data framework for LLM-based applications to ingest, structure, and access private or domain-specific data.
- [Chroma](https://docs.trychroma.com/): An AI-native vector database.

## Getting Started

1. Ensure you have Python 3.12 or later installed on your system.
2. Clone the repository.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Shell Scripts

- Use `./run.sh` in the root folder to run the Streamlit app

## 📝 Contributing

- See `CONTRIBUTIONS.md` file for details on how to contribute to this project.

## Troubleshooting

If you encounter type-related errors or unexpected behavior, please ensure you're using Python 3.12 or later. Earlier versions, especially Python 3.10 and below, may not be fully compatible with all features used in this project.

## Future Developments

We're continuously working on improving Genos Docs. Future updates may include:
- Enhanced privacy settings
- Support for multiple language models
- Improved data ingestion and processing capabilities

Stay tuned for more updates!