package v2

import "strings"

type Grid struct {
	n            int
	queensPlaced int
	// array index = row of queen; value = col of queen
	queens []int
	// array index = row of blocked field; 1 bit in value = blocked column in in current row
	blockedFields []int

	// 1 bit set where field is valid
	fieldMask int
}

func NewGrid(n int) Grid {
	fieldMask := 0
	for i := 0; i < n; i++ {
		fieldMask |= (1 << i)
	}

	return Grid{
		n:             n,
		queensPlaced:  0,
		queens:        make([]int, n),
		blockedFields: make([]int, n),

		fieldMask: fieldMask,
	}
}

func (g Grid) GetCopy() *Grid {
	return &Grid{
		n:             g.n,
		queensPlaced:  g.queensPlaced,
		queens:        append([]int(nil), g.queens...),
		blockedFields: append([]int(nil), g.blockedFields...),

		fieldMask: g.fieldMask,
	}
}

func (g Grid) ToFieldOutput() []string {
	ret := make([]string, g.n)
	for i := range ret {
		if i >= g.queensPlaced {
			break
		}

		queenCol := g.queens[i]
		ret[i] = strings.Repeat(".", queenCol) + "Q" + strings.Repeat(".", g.n-queenCol-1)
	}
	return ret
}

func (g Grid) IsBlocked(row, col int) bool {
	return (g.blockedFields[row] & (1 << col)) != 0
}

func (g *Grid) PlaceQueen(row, col int) {
	g.queens[g.queensPlaced] = col
	g.queensPlaced++

	// start at next row because the current row (and previous rows) are done anyway
	for i := row + 1; i < g.n; i++ {
		distance := i - row

		// block same column
		blockMask := (1 << col)
		// block diagonals
		diagA := (1 << (col + distance)) & g.fieldMask
		diagB := 0
		if (col - distance) >= 0 {
			diagB = (1 << (col - distance)) & g.fieldMask
		}
		// no additional checks needed since values are or'ed by 0 if they're not on the field
		blockMask |= diagA | diagB

		g.blockedFields[i] |= blockMask
	}
}

type Solver struct {
	Results []*Grid
	N       int
}

func (s *Solver) solveNQueensRecurse(grid *Grid, myRow int) {
	if myRow == s.N {
		// we found a solution
		s.Results = append(s.Results, grid)
		return
	}

	for col := 0; col < s.N; col++ {
		if !grid.IsBlocked(myRow, col) {
			nextGrid := grid.GetCopy()
			nextGrid.PlaceQueen(myRow, col)
			s.solveNQueensRecurse(nextGrid, myRow+1)
		}
	}
}

func solveNQueens(n int) [][]string {
	s := &Solver{
		Results: make([]*Grid, 0),
		N:       n,
	}
	base := NewGrid(n)
	s.solveNQueensRecurse(&base, 0)

	// render possible fields
	ret := make([][]string, len(s.Results))
	for i, result := range s.Results {
		ret[i] = result.ToFieldOutput()
	}
	return ret
}

// Runtime: 10 ms, faster than 38.84% of Go online submissions for N-Queens.
// Memory Usage: 6.3 MB, less than 12.40% of Go online submissions for N-Queens.
