# Academic Figure Guide
Han's personal experience on generating academic figures for publications.

## General Rules

1. Use vector graph whenever it is possible.

    There are basically two types of figure format. One is *vector* (e.g., svg, eps) and the other one is *bitmap* (e.g., jpg, png). 
    When we write papers, we should use *vector* format whenever it is possible, since it is relatively lightweight and does not get pixelated when zoomed in. 
    An example is provided in `examples/eps-vs-png`. In this example, we compare the same matplotlib figure in *.eps* and *.png* format. 
    We also provide a brief guide on how we can include *.eps* figures in our latex document. 

    Note that if the figure you use is taken by a camera, then it is not necessary to transform it to vector map, since it will get pixelated anyway.

1. Font consistency.

    In my opinion, if there is any text in the figure, its font should always match the font in latex. 
    There are basically two ways to ensure font consistency. 
    1. When generating the figures, make sure the font matches. For example, in *matplotlib*, we can actually use latex to generate all the text. See `examples/pyplot-latex-font`

1. Print-ability.

    After you finished a paper draft, print it out in black-and-white to see if the figures look strange when printed out this way. 

## Stylish Elements
The items listed below are more about personal preference. But these elements do affect how readers feel about the article.
1. Where should we put figures in our paper.
1. Color.

## Detailed Instructions to Every Type of Figure
1. Image taken by a camera. 
1. Illustrational figures.
    1. 3rd party software.
    1. plot.
1. Plots.