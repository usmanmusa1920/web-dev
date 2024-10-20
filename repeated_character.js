repeated_count = 0;

my_string = "ToMyCommunityPeople".split("");

my_string.some(
    function(v, i, a){
        // v ... current value of the iteration
        // i ... current index of the iteration
        // a ... array being iterated

        r = a.lastIndexOf(v)!= i;
        if (r == true){
            repeated_count += 1;
        }
    }
);

console.log(
    `There is a total of ${repeated_count} repeated character(s).`
);
