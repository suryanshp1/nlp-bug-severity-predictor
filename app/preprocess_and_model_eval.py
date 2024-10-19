import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess_text(text):
    # Convert to lowercase and tokenize
    tokens = word_tokenize(text.lower())
    # Remove stopwords and non-alphanumeric tokens
    stop_words = set(stopwords.words('english'))
    return ' '.join([word for word in tokens if word.isalnum() and word not in stop_words])

def main():
    # Step 1: Load the Excel file
    print("Loading data...")
    df = pd.read_excel('data/bug-severity-data.xlsx')
    df = df.dropna()
    
    # Step 2: Preprocess the descriptions
    print("Preprocessing descriptions...")
    df['PROCESSED_DESCRIPTION'] = df['DESCRIPTION'].apply(preprocess_text)
    
    # Step 3: Save preprocessed data as pickle file
    print("Saving preprocessed data...")
    with open('models/preprocessed_data.pkl', 'wb') as f:
        pickle.dump(df, f)
    
    # Step 4: Prepare data for model training
    X = df['PROCESSED_DESCRIPTION']
    y = df['SEVERITY']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Step 5: Create and fit TF-IDF vectorizer
    print("Creating TF-IDF vectorizer...")
    vectorizer = TfidfVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)
    
    # Step 6: Train the model
    print("Training the model...")
    model = MultinomialNB()
    model.fit(X_train_vectorized, y_train)
    
    # Step 7: Evaluate the model
    y_pred = model.predict(X_test_vectorized)
    print("Model performance:")
    print(classification_report(y_test, y_pred))
    
    # Step 8: Save the model and vectorizer
    print("Saving model and vectorizer...")
    with open('models/bug_severity_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('models/tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    
    print("Process completed successfully!")

if __name__ == "__main__":
    main()