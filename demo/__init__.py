import os
import sys
import time

import requests
import NIA_image2table.util
import NIA_image2table.tables_detection
import NIA_image2table.cells_detection
import NIA_image2table.ocr_image
import NIA_image2table.ocr_to_csv




def convert(img_file, reader):
    image_tables = NIA_image2table.tables_detection.extract_table(img_file)
    #print("Extracted the following tables from the image:")
    #print(image_tables,"\n")

    for image, tables in image_tables:
        #print(f"Processing tables for {image}.")

        for table in tables:
            #print(f"Processing table {table}.")
            cells = NIA_image2table.cells_detection.extract_cell(table)

            ocr = [
                NIA_image2table.ocr_image.ocr_images(cell, reader)
                for cell in cells
            ]
            #print("Extracted {} cells from {}".format(len(ocr), table))
            #print("Cells:")
            for c, o in zip(cells[:3], ocr[:3]):
                with open(o) as ocr_file:
                    # Tesseract puts line feeds at end of text.
                    # Stript it out.
                    text = ocr_file.read().strip()
                    #print("{}: {}".format(c, text))
            # If we have more than 3 cells (likely), print an ellipses
            # to show that we are truncating output for the demo.
            """
            if len(cells) > 3:
                print("...",'\n')
            """
            #csv_value, html_string_return = NIA_image2table.ocr_to_csv.text_files_to_csv(ocr,table)
            #print('\n',"Here is the entire CSV output:",'',csv_value,sep='\n')
            html_string_return = NIA_image2table.ocr_to_csv.text_files_to_csv(ocr, table)


        return html_string_return
