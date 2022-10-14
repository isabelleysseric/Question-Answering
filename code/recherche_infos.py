
import os.path
import pandas as pd
import spacy
from termcolor import colored
from IPython.display import display
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser, MultifieldParser
from whoosh.analysis import StemmingAnalyzer
from whoosh.filedb.filestore import FileStorage


# Variables
nlp = spacy.load("en_core_web_lg")


# Nom du répertoire de l'index inversé
inverted_index_dir = u"index"
if not os.path.exists(inverted_index_dir):
    os.mkdir("index")

# Structure des documents à mettre dans l'index
stem = StemmingAnalyzer()
schema = Schema(title=TEXT(stored=True), content=TEXT(analyzer=stem, stored=True), path=ID(unique=True, stored=True))

# Nom du répertoire du corpus
docs = os.listdir("corpus/")
docs_path = "corpus/"

# Création de la liste de documents
print(colored("Création de la liste de documents...", "red"))
list_docs = []
for doc in docs:
    x = doc.replace('.txt', '')
    d = "".join(docs_path + doc)
    with open(d, 'r') as f:
        list_docs.append({"title": "Doc" + x, "content": f.readline(), "path": doc}, )

# Create an index
storage = FileStorage("index")
#ix = storage.create_index(schema)
ix = storage.open_index()

# Obtenir la taille de l'index
with ix.reader() as reader:
    print("\nNombre de documents dans l'index inversé: ", reader.doc_count(), "\n")


# ajoutr des documents dans l'index inversé
def add_index():
    print(colored("Création de l'index inversé...", "red"))
    writer = ix.writer()
    for doc in list_docs:
        d = "".join(docs_path + doc["path"])
        with open(d, 'r') as f:
            writer.add_document(title=doc["title"], content=doc["content"], path=doc["path"])
    writer.commit()

# Obtenir de l'information sur l'index inversé
def info_index():
    with ix.reader() as reader:

        # Liste du contenu du corpus
        docs_path = {docnum: x["title"] for docnum, x in reader.iter_docs()}
        print("\nNombre de documents dans l'index inversé: ", reader.doc_count(), "\n")

        # Initialisation
        field = "content"
        terms = reader.field_terms(field)
        term_features = dict()

        # Index inversé
        for term in terms:
            info = reader.term_info(field, term)
            postings = reader.postings(field, term)
            posting_list = [docs_path[x] for x in postings.all_ids()]
            term_features[term] = [info.doc_frequency(), posting_list]

        # Affichage de l'index inversé sous forme de tableau
        feature_names = [colored("Nb de documents", "blue"), colored("Liste de postings", "blue")]
        df = pd.DataFrame.from_dict(term_features, orient='index', columns=feature_names)
        display(df)

# afficher les résultats d'une recherche
def show_hits(results):
    result = []
    with ix.searcher() as searcher:
        for hit in results:
            result.append((hit['content'], hit["title"]))
    return result

#  Recherche à l'aide d'une requête par mots clés
def search_content(query, inverted_index, nb):
    with inverted_index.searcher() as searcher:
        field = "content"
        schema = inverted_index.schema
        # Rechercher des termes dans la requête
        query_parser = QueryParser(field, schema)   # group=AndGroup par défaut
        query1 = query_parser.parse(query)
        results = searcher.search(query1, terms=True, limit=nb)
        return show_hits(results)

