text = """hm al, mo tmh hm al, huvh gn hul jzlnhgmt:
qulhulo 'hgn tmaxlo gt hul cgty hm nzrrlo
hul nxgtsn vty voomqn mr mzhovslmzn rmohztl,
mo hm hvel vocn vsvgtnh v nlv mr homzaxln
vty ak mppmngts lty hulc?
hm ygl: hm nxllp;
tm cmol; vty, ak v nxllp hm nvk ql lty
hul ulvoh-vwul vty hul humznvty tvhzovx numwen
huvh rxlnu gn ulgo hm, 'hgn v wmtnzccvhgmt
yldmzhxk hm al qgnu'y. hm ygl, hm nxllp;
hm nxllp: plowuvtwl hm yolvc: vk, hulol'n hul oza;
rmo gt huvh nxllp mr ylvhu quvh yolvcn cvk wmcl
qult ql uvdl nuzrrxly mrr hugn cmohvx wmgx,
cznh sgdl zn pvznl"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

def count_chars(text):
    for char in alphabet:
        print((char, text.count(char)))


if __name__ == "__main__":
    count_chars(text)