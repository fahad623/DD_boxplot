vw train.vw -c --passes 300 -b 24 --oaa 3 -f model.vw --loss_function logistic
vw test.vw -t -i model.vw -p preds.txt
vw test.vw -t -i model.vw -p preds.txt -r raw.txt

vw test.vw -t -i model.vw --bootstrap 100 -p preds.txt -r raw.txt
vw train.vw -c --passes 300 -b 24 --oaa 3 -f model.vw --loss_function logistic --bootstrap 100

holdout off - 
vw train.vw -c --passes 16 -b 24 --oaa 3 -f model.vw --holdout_off --loss_function logistic
weight - custom
average loss = 1.669e-06

holdout off - 
vw train.vw -c --passes 300 -b 24 --oaa 3 -f model.vw --holdout_off --loss_function logistic
weight - 50000
average loss = 1.669e-06

holdout off - 
vw train.vw -c --passes 19 -b 24 --oaa 3 -f model.vw --holdout_off --loss_function logistic
weight - 5
average loss = 0.0103

holdout off - 
vw train.vw -c --passes 13 -b 24 --oaa 3 -f model.vw --holdout_off --loss_function logistic
weight - 3
average loss = 0.01175

holdout off - 
vw train.vw -c --passes 24 -b 24 --oaa 3 -f model.vw --holdout_off --loss_function logistic
weight - 2
average loss = 0.0114

holdout off - 
vw train.vw -c --passes 23 -b 24 --oaa 3 -f model.vw --holdout_off --loss_function logistic
weight - 1
average loss = 0.01255

L2 regularization - 
~/code/vowpal_wabbit/utl/vw-hypersearch -L 1e-10 1e-6 vw train.vw -c -k --passes 300 -b 24 --oaa 3 -f l1_model.vw --loss_function logistic --l2 %

L1 regularization - 
~/code/vowpal_wabbit/utl/vw-hypersearch -L 1e-10 1e-6 vw train.vw -c -k --passes 300 -b 24 --oaa 3 -f l1_model.vw --loss_function logistic --l1 %
8.27867e-10	0.0112147   weight-2
1.72214e-09	0.00868658  weight-9
7.73649e-09	0.0114339   weight-3

vw train.vw -c --passes 300 -b 24 --oaa 3 -f l1_model.vw --loss_function logistic --l1 7.73649e-09
vw train.vw -c --passes 22 -b 24 --oaa 3 -f l1_model.vw --holdout_off --loss_function logistic --l1 7.73649e-09
weight - 3
average loss = 0.01117


Train on reduced features - 
~/code/vowpal_wabbit/utl/vw-hypersearch -L 1e-10 1e-6 vw train.vw -c -k --passes 300 -b 24 --oaa 3 --feature_mask l1_model.vw -f l2_model.vw --loss_function logistic --l2 %
1.72214e-09	0.0115144 weight -3
vw train.vw -c --passes 300 -b 24 --oaa 3 --feature_mask l1_model.vw -f model.vw --loss_function logistic --l2 1.72214e-09 

vw train.vw -c --passes 5 -b 24 --oaa 3 --holdout_off --feature_mask l1_model.vw -f model.vw --loss_function logistic --l2 1.72214e-09 