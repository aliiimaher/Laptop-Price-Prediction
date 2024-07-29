# Laptop-Price-Prediction
This is an AI model for predicting laptop price, trained on about 1200 data.

# Linear Algebra Project: Laptop Price Prediction

## Prepared for
**Dr. Mohammad Taheri**  

## Prepared by
**Ali Maher, [Amir Hossein Ezzati](https://github.com/amirHosseinEz)**

## Date
**13th of July 2024**

---

## Introduction

This project utilizes linear algebra concepts to analyze and predict laptop prices based on data extracted from the e-commerce website, Digikala. The process involves web scraping to collect relevant features such as price, rating, and reviews, followed by data transformation for use in a linear regression model. The model is trained and evaluated to predict laptop prices accurately.

## Project Overview

1. **Data Collection & Data Cleaning**
   - **Web Scraping with Beautiful Soup**: Initial attempts using Beautiful Soup faced issues due to Digikala’s anti-scraping measures.
   - **Switching to Selenium**: Selenium was used for more robust web scraping, overcoming challenges like intermediary screens and varied data formats.
   - **Handling Data Formats**: Conversion of Persian numerals and words to English, parsing mixed data formats, and separating combined values.

2. **Linear Regression Model**
   - **Data Splitting**: Dataset split into training (80%) and testing (20%) sets.
   - **Model Training**: A linear regression model was trained on the training set.
   - **Model Evaluation**: Evaluated using metrics like Mean Squared Error (MSE) and R-squared score, achieving 94% accuracy.

3. **Price Prediction**
   - **GUI Development**: A user-friendly GUI was created using Tkinter, incorporating features like dropdown menus and handling menu item indexing challenges.

## Detailed Steps

### Part 1: Data Collection & Data Cleaning

- **Initial Attempts with Beautiful Soup**: Faced issues with decoy HTML content from Digikala.
- **Switching to Selenium**: Automated browser interactions to bypass intermediary screens and access real HTML content.
- **Handling Diverse Data Formats**: Parsing numerical values embedded in strings, converting Persian text to English, and dealing with mixed formats.
- **Language and Number Conversion**: Translated Persian numerals and units to English equivalents.
- **Automating the Process**: Developed a comprehensive script for efficient data extraction and conversion.

**Challenges and Solutions**:
- **Invalid Data in Columns**: Replaced invalid entries like "متغیر" with acceptable values after research.
- **Internal Storage Column**: Translated and separated combined SSD and HDD values.
- **Non-numerical Columns**: Applied one-hot encoding to convert categorical data into numerical format.

### Part 2: Linear Regression Model

- **Data Splitting**: 80% of data used for training, 20% for testing.
- **Model Training**: Trained a linear regression model on the cleaned dataset.
- **Model Evaluation**: Achieved about 94% accuracy using MSE and R-squared metrics.

### Part 3: Price Prediction

- **GUI Development with Tkinter**: Created a GUI for price prediction.
- **Challenges in Tkinter**: Resolved bugs related to dropdown menu item indexing by appending identifiers to avoid confusion.

## Conclusion

This project demonstrates the practical application of linear algebra in predicting laptop prices. Key achievements include overcoming data scraping and cleaning challenges, effectively using one-hot encoding for categorical data, and developing a highly accurate linear regression model. The user-friendly GUI enhances usability, making the tool accessible for end-users.

![gui_pic](.../...)

## Repository Contents

- **Data Collection Scripts**: Selenium scripts for web scraping.
- **Data Cleaning Scripts**: Python scripts for data cleaning and conversion.
- **Linear Regression Model**: Model training and evaluation scripts.
- **GUI Application**: Tkinter-based GUI for price prediction.
- **Documentation**: Detailed project documentation and process explanation.

---

Thank you for your time and interest in this project. For further exploration and validation.
