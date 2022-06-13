package v2

func minimumTotal(triangle [][]int) int {
	currentRow := make([]int, len(triangle[len(triangle)-1]))
	lastRow := make([]int, len(currentRow))

	var parentLeft, parentRight int
	for i, row := range triangle {
		for j, num := range row {
			if j == 0 {
				if i > 0 {
					parentRight = lastRow[0]
				}

				currentRow[j] = parentRight + num
			} else if j == len(row)-1 {
				parentLeft = lastRow[len(row)-2]

				currentRow[j] = parentLeft + num
			} else {
				parentLeft = lastRow[j-1]
				parentRight = lastRow[j]

				if parentLeft < parentRight {
					currentRow[j] = parentLeft + num
				} else {
					currentRow[j] = parentRight + num
				}
			}
		}

		currentRow, lastRow = lastRow, currentRow
	}

	var minimumPathSum int
	for i, num := range lastRow {
		if i == 0 {
			minimumPathSum = num
		} else if num < minimumPathSum {
			minimumPathSum = num
		}
	}
	return minimumPathSum
}

// Runtime: 3 ms, faster than 93.14% of Go online submissions for Triangle.
// Memory Usage: 3.2 MB, less than 100.00% of Go online submissions for Triangle.
