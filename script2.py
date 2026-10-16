# question 3
from plotnine import ggplot, aes, geom_point, ggtitle
import pandas as pd
import argparse

# a)
df = pd.read_csv("cnv_data.csv")
# print(df.head())
# print(df.columns) # just checking for data structure

plot = (
    ggplot(df, aes(x="position_mb", y="log2_ratio"))
           + geom_point() # defines scatterplot
)
plot.show()

# b)
plot.save("plot.png")

# c)
parser = argparse.ArgumentParser(description="Read a csv file and create a scatterplot.")
# this reads the command line. description is text that shows up if you run python script.py -h
parser.add_argument('--input', required=True, help='Path to the input csv file')
parser.add_argument('--output', required=True, help='Path to output plot file')
# this tells parser that the script expects two arguments
args = parser.parse_args()
# this reads what was typed and stores it in args

df = pd.read_csv(args.input)

plot2 = (
    ggplot(df, aes(x="position_mb", y="log2_ratio"))
           + geom_point() # defines scatterplot
)
plot2.show()
plot2.save(args.output)