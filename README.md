# Markov Chain-Based Surrogate Substitution for De-Identification of Clinical Notes

## Project Overview
This project applies a **Markov chain-based surrogate substitution** method to de-identify patient names in synthetic clinical notes. Due to the unavailability of real clinical data, a synthetic dataset was generated and used to test the effectiveness of different substitution strategies under varying levels of **False Negative Error Rate (FNER)**. This project is a subset of a broader study focused on de-identification in healthcare data and evaluates the Markov chain approach alongside consistent and random substitution strategies.

## Methodology
The methodology focuses on using the Markov chain approach to replace patient names in clinical notes with surrogate names in a way that minimizes the risk of re-identification, especially when NER systems miss some PHI. The core steps in the project include:

1. **Data Preparation**: A synthetic dataset of 100 clinical notes was generated via code in `synthetic_data_generator.py` to simulate real healthcare data while focusing exclusively on the de-identification of patient names. Other fields were masked to simplify analysis.

2. **Simulating FNER**: Different levels of FNER (i.e, 1%, 5%, 10%) were applied to simulate scenarios where NER systems fail to identify some patient names, allowing us to evaluate the effectiveness of the Markov approach under real-world conditions.

3. **Surrogate Substitution Approaches**:
    - **Markov Chain-Based Substitution**: This method uses a transition probability (p=0.5) to balance the reuse of previous surrogates with selecting new surrogates, adding both consistency and randomness to the substitution.
    - **Consistent Substitution**: A single surrogate is used for all patient names, resulting in uniform replacements.
    - **Random Substitution**: New surrogates are randomly assigned for each patient name occurrence.

4. **PHI Leakage Measurement**: The leakage rate was calculated to determine the percentage of real names left unchanged after substitution.

5. **Maximum Surrogate Repeat Size**: The frequency of surrogate reuse was measured to avoid identifiable patterns from forming, which could otherwise increase the risk of re-identification.
