Here are my findings:

Firstly, I experimented with different pool sizes and found out that increasing the pool size did not help.
In fact, it make the accuracy worse. Same applies for decreasing the pool size.
In addition, adding another hidden layer to the network did not help as the accuracy refused to grow within 10 epochs.

Furthermore, changing the size of the learning kernel improved the accuracy with all other variables constant.
I found that increasing the kernel size from 3x3 to 9x9 improved the accuracy by a lot.
Similarly, increasing the size of the hidden layer helped bring the accuracy up by a considerable amount but te training took longer and the process had diminishing returns.
To add, I found that adding another hidden layer beyond the 1 hidden layer did not help much.  
However, experimenting with the dropout option helped a lot. I found that lowering it yielded better results.

