package v1

func minimumTotal(triangle [][]int) int {
	pathSums := make([][]int, len(triangle))

	var parentLeft, parentRight int
	for i, row := range triangle {
		pathSums[i] = make([]int, len(row))

		for j, num := range row {
			if j == 0 {
				if i > 0 {
					parentRight = pathSums[i-1][0]
				}

				pathSums[i][j] = parentRight + num
			} else if j == len(row)-1 {
				parentLeft = pathSums[i-1][len(row)-2]

				pathSums[i][j] = parentLeft + num
			} else {
				parentLeft = pathSums[i-1][j-1]
				parentRight = pathSums[i-1][j]

				if parentLeft < parentRight {
					pathSums[i][j] = parentLeft + num
				} else {
					pathSums[i][j] = parentRight + num
				}
			}
		}
	}

	var minimumPathSum int
	for i, num := range pathSums[len(pathSums)-1] {
		if i == 0 {
			minimumPathSum = num
		} else if num < minimumPathSum {
			minimumPathSum = num
		}
	}
	return minimumPathSum
}

// Runtime: 4 ms, faster than 80.87% of Go online submissions for Triangle.
// Memory Usage: 3.6 MB, less than 36.82% of Go online submissions for Triangle.
