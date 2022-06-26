package v1

func maxScore(cardPoints []int, k int) int {
    prefixSum := make([]int, 1+len(cardPoints))
    
    sum := 0
    for i, num := range cardPoints {
        sum += num
        prefixSum[i+1] = sum
    }
    
    var sumLeft, sumRight, cardsRight, score, maxScore int
    for cardsLeft := 0; cardsLeft <= k; cardsLeft++ {
        cardsRight = k - cardsLeft
        
        sumLeft = 0
        sumRight = 0
        if cardsLeft > 0 {
            sumLeft = prefixSum[cardsLeft]
        }
        if cardsRight > 0 {
            sumRight = prefixSum[len(cardPoints)] - prefixSum[len(cardPoints) - cardsRight]
        }
        
        score = sumLeft + sumRight
        if score > maxScore {
            maxScore = score
        }
    }
    
    return maxScore
}

// Runtime: 95 ms, faster than 34.51% of Go online submissions for Maximum Points You Can Obtain from Cards.
// Memory Usage: 9.4 MB, less than 23.01% of Go online submissions for Maximum Points You Can Obtain from Cards.