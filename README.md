# i18n_translate_tool

`i18n_translate_tool` is a sophisticated utility designed to facilitate the translation of internationalization (i18n) JSON files. It leverages both the DeepL and Google Translate APIs for comprehensive and accurate translations. This tool is invaluable for developers and content creators working on multilingual applications or websites, offering an efficient and streamlined translation workflow.

## Features

- **DeepL and Google Translate Integration**: Uses the DeepL API for high-quality translations and Google Translate as a fallback for languages not supported by DeepL.
- **Selective Translation Logic**: Employs smart logic to use Google Translate for shorter texts, optimizing translation quality.
- **Batch Translation Capability**: Allows for the translation of multiple files simultaneously, greatly enhancing productivity.
- **User-Friendly GUI**: Features a simple and intuitive graphical user interface, making it accessible for users of all skill levels.
- **Robust Error Handling**: Includes comprehensive error handling to ensure smooth operation and ease troubleshooting.
- **Character Count Functionality**: Counts the number of characters to be translated, aiding in the management of API usage and limits.
- **Language Support Check**: Verifies the supported languages for both DeepL and Google Translate, ensuring accurate translations.

## Upcoming Integration

`i18n_translate_tool` is poised to integrate with Nordtools, significantly broadening its range of features and incorporating it into a more extensive toolkit for developers.

## Installation

Clone this repository to get started with `i18n_translate_tool`:

```bash
git clone https://github.com/Juliusolsson05/i18n_translate_tool.git
```

## Dependencies

- Python 3.x
- `requests` library for Python
- `tkinter` for the GUI interface

Install the necessary Python packages using pip:

```bash
pip install requests
```

For `tkinter`, please refer to its [installation guide](https://tkdocs.com/tutorial/install.html), as the installation process can vary depending on your operating system.

## Usage

1. **Launch the Tool**: Execute the `i18n_translate_tool` script.
   ```bash
   python script.py
   ```
2. **Input API Keys**: When prompted, enter your DeepL API key and, if necessary, your Google Translate API key.
3. **Choose i18n Folder**: Select the folder containing your i18n JSON files.
4. **Initiate Translation**: Click the "Calculate Characters and Translate" button to start the translation.

## Contributing

We encourage contributions to `i18n_translate_tool`! Feel free to submit pull requests or open issues for enhancements or bug fixes.

## License

This project is under the [MIT License](LICENSE).

## Note

While this tool currently operates independently, it will soon be part of Nordtools, offering a more comprehensive set of tools for developers.

## TODO

1. ☑  Add so that you can write what key to start from
2. ☑  Add so that DeepL is not used for sentances with less then 4 words, becuase DeepL is bad at straight word translation, use Google Cloud Translate for this instead.
3. ☑  Add a DeepL clean up mode for the translations that has already been made before the >4 word logic
4. ☐  Add a CLI mode aswell
5. ☐  Write so that you can choose between using the GUI or the CLI 
6. ☐  Publish the tool on PIP and maybe node?  
