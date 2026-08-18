# AI/ML-Driven Discovery of Ionic Liquids for Efficient CO₂ Capture

## About the Project

This project was carried out as part of my research internship at **IIT Kharagpur**, focusing on the application of machine learning and cheminformatics for predicting CO₂ solubility in ionic liquids.

Carbon capture is an important part of reducing industrial CO₂ emissions, but conventional solvents can have limitations such as volatility, degradation and high regeneration energy. Ionic liquids are promising alternatives because their properties can be tuned by changing their cation and anion structures.

The central question behind this project was:

**Can molecular information and operating conditions be used to predict the CO₂ absorption behaviour of ionic liquids?**

To investigate this, I developed a complete machine learning workflow, starting from literature data collection and preprocessing and going through molecular descriptor generation, feature selection, model development, validation and interpretation.

---

## What I Worked On

The project involved several stages:

* Collected CO₂ solubility data for ionic liquids from literature and the ILThermo database.
* Cleaned and consolidated experimental datasets.
* Performed exploratory data analysis to understand the effect of temperature, pressure and ionic-liquid chemistry on CO₂ solubility.
* Classified ionic liquids into different cation families.
* Used RDKit to generate molecular descriptors from cation and anion structures.
* Performed correlation analysis and feature selection.
* Trained and compared multiple machine learning models.
* Evaluated models using different validation strategies.
* Analysed feature importance to understand the variables influencing CO₂ solubility.
* Explored physicochemical properties such as pKa and Free Fractional Volume (FFV).
* Developed a prediction workflow for estimating CO₂ solubility from molecular structures and operating conditions.

---

## Dataset

The final dataset contains approximately **5,349 experimental observations** covering around **147 unique ionic liquids**.

The data includes information such as:

* Ionic liquid name
* Cation and anion
* Molecular structures / SMILES
* Temperature
* Pressure
* Experimental CO₂ solubility
* Molecular descriptors generated from chemical structures

The dataset was compiled from published experimental studies and the ILThermo database.

One of the major challenges was that the experimental data was not originally available in a single consistent format. Different studies reported measurements at different temperature and pressure conditions, requiring substantial preprocessing and standardisation before modelling.

---

## Methodology

The overall workflow followed this structure:

```text
Literature / ILThermo Data
          ↓
Data Collection
          ↓
Data Cleaning & Preprocessing
          ↓
Exploratory Data Analysis
          ↓
Cation Family Classification
          ↓
Molecular Structure Processing
          ↓
RDKit Molecular Descriptors
          ↓
Feature Cleaning & Correlation Analysis
          ↓
Feature Selection
          ↓
Machine Learning Models
          ↓
Model Validation & Comparison
          ↓
Feature Importance / Interpretation
          ↓
CO₂ Solubility Prediction
```

---

## Molecular Descriptors

A major part of the project was converting chemical structures into numerical representations that machine learning models could understand.

Using **RDKit**, molecular descriptors were generated from the cation and anion structures. These descriptors capture different molecular and structural characteristics of the ionic liquids.

Examples include:

* Molecular weight
* Molecular volume
* Hydrogen-bond related properties
* Topological descriptors
* Surface-area related properties
* Lipophilicity-related properties
* Other structural and physicochemical characteristics

Because generating a large number of descriptors can introduce redundancy, the descriptors were cleaned and filtered before being used for model development.

---

## Feature Selection

Rather than directly using every generated descriptor, I investigated which features provided the most useful information for predicting CO₂ solubility.

The feature-selection process included:

1. Removing constant features.
2. Removing highly correlated variables.
3. Analysing feature importance from tree-based models.
4. Comparing different feature subsets.
5. Combining molecular descriptors with important experimental variables such as temperature and pressure.

This helped reduce dimensionality while retaining the features most relevant to the prediction problem.

---

## Machine Learning Models

Several regression algorithms were explored and compared:

* Linear Regression
* K-Nearest Neighbours
* Support Vector Regression
* Random Forest
* XGBoost
* Artificial Neural Networks

The objective was not simply to select the model with the highest score, but also to understand how different algorithms perform on chemical datasets and how well they generalise to unseen ionic liquids.

Among the models investigated, **XGBoost demonstrated particularly strong predictive performance**.

---

## Physicochemical Approach

