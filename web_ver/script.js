function compareSigns() {
    let originalSign = document.getElementById("originalSign").value.toUpperCase().replace(/\s+/g, '');
    let newSign = document.getElementById("newSign").value.toUpperCase().replace(/\s+/g, '');
    let showExtraDetails = document.getElementById("showExtraDetails").checked;

    let originalCount = countLetters(originalSign);
    let newCount = countLetters(newSign);

    let neededLetters = subtractCounts(newCount, originalCount);
    let unusedLetters = subtractCounts(originalCount, newCount);
    let sharedLetters = getSharedLetters(originalCount, newCount);

    let resultText = "";

    if (Object.keys(neededLetters).length > 0) {
        resultText += "Letters needed:\n";
        resultText += formatSortedOutput(neededLetters);
    } else {
        resultText += "No extra letters needed!\n";
    }

    // Show extra details only if the checkbox is checked
    if (showExtraDetails) {
        if (Object.keys(sharedLetters).length > 0) {
            resultText += "\nShared letters:\n";
            resultText += formatSortedOutput(sharedLetters);
        }

        if (Object.keys(unusedLetters).length > 0) {
            resultText += "\nLetters no longer needed:\n";
            resultText += formatSortedOutput(unusedLetters);
        }
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

// Find shared letters (letters that exist in both)
function getSharedLetters(count1, count2) {
    let shared = {};
    for (let char in count1) {
        if (count2[char]) {
            shared[char] = Math.min(count1[char], count2[char]);
        }
    }
    return shared;
}

// Format and sort output alphabetically
function formatSortedOutput(letterCounts) {
    return Object.keys(letterCounts)
        .sort()
        .map(char => `${char} - ${letterCounts[char]}`)
        .join("\n") + "\n";
}
