from pathlib import Path
from langchain_community.document_loaders import CSVLoader, TextLoader

# Documents folder (outside backend)
DOCUMENTS_PATH = Path("../documents")


def load_documents():
    documents = []

    # ---------------------------
    # Load CSV Files (Sample Only)
    # ---------------------------
    csv_folder = DOCUMENTS_PATH / "csv"

    if csv_folder.exists():
        for file in csv_folder.glob("*.csv"):
            print(f"Loading CSV: {file.name}")

            loader = CSVLoader(str(file))
            docs = loader.load()

            # Load only first 100 rows from each CSV
            documents.extend(docs[:100])

    # ---------------------------
    # Load TXT Files
    # ---------------------------
    txt_folder = DOCUMENTS_PATH / "txt"

    if txt_folder.exists():
        for file in txt_folder.glob("*.txt"):
            print(f"Loading TXT: {file.name}")

            loader = TextLoader(str(file), encoding="utf-8")
            documents.extend(loader.load())

    print(f"\n✅ Total Documents Loaded: {len(documents)}")

    return documents


if __name__ == "__main__":
    docs = load_documents()