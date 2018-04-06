FONTS=$(ls ./*.ttf)

mkdir ./fb-reports

for font in $FONTS
do
    out_dir=$(basename $font .ttf);
    out_file="./fb-reports/$out_dir.txt";
    fontbakery check-googlefonts $font -l FAIL -C > $out_file
    diffbrowsers $font -fb $font -v glyphs-all -pt 16 -gif -o $out_dir;
done