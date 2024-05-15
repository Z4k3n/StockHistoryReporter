import quantstats as qs 
import customtkinter as ct
import tkinter as tk
from tkinter import messagebox
import os

def show_help():
    message = "Enter the stock ticker corresponding to the company name.\n\n" \
              "Examples:\n" \
              "Facebook Meta - META\n" \
              "Apple - AAPL\n" \
              "Microsoft - MSFT\n" \
              "Tesla - TSLA\n" \
              "Coca-Cola - KO"
    messagebox.showinfo("Help", message)

def generate_report():
    ticker = ticker_entry.get().strip().upper()
    initial_investment = initial_investment_entry.get().strip()

    if ticker == "" or initial_investment == "":
        messagebox.showerror("Error", "Please enter the stock ticker and initial investment amount.")
        return

    try:
        # Extend pandas functionalities from QuantStats
        qs.extend_pandas()

        # Check if a report already exists for the specified ticker
        report_path = os.path.join("reports", f"{ticker}-results.html")
        if os.path.exists(report_path):
            # If a report exists, delete the old report
            os.remove(report_path)
        
        # Download returns for the user-input ticker
        stock = qs.utils.download_returns(ticker)

        # Save the earnings plot to a file
        plot_path = os.path.join("result_charts", f"{ticker}.png")
        stock.plot_earnings(savefig=plot_path, start_balance=float(initial_investment))

        # Generate a snapshot of the ticker's performance
        qs.plots.snapshot(stock, title=f"Earnings of {ticker}")

        # Generate an HTML report with metrics
        qs.reports.html(stock, "SPY", title=f"Earnings of {ticker}", output=report_path, download_filename=report_path)

        messagebox.showinfo("Success", "Report generated successfully.")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate the report:\n{str(e)}")

app = ct.CTk()
app.title("Stock Analyzer v2.0")
app.geometry("400x300")

ticker_label = ct.CTkLabel(app, text="Ticker / Stock Ticker:")
ticker_label.pack(pady=10)

ticker_entry = ct.CTkEntry(app, placeholder_text="E.g., MSFT")
ticker_entry.pack(pady=5)

initial_investment_label = ct.CTkLabel(app, text="Initial investment (USD):")
initial_investment_label.pack(pady=10)

initial_investment_entry = ct.CTkEntry(app, placeholder_text="E.g., 1000")
initial_investment_entry.pack(pady=5)

generate_button = ct.CTkButton(app, text="Generate Report", command=generate_report)
generate_button.pack(pady=20)

help_button = ct.CTkButton(app, text="Help", command=show_help)
help_button.pack(pady=10)

# Disable window resizing by the user
app.resizable(False, False)

app.mainloop()
