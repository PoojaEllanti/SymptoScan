# 🩺 SymptoScan – Smart Symptom Checker

SymptoScan is an intelligent, user-friendly health assistant that helps users identify possible medical conditions based on their symptoms. Designed with Streamlit, it features a clean UI, symptom-to-disease matching logic, and real-world medical advice.

---

## 🚀 Features

- ✅ Enter symptoms as comma-separated text
- ✅ Intelligent matching with real-world conditions
- ✅ Match Confidence Score (%)
- ✅ Medical advice for each condition
- ✅ Beautiful and modern UI
- ✅ Easily expandable dataset (JSON-based)

---

## 🧠 How It Works

1. User inputs symptoms like: `fever, headache, fatigue`
2. SymptoScan compares these with known conditions in a medical database
3. Conditions with matching symptoms are shown in order of confidence
4. Each condition card displays:
   - Name of disease
   - Match percentage
   - Practical advice or next steps

---

## 📷 Screenshots

### 🔍 Input Symptoms
![Input Screenshot](assets/input.png)

### ✅ Result Display
![Output Screenshot](assets/output.png)

---

## 🛠 Tech Stack

| Layer     | Tools/Tech                      |
|-----------|----------------------------------|
| Frontend  | [Streamlit](https://streamlit.io) |
| Backend   | Python                          |
| Data      | JSON symptom-condition mapping  |
| Styling   | HTML/CSS (Streamlit markdown)   |

---

## 📁 Folder Structure

SymptoScan/
├── app.py # Main Streamlit app
├── utils.py # Symptom matcher logic
├── symptom_data.json # Symptom-condition-advice mapping
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 📦 Installation & Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/SymptoScan.git
   cd SymptoScan
   
Install dependencies
pip install -r requirements.txt

Run the app
streamlit run app.py
