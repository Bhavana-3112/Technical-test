import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from transformers import pipeline  

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

user_stories = [
    "As a user, I want to log in to my account so that I can access my data.",
    "As a user, I want to reset my password if I forget it.",
    "As an admin, I want  create new user accounts."
]

acceptance_criteria = [
    "Given the user is on the login page, when they enter valid credentials, then they should be redirected to the dashboard.",
    "Given the user is on the forgot password page, when they enter their email address, then they should receive a password reset link.",
    "Given the admin is on the user management page, when they fill out the new user form and submit it, then a new user account should be created."
]

df = pd.DataFrame({'user_story': user_stories, 'acceptance_criteria': acceptance_criteria})

def preprocess_text(text):
    tokens = word_tokenize(text.lower()) 
    return tokens

df['processed_criteria'] = df['acceptance_criteria'].apply(preprocess_text)

generator = pipeline('text-generation', model='distilgpt2')  

def generate_bdd_test_case(user_story, acceptance_criteria):
    prompt = f"User Story: {user_story}\nAcceptance Criteria: {acceptance_criteria}\nBDD Test Case:\nFeature: "
    generated_text = generator(prompt, max_length=200, num_return_sequences=1)  
    bdd_case = generated_text[0]['generated_text'].split("Feature: ")[1].strip()  
    return bdd_case

df['bdd_test_case'] = df.apply(lambda row: generate_bdd_test_case(row['user_story'], row['acceptance_criteria']), axis=1)


# Playwright Test Script Generation (basic example)
def generate_playwright_script(bdd_test_case):
    lines = bdd_test_case.split('\n')
    test_name = lines[0].replace("Scenario:", "").strip()  
    script = f"""
import {{ test, expect }} from '@playwright/test';

test('{test_name}', async ({{ page }}) => {{
    
    // await page.goto('https://example.com/login');
    // await page.fill('#username', 'testuser');
}});
"""
    return script

df['playwright_script'] = df['bdd_test_case'].apply(generate_playwright_script)

print(df[['user_story', 'acceptance_criteria', 'bdd_test_case', 'playwright_script']])

import os
output_dir = "playwright_tests"  
os.makedirs(output_dir, exist_ok=True)

for index, row in df.iterrows():
    file_name = f"test_{index}.spec.js"  
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, "w") as f:
        f.write(row['playwright_script'])

print(f"Playwright test scripts saved to: {output_dir}")