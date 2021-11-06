# Rule 110 written in Ruby
c=[0]*41
eval"[#{gets}].map{|i|c[i]=1}"+'
c=(0..39).map{|x|putc" X"[u=c[x]]
110[4*c[x-1]+2*u+c[x+1]]}<<0;puts'*40
