import customtkinter as ctk
from Services.currencyConverter import CurrencyConverter
from Services.nbpExchangeRateProvider import NbpExchangeRateProvider
from DTOs.exchangeRate import ExchangeRate

class GuiApp(ctk.CTk):
    def __init__(self, provider: NbpExchangeRateProvider, converter: CurrencyConverter):
        super().__init__()
        self._provider = provider
        self._converter = converter
        self._table = None 

        self.title("Kalkulator Walut NBP")
        self.geometry("400x350")

        self._init_ui()
        self._load_data()

    def _init_ui(self):
        self.lbl_amount = ctk.CTkLabel(self, text="Kwota:")
        self.lbl_amount.pack(pady=5)
        
        self.entry_amount = ctk.CTkEntry(self)
        self.entry_amount.pack(pady=5)

        self.lbl_from = ctk.CTkLabel(self, text="Z waluty:")
        self.lbl_from.pack(pady=5)
        
        self.combo_from = ctk.CTkComboBox(
            self, 
            values=[]
        )
        self.combo_from.pack(pady=5)

        self.lbl_to = ctk.CTkLabel(self, text="Na walutę:")
        self.lbl_to.pack(pady=5)
        
        self.combo_to = ctk.CTkComboBox(
            self, 
            values=[]
        )
        self.combo_to.pack(pady=5)

        self.btn_calc = ctk.CTkButton(self, text="Przelicz", command=self._calculate)
        self.btn_calc.pack(pady=20)

        self.lbl_result = ctk.CTkLabel(self, text="Wynik: ---", font=("Arial", 18))
        self.lbl_result.pack(pady=10)

    def _load_data(self):
        try:
            self._table = self._provider.get_exchange_rate_table()
            
            rates_codes = sorted([r.code for r in self._table.rates])
            codes = ["PLN"] + rates_codes
            
            self.combo_from.configure(values=codes)
            self.combo_to.configure(values=codes)
            
            self.combo_from.set("PLN")
            self.combo_to.set("USD")
            
        except Exception as e:
            self.lbl_result.configure(text=f"Błąd połączenia!", text_color="red")
            print(f"DEBUG ERROR: {e}") 

    def _calculate(self):
        try:
            input_val = self.entry_amount.get()
            input_val = input_val.replace(',', '.')
            
            amount = float(input_val)
            code_from = self.combo_from.get()
            code_to = self.combo_to.get()

            if self._table is None:
                 self.lbl_result.configure(text="Brak danych NBP", text_color="red")
                 return

            rate_from = self._find_rate(code_from)
            rate_to = self._find_rate(code_to)

            if rate_from and rate_to:
                result = self._converter.convert(amount, rate_from, rate_to)
                self.lbl_result.configure(text=f"{result:.2f} {code_to}", text_color="white")
            else:
                 self.lbl_result.configure(text="Błąd waluty", text_color="red")

        except ValueError:
            self.lbl_result.configure(text="Błędna kwota", text_color="red")

    def _find_rate(self, code):
        if code == "PLN":
            return ExchangeRate("Złoty", "PLN", 1.0)
        return self._table.getRateByCode(code)
    
    def run(self):
        self.mainloop()