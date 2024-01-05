import json
import requests
import os
from tkinter import Tk, Label, Entry, Button, filedialog, StringVar, messagebox, simpledialog
from pathlib import Path

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        messagebox.showerror("JSON Format Error", f"Error reading {file_path}: {e}")
        return None

def check_language_support(deepl_api_key, target_lang):
    url = "https://api-free.deepl.com/v2/languages"
    payload = {'auth_key': deepl_api_key}
    response = requests.get(url, params=payload)
    if response.status_code == 200:
        supported_languages = [lang['language'] for lang in response.json()]
        return target_lang.upper() in supported_languages
    else:
        messagebox.showerror("API Error", "Error checking supported languages with DeepL API.")
        return False

def translate_text(deepl_api_key, google_api_key, text, target_lang):
    if len(text.split()) < 4:
        print("test")
        print(text)
        return google_translate_text(google_api_key, text, target_lang)
    else:
        url = "https://api-free.deepl.com/v2/translate"
        payload = {
            'auth_key': deepl_api_key,
            'text': text,
            'target_lang': target_lang.upper()
        }
        response = requests.post(url, data=payload)
        if 'translations' in response.json():
            return response.json()['translations'][0]['text']
        else:
            return None

def count_characters(json_content):
    return sum(len(value) for value in json_content.values())

def translate_and_populate(template_content, target_lang, deepl_api_key, google_api_key):
    translated_content = {}
    for key, value in template_content.items():
        # Updated to pass google_api_key
        translation = translate_text(deepl_api_key, google_api_key, value, target_lang)
        if translation is not None:
            translated_content[key] = translation
    return translated_content

def select_folder():
    folder_path.set(filedialog.askdirectory())

def move_to_not_translated_folder(folder_path, file_name):
    not_translated_folder = Path(folder_path) / 'not_translated'
    not_translated_folder.mkdir(exist_ok=True)
    os.rename(Path(folder_path) / file_name, not_translated_folder / file_name)

def google_translate_text(google_api_key, text, target_lang):
    url = f"https://translation.googleapis.com/language/translate/v2?key={google_api_key}"

    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "q": text,
        "target": target_lang
    })

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200 and 'data' in response.json():
        return response.json()['data']['translations'][0]['translatedText']
    else:
        print("Error:", response.status_code, response.json())
        return None

def get_google_supported_languages(google_api_key):
    url = "https://translation.googleapis.com/language/translate/v2/languages?key={}".format(google_api_key)
    response = requests.get(url)
    if response.status_code == 200:
        languages = response.json().get('data', {}).get('languages', [])
        return [lang['language'] for lang in languages]
    else:
        messagebox.showerror("API Error", "Error fetching supported languages from Google Translate.")
        return []

def fallback_translation(i18n_folder_path, template_content, google_api_key, not_translated_languages):
    supported_languages = get_google_supported_languages(google_api_key)
    google_translate_languages = [lang for lang in not_translated_languages if lang in supported_languages]

    if not google_translate_languages:
        messagebox.showinfo("No Translation Needed", "No additional languages require Google Translate.")
        return

    total_chars = count_characters(template_content) * len(google_translate_languages)
    if messagebox.askyesno("Confirm Google Translation", f"You are about to translate {total_chars} characters for the following language codes with Google Translate: {', '.join(google_translate_languages)}. Do you want to proceed?"):
        for lang in google_translate_languages:
            translated_content = {}
            for key, value in template_content.items():
                translation = google_translate_text(google_api_key, value, lang)
                if translation is not None:
                    translated_content[key] = translation
            if translated_content:
                with open(os.path.join(i18n_folder_path, f'{lang}.json'), 'w', encoding='utf-8') as f:
                    json.dump(translated_content, f, ensure_ascii=False, indent=4)

def confirm_translation():
    i18n_folder_path = folder_path.get()
    template_lang_code = template_lang.get()

    template_file_path = os.path.join(i18n_folder_path, f'{template_lang_code}.json')
    if not os.path.isfile(template_file_path):
        messagebox.showerror("Error", f"No template file found for the language code '{template_lang_code}'.")
        return

    template_content = read_json(template_file_path)
    if template_content is None:
        return

    deepl_api_key = simpledialog.askstring("DeepL API Key", "Enter DeepL API Key:")
    if not deepl_api_key:
        messagebox.showinfo("Cancelled", "Translation cancelled (no DeepL API key provided).")
        return

    google_api_key = simpledialog.askstring("Google API Key", "Enter Google Translate API Key:")
    if not google_api_key:
        messagebox.showinfo("Cancelled", "Translation cancelled (no Google Translate API key provided).")
        return

    target_languages = [file.split('.')[0] for file in os.listdir(i18n_folder_path) if file.endswith('.json') and file != f'{template_lang_code}.json']
    not_translated_languages = []
    for lang in target_languages.copy():
        if not check_language_support(deepl_api_key, lang):
            not_translated_languages.append(lang)
            target_languages.remove(lang)

    total_chars = count_characters(template_content) * len(target_languages)
    if messagebox.askyesno("Confirm Translation", f"You are about to translate {total_chars} characters for the following language codes: {', '.join(target_languages)}. Do you want to proceed?"):
        # Added google_api_key in the function call
        start_translation(i18n_folder_path, template_lang_code, deepl_api_key, google_api_key, template_content, target_languages, not_translated_languages)

def start_translation(i18n_folder_path, template_lang_code, deepl_api_key, google_api_key, template_content, target_languages, not_translated_languages):
    for target_lang_code in target_languages:
        # Updated to pass google_api_key
        translated_content = translate_and_populate(template_content, target_lang_code, deepl_api_key, google_api_key)
        if translated_content:
            with open(os.path.join(i18n_folder_path, f'{target_lang_code}.json'), 'w', encoding='utf-8') as f:
                json.dump(translated_content, f, ensure_ascii=False, indent=4)
        else:
            not_translated_languages.append(target_lang_code)

    if not_translated_languages:
        messagebox.showinfo("Partial Completion", "Initial translation is complete. Enter your Google Translate API key for additional languages.")
        google_api_key = simpledialog.askstring("Google API Key", "Enter Google Translate API Key:")
        if google_api_key:
            fallback_translation(i18n_folder_path, template_content, google_api_key, not_translated_languages)

root = Tk()
root.title("i18n Translator")

folder_path = StringVar()
template_lang = StringVar()

Label(root, text="Template Language Code:").pack()
Entry(root, textvariable=template_lang).pack()

Label(root, text="i18n Folder Path:").pack()
Entry(root, textvariable=folder_path).pack()
Button(root, text="Browse", command=select_folder).pack()

Button(root, text="Calculate Characters and Translate", command=confirm_translation).pack()

root.mainloop()

