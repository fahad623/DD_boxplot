vw train.vw -c --passes 300 -b 24 --oaa 25 -f model.vw --loss_function logistic
vw test.vw -t -i model.vw -p preds.txt
vw test.vw -t -i model.vw -p preds.txt -r raw.txt


~/code/vowpal_wabbit/utl/vw-hypersearch -L 1e-10 0.1 vw train.vw -c --passes 300 -b 24 --oaa 25 -f l2_model.vw --loss_function logistic --l2 %

holdout off - 
vw train.vw -c --passes 41 -b 24 --oaa 25 -f model.vw --holdout_off --loss_function logistic