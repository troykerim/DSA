def characterReplacement(self, s: str, k: int) -> int:
    # Initialize variables
    windowStart = 0  # Starting index of the current window
    maxLengthCount = 0  # Maximum length of substring with repeating characters
    maxRepeatingCharCountInHashmap = 0  # Maximum count of any single character in the current window
    hashMap = {}  # Dictionary to store character counts in the current window
    
    # Loop through each character in the string
    for i in range(len(s)):
        # Update count of current character in hashMap
        hashMap[s[i]] = hashMap.get(s[i], 0) + 1
        
        # Update maxRepeatingCharCountInHashmap with the maximum count of any character in the current window
        maxRepeatingCharCountInHashmap = max(maxRepeatingCharCountInHashmap, hashMap[s[i]])
        
        # Check if the number of replacements needed exceeds k
        if (i - windowStart + 1) - maxRepeatingCharCountInHashmap > k:
            # Adjust the window by moving windowStart to the right
            hashMap[s[windowStart]] -= 1  # Decrease count of the character going out of the window
            
            # Remove character from hashMap if its count becomes zero
            if hashMap[s[windowStart]] == 0:
                del hashMap[s[windowStart]]
            
            windowStart += 1  # Slide the window to the right
        
        # Update maxLengthCount with the maximum length of valid substring found so far
        maxLengthCount = max(maxLengthCount, i - windowStart + 1)
    
    # Return the maximum length of substring with repeating characters that can be made the same with k replacements
    return maxLengthCount