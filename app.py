import pandas as pd

from pathlib import Path
from shiny import App, reactive, render, ui


infile = Path(__file__).parent / "disc-data.csv"
df = pd.read_csv(infile)
df = df.replace(r"\n", " ", regex=True)


app_ui = ui.page_fluid(
    ui.panel_title("Disc Finder", "Disc Finder"),
    ui.input_action_button("show", "What is this page?"),
    ui.input_slider(
        "speed",
        "Speed",
        min=df["SPEED"].min(),
        max=df["SPEED"].max(),
        value=5,
        step=0.5,
    ),
    ui.input_slider(
        "stability",
        "Stability",
        min=df["STABILITY"].min(),
        max=df["STABILITY"].max(),
        value=0,
        step=0.1,
    ),
    ui.input_checkbox("beaded", "Beaded", True),
    ui.input_checkbox("not_beaded", "No Bead", True),
    ui.output_table("result"),
)


def server(input, output, session):
    @reactive.Effect
    @reactive.event(input.show)
    def _():
        m = ui.modal(
            "This page helps disc golfers find discs based on speed and stability, or rather how far the disc travels through the air and its flight path. The beaded/not beaded filters remove discs that have a shape that some users have a preference for or against.",
            easy_close=True,
            footer=None,
        )
        ui.modal_show(m)

    @output
    @render.table
    def result():
        speed_mask = df["SPEED"] == input.speed()
        stability_mask = df["STABILITY"] == input.stability()
        beaded_mask = df["BEAD"] == "Yes"
        not_beaded_mask = df["BEAD"] == "No"

        if input.not_beaded() & input.beaded():
            return df[speed_mask & stability_mask]
        if input.beaded():
            if input.not_beaded():  # needed to cover unselecting/reselecting
                return df[speed_mask & stability_mask]
            else:
                return df[speed_mask & stability_mask & beaded_mask]
        elif input.not_beaded():
            if input.beaded():  # needed to cover unselecting/reselecting
                return df[speed_mask & stability_mask]
            else:
                return df[speed_mask & stability_mask & not_beaded_mask]
        else:
            return df[speed_mask & stability_mask]


app = App(app_ui, server, debug=True)
