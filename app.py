from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar


app = Flask(__name__, static_folder="templates")


def bar_base():
    c = (
        Bar()
        .add_xaxis(["pippo", "pluto", "paperino", "minnie", "topolino", "paperina"])
        .add_yaxis("A", [randrange(0, 100) for _ in range(6)])
        .add_yaxis("B", [randrange(0, 100) for _ in range(6)])
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-Chart", subtitle="barchart"))
    )
    return c


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()


if __name__ == "__main__":
    app.run()