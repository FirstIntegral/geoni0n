import csv
from shapely import wkt
from shapely.geometry import MultiPolygon, Polygon
import tkinter as tk
from tkinter import filedialog


# Creating a function to open the file dialog
def open_file_dialog():
    file_path = filedialog.askopenfilename()

    if file_path.endswith(".csv"):
        process_file(file_path)
        root.destroy()

    else:
        print("Not a .csv file. Please select a .csv file.")


# Creating a function to process the CSV file
def process_file(file_path):
    with open(file_path, "r") as csv_file:
        content = csv.reader(csv_file)

        polygons = []

        for shape in content:
            polygon_wkt = shape[0]
            # Making the shape string from the .csv file into a geometry object to perform operations on it later
            polygon = wkt.loads(polygon_wkt)

            # Making sure it's either a polygon or a multipolygon and not a point, or line.
            if not isinstance(polygon, (Polygon, MultiPolygon)):
                print(f"Unsupported geometry type: {type(polygon).__name__}")
                continue

            # Checking validity of the shape
            if not polygon.is_valid:
                print(f"Invalid shape: {polygon_wkt}")

                # If invalid, attempting to fix the invalid polygon using the buffer method
                polygon = polygon.buffer(0)
                if not polygon.is_valid:
                    print(f"Shape couldn't be fixed for: {polygon_wkt}")
                    continue

                print(f"Fixed shape for: {polygon_wkt}")

            polygons.append(polygon)

        if not polygons:
            print("No valid polygons found in the file.")
            return

        # Computing the convex hull union of the polygons
        multipolygon = MultiPolygon(polygons)
        convex_hull = multipolygon.convex_hull
        print("Convex hull union (WKT):", convex_hull)


root = tk.Tk()
root.title("geoni0n")

open_file_button = tk.Button(root, text="Open File", command=open_file_dialog)
open_file_button.pack()

root.mainloop()
