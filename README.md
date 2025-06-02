# **Diagnostic Cell Analyzer**  

A **machine learning-powered** tool that assists medical professionals in analyzing cell measurements to predict diagnostic outcomes. Users input numerical features via sliders, and the app provides real-time predictions with interactive visualizations.  

---

## **Key Features**  

### **1. Interactive Input System**  
- Adjust **cell measurements** using sliders (radius, texture, perimeter, etc.)  
- Real-time updates on predictions  

### **2. Dynamic Data Visualization**  
- **Interactive Plotly graph** (radar chart, scatter plot, or bar chart)  
- Visual representation of input features  

### **3. Real-Time Prediction**  
- **Instant classification** (Benign/Malignant)  
- Probability score display  

### **4. Export & Reporting**  
- Export measurements as **CSV**  
- Save graphs for medical reports  

---

## **Installation**  

### **Prerequisites**  
- Python 3.6+  
- pip  

### **Steps**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/diagnostic-cell-analyzer.git
   cd diagnostic-cell-analyzer
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

---

## **Usage**  

1. **Launch the app**:  
   ```bash
   streamlit run app.py
   ```  

2. **Adjust cell measurements** using the sliders on the **left panel**.  

3. **View real-time updates**:  
   - **Middle panel**: Interactive Plotly graph (radar chart, scatter plot, etc.)  
   - **Right panel**: Prediction (Benign/Malignant) + confidence score  

4. **Export data**:  
   - Download measurements as **CSV**  
   - Save graphs as images  

---

## **App Layout Overview**  

| **Left Panel** (Input) | **Middle Panel** (Visualization) | **Right Panel** (Output) |
|------------------------|----------------------------------|--------------------------|
| - Sliders for cell measurements (radius, texture, etc.) | - Interactive Plotly graph (radar/bar/scatter) | - Prediction (Benign/Malignant) |
| - Reset/Default buttons | - Dynamic updates on slider changes | - Probability percentage |
| - Export CSV option | - Hover tooltips for details | - Risk assessment summary |
