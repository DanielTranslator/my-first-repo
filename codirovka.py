text = input("Введите текст: ")

encoded_data = {}

encodings = ['koi8_r', 'utf-8', 'utf-16', 'windows-1251', 'iso-8859-5']

for encoding in encodings:
    try:
        encoded = text.encode(encoding)
        encoded_data[encoding] = encoded

    except UnicodeEncodeError as e:
        encoded_data[encoding] = f'Ошибка кодирования: {e}'

decoded_data = {}

for encoding, data in encoded_data.items():
    if isinstance(data, bytes):
        try:
            decoded = data.decode(encoding)
            decoded_data[encoding] = decoded

        except UnicodeDecodeError as e:
            decoded_data[encoding] = f'Ошибка декодирования: {e}'
    else:
        decoded_data[encoding] = data

import pandas as pd

results = pd.DataFrame({
    'Encoding': encodings,
    'Encoded (Bytes)': [encoded_data[enc] if isinstance(encoded_data[enc], bytes) else 'Ошибка' for enc in encodings],
    'Decoded (Text)': [decoded_data[enc] for enc in encodings]
})

from tabulate import tabulate

print(tabulate(results, headers='keys', tablefmt='grid'))

results.to_excel('Results.xlsx', index=False)