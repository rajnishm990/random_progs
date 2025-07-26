import string

# Define English stop words set
STOP_WORDS = {
    'a', 'an', 'and', 'the', 'or', 'of', 'to', 'in', 'for', 'on', 'with',
    'at', 'by', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him',
    'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their', 'this',
    'that', 'these', 'those', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
    'may', 'might', 'must', 'can', 'could', 'as', 'but', 'if', 'or', 'because',
    'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
    'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from', 'up',
    'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
    'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
    'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
    'only', 'own', 'same', 'so', 'than', 'too', 'very'
} 

def preprocess_text(text: str) -> str:
    """Preprocess text: case conversion, punctuation removal, tokenization, stop word removal"""

    #change case 
    text = text.lower()

    #remove punctuation
    translator = text.maketrans('','', string.punctuation)
    text =text.translate(translator)

    #tokenization : Tokenization (simple space splitting; more complex logic can be used in practical applications)
    tokens = text.split() 

    #removing stop words 
    tokens = [token for token in tokens if token not in STOP_WORDS and token.strip()!='']

    #stemming 

    tokens = [stem_token(token) for token in tokens]

    return tokens 

def stem_token(token: str)-> str:
    """Simple stemming function (more complex algorithms can be used in practical applications)"""
    # Handle common suffixes
    suffixes = ['ing', 'ly', 'ed', 'es', 's'] 

    for suffix in suffixes :
        if token.endswith(suffix) and len(token)> len(suffix):
            return token[:-len(suffix)]
    return token 


