package v1

type NumMatrix struct {
	m [][]int
}

func Constructor(matrix [][]int) NumMatrix {
	rows := len(matrix)
	cols := len(matrix[0])
	m := make([][]int, rows)
	for i := range matrix {
		m[i] = make([]int, cols)

		psum := 0
		for j := range matrix[i] {
			psum += matrix[i][j]

			valueOfFieldAbove := 0
			if i > 0 {
				valueOfFieldAbove = m[i-1][j]
			}
			// this value is the sum of all cells left and above in the original matrix
			m[i][j] = psum + valueOfFieldAbove
		}
	}

	//for _, row := range m {
	//    fmt.Println(row)
	//}

	return NumMatrix{
		m: m,
	}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	topLeft := 0
	bottomLeft := 0
	topRight := 0

	if row1 > 0 && col1 > 0 {
		topLeft = this.m[row1-1][col1-1]
	}
	if col1 > 0 {
		bottomLeft = this.m[row2][col1-1]
	}
	if row1 > 0 {
		topRight = this.m[row1-1][col2]
	}
	bottomRight := this.m[row2][col2]

	// we accounted for topLeft twice because it's contained in bottomLeft *and* in topRight,
	// therefore we need to add it back once
	return bottomRight - bottomLeft - topRight + topLeft
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */

// Runtime: 673 ms, faster than 87.80% of Go online submissions for Range Sum Query 2D - Immutable.
// Memory Usage: 16.4 MB, less than 43.90% of Go online submissions for Range Sum Query 2D - Immutable.
