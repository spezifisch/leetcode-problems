package v1

type TrieNode struct {
	Children   [26]*TrieNode
	ChildCount int
	EndOfWord  bool
}

// InsertSpecial inserts the reversed word into the Trie
// and counts added characters and words (for the # symbols) according to the desired encoding
func (t *TrieNode) InsertSpecial(word string) (addedNodes, addedWords int) {
	// start at the current node (called on the root node of the Trie)
	node := t
	for i := range word {
		// begin at last letter of the word
		// only english lowercase letters are possible,
		// so we're using a children array with static size
		idx := int(word[len(word)-1-i]) - int('a')

		// add a new branch with a child to the Trie if needed
		newBranch := false
		if node.Children[idx] == nil {
			node.Children[idx] = &TrieNode{}
			node.ChildCount++
			addedNodes++
			newBranch = true
		}

		// handle edge case: a longer word with the same ending as an existing word is added,
		// e.g. ["time", "atime"] => "atime#"
		if node.EndOfWord && node.ChildCount <= 1 {
			node.EndOfWord = false
			addedWords--
		}

		// handle edge case: we need another copy of the word in the output string
		// when we add new children to a node that already has children,
		// e.g. ["time", "atime", "btime"] => "atime#btime#"
		if newBranch && node.ChildCount > 1 {
			// add count of (current depth in Trie - 1),
			// e.g. because we needed to add "btime" to the output string,
			// subtract 1 because we already counted an added node when adding the new branch
			addedNodes += i
		}

		// next layer
		node = node.Children[idx]
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
	}

	// every Trie node is a character in our output string,
	// for each full word we need to add a "#"
	return nodeCount + wordCount
}

// Runtime: 24 ms, faster than 76.47% of Go online submissions for Short Encoding of Words.
// Memory Usage: 7.7 MB, less than 52.94% of Go online submissions for Short Encoding of Words.
