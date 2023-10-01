
# Amaç : Çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
# Key'ler orginal değerler value ise değiştirilmiştir değerler olacaktır.

number = range(10)
new_dict = {}

{n: n ** 2 for n in number if n % 2 == 0}
