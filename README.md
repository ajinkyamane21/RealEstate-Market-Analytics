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

```bash
git clone https://github.com/ajinkyamane21/RealEstate-Market-Analytics.git
cd RealEstate-Market-Analytics
python -m venv venv
venv\Scripts\activate
cd frontend
pip install -r requirements.txt
npm install
npm install concurrently
npm run runui
```



## Usage
• Search a location (example: Wakad) and click Analyze  
• For comparison, enter two names in a query (example: Compare Ambegaon Budruk and Aundh)  
• If the location is invalid, the interface shows a message below the search box

## Project Structure
backend/      → Django API and dataset
frontend/     → React UI

## 🎥 Demo Video
[▶️ Watch Demo](https://github.com/ajinkyamane21/RealEstate-Market-Analytics/raw/main/Demo%20Project.mp4)


## Developer
Ajinkya Mane
