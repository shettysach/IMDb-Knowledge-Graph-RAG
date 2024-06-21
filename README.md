#### IMDb Knowledge Graph RAG 
##### Made using Neo4j, LangChain, Gemini API and IMDb Top 250 movies dataset

<div align="center">
    <img src="./assets/nwgraph.png" align="center" height="60%" width="60%">
    <p> Click and zoom in to see details.</p>
</div>

- Neo4j database stores the network graph.
    * There are 3 types of nodes - Movie, Genre, Person
    * Person can be - Actor, Director, Writer or a combination of these
    * Relationships are -
        - Person - [ WROTE / ACTED_IN / DIRECTED ] -> Movie
        - Movie - [ BELONGS_TO ] -> Genre
- LangChain and Gemini are used for the pipeline, which 
    * Processes the natural language prompt
    * Generates a Cypher query
    * Queries the Neo4j database with generated query and gets back the result in JSON
    * Parses the JSON and responds back in natural language

<div align="center">
    <img src="./assets/streamlit.png" align="center" height="75%" width="75%">
</div>

##### Steps to run -
- Clone the repo and navigate to the diretory.
- Download the [dataset](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset), rename and move it to the `/data` directory as `imdb.csv`.
- Create a virtual environment with Python version 3.10.14, install the requirements from `requirements.txt`.
    For Conda,
    ```
    $ conda create --name <env> --file ./requirements.txt
    ```
- Recommended - Create new Neo4j database. ([for Community edition](https://stackoverflow.com/a/62564995))
- Start the Neo4j server.
- Fill in Neo4j credentials and Gemini API key in `.env_template` and rename to `.env`.
- First create the network graph by running the Jupyter notebook `./src/Knowledge_Graph.ipynb`.
- Run the Jupyter notebook `./src/Graph_RAG.ipynb.ipynb`
- Run the Streamlit web app by running
    ```
    streamlit run ./src/App.py
    ```

##### Credits
- [Chidambara Raju G - IMDb Top 250 Movies Dataset](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset)
