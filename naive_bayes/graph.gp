set title 'Wine recognition dataset'
set grid
set term png
set encoding utf8

rgb(r,g,b) = 65536 * int(r) + 256 * int(g) + int(b)
color0=rgb(255,0,0)
color1=rgb(0,255,0)
color2=rgb(0,0,255)
get_color(x) = x==0 ? color0 : x==1 ? color1 : color2

set xlabel 'Alcohol'
set ylabel 'Malic acid'
set output 'alcohol__malic_acid.png'
plot 'alcohol__malic_acid.csv' using 1:2:(get_color($3)) w p lc rgb variable pointtype 7 title ""

set xlabel 'Ash'
set ylabel 'Alcalinity of ash'
set output 'ash__alcalinity_of_ash.png'
plot 'ash__alcalinity_of_ash.csv' using 1:2:(get_color($3)) w p lc rgb variable pointtype 7 title ""

set xlabel 'Magnesium'
set ylabel 'Total phenols'
set output 'magnesium__total_phenols.png'
plot 'magnesium__total_phenols.csv' using 1:2:(get_color($3)) w p lc rgb variable pointtype 7 title ""

set xlabel 'Flavanoids'
set ylabel 'Nonflavanoid phenols'
set output 'flavanoids__nonflavanoid_phenols.png'
plot 'flavanoids__nonflavanoid_phenols.csv' using 1:2:(get_color($3)) w p lc rgb variable pointtype 7 title ""

set xlabel 'Proanthocyanins'
set ylabel 'Color intensity'
set output 'proanthocyanins__color_intensity.png'
plot 'proanthocyanins__color_intensity.csv' using 1:2:(get_color($3)) w p lc rgb variable pointtype 7 title ""

set xlabel 'Hue'
set ylabel 'OD280/OD315 of diluted wines'
set output 'hue__od280-od315_of_diluted_wines.png'
plot 'hue__od280-od315_of_diluted_wines.csv' using 1:2:(get_color($3)) w p lc rgb variable pointtype 7 title ""
