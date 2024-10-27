-- Function to create a three dimensional table with a range of n for each set
function threeDTable(n)
	local t = {}
	for i = 1, n do
		t[i] = {}
		for j = 1, n do
			t[i][j] = {}
			for k = 1, n do
				t[i][j][k] = i + j + k
			end
		end
	end
	return t
end	

