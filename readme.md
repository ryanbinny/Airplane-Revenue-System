# ✈️ Airplane Revenue System — Flask Mini Project

A web application built using Flask, HTML, and CSS that calculates the total revenue for an airline company based on:

- Number of passengers (Economy, Business, First Class)
- Distance flown (in km)
- Aircraft type (A320, B737, A380)

---

## 🧮 Features

- Calculates base revenue per passenger class
- Applies:
  - ✅ 10% surcharge if total passengers > 300 (on ticket price)
  - ✅ 5% discount if distance > 5000 km
  - ✅ ₹100,000 bonus for A380 with more than 250 passengers
- Displays full breakdown of calculations
- Input validation for all fields
- Clean and responsive UI with custom CSS

---

## 🗂️ Project Structure

AirplaneRevenueSystem/
├── app.py
├── templates/
│ ├── index.html
│ └── result.html
├── static/
│ └── style.css
├── screens/ 
├── README.md
├── requirements.txt


---

## 🚀 How to Run

1. Open terminal and activate virtual environment:
   ```bash
   .\venv\Scripts\activate   # Windows PowerShell
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   python app.py
4. Open browser and go to:
   http://localhost:5000

📸 Screenshots
Include form and result screenshots in the /screens folder and embed here if needed.

🧾 Dependencies
Flask

👤 Author
Ryan Binny Mathews






