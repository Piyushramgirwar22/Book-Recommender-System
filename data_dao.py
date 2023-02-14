import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

# df = pd.read_csv(r'C:\Users\lenovo\OneDrive\Desktop\mybooks project\app_folder\mybooks_project_data.csv')

# print(df)

def visits(visit_range, df):
    new_df = df[df['cluster'] == visit_range]
    return new_df.T.to_dict().values()

# print(book_range('low range', df))

def year_range(a,b,df):
    df1 = df[(df['year']>=a)&(df['year']<=b)]
    return df1.T.to_dict().values()





# Create a function that takes a book title as input and returns the top 5 books most similar to it based on genre
def recommend_books(title,df):
    # Load the data into a Pandas DataFrame
    books = df

# Create a feature matrix by converting the genres of the books into dummy variables
    book_features = pd.get_dummies(books["genre"])

# Calculate the cosine similarity between each pair of books based on their genre features
    cosine_sim = cosine_similarity(book_features)
    # Find the index of the book with the given title
    index = books[books["book_name"] == title].index[0]
    
    # Get the cosine similarity scores of all books with respect to the book at the given index
    sim_scores = list(enumerate(cosine_sim[index]))
    
    # Sort the cosine similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 5 books with the highest cosine similarity scores
    top_books = [i[0] for i in sim_scores[1:6]]
    
    new = pd.DataFrame(books.iloc[top_books])
    
    # Return the titles of the top 5 books
    return new.T.to_dict().values()