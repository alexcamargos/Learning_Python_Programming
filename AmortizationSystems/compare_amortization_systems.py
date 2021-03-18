#  #!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: compare_amortization_systems.py
#  Version: 0.0.1
#  Summary: Para que a dívida seja totalmente paga, o tomador deve quitar o montante inicial adicionado aos juros
#  acrescidos. A forma como o valor total do saldo devedor será calculado é definida de acordo com o sistema de
#  amortização aplicado. Ele caracteriza como a dívida vai ser diminuída até chegar a sua total liquidação.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#
#  --------------------------------------------------------------------------------------------------------------------

import argparse

from main import main_cli
from main import main_gui

def main():
    """Compare Amortization Systems SAC and Price table main function."""

    parser = argparse.ArgumentParser()
    parser.add_argument('-g',
                        '--gui',
                        action='store_true',
                        help="Run Compare Amortization SAC Systems and price list in GUI mode.")
    parser.add_argument('-c',
                        '--cli',
                        action='store_true',
                        help="Run Compare Amortization SAC Systems and price list in CLI mode.")

    args = parser.parse_args()
    if args.gui:
        main_gui()
    else:
        main_cli()


if __name__ == '__main__':
    main()
