package v1

type TrieNode struct {
	Children   [26]*TrieNode
	ChildCount int
	EndOfWord  bool
}

func (t *TrieNode) InsertSpecial(word string) (addedNodes, addedWords int) {
	node := t
	depth := 0
	for i := range word {
		depth++
		// begin at last letter
		idx := int(word[len(word)-1-i]) - int('a')
		newBranch := false
		if node.Children[idx] == nil {
			node.Children[idx] = &TrieNode{}
			node.ChildCount++
			addedNodes++
			newBranch = true
		}
		if node.EndOfWord && node.ChildCount <= 1 {
			node.EndOfWord = false
			addedWords--
		}
		if newBranch && node.ChildCount > 1 {
			addedNodes += depth - 1
		}
		node = node.Children[idx]
	}

	if node.EndOfWord || node.ChildCount > 0 {
		addedNodes = 0
	}

	// only count an added word if
	// * it doesn't already exist
	// * it's not part of a longer word (this leaf node doesn't have any children)
	if !node.EndOfWord && node.ChildCount == 0 {
		node.EndOfWord = true
		addedWords++
	}
	return
}

func minimumLengthEncoding(words []string) int {
	var nodeCount, wordCount int

	root := &TrieNode{}
	var addedNodes, addedWords int
	for _, word := range words {
		addedNodes, addedWords = root.InsertSpecial(word)
		nodeCount += addedNodes
		wordCount += addedWords
		//fmt.Printf("added %d nodes %d words\n", addedNodes, addedWords)
	}

	//fmt.Println("--")
	return nodeCount + wordCount
}

// Runtime: 24 ms, faster than 76.47% of Go online submissions for Short Encoding of Words.
// Memory Usage: 7.7 MB, less than 52.94% of Go online submissions for Short Encoding of Words.