Alongside the molecular-descriptor-based approach, I also explored a chemistry-driven representation using physicochemical properties.

This included:

* Cation pKa
* Anion pKa
* ΔpKa-related information
* Free Fractional Volume (FFV)
* Temperature
* Pressure

This approach helped investigate whether physically meaningful properties could provide useful predictive information alongside conventional molecular descriptors.

---

## Model Validation

Model performance was evaluated using:

* R²
* RMSE
* MAE

In addition to a standard train/test split, cross-validation and group-based validation approaches were explored.

This was particularly important because multiple experimental measurements can exist for the same ionic liquid under different conditions. Randomly splitting such data can result in closely related samples appearing in both the training and testing sets.

Group-based validation therefore provided a more meaningful way to investigate how the model performs when dealing with ionic liquids that were not directly represented in the training data.

---

## Model Interpretation

Predictive performance alone is not sufficient for a scientific application.

Feature importance analysis was therefore used to investigate which molecular and experimental variables contributed most strongly to the predictions.

This helped connect the machine learning results back to the underlying chemistry and experimental conditions.

The analysis highlighted the importance of variables associated with **temperature, pressure and the molecular/physicochemical characteristics of the ionic liquids**.

---

## Prediction Application

The trained model was also integrated into a prediction workflow designed to make the research more accessible.

The basic workflow is:

```text
Cation SMILES
      +
Anion SMILES
      +
Temperature
      +
Pressure
          ↓
Molecular Descriptor Generation
          ↓
Selected Features
          ↓
Trained ML Model
          ↓
Predicted CO₂ Solubility
```

This provides a computational approach for screening ionic liquids before carrying out extensive experimental measurements.

---

## Tech Stack

**Programming**

* Python

**Data Analysis**

* Pandas
* NumPy
* Matplotlib
* Seaborn

**Machine Learning**

* Scikit-learn
* XGBoost
* Optuna

**Cheminformatics**

* RDKit

**Model Interpretation**

* Feature Importance
* SHAP

**Application**

* Streamlit

---

## Key Takeaway

The main outcome of this project was not simply developing a model with a high predictive score.

The broader objective was to build a workflow connecting:

**experimental data → molecular structure → chemical descriptors → machine learning → model interpretation → CO₂ solubility prediction**

The project also highlighted an important challenge when applying machine learning to chemical datasets: strong predictive performance needs to be considered alongside data distribution, chemical diversity and the ability of the model to generalise to unseen ionic liquids.

Overall, the work demonstrates how machine learning and cheminformatics can support the computational screening and discovery of ionic liquids for CO₂ capture, potentially reducing the amount of experimental trial-and-error required.

---

## Repository Structure

```text
ionic-liquid-co2-solubility/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── eda.ipynb
│   ├── descriptor_generation.ipynb
│   ├── feature_selection.ipynb
│   └── model_training.ipynb
│
├── models/
│   └── trained_models/
│
├── app/
│   └── streamlit_app.py
│
├── results/
│   ├── figures/
│   └── model_results/
│
├── requirements.txt
└── README.md
```

---

## Acknowledgements

This research project was carried out during my research internship at **IIT Kharagpur**.

**Under the guidance of Dr. Namrata D. Gaikwad**
**Under the supervision of Dr. Indrajit Das**

I am grateful for their guidance, support and valuable feedback throughout the project.

The internship provided me with an opportunity to work at the intersection of **chemical engineering, machine learning and cheminformatics**, and to apply computational methods to a real research problem in carbon capture.

---

## Future Work

Some possible directions for extending this work include:

* Expanding the dataset with additional experimental measurements.
* Using stricter chemical-group-based validation strategies.
* Exploring molecular fingerprints and graph-based representations.
* Investigating graph neural networks for molecular representation learning.
* Performing more extensive hyperparameter optimisation.
* Adding uncertainty estimation to model predictions.
* Screening larger libraries of unexplored ionic liquids.
* Integrating machine learning with experimental design to identify promising candidates for laboratory validation.

---

## Author

**Jaideep Singh**
Chemical Engineering, Birla Institute of Technology, Mesra
Research Intern — IIT Kharagpur

If you find this project useful or have suggestions for improving the modelling approach, feel free to explore the repository and build upon the work.
