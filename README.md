# Academic Figure Guide
Han's personal experience on generating academic figures for publications.

## General Rules

1. Use vector graph whenever it is possible.

    There are basically two types of figure format. One is *vector* (e.g., svg, eps) and the other one is *bitmap* (e.g., jpg, png). 
    We should use *vector* format whenever it is possible, since it is relatively lightweight and does not get pixelated when zoomed in. 
    An example is provided in `examples/eps-vs-png`. In this example, we compare the same matplotlib figure in *.eps* and *.png* format. 
    We also provide a brief guide on how we can include *.eps* figures in our latex document. 

    Note that if the figure you use is taken by a camera, then it is not necessary to transform it to vector map unless you want to reduce document size.

1. Font consistency.

    The font of text in figures should always match the font of the main text. 
    There are basically three ways to ensure font consistency. 
    1. When generating the figures, make sure the font matches. For example, in *matplotlib*, we can actually use latex to generate all the text. See `examples/pyplot-latex-font`.
    1. Generate figures without text, and manually add text in latex later. We will use latex package [*overpic*](http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/overpic/overpic.pdf) for this purpose. An example is provided in `examples/overpic`. 
    1. Sometimes you can just "draw" the figure in latex using [the *tikz* package](https://www.overleaf.com/learn/latex/TikZ_package).

1. Print-ability.

    After you finished a paper draft, print it out in black-and-white to see if the figures look strange when printed out this way. 

## Stylish Elements 
The items listed below are more about personal preference.

1. Where should we put figures in our paper.

    In my opinion, besides the evaluation section, we should also put figures in our paper wherever it can help readers understand the content. For example, in [this paper](https://arc.cs.rutgers.edu/files/FenHanGaoYuRSS19.pdf), several figures are included to clarify the problem definition and algorithm structure.

1. Color.

    Apart from black, three colors I often use are green, light blue, and orange (see Fig.2 in [this paper](https://arxiv.org/pdf/1904.02598.pdf)). The resulting figure often looks good in terms of coloring. 

## Detailed Instructions to Every Type of Figure (unfinished)

1. Image taken by a camera. 

1. Illustrational figures.

    1. 3rd party software, e.g., 
    [Adobe Illustrator](https://www.adobe.com/products/illustrator.html) ($20 per month),
    [Gravit Designer](https://designer.gravit.io/) (free).
    1. [Tikz](https://www.overleaf.com/learn/latex/TikZ_package).

1. Plots in the evaluation section.
