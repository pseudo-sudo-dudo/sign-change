function compareSigns() {
    let originalSign = document.getElementById("originalSign").value.toUpperCase().replace(/\s+/g, '');
    let newSign = document.getElementById("newSign").value.toUpperCase().replace(/\s+/g, '');

    let originalCount = countLetters(originalSign);
    let newCount = countLetters(newSign);

    let neededLetters = subtractCounts(newCount, originalCount);
    let unusedLetters = subtractCounts(originalCount, newCount);

    let resultText = "";

    if (Object.keys(neededLetters).length > 0) {
        resultText += "Letters needed:\n";
        resultText += formatSortedOutput(neededLetters);
    } else {
        resultText += "No extra letters needed!\n";
    }

    if (Object.keys(unusedLetters).length > 0) {
        resultText += "\nLetters no longer needed:\n";
        resultText += formatSortedOutput(unusedLetters);
    }

    document.getElementById("result").textContent = resultText;
}

// Count occurrences of each letter
function countLetters(str) {
    let count = {};
    for (let char of str) {
        count[char] = (count[char] || 0) + 1;
    }
    return count;
}

// Find letters in one object but not in another
function subtractCounts(main, sub) {
    let diff = {};
    for (let char in main) {
        let countDiff = main[char] - (sub[char] || 0);
        if (countDiff > 0) {
            diff[char] = countDiff;
        }
    }
    return diff;
}

// Format and sort output alphabetically
function formatSortedOutput(letterCounts) {
    return Object.keys(letterCounts)
        .sort() // Sort alphabetically
        .map(char => `${char} - ${letterCounts[char]}`)
        .join("\n") + "\n";
}
