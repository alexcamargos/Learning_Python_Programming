#!/usr/bin/env python
# encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: dolar_ptax_gui.py
# Version: 0.0.1
#
# Summary: Consumindo a API Dólar comercial (venda e compra) - cotações diárias
#          disponibilizada pelo Portal Brasileiro de Dados Abertos do Banco Central.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""Dólar Ptax é a média aritmética das taxas obtidas em quatro consultas diárias de câmbio."""

import re
import tkinter
from datetime import date
from tkinter import ttk

import dolar_ptax_bacen_api_consumer


class DolarPtaxRealTimeCurrencyConverter:
    def __init__(self, day, valor_dolar_ptax_compra):
        self.day = day
        self.valor_dolar_ptax_compra = valor_dolar_ptax_compra

    def convert(self, amount):
        valor_reais = self.valor_dolar_ptax_compra * amount

        return round(valor_reais, 2)


class CurrencyConverterGUI(tkinter.Tk):
    def __init__(self, dolar_ptax_converter):

        # Create instance
        super(CurrencyConverterGUI, self).__init__()

        # Set a title.
        self.title('Real Time Dólar Ptax Converter')

        # Set windows geometry.
        self.geometry('500x300')

        self.currency_converter = dolar_ptax_converter

        # Intro tkinter.Label
        self.intro_label = tkinter.Label(self,
                                         text='Welcome to Real Time Dólar Ptax Converter',
                                         bg='blue',
                                         fg='white',
                                         padx=10,
                                         pady=10,
                                         borderwidth=0)
        self.intro_label.config(font=('Cambria', 17, 'bold'))
        self.intro_label.place(x=10, y=5)

        # Information tkinter.Label
        self.information_label = tkinter.Label(self,
                                               text=f'1 Dólar americano igual a '
                                                    f'{self.currency_converter.valor_dolar_ptax_compra :.2f} '
                                                    f'Real brasileiro\n'
                                                    f'Date: {self.currency_converter.day}',
                                               padx=20,
                                               pady=20,
                                               borderwidth=5)
        self.information_label.config(font=('Calibri', 16, 'bold'))

        self.information_label.place(x=10, y=60)

        # Entry box tkinter.Entry
        valid = (self.register(self.restrict_number_only), '%d', '%P')
        self.amount_field = tkinter.Entry(self,
                                          bd=3,
                                          relief=tkinter.RIDGE,
                                          justify=tkinter.CENTER,
                                          validate='key',
                                          validatecommand=valid)
        self.amount_field.place(x=30, y=180)

        self.converted_amount_field_label = tkinter.Label(self,
                                                          text='',
                                                          fg='black',
                                                          bg='white',
                                                          relief=tkinter.RIDGE,
                                                          justify=tkinter.CENTER,
                                                          width=17,
                                                          borderwidth=3)
        self.converted_amount_field_label.place(x=346, y=180)

        # From currency ttk.Combobox
        self.from_currency_variable = tkinter.StringVar(self)
        self.from_currency_variable.set('USD - EUA')
        self.to_currency_variable = tkinter.StringVar(self)
        self.to_currency_variable.set('BRL - Brazil')

        font = ('Calibre', 12, 'bold')
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self,
                                                   textvariable=self.from_currency_variable,
                                                   values=['USD - EUA'],
                                                   font=font,
                                                   state='readonly',
                                                   width=12,
                                                   justify=tkinter.CENTER)
        self.from_currency_dropdown.place(x=30, y=150)

        # To currency ttk.Combobox
        self.to_currency_dropdown = ttk.Combobox(self,
                                                 textvariable=self.to_currency_variable,
                                                 values=['BRL - Brazil'],
                                                 font=font,
                                                 state='readonly',
                                                 width=12,
                                                 justify=tkinter.CENTER)
        self.to_currency_dropdown.place(x=340, y=150)

        # Convert tkinter.Button
        self.convert_button = tkinter.Button(self, text='Convert', fg='black', command=self.perform_conversion)
        self.convert_button.config(font=('Calibre', 10, 'bold'))
        self.convert_button.place(x=225, y=160)

        self.notes_info_label= tkinter.Label(self,
                                             text='O cálculo efetuado tem caráter informativo e não '
                                                  'substitui as disposições\nda norma cambial brasileira '
                                                  'para casos específicos de conversão.',
                                             padx=20,
                                             pady=20,
                                             borderwidth=5)
        self.notes_info_label.config(font=('Cambria', 10), justify='left')
        self.notes_info_label.place(x=0, y=240)

    def perform_conversion(self):
        amount = float(self.amount_field.get())
        # from_converted = self.from_currency_dropdown.get()
        # to_converted = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(amount)
        self.converted_amount_field_label.config(text=str(converted_amount))

    @staticmethod
    def restrict_number_only(action, string):
        regex = re.compile(r'[0-9,]*?(\.)?[0-9,]*$')
        result = regex.match(string)

        return string == '' or string.count('.') <= 1 and result is not None


def main():
    # today = date.today()
    today = date(2021, 3, 26)

    cotacao = dolar_ptax_bacen_api_consumer.DolarPtaxBacen(mode=dolar_ptax_bacen_api_consumer.ModosConsulta.por_dia,
                                                           data_cotacao=today)

    real_time_currency_converter = DolarPtaxRealTimeCurrencyConverter(today, cotacao.valor_compra)

    dolar_ptax_converter_gui = CurrencyConverterGUI(real_time_currency_converter)

    dolar_ptax_converter_gui.mainloop()


if __name__ == '__main__':
    main()
