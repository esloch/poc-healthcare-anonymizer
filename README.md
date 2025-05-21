# 🧠 Healthcare Anonymizer

A Python tool for anonymizing sensitive information in healthcare clinical notes, with a focus on mental health domains including **psychosis**, **dementia**, **depression**, and **suicidal ideation**.

Built using [Microsoft Presidio](https://github.com/microsoft/presidio), it provides a customizable, Pythonic way to process clinical text and remove personally identifiable information (PII).

---

## 🚀 Features

- Detects and anonymizes common PII types:
  - ✅ Person names
  - ✅ Email addresses
  - ✅ Dates
  - ✅ General locations (e.g., cities, countries, states)
  - ✅ Phone numbers (international formats)
- Replaces sensitive values with a standard token (`<REDACTED>`)
- Extensible for medical and mental health use cases
- Modular Python project with unit tests and example notebook

---

## 📦 Install Dependencies

You can install all required Python packages using:

```bash
pip install -r requirements.txt
````

Make sure you are using Python 3.9–3.12 for compatibility with `presidio-analyzer`.

---

## 📌 Supported Entities (Presidio Defaults)

Presidio's default NLP engine supports the following entity types, which are used in this project:

| Entity Type     | Description                 |
| --------------- | --------------------------- |
| `PERSON`        | Full names, first names     |
| `EMAIL_ADDRESS` | Email addresses             |
| `DATE_TIME`     | Dates in various formats    |
| `PHONE_NUMBER`  | International phone numbers |
| `LOCATION`      | Countries, cities, regions  |

---

## ⚠️ Known Limitations

* 🔹 **Street addresses like "123 Elm St" are NOT detected** by default.

  * Presidio’s built-in `LOCATION` recognizer only handles general geographic entities (cities, countries).
  * Street-level address detection requires a custom recognizer.

* 🔹 **Phone numbers must be in standard formats**:

  * ✅ Detected: `+1-541-754-3010`, `(541) 754-3010`, `541-754-3010`
  * ❌ Not Detected: `555-1234` (short/local format)

These limitations are typical for de-identification systems and can be addressed by extending the project with **custom recognizers** based on regular expressions or external libraries.

---

## 📓 Example Usage

```python
from healthcare_anonymizer.anonymizer import HealthcareAnonymizer

anonymizer = HealthcareAnonymizer()

text = "John Doe visited Paris on 12/03/2023. His email is john@example.com."
output = anonymizer.anonymize_text(text)

print(output)
# Output: <REDACTED> visited <REDACTED> on <REDACTED>. His email is <REDACTED>.
```

---

## 🧠 Focus Areas

This project is intended to support research and clinical use cases in:

* Mental health documentation
* Psychiatric assessments
* Case studies for psychosis, depression, dementia, and suicide prevention
* Ethics-compliant data collection and analysis

---

## 🤝 Contributions & Extensions

Future improvements may include:

* [ ] Custom recognizers for street addresses
* [ ] Export to FHIR-compatible formats
* [ ] PDF and clinical document ingestion
* [ ] Streamlit or web interface

PRs are welcome!

---

## 🪪 License

MIT License — free to use and modify.
