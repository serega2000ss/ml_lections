set title 'Diabets Regression'
set ylabel 'Disease progression'
set xlabel 'Body mass index [2]'
set grid
set term png
set output 'diabets_2.png'
plot 'diabets_2_train.csv' with points pointtype 1 title "Train", \
'diabets_2_test.csv' with points pointtype 7 lc rgb "green" title "Test", \
'diabets_2_pred.csv' with points pointtype 5 lc rgb "red" title "Prediction", \
'diabets_2_pred.csv' with lines lc rgb "red" title "Prediction"
