## Automated Data Preprocessing and Histogram Visualisation

This Streamlit application assists you with cleaning and visualizing your data in a user-friendly way. It offers functionalities for handling missing values and encoding categorical columns, along with basic data exploration through histograms.

**Getting Started:**

1. Ensure you have Python installed (`https://www.python.org/downloads/`).
2. Install required libraries:
   ```bash
   pip install streamlit pandas matplotlib seaborn scikit-learn
   ```

**Running the App:**

1. Save the provided Python code as a file (e.g., `data_cleaner.py`).
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script using:
   ```bash
   streamlit run data_cleaner.py
   ```

**Using the App:**

* Upload a CSV file containing your data.
* Select a method for handling missing values:
    * **Drop:** Removes rows with missing values.
    * **Mean/Median/Mode:** Imputes missing values using the respective statistical measure of the column.
    * **Constant:** Fills missing values with a user-specified constant value.
    * **Forward Fill/Backward Fill:** Replaces missing values with the previous/next non-missing value.
* (Optional) Choose categorical columns for encoding (converts text labels to numerical values).
* Explore your data's distribution using the histogram visualization. Select a feature to view its histogram.
* Download the preprocessed data as a CSV file for further analysis.

**Limitations:**

* Currently only supports histogram visualization. Pie chart functionality is planned for future updates.

**Further Enhancements:**

* Implement additional data cleaning techniques like outlier handling and feature scaling.
* Provide more visualization options (scatter plots, boxplots, etc.).
* Integrate functionalities for data transformation and feature engineering.