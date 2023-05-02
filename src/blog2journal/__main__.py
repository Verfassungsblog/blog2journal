import argparse
import re
import pandas
import pypandoc


def main():
    parser = argparse.ArgumentParser(prog="Blog2Journal",
                                     usage="Create a journal in LaTeX based on your (wordpress) blog posts.")
    parser.add_argument('input_csv')
    args = parser.parse_args()
    print("Loading " + args.input_csv)
    convert(pandas.read_csv(args.input_csv))


def convert(csv_input):
    include_list = ""
    for row in csv_input.itertuples(index=True, name='Pandas'):
        include_list += "\\include{articles/" + row.doi.replace("/", "_") + ".tex}\n"
        process_row(row)

    f = open("include_list.txt", "w")
    f.write(include_list)


def process_row(row):
    print("Converting \"" + row.Title + "\"")

    f = open(str(row.doi.replace("/", "_")) + ".tex", "w")
    beginarticlecommand = "\\beginarticle";
    if not pandas.isnull(row.subheadline):
        beginarticlecommand += "[" + row.subheadline + "]"
    else:
        beginarticlecommand += "[]"
    beginarticlecommand += "{" + row.Title + "}"
    beginarticlecommand += "{" + row.Title + "}"
    beginarticlecommand += "{" + row.author.replace(",", ", ") + "}"
    beginarticlecommand += "{" + row.Permalink + "}"
    beginarticlecommand += "{" + row.doi + "}"
    f.write(beginarticlecommand + "\n" + "\\begin{multicols}{2}\\noindent\n")

    newcontent = ""

    for line in row.Content.split("\n"):
        if line.startswith("<"):
            newcontent += line
        else:
            newcontent += "<p>" + line + "</p>"

    newcontent = pypandoc.convert_text(newcontent, 'tex', format='html')
    newcontent = re.sub(r'(?<!\n)\n(?!\n)', ' ', newcontent)
    newcontent = newcontent.replace("((", "\\footnote{").replace("))", "}")
    newcontent = newcontent.replace("\\subsection", "\\section*")
    newcontent = newcontent.replace("\\texorpdfstring{\\textbf", "\\texorpdfstring{") + "\\\\ \n\n"
    newcontent = newcontent.replace("% \section*", "\\section*")
    f.write(newcontent)
    f.write("\\end{multicols}")


if __name__ == '__main__':
    main()
