## Convert your wordpress blog posts to a Journal in 5 minutes

### Downloading your posts
You will need to export your posts to a csv file.
We're recommanding the wordpress plugin "[WP Import Export Lite](https://wordpress.org/plugins/wp-import-export-lite/)", but you may use any other plugin.

#### Settings for WP Import Export
* Open the export page and select "Post" as export type.
* optional: filter posts by status (e.g. only published posts), categories and/or date
* choose at least the following fields: ID, Title, Date, author, Content, Permalink, doi.
* choose CSV as export file type.

#### CSV requirements
Coming Soon, use WP Import Export for now

### Create LaTeX project
To use your posts, you will need to create a latex project. Either install latex to your local machine or use [Overleaf](https://overleaf.com). You can download all necessary project files here (COMING SOON).

### Preparation & Setup
* Clone this repository or download as ZIP (Code -> Download ZIP) and unzip.
* Install [python3 (bundled with pip)](https://www.python.org/) if not already installed.
* Open a terminal / cmd and open the project folder with the downloaded files
* install required packages with ```pip install -r requirements.txt```


### Use this tool to convert your posts
* Open a terminal / cmd and open the project folder with the downloaded files
* Execute ```cd src```
* Execute ```python -m blog2journal <path>```, replace \<path> with the path to your downloaded csv.
* Move/Upload all generated .tex files to the articles folder in your latex project and copy/paste all include commands from the includes_list.txt to your main.tex
* You're done!