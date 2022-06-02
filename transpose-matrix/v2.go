package main

func transpose(matrix [][]int) [][]int {
	ret := make([][]int, len(matrix[0]))
	for i := 0; i < len(matrix[0]); i++ {
		ret[i] = make([]int, len(matrix))
		for j := 0; j < len(matrix); j++ {
			ret[i][j] = matrix[j][i]
		}
	}
	return ret
}

// Runtime: 16 ms, faster than 21.57% of Go online submissions for Transpose Matrix.
// Memory Usage: 6.8 MB, less than 7.84% of Go online submissions for Transpose Matrix.
