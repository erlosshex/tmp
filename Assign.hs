-- file: Assign.hs

myAdd a b c=let x=a+b
                y=b+c
		z=c+a
	    in x+y+z


myDrop n xs =
    if n<=0 || null xs
    then xs
    else myDrop (n-1) (tail xs)