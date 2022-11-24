"""
File: babygraphics.py
Name: Thomas
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    space = (width - 2*GRAPH_MARGIN_SIZE) / len(YEARS)
    return int(GRAPH_MARGIN_SIZE + space * year_index)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    x0 = y0 = 0
    for i in range(len(lookup_names)):  # Loop over lookup_names.
        for j in range(len(YEARS)):  # Loop over YEARS.
            # If a names with matching YEARS was found, read rank, calculate y coordinate.
            if str(YEARS[j]) in name_data[lookup_names[i]]:
                rank = name_data[lookup_names[i]][str(YEARS[j])]
                y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(rank)
            # If no matching years was found, sets rank as '*', and also sets y coordinate.
            else:
                rank = '*'
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            x = get_x_coordinate(CANVAS_WIDTH, j)  # Calculate x coordinate.
            canvas.create_text(x + TEXT_DX, y, text=str(lookup_names[i]) + " " + rank, anchor=tkinter.SW,
                               fill=COLORS[(i + len(COLORS)) % len(COLORS)])
            if j > 0:  # Create lines.
                canvas.create_line(x0, y0, x, y, width=LINE_WIDTH, fill=COLORS[(i + len(COLORS)) % len(COLORS)])
            x0 = x
            y0 = y
    """
    # The first method I wrote, by creating a new dic including all the years' ranking, 
    # and then create lines in the second step, but is a little bit more complicated than the previous method.
    for i in range(len(lookup_names)):
        for key in name_data:
            if lookup_names[i] == key:
                name_data1 = {}
                count = 0
                for j in range(len(YEARS)):
                    switch = False
                    for year in name_data[key]:
                        if int(YEARS[j]) == int(year):
                            switch = True
                            name_data1[YEARS[j]] = name_data[key][year]
                        if not switch:
                            name_data1[YEARS[j]] = '*'
                x1 = get_x_coordinate(CANVAS_WIDTH, 0)
                if name_data1[YEARS[0]] == '*':
                    y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    y1 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(name_data1[YEARS[0]])
                for year1 in name_data1:
                    x2 = get_x_coordinate(CANVAS_WIDTH, count)
                    if name_data1[year1] == '*':
                        y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    else:
                        y2 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(name_data1[year1])
                    canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[(i+len(COLORS)) % len(COLORS)])
                    canvas.create_text(x2+TEXT_DX, y2, text=key + " " + name_data1[year1], anchor=tkinter.SW,
                                       fill=COLORS[(i+len(COLORS)) % len(COLORS)])
                    count += 1
                    x1 = x2
                    y1 = y2
    """


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
