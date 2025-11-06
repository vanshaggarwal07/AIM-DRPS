<div align="center">

# 🔥 AIM-DRPS: Advanced Intelligent Model for Degradation and Risk Prediction System

[![GitHub license](https://img.shields.io/github/license/vanshaggarwal07/AIM-DRPS?style=for-the-badge)](https://github.com/vanshaggarwal07/AIM-DRPS/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/vanshaggarwal07/AIM-DRPS?style=for-the-badge)](https://github.com/vanshaggarwal07/AIM-DRPS/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/vanshaggarwal07/AIM-DRPS?style=for-the-badge)](https://github.com/vanshaggarwal07/AIM-DRPS/issues)

</div>

## 🚀 Overview
AIM-DRPS is an intelligent system designed to predict explosive dissolution rates and assess associated risks using machine learning. This application helps in analyzing and predicting the behavior of different explosive materials under various conditions, ensuring safety and efficiency in industrial applications.

## ✨ Features

- **Predictive Analytics**: Accurately predict dissolution rates of explosive materials
- **Risk Assessment**: Classify risk levels (Low, Medium, High) for different scenarios
- **Interactive Dashboard**: User-friendly interface with real-time visualizations
- **Data Processing**: Advanced data preprocessing and feature engineering
- **Machine Learning Models**: Pre-trained models for instant predictions

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aim-drps.git
   cd aim-drps
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚦 Quick Start

1. Run the Streamlit application:
   ```bash
   streamlit run AST1.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`

3. Use the interactive dashboard to make predictions and analyze results

## 🧠 Model Details

- **Dissolution Rate Prediction**: Regression model for predicting material dissolution rates
- **Risk Level Classification**: Classification model for assessing risk levels
- **Trained Models**:
  - `dissolution_regressor_model.pkl` - For dissolution rate prediction
  - `risk_classifier_model.pkl` - For risk level classification

## 📊 Data Processing

The system includes robust data processing capabilities:
- Data cleaning and normalization
- Feature engineering
- Handling missing values and outliers
- Categorical variable encoding

## 📂 Project Structure

```
AIM-DRPS/
├── AST1.py                # Main Streamlit application
├── datahandling.py        # Data processing utilities
├── newdata.py             # Data preprocessing script
├── notebook.py            # Jupyter notebook conversion
├── requirements.txt       # Project dependencies
├── dissolution_regressor_model.pkl    # Pre-trained model
├── risk_classifier_model.pkl          # Pre-trained model
└── preprocessed_explosive_data.csv    # Processed dataset
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For any questions or feedback, please contact [Your Email] or open an issue on GitHub.

---

<div align="center">
  Made with ❤️ by VANSH AGGARWAL | 2025
</div>