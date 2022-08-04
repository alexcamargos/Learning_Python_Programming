#!/usr/bin/env python
#  encoding: utf-8
#
#  ---------------------------------------------------------------------------
#  Name: counting_words_pythonic.py
#  Version: 0.0.1
#  Summary: Write a program to count the frequencies of unique words from standard input,
#           then print them out with their frequencies, ordered most frequent first.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ---------------------------------------------------------------------------

"""

Write a program to count the frequencies of unique words from standard input,
then print them out with their frequencies, ordered most frequent first.

For example, given this input:
    The foo the foo the
    defenestration the

The program should print the following:
    the 4
    foo 2
    defenestration 1

"""

from collections import Counter
from string import punctuation


LOREM_IPSUM = '''Mas devo explicar-lhe como nasceu toda essa ideia equivocada de denunciar um prazer
              e louvar a dor, e lhe darei um relato completo do sistema, expondo os ensinamentos
              reais do grande explorador da verdade, o mestre-construtor. da felicidade humana.
              Ninguém rejeita, não gosta, ou evita o prazer em si, porque é prazer, mas porque
              aqueles que não sabem como buscar prazer encontram racionalmente consequências que são
              extremamente dolorosas. Tampouco há alguém que ame, busque ou deseje obter dor de si
              mesmo, porque é dor, mas ocasionalmente ocorrem circunstâncias em que a labuta e a dor
              podem lhe proporcionar um grande prazer. Para dar um exemplo trivial, qual de nós
              empreende algum exercício físico laborioso, exceto para obter alguma vantagem disso?
              Mas quem tem o direito de criticar um homem que escolhe desfrutar de um prazer que não
              tem consequências irritantes, ou alguém que evita uma dor que não produz prazer
              resultante? Por outro lado, denunciamos com justa indignação e antipatia homens que
              são tão enganados e desmoralizados pelos encantos do prazer do momento, tão cegados
              pelo desejo, que não podem prever a dor e os problemas que estão fadados a acontecer;
              e a culpa igual pertence àqueles que falham em seu dever através da fraqueza da
              vontade, o que é o mesmo que dizer através do encolhimento da labuta e da dor. Esses
              casos são perfeitamente simples e fáceis de distinguir. Em uma hora livre, quando
              nosso poder de escolha é desimpedido e quando nada impede que sejamos capazes de fazer
              o que mais gostamos, todo prazer é para ser bem-vindo e toda dor evitada. Mas, em
              certas circunstâncias, e devido às reivindicações de dever ou às obrigações dos
              negócios, frequentemente ocorrerá que os prazeres devem ser repudiados e os
              aborrecimentos aceitos. O homem sábio, portanto, sempre se atém a esse princípio de
              seleção: rejeita os prazeres para assegurar outros prazeres maiores ou tolera dores
              para evitar dores piores.'''


def counting_words(text: str) -> list:
    """Counting words from text."""

    # List the n most common elements and their counts
    # from the most common to the least.
    return Counter(text.lower().split()).most_common()


if __name__ == '__main__':

    # Remove punctuation from string
    lorem_ipsum = ''.join(char for char in LOREM_IPSUM if char not in punctuation)

    result = counting_words(lorem_ipsum)
    
    for word, count in result:
        print(f'{word} - {count}')
