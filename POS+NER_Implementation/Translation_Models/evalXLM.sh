src=$1
model=$2

sh inferPre.sh sum \
               $src \
               ../$model/codes \
               ../$model/vocab \
               ../$model/evaluate.sum.bpe

cat ../$model/evaluate.sum.bpe | \
        python translate.py --exp_name XLMinfer123 \
        --src_lang sum --tgt_lang en \
        --model_path ../$model/checkpoint.pt --output_path $out
