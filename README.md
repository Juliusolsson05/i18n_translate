# i18n_translate_tool

`i18n_translate_tool` is a powerful utility designed to streamline the process of translating internationalization (i18n) JSON files. It leverages the DeepL API for accurate translations and falls back on Google Translate for languages not supported by DeepL. This tool is especially useful for developers and content creators working on multilingual applications or websites, ensuring a seamless and efficient translation workflow.

## Features

- **DeepL Translation**: Utilizes the DeepL API for high-quality translations.
- **Google Translate Fallback**: Automatically uses Google Translate for languages not supported by DeepL.
- **Batch Translation**: Enables translation of multiple files at once, saving time and effort.
- **User-Friendly GUI**: Simple and intuitive graphical user interface for ease of use.
- **Error Handling**: Robust error handling for smooth operation and troubleshooting.

## Future Integration

`i18n_translate_tool` is set to be merged with Nordtools, further expanding its capabilities and integrating it into a suite of useful tools for developers.

## Installation

To get started with `i18n_translate_tool`, clone this repository to your local machine:

```bash
git clone https://github.com/Juliusolsson05/i18n_translate_tool.git
```

## Dependencies

- Python 3.x
- `requests` library for Python

You can install the required Python package using pip:

```bash
pip install requests
```

## Usage

1. **Start the Tool**: Run the `i18n_translate_tool` script.
   ```bash
   python script.py
   ```
2. **Set API Keys**: Enter your DeepL API key, and if necessary, your Google Translate API key when prompted.
3. **Select i18n Folder**: Choose the folder containing your i18n JSON files.
4. **Start Translation**: Click the "Calculate Characters and Translate" button to begin the translation process.

## Contributing

Contributions to `i18n_translate_tool` are welcome! Please feel free to submit pull requests or open issues to improve the functionality or address any bugs.

## License

This project is licensed under [MIT License](LICENSE).

## Note

This tool is currently independent but will be merged with Nordtools in the future to provide a comprehensive toolkit for developers.
