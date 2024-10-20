<?php
function findRepeatedCharacters($string) {
    $charCount = [];
    
    // Loop through each character in the string
    for ($i = 0; $i < strlen($string); $i++) {
        $char = $string[$i];
        
        // Count occurrences of each character
        if (isset($charCount[$char])) {
            $charCount[$char]++;
        } else {
            $charCount[$char] = 1;
        }
    }
    
    // Find and print repeated characters
    $repeatedChars = [];
    foreach ($charCount as $char => $count) {
        if ($count > 1) {
            $repeatedChars[] = $char;
        }
    }

    if (empty($repeatedChars)) {
        echo "No repeated characters found.";
    } else {
        echo "Repeated characters: " . implode(", ", $repeatedChars);
    }
}

// Example usage
$string = "programming";
findRepeatedCharacters($string);
?>
