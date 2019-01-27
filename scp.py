from subprocess import call
import sys

for argument in sys.argv:
    if argument.endswith('/'):
        copy = "scp -r -P 5022 "+argument+" ndalctes@world-305.fr.planethoster.net:/home/ndalctes/public_html/dev/dmn"
    else
        copy = "scp -P 5022 "+argument+" ndalctes@world-305.fr.planethoster.net:/home/ndalctes/public_html/dev/dmn"

    call(copy)
    