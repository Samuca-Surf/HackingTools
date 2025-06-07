
url=$1

echo "===================="
echo "Analizando $1"
echo "===================="

wget $1

grep "href" index.html > saida
grep "http" saida | cut -d "/" -f 3 | grep "\." | grep -v " " | sort -u > dominios

for domain in $(cat dominios)
do
    host $domain | grep -v "not found"
done