# from django_presentation import forms
from django_presentation.forms import *
# from django_presentation.forms import FormPresentation

class FP(FormPresentation):
    test2=Input()
    but1=Button()
    test=Input()
    but2=Button()


def test_presentation():
    # asdhf
    # assert repr(dir(django_presentation.form))=='asdf'
    p=FP()
    # raise Exception('test')
    assert p.draw()=='a'
    # assert 1==0