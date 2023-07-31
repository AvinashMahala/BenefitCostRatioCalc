#This file will contain the Homepage class.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import uuid

class Homepage(ttk.Frame):
    def __init__(self, master=None, notebook=None):
        super().__init__(master)
        self.notebook = notebook
        self.create_widgets()
        self.uuid=""
        self.bridgeId=""

    def create_widgets(self):
        self.start_calculation_area = ttk.LabelFrame(self, text="Start Calculation Area")
        self.start_calculation_area.pack(fill="both", expand=True)
        self.bridge_id_entry = ttk.Entry(self.start_calculation_area)
        self.bridge_id_entry.pack()
        self.calculation_button = ttk.Button(self.start_calculation_area, text="Generate Unique Calculation", command=self.generate_calculation)
        self.calculation_button.pack()

    def generate_calculation(self):
        bridge_id = self.bridge_id_entry.get()
        unique_id = str(uuid.uuid4())
        self.uuid=unique_id
        self.bridgeId=bridge_id
        self.master.database.insert_calculation_metadata(bridge_id, unique_id)
        self.master.activate_tabs(bridge_id, unique_id)
        self.master.show_msg(f"Successfully stored the Bridge ID: {bridge_id} and UUID: {unique_id}")

