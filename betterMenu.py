    #!/usr/bin/env python
    # -*-coding: utf8-*-
from __future__ import (absolute_import, division,
                            print_function, unicode_literals)
class Choice(object):
    def __init__(self, desc):
        self.desc = desc
    def on_selection(self, menu, index):
        print("'{}' was selected".format(self.desc))
        return self
class ExitChoice(Choice):
    def on_selection(self, menu, index):
        print("bye")
        raise SystemExit
class Menu(object):
    def __init__(self, question):
        self.question = question
        self.choices = []
    def add_choices(self, choices):
        self.choices.extend(choices)
    def input(self):
        choice_list = "\n".join("    {}) {}".format(i, x.desc) for i, x in enumerate(self.choices, 1))
        s = """{}\n{}\n""".format(self.question, choice_list)
        prompt = "? "
        while True:
            user = input(s + prompt)
            try:
                c = int(user.strip())
                choice = self.choices[c-1]
            except (IndexError, ValueError):
                    prompt = "ERROR: please input an integer in {}..{}\n? ".format(1, len(self.choices))
                    continue
        return choice.on_selection(self, c-1)
    def main(self):
        menu = Menu("Please select an item")
        menu.add_choices([
            Choice('porkchop'), Choice('guera'), Choice('scooter'),
            Choice('houdini'), ExitChoice('exit'),
        ])
        menu.input()
    if __name__ == '__main__':
        main()
    """ my output -->
    Please select an item
        1) porkchop
        2) guera
        3) scooter
        4) houdini
        5) exit
    ? 4
    'houdini' was selected
    """