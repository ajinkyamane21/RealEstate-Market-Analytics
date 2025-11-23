# Real Estate Dashboard

This project is a full stack web application built to analyze real-estate locality data from an Excel dataset.
The user can search an area in the dashboard and the system displays:

• A summary of the selected location  
• A year-wise price and demand trend chart  
• A filtered table for the selected location  

The application also supports comparison between two areas when both names are entered in one query.

## Technologies Used
Frontend:
• React
• Bootstrap
• Recharts

Backend:
• Django
• Python (Pandas for Excel processing)

Dataset:
• Excel file (Sample_data.xlsx)

## How to Run the Project

### 1. Install backend dependencies
cd backend
pip install -r requirements.txt

(or manually)
pip install django pandas openpyxl

### 2. Install frontend dependencies
cd frontend
npm install

### 3. Start the project (single command)
cd frontend
npm run runui

This starts both:
• Django backend  
• React frontend  

After launch, open the browser at:
http://localhost:3000/

## Usage
• Search a location (example: Wakad) and click Analyze  
• For comparison, enter two names in a query (example: Compare Ambegaon Budruk and Aundh)  
• If the location is invalid, the interface shows a message below the search box

## Project Structure
backend/      → Django API and dataset
frontend/     → React UI

## 🎥 Demo Video
[▶️ Watch Demo](https://github.com/ajinkyamane21/RealEstate-Market-Analytics/raw/main/Demo Project.mp4)


## Developer
Ajinkya Mane
