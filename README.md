![Screenshot (31)](https://github.com/user-attachments/assets/64455ef6-d56b-4d66-befe-c81bdb157353)
![Screenshot (30)](https://github.com/user-attachments/assets/0a02f9d2-437a-4a41-ab7f-99dee16e91ea)
![Screenshot (32)](https://github.com/user-attachments/assets/b6d5450d-e85d-415f-9a2d-300fded6b2a1)
![Screenshot (171)](https://github.com/user-attachments/assets/01b8783c-e391-445c-b776-5b396c9752db)

# 🎬 Script Writer App

A Django-based script writing tool designed for authors, screenwriters, and creative minds who want to break stories into emotional, place-based scenes. The app allows writers to input pieces of a story — like place, emotion, voice, and context — and group them into a structured chapter.

---

## ✨ Features

- Input fields for:
  - 🏙️ **Place**
  - 💫 **Emotional Aspect**
  - 🗣️ **Voice/Person’s Name**
  - 📜 **Context** (the actual script or dialogue)
- **Add** button to append entries and preview them instantly.
- **Publish** button to group all current entries into a single **Chapter** (like a scene card).
- View unpublished entries before finalizing.
- Organized data models using Django ORM.

---

## 🧱 Technologies

- Python 3.x
- Django 4.x+
- HTML + CSS (customizable frontend)
- Bootstrap/Tailwind (optional for styling)

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/script-writing-app.git
cd script-writing-app
2. Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Server
bash
Copy
Edit

python manage.py migrate
python manage.py runserver
Visit http://127.0.0.1:8000/ to view the app.

🗃️ Project Structure
bash
Copy
Edit
script-writing-app/
├── .venv/                  # Virtual environment (excluded from Git)
├── scripts/                # Your script writing app
├── yourproject/            # Django project files (settings, urls)
├── requirements.txt        # Python dependencies
├── db.sqlite3              # Local dev database
├── manage.py
└── README.md
✍️ Planned Improvements
Editable previews before publishing

Rich text editor for script input

Chapter titling & organization

Export as PDF or markdown

Authentication for multiple users

📄 License
This project is open-source and available under the MIT License.

🤝 Contributing
Pull requests are welcome! If you have ideas for improving the structure, features, or UI, feel free to fork the project and submit a PR.

yaml
Copy
Edit

---

Let me know if you want:
- A styled `LICENSE` file (MIT)
- Contributor guidelines (`CONTRIBUTING.md`)
- Badges (like GitHub stars, license, etc.)

We can also add screenshots once you build the UI. Ready for the next step — forms and views?







