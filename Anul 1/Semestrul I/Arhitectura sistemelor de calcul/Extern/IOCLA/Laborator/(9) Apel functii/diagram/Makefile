DIA = dia
INKSCAPE = inkscape
EPSTOPDF = epstopdf

DIA_FILES = stack-in-function-call.dia
SVG_FILES =
EPS_FILES = $(DIA_FILES:.dia=.eps) $(SVG_FILES:.svg=.eps)
PDF_FILES = $(DIA_FILES:.dia=.pdf) $(SVG_FILES:.svg=.pdf)
PNG_FILES = $(DIA_FILES:.dia=.png) $(SVG_FILES:.svg=.png)

.PHONY: all clean

all: $(PDF_FILES) $(PNG_FILES)

%.pdf: %.eps
	$(EPSTOPDF) $<

%.eps: %.dia
	$(DIA) -t eps-pango -e $@ $<

%.png: %.dia
	$(DIA) -t png -e $@ $<

%.eps: %.svg
	$(INKSCAPE) -E $@ $<

%.png: %.svg
	$(INKSCAPE) -e $@ $<

clean:
	-rm -f $(EPS_FILES) $(PDF_FILES) $(PNG_FILES)
