#!/bin/sh

mkdir -p /usr/share/texmf/tex/latex/fontawesome/
mkdir -p /usr/share/texmf-dist/tex/latex/fontawesome/
cp CTAN/fontawesome.sty /usr/share/texmf/tex/latex/fontawesome/
cp CTAN/fontawesome.sty /usr/share/texmf-dist/tex/latex/fontawesome/

mkdir -p /usr/share/texmf-dist/fonts/opentype/public/fontawesome/
cp CTAN/FontAwesome.otf /usr/share/texmf-dist/fonts/opentype/public/fontawesome/
