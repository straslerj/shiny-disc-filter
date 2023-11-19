# Shiny Disc Filter
Using Shiny to create a disc golf disc filter by speed and stability.

## Using on the Web

To use this tool on the web, simply navigate to https://jakestrasler.shinyapps.io/disc-filter/

## Running Locally

Using this app locally is relatively straightforward:

1. Ensure the packages you need are installed: `pip install pandas pathlib shiny uvicorn`
2. In a terminal run `shiny run --reload app.py`. Ensure you are in the "shiny-disc-filter/" directory.
3. Click the link in the output of the above terminal command (it should be something like `Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)`).
4. Done! Because the `--reload` command was used in Step 2, any changes made to the code will be reflected upon saving the file (you do not need to kill the process and start it again.)
