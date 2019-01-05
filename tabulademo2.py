import tabula


# Read remote pdf into DataFrame
df2 = tabula.read_pdf("E:\\report_100000_1.pdf")

# convert PDF into CSV
tabula.convert_into("E:\\report_100000_1.pdf", "output.csv", output_format="csv")