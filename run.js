function findDifferences(original, newSign) {
    // Remove spaces and convert to uppercase
    original = original.replace(/\s+/g, '').toUpperCase();
    newSign = newSign.replace(/\s+/g, '').toUpperCase();

    // Count characters in both strings
    const countCharacters = (str) => {
        const counts = {};
        for (const char of str) {
            counts[char] = (counts[char] || 0) + 1;
        }
        return counts;
    };

    const ogCount = countCharacters(original);
    const newCount = countCharacters(newSign);

    // Calculate differences
    const differences = {};
    for (const char in newCount) {
        if (!ogCount[char] || newCount[char] > ogCount[char]) {
            differences[char] = (differences[char] || 0) + (newCount[char] - (ogCount[char] || 0));
        }
    }

    return differences;
}

// Example usage
const original = "HELLO WORLD";
const newSign = "HOLD ON";
console.log(findDifferences(original, newSign));
